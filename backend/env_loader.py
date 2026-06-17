"""从仓库根目录加载 .env（任意启动方式均生效）。"""
from __future__ import annotations

import os
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOADED = False


def load_dotenv(force: bool = False) -> None:
    global _LOADED
    if _LOADED and not force:
        return
    path = _REPO_ROOT / ".env"
    if not path.is_file():
        _LOADED = True
        return
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if not key or not val:
                continue
            # .env 中的非空值优先（修复 shell 里空变量挡住 setdefault）
            os.environ[key] = val
    _migrate_legacy_autonarro_env()
    _LOADED = True


def _migrate_legacy_autonarro_env() -> None:
    """AUTONARRO_* → NARRO_*（不覆盖已有 NARRO_*）。"""
    for key, val in list(os.environ.items()):
        if not key.startswith("AUTONARRO_"):
            continue
        os.environ.setdefault("NARRO_" + key[len("AUTONARRO_") :], val)
