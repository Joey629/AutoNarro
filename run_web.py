#!/usr/bin/env python3
"""启动 Web 服务：前端 http://127.0.0.1:8000"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "backend"))

from bootstrap import bootstrap_repo

bootstrap_repo()

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8000"))
    print(f"金声玉叙 → http://127.0.0.1:{port}")
    uvicorn.run(
        "backend.api.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )
