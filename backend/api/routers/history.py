"""评估历史、导出、专家标注。"""
from __future__ import annotations

import csv
import io

from api.schemas import ChatRequest, ExpertOverrideRequest, RecordLabelRequest
from auth import require_access
from evaluation_store import (
    delete_evaluation,
    get_evaluation,
    list_evaluations,
    save_expert_override,
    update_record_label,
)
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

router = APIRouter(tags=["history"])

EXPERT_OVERRIDE_FIELDS = frozenset(
    {"pred_SC_Sum", "micro_sum", *[f"A{i}" for i in range(2, 17)]}
)


@router.get("/api/history")
def history(
    limit: int = 50,
    child_id: str | None = None,
    _: None = Depends(require_access),
):
    return {"items": list_evaluations(limit=min(limit, 200), child_id=child_id)}


@router.get("/api/history/{evaluation_id}")
def history_detail(evaluation_id: int, _: None = Depends(require_access)):
    row = get_evaluation(evaluation_id)
    if not row:
        raise HTTPException(status_code=404, detail="记录不存在")
    return row


def _rename_evaluation(evaluation_id: int, record_label: str) -> dict:
    if not get_evaluation(evaluation_id):
        raise HTTPException(status_code=404, detail="记录不存在")
    if not update_record_label(evaluation_id, record_label):
        raise HTTPException(status_code=400, detail="名称无效")
    return {"ok": True, "evaluation_id": evaluation_id, "record_label": record_label.strip()}


def _delete_evaluation_record(evaluation_id: int) -> dict:
    if not get_evaluation(evaluation_id):
        raise HTTPException(status_code=404, detail="记录不存在")
    if not delete_evaluation(evaluation_id):
        raise HTTPException(status_code=404, detail="记录不存在")
    return {"ok": True, "evaluation_id": evaluation_id}


@router.patch("/api/history/{evaluation_id}")
def history_rename_patch(
    evaluation_id: int,
    body: RecordLabelRequest,
    _: None = Depends(require_access),
):
    return _rename_evaluation(evaluation_id, body.record_label)


@router.post("/api/history/{evaluation_id}/rename")
def history_rename_post(
    evaluation_id: int,
    body: RecordLabelRequest,
    _: None = Depends(require_access),
):
    """POST 别名：部分反向代理/旧部署对 PATCH 返回 405 时使用。"""
    return _rename_evaluation(evaluation_id, body.record_label)


@router.delete("/api/history/{evaluation_id}")
def history_delete_http(evaluation_id: int, _: None = Depends(require_access)):
    return _delete_evaluation_record(evaluation_id)


@router.post("/api/history/{evaluation_id}/delete")
def history_delete_post(evaluation_id: int, _: None = Depends(require_access)):
    """POST 别名：部分环境对 DELETE 返回 405 时使用。"""
    return _delete_evaluation_record(evaluation_id)


@router.get("/api/history/{evaluation_id}/export")
def export_evaluation(
    evaluation_id: int,
    format: str = "txt",
    _: None = Depends(require_access),
):
    row = get_evaluation(evaluation_id)
    if not row:
        raise HTTPException(status_code=404, detail="记录不存在")
    if format == "txt":
        return Response(
            content=(row["report_text"] or "").encode("utf-8"),
            media_type="text/plain; charset=utf-8",
            headers={"Content-Disposition": f'attachment; filename="report_{evaluation_id}.txt"'},
        )
    if format == "csv":
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(
            [
                "id",
                "model_version",
                "created_at",
                "story_type",
                "task_type",
                "age",
                "pred_SC_Sum",
                "micro_sum",
            ]
        )
        w.writerow(
            [
                row["id"],
                row.get("model_version", ""),
                row["created_at"],
                row["story_type"],
                row["task_type"],
                row["age"],
                row["regression"].get("pred_SC_Sum"),
                row["microstructure"].get("sum"),
            ]
        )
        return Response(
            content=buf.getvalue().encode("utf-8-sig"),
            media_type="text/csv; charset=utf-8",
            headers={"Content-Disposition": f'attachment; filename="report_{evaluation_id}.csv"'},
        )
    raise HTTPException(status_code=400, detail="format 须为 txt 或 csv")


@router.post("/api/history/{evaluation_id}/override")
def expert_override(
    evaluation_id: int,
    body: ExpertOverrideRequest,
    _: None = Depends(require_access),
):
    if body.field not in EXPERT_OVERRIDE_FIELDS:
        raise HTTPException(status_code=400, detail="不支持的 override 字段")
    row = get_evaluation(evaluation_id)
    if not row:
        raise HTTPException(status_code=404, detail="记录不存在")
    orig = ""
    if body.field == "pred_SC_Sum":
        orig = str(row["regression"].get("pred_SC_Sum", ""))
    elif body.field == "micro_sum":
        orig = str(row["microstructure"].get("sum", ""))
    oid = save_expert_override(
        evaluation_id,
        body.field,
        body.override_value,
        original_value=orig,
        note=body.note,
        reviewer=body.reviewer,
    )
    return {"ok": True, "override_id": oid, "evaluation_id": evaluation_id}


@router.post("/api/chat")
def chat(req: ChatRequest, _: None = Depends(require_access)):
    from llm_service import free_chat, is_llm_available

    if not is_llm_available():
        raise HTTPException(status_code=503, detail="未配置 DEEPSEEK_API_KEY")
    row = get_evaluation(req.evaluation_id) if req.evaluation_id else None
    if req.evaluation_id and not row:
        raise HTTPException(status_code=404, detail="评估记录不存在")
    try:
        reply = free_chat(row, req.message.strip(), req.history)
        return {"ok": True, "reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail="对话请求失败") from e


@router.get("/api/children/{child_id}/timeline")
def child_timeline(child_id: str, limit: int = 100, _: None = Depends(require_access)):
    from admin_analytics import child_growth_series
    from evaluation_store import list_child_timeline

    cid = child_id.strip()
    items = list_child_timeline(cid, limit=min(limit, 500))
    if not items:
        raise HTTPException(status_code=404, detail="未找到该儿童的评估记录")
    growth = child_growth_series(cid)
    return {"child_id": cid, "count": len(items), "items": items, "growth": growth}
