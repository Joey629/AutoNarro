"""单条评估与教练对话。"""
from __future__ import annotations

import time

from api.schemas import CoachRequest, EvaluateRequest
from auth import require_access
from evaluation_service import EvaluationService
from evaluation_store import get_evaluation, log_request
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(tags=["evaluate"])


@router.post("/api/evaluate")
def evaluate(req: EvaluateRequest, _: None = Depends(require_access)):
    t0 = time.time()
    try:
        out = EvaluationService.get().start_evaluation_async(
            req.text.strip(),
            req.age,
            req.left_behind,
            story_type=req.story_type,
            task_type=req.task_type,
            child_id=req.child_id,
            child_name=req.child_name,
            class_name=req.class_name,
            source="web_single",
            coach_mode=req.coach_mode or "free",
            dialogue_log=req.dialogue_log or [],
        )
        log_request("/api/evaluate", "POST", 200, "", int((time.time() - t0) * 1000))
        return out
    except HTTPException:
        raise
    except RuntimeError as e:
        log_request("/api/evaluate", "POST", 503, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=503, detail=str(e)) from e
    except Exception as e:
        log_request("/api/evaluate", "POST", 500, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=500, detail="评估失败，请稍后重试") from e


@router.post("/api/evaluate/{evaluation_id}/coach")
def evaluation_coach(
    evaluation_id: int,
    body: CoachRequest,
    _: None = Depends(require_access),
):
    from llm_service import coach_after_evaluation, is_llm_available

    if not is_llm_available():
        raise HTTPException(
            status_code=503,
            detail="未配置 DeepSeek：请设置 DEEPSEEK_API_KEY 并复制 llm_config.json",
        )
    row = get_evaluation(evaluation_id)
    if not row:
        raise HTTPException(status_code=404, detail="记录不存在")
    try:
        reply = coach_after_evaluation(row, body.question)
        return {"ok": True, "evaluation_id": evaluation_id, "reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail="辅导请求失败") from e
