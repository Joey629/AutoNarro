"""生产部署安全：阻断语料泄露路径、安全响应头、可选强制 API Key。"""
from __future__ import annotations

import os
import re
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

# 禁止通过 HTTP 访问的路径模式（含 narratives.csv 与原始语料）
_BLOCKED_PATH_RE = re.compile(
    r"(^/data/)|"
    r"(narratives\.csv)|"
    r"(\.csv$)|"
    r"(^/models/)|"
    r"(^/src/)|"
    r"(^/configs/llm_config\.json)|"
    r"(evaluations\.db)",
    re.I,
)

# 仅允许公开的静态前缀（营销站 + 前端）
_PUBLIC_PREFIXES = (
    "/static/",
    "/website/",
    "/platform",
    "/app",
    "/api/health",
    "/api/meta",
    "/api/about",
    "/robots.txt",
    "/favicon.ico",
)


class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if _BLOCKED_PATH_RE.search(path) and not path.startswith("/api/"):
            return JSONResponse({"detail": "禁止访问"}, status_code=403)

        if path.startswith("/api/") and os.environ.get("NARRO_REQUIRE_API_KEY", "").lower() in (
            "1",
            "true",
            "yes",
        ):
            expected = os.environ.get("NARRO_API_KEY", "").strip()
            if expected:
                key = request.headers.get("x-api-key") or request.headers.get("X-API-Key")
                if key != expected:
                    return JSONResponse({"detail": "需要有效 X-API-Key"}, status_code=401)

        response: Response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "microphone=(self), camera=()"
        if os.environ.get("NARRO_HTTPS", "").lower() in ("1", "true", "yes"):
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response
