#!/usr/bin/env python3
"""重训宏观 SC 双轨（轨 A MAIN + 轨 B 直接 SC，序数 XGB）。

  PYTHONPATH=src python scripts/train_macro.py

默认输出 models/macro_sc_main/ 与 models/macro_sc_direct/。
设 NARRO_SC_DUAL_TRAIN=0 可仅训 legacy 回归至 NARRO_MACRO_OUTPUT_DIR。

见 docs/SC_DUAL_TRACK.md、docs/TRAINING.md。
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    os.chdir(ROOT)
    env = os.environ.copy()
    env.setdefault("NARRO_MICRO_CKPT", "models/micro_narro_v4.pth")
    env.setdefault("NARRO_MICRO_MODEL", "Morton-Li/QiDeBERTa-base")
    env.setdefault("NARRO_MICRO_CONFIG", "configs/micro_narro_v4.json")
    env.setdefault("NARRO_SC_DUAL_TRAIN", "1")
    env.setdefault("NARRO_SC_MAIN_DIR", "models/macro_sc_main")
    env.setdefault("NARRO_SC_DIRECT_DIR", "models/macro_sc_direct")
    env.setdefault(
        "NARRO_MACRO_OUTPUT_DIR",
        "models/macro_xgb_narro_v4",
    )
    env.setdefault("NARRO_BART_DIR", "models/bart_narro_v4")
    env.setdefault("NARRO_BART_FORCE_CPU", "1")
    env["PYTHONPATH"] = str(ROOT / "src")

    ckpt = ROOT / env["NARRO_MICRO_CKPT"]
    if not ckpt.is_file():
        print(f"缺少宏观 SS 权重: {ckpt}")
        print("请先: PYTHONPATH=src python scripts/train_micro.py --skip-smoke")
        return 1

    print("=== Narro v4 宏观 SC 双轨训练 ===")
    print(f"  宏观 SS: {env['NARRO_MICRO_CKPT']}")
    print(f"  BART: {env['NARRO_BART_DIR']}")
    if env.get("NARRO_SC_DUAL_TRAIN", "1") == "1":
        print(f"  轨 A (MAIN): {env['NARRO_SC_MAIN_DIR']}")
        print(f"  轨 B (直接): {env['NARRO_SC_DIRECT_DIR']}")
    else:
        print(f"  legacy 输出: {env['NARRO_MACRO_OUTPUT_DIR']}")
    r = subprocess.run(
        [sys.executable, str(ROOT / "src" / "train_macro_xgb.py")],
        env=env,
    )
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
