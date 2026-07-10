"""Vercel FastAPI entrypoint (standard api/index.py location)."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "backend"))

from bootstrap import bootstrap_repo

bootstrap_repo()

from api.main import app  # noqa: E402

__all__ = ["app"]
