"""统一入口：仓库根目录、sys.path、.env。"""
from __future__ import annotations

import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent


def repo_root() -> Path:
    return _REPO_ROOT


def bootstrap_repo() -> Path:
    root = str(_REPO_ROOT)
    for sub in ("src", "backend"):
        p = os.path.join(root, sub)
        if p not in sys.path:
            sys.path.insert(0, p)
    os.chdir(root)
    from env_loader import load_dotenv

    load_dotenv()
    return _REPO_ROOT
