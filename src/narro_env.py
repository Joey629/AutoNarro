"""Narro 环境变量；兼容旧 AUTONARRO_* 前缀。"""
from __future__ import annotations

import os


def migrate_legacy_env() -> None:
    """若仅设置 AUTONARRO_* / 旧 NARRO_M4_*，则映射到 NARRO_*（不覆盖已显式设置的 NARRO_*）。"""
    legacy_m4 = {
        "NARRO_M4_CONFIG": "NARRO_MICRO_CONFIG",
        "NARRO_M4_CKPT": "NARRO_MICRO_CKPT",
        "NARRO_M4_MODEL": "NARRO_MICRO_MODEL",
        "AUTONARRO_M4_CONFIG": "NARRO_MICRO_CONFIG",
        "AUTONARRO_M4_CKPT": "NARRO_MICRO_CKPT",
        "AUTONARRO_M4_MODEL": "NARRO_MICRO_MODEL",
    }
    for old, new in legacy_m4.items():
        if os.environ.get(old) and not os.environ.get(new):
            os.environ[new] = os.environ[old]

    for key, val in list(os.environ.items()):
        if not key.startswith("AUTONARRO_"):
            continue
        new_key = "NARRO_" + key[len("AUTONARRO_") :]
        os.environ.setdefault(new_key, val)


def env(name: str, default: str = "") -> str:
    """读取 NARRO_<name>，回退 AUTONARRO_<name>。"""
    migrate_legacy_env()
    return os.environ.get(f"NARRO_{name}") or os.environ.get(f"AUTONARRO_{name}", default)


migrate_legacy_env()
