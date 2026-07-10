#!/usr/bin/env python3
"""FastAPI 后端：儿童叙事自动评估 API。"""
from __future__ import annotations

import json
import os
import sys
from contextlib import asynccontextmanager
from pathlib import Path

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, os.path.join(_REPO_ROOT, "backend"))

from bootstrap import bootstrap_repo

bootstrap_repo()

from api.routers import (
    admin,
    auth,
    batch,
    coach_guide,
    evaluate,
    history,
    personalized_books,
    pn_agent,
    profile,
    system,
)
from evaluation_store import init_db, maybe_backfill_record_labels
from personalized_picture_book_store import init_db as init_personalized_books_db
from logging_config import setup_logging
from paths import FRONTEND_DIR, REPO_ROOT
from security import SecurityMiddleware

WEBSITE_DIR = REPO_ROOT / "website"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles

logger = setup_logging()

_NO_CACHE_HEADERS = {
    "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
    "Pragma": "no-cache",
    "Expires": "0",
}


def _cors_origins() -> list[str]:
    raw = os.environ.get("NARRO_CORS_ORIGINS", "").strip()
    if raw:
        return [o.strip() for o in raw.split(",") if o.strip()]
    return ["*"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    init_personalized_books_db()
    maybe_backfill_record_labels()
    try:
        from llm_service import is_llm_available

        if is_llm_available():
            logger.info("DeepSeek AI 辅导已启用")
        else:
            logger.warning(
                "DEEPSEEK_API_KEY 未生效：请在项目根目录 .env 填入密钥并保存，然后重启 python run_web.py"
            )
    except Exception:
        pass
    if os.environ.get("NARRO_PRELOAD_MODELS", "").strip().lower() in ("1", "true", "yes"):
        try:
            from evaluation_service import EvaluationService

            EvaluationService.get().load()
            logger.info("模型已预加载（NARRO_PRELOAD_MODELS=1）")
        except Exception as e:
            logger.warning("模型预加载失败: %s", e)
    logger.info("Narro API 启动 tenant=%s", os.environ.get("NARRO_TENANT_ID", "default"))
    auth_ok = "/api/auth/register" in app.openapi().get("paths", {})
    if not auth_ok:
        logger.error(
            "认证路由未注册：请从项目根目录执行 python run_web.py，并确认 backend/api/routers/auth.py 存在"
        )
    else:
        logger.info("认证 API 已就绪 (/api/auth/register, /api/auth/login)")
    yield
    logger.info("Narro API 关闭")


app = FastAPI(title="Narro 叙事评估", version="POC-1.3", lifespan=lifespan)
app.add_middleware(SecurityMiddleware)

_origins = _cors_origins()
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials="*" not in _origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system.router)
app.include_router(auth.router)
app.include_router(evaluate.router)
app.include_router(history.router)
app.include_router(admin.router)
app.include_router(profile.router)
app.include_router(batch.router)
app.include_router(coach_guide.router)
app.include_router(personalized_books.router)
app.include_router(pn_agent.router)


def _should_disable_browser_cache(path: str) -> bool:
    if path in ("/", "/platform", "/app"):
        return True
    if path.startswith("/static/") or path.startswith("/website/"):
        return path.endswith((".css", ".js", ".html", ".map"))
    return False


@app.middleware("http")
async def disable_frontend_cache(request, call_next):
    if os.environ.get("NARRO_ALLOW_STATIC_CACHE", "").strip() in ("1", "true", "yes"):
        return await call_next(request)
    response = await call_next(request)
    if _should_disable_browser_cache(request.url.path):
        for k, v in _NO_CACHE_HEADERS.items():
            response.headers[k] = v
    return response


@app.get("/robots.txt")
def robots_txt():
    return Response(
        content="User-agent: *\nDisallow: /data/\nDisallow: /api/\nAllow: /\n",
        media_type="text/plain",
    )


@app.get("/")
def marketing_home():
    if (WEBSITE_DIR / "index.html").is_file():
        return FileResponse(WEBSITE_DIR / "index.html", headers=_NO_CACHE_HEADERS)
    return FileResponse(FRONTEND_DIR / "index.html", headers=_NO_CACHE_HEADERS)


@app.get("/platform")
def saas_platform():
    return FileResponse(FRONTEND_DIR / "index.html", headers=_NO_CACHE_HEADERS)


@app.get("/app")
def saas_app_legacy():
    return RedirectResponse(url="/platform", status_code=301)


_static = FRONTEND_DIR / "static"
if _static.is_dir():
    app.mount("/static", StaticFiles(directory=_static), name="static")

_website_static = WEBSITE_DIR
if (_website_static / "css").is_dir():
    app.mount("/website", StaticFiles(directory=_website_static), name="website")
