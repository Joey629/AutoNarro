"""API Key 鉴权：用户 Key / 管理员 Key，支持 fail-closed。"""
from __future__ import annotations

import os
import secrets

from fastapi import Header, HTTPException


def _require_key_enabled() -> bool:
    return os.environ.get("NARRO_REQUIRE_API_KEY", "").strip().lower() in (
        "1",
        "true",
        "yes",
    )


def _user_api_key_expected() -> str:
    return os.environ.get("NARRO_API_KEY", "").strip()


def _admin_api_key_expected() -> str:
    return os.environ.get("NARRO_ADMIN_API_KEY", "").strip()


def admin_emails() -> set[str]:
    raw = os.environ.get("NARRO_ADMIN_EMAILS", "") or os.environ.get("NARRO_ADMIN_EMAIL", "")
    return {part.strip().lower() for part in raw.split(",") if part.strip()}


def is_admin_user(user: dict | None) -> bool:
    if not user:
        return False
    email = (user.get("email") or "").strip().lower()
    from account_store import builtin_admin_login

    if email == builtin_admin_login():
        return True
    allowed = admin_emails()
    return email in allowed if allowed else False


def public_user(user: dict) -> dict:
    out = dict(user)
    out["is_admin"] = is_admin_user(user)
    return out


def optional_api_key(x_api_key: str | None = Header(default=None, alias="X-API-Key")) -> None:
    """兼容旧路由：配置了 Key 则校验；NARRO_REQUIRE_API_KEY=1 时未配置 Key 则拒绝。"""
    require = _require_key_enabled()
    expected = _user_api_key_expected()
    if require and not expected:
        raise HTTPException(
            status_code=503,
            detail="NARRO_REQUIRE_API_KEY=1 但未设置 NARRO_API_KEY",
        )
    if require or expected:
        if not x_api_key or x_api_key != expected:
            raise HTTPException(status_code=401, detail="无效或缺少 X-API-Key")


def require_api_key(x_api_key: str | None = Header(default=None, alias="X-API-Key")) -> None:
    """敏感用户 API：REQUIRE=1 时必须带有效用户 Key。"""
    optional_api_key(x_api_key)


def _bearer_token(authorization: str | None) -> str | None:
    if authorization and authorization.lower().startswith("bearer "):
        return authorization[7:].strip() or None
    return None


def _guest_user() -> dict:
    return {
        "id": 0,
        "email": "",
        "display_name": "访客",
        "avatar_id": "default",
        "phone": "",
    }


def resolve_current_user(
    authorization: str | None = Header(default=None),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict | None:
    """Bearer 会话优先；配置了 API Key 时校验 Key 后返回访客；否则开放模式下返回访客。"""
    token = _bearer_token(authorization)
    if token:
        from account_store import get_user_by_token

        user = get_user_by_token(token)
        if user:
            return public_user(user)
    expected = _user_api_key_expected()
    require = _require_key_enabled()
    if require or expected:
        try:
            optional_api_key(x_api_key)
        except HTTPException:
            return None
    return _guest_user()


def require_user(
    authorization: str | None = Header(default=None),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict:
    """须为已登录用户（不接受开放模式下的访客）。"""
    user = resolve_current_user(authorization, x_api_key)
    if not user or user.get("id", 0) <= 0:
        raise HTTPException(status_code=401, detail="请先登录")
    return user


def require_access(
    authorization: str | None = Header(default=None),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict:
    """已登录用户、有效 API Key，或开放模式下的访客。"""
    user = resolve_current_user(authorization, x_api_key)
    if not user:
        raise HTTPException(status_code=401, detail="请先登录或提供 API Key")
    return user


def _admin_key_ok(x_api_key: str | None) -> bool:
    if not x_api_key:
        return False
    admin = _admin_api_key_expected()
    if admin and secrets.compare_digest(x_api_key, admin):
        return True
    user = _user_api_key_expected()
    if user and not admin and secrets.compare_digest(x_api_key, user):
        return True
    return False


def require_admin_access(
    authorization: str | None = Header(default=None),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict:
    """管理端 API：管理员会话或有效管理员 API Key。"""
    if _admin_key_ok(x_api_key):
        return {"id": 0, "email": "", "display_name": "API 管理员", "is_admin": True}

    user = resolve_current_user(authorization, x_api_key)
    if user and user.get("id", 0) > 0 and is_admin_user(user):
        return user

    require = _require_key_enabled()
    if require and not _admin_api_key_expected() and not _user_api_key_expected():
        raise HTTPException(
            status_code=503,
            detail="NARRO_REQUIRE_API_KEY=1 但未设置 NARRO_API_KEY / NARRO_ADMIN_API_KEY",
        )
    raise HTTPException(status_code=403, detail="需要管理员权限")


def require_admin_key(
    authorization: str | None = Header(default=None),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> None:
    """兼容旧依赖：管理员会话或 API Key。"""
    require_admin_access(authorization=authorization, x_api_key=x_api_key)
