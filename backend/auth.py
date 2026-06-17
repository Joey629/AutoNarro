"""API Key 鉴权：用户 Key / 管理员 Key，支持 fail-closed。"""
from __future__ import annotations

import os

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
            return user
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


def require_admin_key(x_api_key: str | None = Header(default=None, alias="X-API-Key")) -> None:
    """管理端 API：优先 NARRO_ADMIN_API_KEY；未配置时回退 NARRO_API_KEY。"""
    require = _require_key_enabled()
    admin = _admin_api_key_expected()
    user = _user_api_key_expected()
    if admin:
        if not x_api_key or x_api_key != admin:
            raise HTTPException(status_code=403, detail="需要有效管理员 X-API-Key")
        return
    if user:
        if not x_api_key or x_api_key != user:
            raise HTTPException(status_code=401, detail="无效或缺少 X-API-Key")
        return
    if require:
        raise HTTPException(
            status_code=503,
            detail="NARRO_REQUIRE_API_KEY=1 但未设置 NARRO_API_KEY / NARRO_ADMIN_API_KEY",
        )
