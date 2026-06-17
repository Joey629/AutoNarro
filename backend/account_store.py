"""用户账户与会话（邮箱登录，供家庭版 SaaS）。"""
from __future__ import annotations

import hashlib
import re
import secrets
import sqlite3
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from evaluation_store import _db_path, init_db

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_SESSION_DAYS = 30
_PBKDF2_ITERATIONS = 210_000


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${_PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"


def _verify_password(password: str, stored: str) -> bool:
    try:
        algo, iters_s, salt_hex, digest_hex = stored.split("$", 3)
        if algo != "pbkdf2_sha256":
            return False
        iters = int(iters_s)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
        got = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iters)
        return secrets.compare_digest(got, expected)
    except (ValueError, TypeError):
        return False


def ensure_account_tables(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            display_name TEXT NOT NULL DEFAULT '',
            avatar_id TEXT NOT NULL DEFAULT 'default',
            phone TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS user_sessions (
            token TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
    )


def _user_row_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "id": int(row["id"]),
        "email": row["email"] or "",
        "display_name": row["display_name"] or "",
        "avatar_id": row["avatar_id"] or "default",
        "phone": row["phone"] or "",
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }


def register_user(*, email: str, password: str, display_name: str = "") -> dict[str, Any]:
    init_db()
    email_clean = (email or "").strip().lower()
    if not _EMAIL_RE.match(email_clean):
        raise ValueError("邮箱格式不正确")
    if len(password or "") < 8:
        raise ValueError("密码至少 8 位")
    name = (display_name or "").strip()[:64] or email_clean.split("@")[0][:64]
    now = _now_iso()
    with sqlite3.connect(_db_path()) as conn:
        ensure_account_tables(conn)
        if conn.execute("SELECT 1 FROM users WHERE email = ?", (email_clean,)).fetchone():
            raise ValueError("该邮箱已注册")
        cur = conn.execute(
            """
            INSERT INTO users (email, password_hash, display_name, avatar_id, phone, created_at, updated_at)
            VALUES (?, ?, ?, 'default', '', ?, ?)
            """,
            (email_clean, _hash_password(password), name, now, now),
        )
        user_id = int(cur.lastrowid)
    user = get_user_by_id(user_id)
    assert user
    return user


def authenticate_user(*, email: str, password: str) -> Optional[dict[str, Any]]:
    init_db()
    email_clean = (email or "").strip().lower()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        ensure_account_tables(conn)
        row = conn.execute("SELECT * FROM users WHERE email = ?", (email_clean,)).fetchone()
    if not row or not _verify_password(password, row["password_hash"]):
        return None
    return _user_row_to_dict(row)


def create_session(user_id: int) -> str:
    init_db()
    token = secrets.token_urlsafe(32)
    now = datetime.now(timezone.utc)
    expires = now + timedelta(days=_SESSION_DAYS)
    with sqlite3.connect(_db_path()) as conn:
        ensure_account_tables(conn)
        conn.execute(
            """
            INSERT INTO user_sessions (token, user_id, created_at, expires_at)
            VALUES (?, ?, ?, ?)
            """,
            (token, user_id, now.isoformat(), expires.isoformat()),
        )
    return token


def revoke_session(token: str) -> None:
    if not token:
        return
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        ensure_account_tables(conn)
        conn.execute("DELETE FROM user_sessions WHERE token = ?", (token.strip(),))


def get_user_by_token(token: str) -> Optional[dict[str, Any]]:
    if not token:
        return None
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        ensure_account_tables(conn)
        row = conn.execute(
            """
            SELECT u.* FROM user_sessions s
            JOIN users u ON u.id = s.user_id
            WHERE s.token = ? AND s.expires_at > ?
            """,
            (token.strip(), _now_iso()),
        ).fetchone()
    if not row:
        return None
    return _user_row_to_dict(row)


def get_user_by_id(user_id: int) -> Optional[dict[str, Any]]:
    init_db()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        ensure_account_tables(conn)
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return _user_row_to_dict(row) if row else None


def update_user_account(user_id: int, data: dict[str, Any]) -> dict[str, Any]:
    init_db()
    fields = []
    values: list[Any] = []
    if "display_name" in data:
        fields.append("display_name = ?")
        values.append((data.get("display_name") or "").strip()[:64])
    if "avatar_id" in data:
        aid = (data.get("avatar_id") or "default").strip()[:32]
        if aid not in ALLOWED_AVATAR_IDS:
            aid = "default"
        fields.append("avatar_id = ?")
        values.append(aid)
    if "phone" in data:
        fields.append("phone = ?")
        values.append((data.get("phone") or "").strip()[:32])
    if "password" in data and data["password"]:
        pwd = data["password"]
        if len(pwd) < 8:
            raise ValueError("新密码至少 8 位")
        fields.append("password_hash = ?")
        values.append(_hash_password(pwd))
    if not fields:
        user = get_user_by_id(user_id)
        if not user:
            raise ValueError("用户不存在")
        return user
    fields.append("updated_at = ?")
    values.append(_now_iso())
    values.append(user_id)
    with sqlite3.connect(_db_path()) as conn:
        ensure_account_tables(conn)
        conn.execute(f"UPDATE users SET {', '.join(fields)} WHERE id = ?", values)
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("用户不存在")
    return user


ALLOWED_AVATAR_IDS = frozenset({"default", "child-boy", "child-girl", "caregiver"})
