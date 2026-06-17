"""讲故事 AI 引导与家长问卷。"""
from __future__ import annotations

import time

from api.schemas import ParentSurveyRequest, StoryCoachGuideRequest
from auth import require_access, require_user
from evaluation_store import get_evaluation, log_request, save_parent_survey
from fastapi import APIRouter, Depends, HTTPException
from parent_survey import load_likert_config, score_survey, triangulation_note
from story_coach import guide_child

router = APIRouter(tags=["coach"])


@router.get("/api/parent-survey/config")
def parent_survey_config(_: dict = Depends(require_user)):
    return load_likert_config()


@router.post("/api/evaluate/{evaluation_id}/parent-survey")
def submit_parent_survey(
    evaluation_id: int,
    body: ParentSurveyRequest,
    _: dict = Depends(require_user),
):
    row = get_evaluation(evaluation_id)
    if not row:
        raise HTTPException(status_code=404, detail="记录不存在")
    if (row.get("status") or "") not in ("completed", "pending"):
        pass
    scored = score_survey(body.answers)
    from datetime import datetime, timezone

    survey = {
        **scored,
        "answers": body.answers,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "triangulation": triangulation_note(
            scored,
            micro_sum=(row.get("microstructure") or {}).get("sum"),
            pred_sc_sum=(row.get("regression") or {}).get("pred_SC_Sum"),
        ),
    }
    save_parent_survey(evaluation_id, survey)
    return {"ok": True, "evaluation_id": evaluation_id, "parent_survey": survey}


@router.post("/api/story-coach/guide")
def story_coach_guide(body: StoryCoachGuideRequest, _: None = Depends(require_access)):
    t0 = time.time()
    try:
        out = guide_child(
            phase=body.phase,
            story_type=body.story_type,
            story_label=body.story_label or body.story_type,
            panel_index=body.panel_index,
            panel_total=body.panel_total,
            caption=body.caption,
            child_utterance=body.child_utterance,
            history=body.history,
            use_llm=body.use_llm,
        )
        log_request("/api/story-coach/guide", "POST", 200, "", int((time.time() - t0) * 1000))
        return out
    except Exception as e:
        log_request("/api/story-coach/guide", "POST", 500, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=500, detail="引导生成失败") from e
