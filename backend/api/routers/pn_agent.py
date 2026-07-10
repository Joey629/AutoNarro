"""PN agent 语音通话对话。"""
from __future__ import annotations

import time

from api.schemas import PnAgentChatRequest, PnAgentSaveRequest, PnAgentTtsRequest
from auth import require_access
from evaluation_store import log_request, save_pn_agent_session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

router = APIRouter(tags=["pn-agent"])


@router.post("/api/pn-agent/chat")
def pn_agent_chat_endpoint(body: PnAgentChatRequest, _: None = Depends(require_access)):
    from llm_service import is_llm_available, pn_agent_chat

    if not is_llm_available():
        raise HTTPException(status_code=503, detail="未配置 DEEPSEEK_API_KEY")
    t0 = time.time()
    try:
        reply, session = pn_agent_chat(
            body.message.strip(),
            body.history,
            body.session,
            child_name=body.child_name,
            child_age=body.child_age,
        )
        log_request("/api/pn-agent/chat", "POST", 200, "", int((time.time() - t0) * 1000))
        return {"ok": True, "reply": reply, "session": session}
    except Exception as e:
        log_request("/api/pn-agent/chat", "POST", 500, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=500, detail="PN 对话请求失败") from e


@router.post("/api/pn-agent/sessions")
def pn_agent_save_session(body: PnAgentSaveRequest, user: dict = Depends(require_access)):
    t0 = time.time()
    try:
        age = body.child_age if body.child_age is not None else 5
        eid = save_pn_agent_session(
            dialogue_log=body.dialogue_log,
            child_id=body.child_id,
            child_name=body.child_name,
            age=age,
            class_name=body.class_name,
            elapsed_ms=body.elapsed_ms,
            session=body.session,
            user_id=int(user.get("id") or 0),
        )
        log_request("/api/pn-agent/sessions", "POST", 200, str(eid), int((time.time() - t0) * 1000))
        return {"ok": True, "evaluation_id": eid}
    except ValueError as e:
        log_request("/api/pn-agent/sessions", "POST", 400, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        log_request("/api/pn-agent/sessions", "POST", 500, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=500, detail="保存通话记录失败") from e


@router.get("/api/pn-agent/tts/status")
def pn_agent_tts_status(_: None = Depends(require_access)):
    from volc_tts_service import volc_tts_config

    return volc_tts_config()


@router.post("/api/pn-agent/tts")
def pn_agent_tts(body: PnAgentTtsRequest, _: None = Depends(require_access)):
    from volc_tts_service import is_volc_tts_available, synthesize_speech

    if not is_volc_tts_available():
        raise HTTPException(
            status_code=503,
            detail="未配置豆包语音：请设置 VOLC_TTS_APP_ID 与 VOLC_TTS_ACCESS_TOKEN",
        )
    t0 = time.time()
    try:
        audio, mime = synthesize_speech(
            body.text.strip(),
            speed_ratio=body.speed_ratio,
            pitch_ratio=body.pitch_ratio,
        )
        log_request("/api/pn-agent/tts", "POST", 200, "", int((time.time() - t0) * 1000))
        return Response(content=audio, media_type=mime)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except RuntimeError as e:
        log_request("/api/pn-agent/tts", "POST", 503, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=503, detail=str(e)) from e
    except Exception as e:
        log_request("/api/pn-agent/tts", "POST", 500, str(e), int((time.time() - t0) * 1000))
        raise HTTPException(status_code=500, detail="语音合成失败") from e
