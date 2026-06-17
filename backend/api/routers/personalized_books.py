"""专属练习绘本：多次评估 → DeepSeek 文本 → 场景 SVG 插画。"""
from __future__ import annotations

from api.schemas import PersonalizedBookGenerateRequest
from auth import require_access
from fastapi import APIRouter, Depends, HTTPException
from llm_service import is_llm_available
from personalized_picture_book_service import (
    generate_for_child,
    get_book,
    get_child_generation_status,
    list_books,
)
from personalized_picture_book_store import init_db

router = APIRouter(tags=["personalized-books"])


@router.get("/api/personalized-picture-books/status")
def personalized_status(
    child_id: str = "",
    _: None = Depends(require_access),
):
    init_db()
    return get_child_generation_status(child_id)


@router.get("/api/personalized-picture-books")
def personalized_list(
    child_id: str = "",
    limit: int = 30,
    _: None = Depends(require_access),
):
    init_db()
    if not (child_id or "").strip():
        return {"items": [], "message": "请提供 child_id"}
    return {"items": list_books(child_id=child_id, limit=min(limit, 100))}


@router.get("/api/personalized-picture-books/{book_id}")
def personalized_detail(book_id: int, _: None = Depends(require_access)):
    init_db()
    row = get_book(book_id)
    if not row:
        raise HTTPException(status_code=404, detail="绘本不存在")
    return row


@router.post("/api/personalized-picture-books/generate")
def personalized_generate(
    body: PersonalizedBookGenerateRequest,
    _: None = Depends(require_access),
):
    init_db()
    if not is_llm_available():
        raise HTTPException(
            status_code=503,
            detail="未配置 DeepSeek API。绘本文字需 LLM；插画使用内置场景图（非文生图）。",
        )
    try:
        return generate_for_child(
            child_id=body.child_id,
            child_name=body.child_name,
            evaluation_ids=body.evaluation_ids or None,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"生成失败：{e}") from e
