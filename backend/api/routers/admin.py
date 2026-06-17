"""园所管理端聚合 API。"""
from __future__ import annotations

from auth import require_admin_key
from fastapi import APIRouter, Depends

router = APIRouter(tags=["admin"])


@router.get("/api/admin/overview")
def admin_overview(class_name: str | None = None, _: None = Depends(require_admin_key)):
    from admin_analytics import admin_overview as _overview

    return _overview(class_name=class_name)


@router.get("/api/admin/alerts")
def admin_alerts(class_name: str | None = None, _: None = Depends(require_admin_key)):
    from admin_analytics import _expert_norms_by_age_story, _load_all_evaluations, compute_alerts

    rows = _load_all_evaluations()
    if class_name:
        rows = [r for r in rows if (r.get("class_name") or "") == class_name]
    return {"alerts": compute_alerts(rows, _expert_norms_by_age_story())}


@router.get("/api/admin/children")
def admin_children(class_name: str | None = None, _: None = Depends(require_admin_key)):
    from admin_analytics import list_children

    return {"items": list_children(class_name=class_name)}
