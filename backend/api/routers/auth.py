"""用户注册、登录、会话。"""
from __future__ import annotations

from api.schemas import (
    AccountUpdateRequest,
    AuthLoginRequest,
    AuthRegisterRequest,
    ChangePasswordRequest,
)
from auth import require_user
from fastapi import APIRouter, Depends, Header, HTTPException

router = APIRouter(tags=["auth"])


@router.get("/api/auth/ping")
def auth_ping():
    """健康检查：确认认证路由已加载（部署后可用于排查 404）。"""
    return {"ok": True, "service": "narro-auth", "version": "1"}


@router.post("/api/auth/register")
def auth_register(body: AuthRegisterRequest):
    from account_store import create_session, register_user
    from user_profile_store import ensure_profile_for_user

    try:
        user = register_user(
            email=body.email,
            password=body.password,
            display_name=body.display_name,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    profile = ensure_profile_for_user(user["id"])
    token = create_session(user["id"])
    return {"ok": True, "token": token, "user": user, "profile": profile}


@router.post("/api/auth/login")
def auth_login(body: AuthLoginRequest):
    from account_store import authenticate_user, create_session

    user = authenticate_user(email=body.email, password=body.password)
    if not user:
        raise HTTPException(status_code=401, detail="邮箱或密码错误")
    from user_profile_store import get_family_profile_for_user

    token = create_session(user["id"])
    profile = get_family_profile_for_user(user["id"])
    return {"ok": True, "token": token, "user": user, "profile": profile}


@router.post("/api/auth/logout")
def auth_logout(authorization: str | None = Header(default=None)):
    from account_store import revoke_session

    if authorization and authorization.lower().startswith("bearer "):
        revoke_session(authorization[7:].strip())
    return {"ok": True}


@router.get("/api/auth/me")
def auth_me(user: dict = Depends(require_user)):
    from user_profile_store import get_family_profile_for_user

    profile = get_family_profile_for_user(user["id"])
    return {"ok": True, "user": user, "profile": profile}


@router.patch("/api/auth/account")
def auth_update_account(
    body: AccountUpdateRequest,
    user: dict = Depends(require_user),
):
    from account_store import update_user_account

    if user.get("id", 0) <= 0:
        raise HTTPException(status_code=401, detail="请先登录")
    payload = body.model_dump(exclude_unset=True)
    try:
        updated = update_user_account(user["id"], payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    return {"ok": True, "user": updated}


@router.post("/api/auth/change-password")
def auth_change_password(
    body: ChangePasswordRequest,
    user: dict = Depends(require_user),
):
    from account_store import authenticate_user, update_user_account

    if user.get("id", 0) <= 0:
        raise HTTPException(status_code=401, detail="请先登录")
    current = authenticate_user(email=user["email"], password=body.current_password)
    if not current:
        raise HTTPException(status_code=400, detail="当前密码不正确")
    updated = update_user_account(user["id"], {"password": body.new_password})
    return {"ok": True, "user": updated}
