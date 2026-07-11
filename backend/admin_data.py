"""管理员：全量用户与产品使用记录。"""
from __future__ import annotations

import json
import sqlite3
from typing import Any

from evaluation_store import _db_path, init_db
from user_profile_store import _ensure_profile_table


def list_registered_users(*, limit: int = 500) -> list[dict[str, Any]]:
    init_db()
    cap = max(1, min(int(limit), 2000))
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        _ensure_profile_table(conn)
        rows = conn.execute(
            """
            SELECT
                u.id,
                u.email,
                u.display_name,
                u.phone,
                u.created_at,
                u.updated_at,
                fp.child_name,
                fp.child_id,
                fp.age,
                fp.class_name,
                (
                    SELECT COUNT(*)
                    FROM evaluations e
                    WHERE e.user_id = u.id
                ) AS n_evaluations,
                (
                    SELECT MAX(e.created_at)
                    FROM evaluations e
                    WHERE e.user_id = u.id
                ) AS last_eval_at
            FROM users u
            LEFT JOIN family_profile fp ON fp.user_id = u.id
            ORDER BY u.id DESC
            LIMIT ?
            """,
            (cap,),
        ).fetchall()
    return [
        {
            "id": int(r["id"]),
            "email": r["email"] or "",
            "display_name": r["display_name"] or "",
            "phone": r["phone"] or "",
            "created_at": r["created_at"],
            "updated_at": r["updated_at"],
            "child_name": r["child_name"] or "",
            "child_id": r["child_id"] or "",
            "age": int(r["age"]) if r["age"] is not None else None,
            "class_name": r["class_name"] or "",
            "n_evaluations": int(r["n_evaluations"] or 0),
            "last_eval_at": r["last_eval_at"] or "",
        }
        for r in rows
    ]


def list_product_records(*, limit: int = 500) -> list[dict[str, Any]]:
    from tenant import current_tenant_id

    init_db()
    cap = max(1, min(int(limit), 2000))
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT
                e.id,
                e.user_id,
                e.created_at,
                e.source,
                e.story_type,
                e.task_type,
                e.age,
                e.child_id,
                e.child_name,
                e.class_name,
                e.record_label,
                e.status,
                e.status_message,
                e.coach_mode,
                e.elapsed_ms,
                e.regression_json,
                e.microstructure_json,
                u.email AS user_email,
                u.display_name AS user_display_name
            FROM evaluations e
            LEFT JOIN users u ON u.id = e.user_id
            WHERE e.tenant_id = ?
            ORDER BY e.id DESC
            LIMIT ?
            """,
            (tid, cap),
        ).fetchall()
    out: list[dict[str, Any]] = []
    for r in rows:
        reg = json.loads(r["regression_json"] or "{}")
        micro = json.loads(r["microstructure_json"] or "{}")
        out.append(
            {
                "id": int(r["id"]),
                "user_id": int(r["user_id"] or 0),
                "user_email": r["user_email"] or "",
                "user_display_name": r["user_display_name"] or "",
                "created_at": r["created_at"],
                "source": r["source"] or "",
                "story_type": r["story_type"] or "",
                "task_type": r["task_type"] or "",
                "age": r["age"],
                "child_id": r["child_id"] or "",
                "child_name": r["child_name"] or "",
                "class_name": r["class_name"] or "",
                "record_label": r["record_label"] or "",
                "status": (r["status"] or "") or "completed",
                "status_message": r["status_message"] or "",
                "coach_mode": r["coach_mode"] or "",
                "elapsed_ms": r["elapsed_ms"],
                "pred_SC_Sum": reg.get("pred_SC_Sum"),
                "micro_sum": micro.get("sum"),
            }
        )
    return out


def admin_storage_summary() -> dict[str, Any]:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        users = int(conn.execute("SELECT COUNT(*) FROM users").fetchone()[0])
        evals = int(conn.execute("SELECT COUNT(*) FROM evaluations").fetchone()[0])
        sessions = int(conn.execute("SELECT COUNT(*) FROM user_sessions").fetchone()[0])
    return {
        "users": users,
        "evaluations": evals,
        "sessions": sessions,
    }
