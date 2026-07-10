#!/usr/bin/env python3
"""仅从 bundle 训练 SC 双轨 XGB（跳过 BART/BERT，规避 macOS 段错误）。"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    os.chdir(ROOT)
    env = os.environ.copy()
    env.setdefault("NARRO_SKIP_XGB_CV", "1")
    env.setdefault("NARRO_XGB_N_JOBS", "1")
    env.setdefault("NARRO_MACRO_BUNDLE_CACHE", "data/macro_sc_dual_bundle.npz")
    env.setdefault("NARRO_SC_MAIN_DIR", "models/macro_sc_main")
    env.setdefault("NARRO_SC_DIRECT_DIR", "models/macro_sc_direct")
    env["PYTHONPATH"] = str(ROOT / "src")

    bundle = ROOT / env["NARRO_MACRO_BUNDLE_CACHE"]
    if not bundle.is_file():
        print(f"缺少 bundle: {bundle}")
        return 1

    print("=== SC 双轨 XGB-only（无 PyTorch）===")
    r = subprocess.run(
        [sys.executable, str(ROOT / "src" / "train_macro_xgb_bundle_only.py")],
        env=env,
    )
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
