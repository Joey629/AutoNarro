"""家庭档案与洞察。"""
from __future__ import annotations

from api.schemas import FamilyProfileUpdate
from auth import require_user
from fastapi import APIRouter, Depends

router = APIRouter(tags=["profile"])


@router.get("/api/profile")
def get_profile(user: dict = Depends(require_user)):
    from user_profile_store import get_family_profile_for_user

    profile = get_family_profile_for_user(user["id"])
    return {"ok": True, "profile": profile, "user": user}


@router.put("/api/profile")
def put_profile(body: FamilyProfileUpdate, user: dict = Depends(require_user)):
    from user_profile_store import save_family_profile_for_user

    profile = save_family_profile_for_user(user["id"], body.model_dump())
    return {"ok": True, "profile": profile, "user": user}


@router.post("/api/profile")
def post_profile(body: FamilyProfileUpdate, user: dict = Depends(require_user)):
    return put_profile(body, user)


@router.get("/api/insights")
def insights(user: dict = Depends(require_user)):
    from admin_analytics import user_insights

    return user_insights()
