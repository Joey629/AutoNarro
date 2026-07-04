"""Vercel FastAPI entrypoint (standard api/index.py location)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_BACKEND = _ROOT / "backend"
_SRC = _ROOT / "src"
for p in (_SRC, _BACKEND):
    s = str(p)
    if s not in sys.path:
        sys.path.insert(0, s)
os.chdir(_ROOT)

from api.main import app  # noqa: E402

__all__ = ["app"]
