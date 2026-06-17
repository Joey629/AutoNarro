#!/usr/bin/env python3
"""启动 Web 服务：前端 http://127.0.0.1:8000"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
for sub in ("src", "backend"):
    p = os.path.join(ROOT, sub)
    if p not in sys.path:
        sys.path.insert(0, p)
os.chdir(ROOT)


if __name__ == "__main__":
    sys.path.insert(0, os.path.join(ROOT, "backend"))
    from env_loader import load_dotenv

    load_dotenv()
    import uvicorn

    port = int(os.environ.get("PORT", "8000"))
    print(f"Narro Web → http://127.0.0.1:{port}")
    uvicorn.run(
        "backend.api.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )
