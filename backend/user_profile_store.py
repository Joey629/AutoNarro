"""家庭/儿童基本信息（按登录用户隔离，供评估与洞察关联）。"""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from typing import Any

from evaluation_store import _db_path, init_db

DEFAULT_PROFILE: dict[str, Any] = {
    "caregiver_name": "",
    "child_name": "",
    "child_id": "",
    "age": 5,
    "gender": "",
    "left_behind": 0,
    "class_name": "",
    "notes": "",
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _row_to_profile(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "caregiver_name": row["caregiver_name"] or "",
        "child_name": row["child_name"] or "",
        "child_id": row["child_id"] or "",
        "age": int(row["age"]) if row["age"] is not None else 5,
        "gender": row["gender"] or "",
        "left_behind": int(row["left_behind"] or 0),
        "class_name": row["class_name"] or "",
        "notes": row["notes"] or "",
        "updated_at": row["updated_at"],
    }


def _ensure_profile_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS family_profile (
            user_id INTEGER PRIMARY KEY,
            caregiver_name TEXT NOT NULL DEFAULT '',
            child_name TEXT NOT NULL DEFAULT '',
            child_id TEXT NOT NULL DEFAULT '',
            age INTEGER NOT NULL DEFAULT 5,
            gender TEXT NOT NULL DEFAULT '',
            left_behind INTEGER NOT NULL DEFAULT 0,
            class_name TEXT NOT NULL DEFAULT '',
            notes TEXT NOT NULL DEFAULT '',
            updated_at TEXT NOT NULL
        )
        """
    )
    cols = {r[1] for r in conn.execute("PRAGMA table_info(family_profile)").fetchall()}
    if "user_id" in cols:
        return
    if "id" in cols:
        conn.execute(
            """
            CREATE TABLE family_profile_v2 (
                user_id INTEGER PRIMARY KEY,
                caregiver_name TEXT NOT NULL DEFAULT '',
                child_name TEXT NOT NULL DEFAULT '',
                child_id TEXT NOT NULL DEFAULT '',
                age INTEGER NOT NULL DEFAULT 5,
                gender TEXT NOT NULL DEFAULT '',
                left_behind INTEGER NOT NULL DEFAULT 0,
                class_name TEXT NOT NULL DEFAULT '',
                notes TEXT NOT NULL DEFAULT '',
                updated_at TEXT NOT NULL
            )
            """
        )
        conn.row_factory = sqlite3.Row
        legacy = conn.execute("SELECT * FROM family_profile WHERE id = 1").fetchone()
        if legacy:
            conn.execute(
                """
                INSERT INTO family_profile_v2 (
                    user_id, caregiver_name, child_name, child_id, age, gender,
                    left_behind, class_name, notes, updated_at
                ) VALUES (0, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    legacy["caregiver_name"],
                    legacy["child_name"],
                    legacy["child_id"],
                    legacy["age"],
                    legacy["gender"],
                    legacy["left_behind"],
                    legacy["class_name"],
                    legacy["notes"],
                    legacy["updated_at"],
                ),
            )
        conn.execute("DROP TABLE family_profile")
        conn.execute("ALTER TABLE family_profile_v2 RENAME TO family_profile")


def get_family_profile_for_user(user_id: int) -> dict[str, Any]:
    init_db()
    uid = int(user_id)
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        _ensure_profile_table(conn)
        row = conn.execute(
            "SELECT * FROM family_profile WHERE user_id = ?", (uid,)
        ).fetchone()
    if not row:
        return {**DEFAULT_PROFILE, "updated_at": None}
    return _row_to_profile(row)


def get_family_profile() -> dict[str, Any]:
    return get_family_profile_for_user(0)


def ensure_profile_for_user(user_id: int) -> dict[str, Any]:
    init_db()
    uid = int(user_id)
    existing = get_family_profile_for_user(uid)
    if existing.get("updated_at"):
        return existing
    now = _now_iso()
    with sqlite3.connect(_db_path()) as conn:
        _ensure_profile_table(conn)
        conn.execute(
            """
            INSERT OR IGNORE INTO family_profile (
                user_id, caregiver_name, child_name, child_id, age, gender,
                left_behind, class_name, notes, updated_at
            ) VALUES (?, '', '', '', 5, '', 0, '', '', ?)
            """,
            (uid, now),
        )
    return get_family_profile_for_user(uid)


def save_family_profile_for_user(user_id: int, data: dict[str, Any]) -> dict[str, Any]:
    init_db()
    uid = int(user_id)
    age = int(data.get("age", 5))
    if age < 3 or age > 12:
        age = 5
    left = 1 if int(data.get("left_behind", 0)) else 0
    payload = {
        "caregiver_name": (data.get("caregiver_name") or "").strip()[:64],
        "child_name": (data.get("child_name") or "").strip()[:64],
        "child_id": (data.get("child_id") or "").strip()[:64],
        "age": age,
        "gender": (data.get("gender") or "").strip()[:16],
        "left_behind": left,
        "class_name": (data.get("class_name") or "").strip()[:64],
        "notes": (data.get("notes") or "").strip()[:500],
        "updated_at": _now_iso(),
    }
    with sqlite3.connect(_db_path()) as conn:
        _ensure_profile_table(conn)
        conn.execute(
            """
            INSERT INTO family_profile (
                user_id, caregiver_name, child_name, child_id, age, gender,
                left_behind, class_name, notes, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                caregiver_name = excluded.caregiver_name,
                child_name = excluded.child_name,
                child_id = excluded.child_id,
                age = excluded.age,
                gender = excluded.gender,
                left_behind = excluded.left_behind,
                class_name = excluded.class_name,
                notes = excluded.notes,
                updated_at = excluded.updated_at
            """,
            (
                uid,
                payload["caregiver_name"],
                payload["child_name"],
                payload["child_id"],
                payload["age"],
                payload["gender"],
                payload["left_behind"],
                payload["class_name"],
                payload["notes"],
                payload["updated_at"],
            ),
        )
    return get_family_profile_for_user(uid)


def save_family_profile(data: dict[str, Any]) -> dict[str, Any]:
    return save_family_profile_for_user(0, data)
