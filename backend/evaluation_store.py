"""评估记录、批量任务、请求审计 — SQLite。"""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


def _db_path() -> Path:
    from paths import DATA_DIR

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR / "evaluations.db"


def _migrate(conn: sqlite3.Connection) -> None:
    cols = {r[1] for r in conn.execute("PRAGMA table_info(evaluations)").fetchall()}
    if "model_version" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN model_version TEXT DEFAULT ''")
    if "linguistic_json" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN linguistic_json TEXT DEFAULT ''")
    if "child_id" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN child_id TEXT DEFAULT ''")
    if "child_name" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN child_name TEXT DEFAULT ''")
    if "parent_summary" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN parent_summary TEXT DEFAULT ''")
    if "class_name" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN class_name TEXT DEFAULT ''")
    if "record_label" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN record_label TEXT DEFAULT ''")
    if "tenant_id" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN tenant_id TEXT DEFAULT 'default'")
        conn.execute("UPDATE evaluations SET tenant_id = 'default' WHERE tenant_id IS NULL OR tenant_id = ''")
    if "status" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN status TEXT DEFAULT 'completed'")
        conn.execute(
            "UPDATE evaluations SET status = 'completed' WHERE status IS NULL OR status = ''"
        )
    if "status_message" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN status_message TEXT DEFAULT ''")
    if "parent_survey_json" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN parent_survey_json TEXT DEFAULT ''")
    if "coach_mode" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN coach_mode TEXT DEFAULT 'free'")
    if "dialogue_log_json" not in cols:
        conn.execute("ALTER TABLE evaluations ADD COLUMN dialogue_log_json TEXT DEFAULT ''")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expert_overrides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evaluation_id INTEGER NOT NULL,
            field TEXT NOT NULL,
            original_value TEXT,
            override_value TEXT NOT NULL,
            note TEXT DEFAULT '',
            reviewer TEXT DEFAULT '',
            created_at TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS request_audit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            endpoint TEXT NOT NULL,
            method TEXT,
            status_code INTEGER,
            detail TEXT,
            elapsed_ms INTEGER
        )
        """
    )


def init_db() -> None:
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                source TEXT NOT NULL DEFAULT 'web',
                text TEXT NOT NULL,
                story_type TEXT NOT NULL,
                task_type TEXT,
                age INTEGER,
                left_behind INTEGER,
                predicted_ist_words TEXT,
                report_text TEXT,
                regression_json TEXT,
                microstructure_json TEXT,
                linguistic_json TEXT DEFAULT '',
                benchmark_source TEXT,
                elapsed_ms INTEGER,
                model_version TEXT DEFAULT '',
                child_id TEXT DEFAULT '',
                child_name TEXT DEFAULT '',
                parent_summary TEXT DEFAULT '',
                class_name TEXT DEFAULT '',
                tenant_id TEXT DEFAULT 'default'
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS batch_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                filename TEXT,
                total_rows INTEGER,
                completed_rows INTEGER,
                failed_rows INTEGER DEFAULT 0,
                status TEXT,
                summary_json TEXT,
                errors_json TEXT,
                model_version TEXT DEFAULT ''
            )
            """
        )
        _migrate(conn)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


_STORY_LABELS = {"cat": "小猫", "dog": "小狗", "bird": "小鸟", "goat": "小羊"}


def _format_record_label(story_type: str, created_at: str, sequence: int) -> str:
    story = _STORY_LABELS.get(story_type, story_type or "故事")
    date_str = "未知日期"
    if created_at:
        try:
            raw = created_at.replace("Z", "+00:00")
            dt = datetime.fromisoformat(raw)
            date_str = f"{dt.month}月{dt.day}日"
        except ValueError:
            date_str = created_at[:10]
    return f"第{sequence}次 · {story}故事 · {date_str}"


def _set_default_record_label(conn: sqlite3.Connection, evaluation_id: int, story_type: str, created_at: str) -> str:
    n = conn.execute("SELECT COUNT(*) FROM evaluations").fetchone()[0]
    label = _format_record_label(story_type, created_at, int(n))
    conn.execute("UPDATE evaluations SET record_label = ? WHERE id = ?", (label, evaluation_id))
    return label


def log_request(endpoint: str, method: str, status_code: int, detail: str = "", elapsed_ms: int = 0) -> None:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            "INSERT INTO request_audit (created_at, endpoint, method, status_code, detail, elapsed_ms) VALUES (?,?,?,?,?,?)",
            (_now_iso(), endpoint, method, status_code, detail[:500], elapsed_ms),
        )


_backfill_labels_done = False


def maybe_backfill_record_labels() -> None:
    global _backfill_labels_done
    if _backfill_labels_done:
        return
    backfill_record_labels()
    _backfill_labels_done = True


def save_evaluation(
    *,
    source: str,
    text: str,
    story_type: str,
    task_type: Optional[str],
    age: int,
    left_behind: int,
    predicted_ist_words: str,
    report_text: str,
    regression: dict,
    microstructure: dict,
    linguistics: Optional[dict] = None,
    parent_summary: str = "",
    child_id: str = "",
    child_name: str = "",
    class_name: str = "",
    benchmark_source: str,
    elapsed_ms: int,
    model_version: str = "",
) -> int:
    from tenant import current_tenant_id

    init_db()
    created_at = _now_iso()
    tenant_id = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            """
            INSERT INTO evaluations (
                created_at, source, text, story_type, task_type, age, left_behind,
                predicted_ist_words, report_text, regression_json, microstructure_json,
                linguistic_json, benchmark_source, elapsed_ms, model_version,
                child_id, child_name, parent_summary, class_name, tenant_id
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                created_at,
                source,
                text,
                story_type,
                task_type or "",
                age,
                left_behind,
                predicted_ist_words,
                report_text,
                json.dumps(regression, ensure_ascii=False),
                json.dumps(microstructure, ensure_ascii=False),
                json.dumps(linguistics or {}, ensure_ascii=False),
                benchmark_source,
                elapsed_ms,
                model_version,
                child_id or "",
                child_name or "",
                parent_summary or "",
                class_name or "",
                tenant_id,
            ),
        )
        eid = int(cur.lastrowid)
        _set_default_record_label(conn, eid, story_type, created_at)
        return eid


def update_evaluation_session_meta(
    evaluation_id: int,
    *,
    coach_mode: str = "free",
    dialogue_log: Optional[list] = None,
) -> None:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    log_json = json.dumps(dialogue_log or [], ensure_ascii=False)
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            """
            UPDATE evaluations
            SET coach_mode = ?, dialogue_log_json = ?
            WHERE id = ? AND tenant_id = ?
            """,
            (coach_mode[:32], log_json, evaluation_id, tid),
        )


def save_parent_survey(evaluation_id: int, survey: dict) -> None:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            """
            UPDATE evaluations SET parent_survey_json = ?
            WHERE id = ? AND tenant_id = ?
            """,
            (json.dumps(survey, ensure_ascii=False), evaluation_id, tid),
        )


def create_pending_evaluation(
    *,
    source: str,
    text: str,
    story_type: str,
    task_type: Optional[str],
    age: int,
    left_behind: int,
    child_id: str = "",
    child_name: str = "",
    class_name: str = "",
    status_message: str = "已提交，等待分析…",
    coach_mode: str = "free",
    dialogue_log: Optional[list] = None,
) -> int:
    """立即创建占位记录，供异步评估写入结果。"""
    from tenant import current_tenant_id

    init_db()
    created_at = _now_iso()
    tenant_id = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            """
            INSERT INTO evaluations (
                created_at, source, text, story_type, task_type, age, left_behind,
                predicted_ist_words, report_text, regression_json, microstructure_json,
                linguistic_json, benchmark_source, elapsed_ms, model_version,
                child_id, child_name, parent_summary, class_name, tenant_id,
                status, status_message, coach_mode, dialogue_log_json
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                created_at,
                source,
                text,
                story_type,
                task_type or "",
                age,
                left_behind,
                "",
                "",
                json.dumps({}, ensure_ascii=False),
                json.dumps({"sum": None, "max": 15, "tasks": []}, ensure_ascii=False),
                json.dumps({}, ensure_ascii=False),
                "",
                0,
                "",
                child_id or "",
                child_name or "",
                "",
                class_name or "",
                tenant_id,
                "pending",
                status_message,
                (coach_mode or "free")[:32],
                json.dumps(dialogue_log or [], ensure_ascii=False),
            ),
        )
        eid = int(cur.lastrowid)
        _set_default_record_label(conn, eid, story_type, created_at)
        return eid


def update_evaluation_status(
    evaluation_id: int,
    status: str,
    status_message: str = "",
) -> None:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            """
            UPDATE evaluations
            SET status = ?, status_message = ?
            WHERE id = ? AND tenant_id = ?
            """,
            (status, status_message[:500], evaluation_id, tid),
        )


def complete_evaluation(
    evaluation_id: int,
    *,
    predicted_ist_words: str,
    report_text: str,
    regression: dict,
    microstructure: dict,
    linguistics: Optional[dict] = None,
    parent_summary: str = "",
    benchmark_source: str,
    elapsed_ms: int,
    model_version: str = "",
) -> None:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            """
            UPDATE evaluations SET
                predicted_ist_words = ?,
                report_text = ?,
                regression_json = ?,
                microstructure_json = ?,
                linguistic_json = ?,
                parent_summary = ?,
                benchmark_source = ?,
                elapsed_ms = ?,
                model_version = ?,
                status = 'completed',
                status_message = ''
            WHERE id = ? AND tenant_id = ?
            """,
            (
                predicted_ist_words,
                report_text,
                json.dumps(regression, ensure_ascii=False),
                json.dumps(microstructure, ensure_ascii=False),
                json.dumps(linguistics or {}, ensure_ascii=False),
                parent_summary,
                benchmark_source,
                elapsed_ms,
                model_version,
                evaluation_id,
                tid,
            ),
        )


def fail_evaluation(evaluation_id: int, message: str) -> None:
    update_evaluation_status(evaluation_id, "failed", message[:500])


def delete_evaluation(evaluation_id: int) -> bool:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            "DELETE FROM evaluations WHERE id = ? AND tenant_id = ?",
            (evaluation_id, tid),
        )
        conn.execute("DELETE FROM expert_overrides WHERE evaluation_id = ?", (evaluation_id,))
        return cur.rowcount > 0


def update_record_label(evaluation_id: int, label: str) -> bool:
    from tenant import current_tenant_id

    init_db()
    clean = (label or "").strip()[:120]
    if not clean:
        return False
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            "UPDATE evaluations SET record_label = ? WHERE id = ? AND tenant_id = ?",
            (clean, evaluation_id, tid),
        )
        return cur.rowcount > 0


def backfill_record_labels() -> None:
    """为旧记录补全可读名称。"""
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, story_type, created_at, record_label FROM evaluations ORDER BY id ASC"
        ).fetchall()
        for i, r in enumerate(rows, start=1):
            if (r["record_label"] or "").strip():
                continue
            label = _format_record_label(r["story_type"], r["created_at"], i)
            conn.execute(
                "UPDATE evaluations SET record_label = ? WHERE id = ?",
                (label, int(r["id"])),
            )


def list_evaluations(limit: int = 50, child_id: Optional[str] = None) -> list[dict]:
    from tenant import current_tenant_id

    init_db()
    maybe_backfill_record_labels()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        q = """
            SELECT id, created_at, source, story_type, task_type, age, model_version,
                   regression_json, microstructure_json, elapsed_ms, child_id, child_name, class_name,
                   record_label, status, status_message
            FROM evaluations
            WHERE tenant_id = ?
        """
        args: list[Any] = [tid]
        if child_id:
            q += " AND child_id = ?"
            args.append(child_id.strip())
        q += " ORDER BY id DESC LIMIT ?"
        args.append(limit)
        rows = conn.execute(q, args).fetchall()
    out = []
    for r in rows:
        reg = json.loads(r["regression_json"] or "{}")
        micro = json.loads(r["microstructure_json"] or "{}")
        out.append(
            {
                "id": r["id"],
                "created_at": r["created_at"],
                "source": r["source"],
                "story_type": r["story_type"],
                "task_type": r["task_type"],
                "age": r["age"],
                "model_version": r["model_version"],
                "pred_SC_Sum": reg.get("pred_SC_Sum"),
                "micro_sum": micro.get("sum"),
                "elapsed_ms": r["elapsed_ms"],
                "child_id": r["child_id"] if "child_id" in r.keys() else "",
                "child_name": r["child_name"] if "child_name" in r.keys() else "",
                "class_name": r["class_name"] if "class_name" in r.keys() else "",
                "record_label": r["record_label"] if "record_label" in r.keys() else "",
                "status": (r["status"] if "status" in r.keys() else None) or "completed",
                "status_message": r["status_message"] if "status_message" in r.keys() else "",
            }
        )
    return out


def list_child_timeline(child_id: str, limit: int = 100) -> list[dict]:
    """同一儿童多次评估（纵向）。"""
    return list_evaluations(limit=limit, child_id=child_id)


def save_expert_override(
    evaluation_id: int,
    field: str,
    override_value: str,
    *,
    original_value: str = "",
    note: str = "",
    reviewer: str = "",
) -> int:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            """
            INSERT INTO expert_overrides (
                evaluation_id, field, original_value, override_value, note, reviewer, created_at
            ) VALUES (?,?,?,?,?,?,?)
            """,
            (
                evaluation_id,
                field,
                original_value,
                override_value,
                note,
                reviewer,
                _now_iso(),
            ),
        )
        return int(cur.lastrowid)


def list_overrides(evaluation_id: int) -> list[dict]:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM expert_overrides WHERE evaluation_id=? ORDER BY id DESC",
            (evaluation_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_evaluation(evaluation_id: int) -> Optional[dict]:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM evaluations WHERE id = ? AND tenant_id = ?",
            (evaluation_id, tid),
        ).fetchone()
    if not row:
        return None
    status = (row["status"] if "status" in row.keys() else None) or "completed"
    return {
        "id": row["id"],
        "evaluation_id": row["id"],
        "created_at": row["created_at"],
        "source": row["source"],
        "text": row["text"],
        "story_type": row["story_type"],
        "task_type": row["task_type"],
        "age": row["age"],
        "left_behind": row["left_behind"],
        "predicted_ist_words": row["predicted_ist_words"],
        "report_text": row["report_text"],
        "regression": json.loads(row["regression_json"] or "{}"),
        "microstructure": json.loads(row["microstructure_json"] or "{}"),
        "linguistics": json.loads(row["linguistic_json"] or "{}")
        if "linguistic_json" in row.keys()
        else {},
        "narrative_quality": (
            json.loads(row["linguistic_json"] or "{}").get("narrative_quality")
            if "linguistic_json" in row.keys()
            else None
        ),
        "benchmark_source": row["benchmark_source"],
        "elapsed_ms": row["elapsed_ms"],
        "model_version": row["model_version"] if "model_version" in row.keys() else "",
        "child_id": row["child_id"] if "child_id" in row.keys() else "",
        "child_name": row["child_name"] if "child_name" in row.keys() else "",
        "parent_summary": row["parent_summary"] if "parent_summary" in row.keys() else "",
        "record_label": row["record_label"] if "record_label" in row.keys() else "",
        "status": status,
        "status_message": row["status_message"] if "status_message" in row.keys() else "",
        "coach_mode": row["coach_mode"] if "coach_mode" in row.keys() else "free",
        "dialogue_log": json.loads(row["dialogue_log_json"] or "[]")
        if "dialogue_log_json" in row.keys()
        else [],
        "parent_survey": json.loads(row["parent_survey_json"] or "{}")
        if "parent_survey_json" in row.keys() and (row["parent_survey_json"] or "").strip()
        else None,
        "expert_overrides": list_overrides(evaluation_id),
    }


def create_batch_job(filename: str, total_rows: int, model_version: str = "") -> int:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            """
            INSERT INTO batch_jobs (created_at, filename, total_rows, completed_rows, failed_rows, status, model_version)
            VALUES (?,?,?,0,0,'queued',?)
            """,
            (_now_iso(), filename, total_rows, model_version),
        )
        return int(cur.lastrowid)


def update_batch_job(
    job_id: int,
    *,
    status: Optional[str] = None,
    completed_rows: Optional[int] = None,
    failed_rows: Optional[int] = None,
    summary_json: Optional[str] = None,
    errors_json: Optional[str] = None,
) -> None:
    init_db()
    fields, vals = [], []
    if status is not None:
        fields.append("status=?")
        vals.append(status)
    if completed_rows is not None:
        fields.append("completed_rows=?")
        vals.append(completed_rows)
    if failed_rows is not None:
        fields.append("failed_rows=?")
        vals.append(failed_rows)
    if summary_json is not None:
        fields.append("summary_json=?")
        vals.append(summary_json)
    if errors_json is not None:
        fields.append("errors_json=?")
        vals.append(errors_json)
    if not fields:
        return
    vals.append(job_id)
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(f"UPDATE batch_jobs SET {', '.join(fields)} WHERE id=?", vals)


def get_batch_job(job_id: int) -> Optional[dict]:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM batch_jobs WHERE id=?", (job_id,)).fetchone()
    if not row:
        return None
    return {
        "id": row["id"],
        "created_at": row["created_at"],
        "filename": row["filename"],
        "total_rows": row["total_rows"],
        "completed_rows": row["completed_rows"],
        "failed_rows": row["failed_rows"],
        "status": row["status"],
        "summary": json.loads(row["summary_json"] or "null") if row["summary_json"] else None,
        "errors": json.loads(row["errors_json"] or "[]") if row["errors_json"] else [],
        "model_version": row["model_version"],
    }
