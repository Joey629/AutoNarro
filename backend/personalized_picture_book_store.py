"""专属练习绘本 — SQLite 存储。"""
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


def init_db() -> None:
    with sqlite3.connect(_db_path()) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS personalized_picture_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                tenant_id TEXT NOT NULL DEFAULT 'default',
                child_id TEXT NOT NULL DEFAULT '',
                child_name TEXT NOT NULL DEFAULT '',
                age INTEGER,
                evaluation_ids_json TEXT NOT NULL DEFAULT '[]',
                title TEXT NOT NULL DEFAULT '',
                target_skills_json TEXT NOT NULL DEFAULT '[]',
                book_json TEXT NOT NULL DEFAULT '{}',
                profile_json TEXT NOT NULL DEFAULT '{}',
                status TEXT NOT NULL DEFAULT 'ready',
                error_message TEXT NOT NULL DEFAULT ''
            )
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_ppb_child
            ON personalized_picture_books (tenant_id, child_id, id DESC)
            """
        )


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def insert_book(
    *,
    child_id: str,
    child_name: str,
    age: int,
    evaluation_ids: list[int],
    title: str,
    target_skills: list[str],
    book: dict[str, Any],
    profile: dict[str, Any],
    status: str = "ready",
    error_message: str = "",
) -> int:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        cur = conn.execute(
            """
            INSERT INTO personalized_picture_books (
                created_at, tenant_id, child_id, child_name, age,
                evaluation_ids_json, title, target_skills_json,
                book_json, profile_json, status, error_message
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                _now(),
                tid,
                (child_id or "").strip(),
                (child_name or "").strip(),
                int(age),
                json.dumps(evaluation_ids, ensure_ascii=False),
                (title or "").strip()[:200],
                json.dumps(target_skills, ensure_ascii=False),
                json.dumps(book, ensure_ascii=False),
                json.dumps(profile, ensure_ascii=False),
                status,
                (error_message or "")[:500],
            ),
        )
        return int(cur.lastrowid)


def get_book(book_id: int) -> Optional[dict[str, Any]]:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM personalized_picture_books WHERE id = ? AND tenant_id = ?",
            (book_id, tid),
        ).fetchone()
    if not row:
        return None
    return _row_to_dict(row)


def list_books(*, child_id: str, limit: int = 30) -> list[dict[str, Any]]:
    from tenant import current_tenant_id

    init_db()
    tid = current_tenant_id()
    cid = (child_id or "").strip()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT id, created_at, child_id, child_name, age, title,
                   target_skills_json, evaluation_ids_json, status
            FROM personalized_picture_books
            WHERE tenant_id = ? AND child_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (tid, cid, min(limit, 100)),
        ).fetchall()
    out = []
    for r in rows:
        item = _row_to_dict(r, include_book=False)
        try:
            book = json.loads(r["book_json"] or "{}")
            pages = book.get("pages") or []
            item["book"] = {"pages": pages[:1], "parent_tip": book.get("parent_tip", "")}
            if pages:
                item["cover_image"] = pages[0].get("image", "")
        except json.JSONDecodeError:
            item["book"] = {"pages": []}
        out.append(item)
    return out


def _row_to_dict(row: sqlite3.Row, *, include_book: bool = True) -> dict[str, Any]:
    out: dict[str, Any] = {
        "id": row["id"],
        "created_at": row["created_at"],
        "child_id": row["child_id"],
        "child_name": row["child_name"],
        "age": row["age"],
        "title": row["title"],
        "target_skills": json.loads(row["target_skills_json"] or "[]"),
        "evaluation_ids": json.loads(row["evaluation_ids_json"] or "[]"),
        "status": row["status"],
        "error_message": row["error_message"] if "error_message" in row.keys() else "",
    }
    if include_book:
        book = json.loads(row["book_json"] or "{}")
        profile = json.loads(row["profile_json"] or "{}")
        out["book"] = book
        out["profile"] = profile
        out["pages"] = book.get("pages") or []
    return out
