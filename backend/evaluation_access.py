"""评估记录访问控制：登录用户仅能访问本人记录。"""
from __future__ import annotations

from fastapi import HTTPException


def list_filter_user_id(current_user: dict | None) -> int | None:
    uid = int((current_user or {}).get("id") or 0)
    return uid if uid > 0 else None


def evaluation_visible_to_user(row_user_id: int | None, current_user: dict | None) -> bool:
    uid = int((current_user or {}).get("id") or 0)
    rid = int(row_user_id or 0)
    if uid <= 0:
        return rid <= 0
    return rid == uid


def assert_evaluation_access(row: dict, current_user: dict | None) -> None:
    if not evaluation_visible_to_user(row.get("user_id"), current_user):
        raise HTTPException(status_code=404, detail="记录不存在")


def get_evaluation_for_user(evaluation_id: int, current_user: dict | None):
    from evaluation_store import get_evaluation

    row = get_evaluation(evaluation_id)
    if not row:
        raise HTTPException(status_code=404, detail="记录不存在")
    assert_evaluation_access(row, current_user)
    return row
