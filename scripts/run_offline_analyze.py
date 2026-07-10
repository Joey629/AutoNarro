#!/usr/bin/env python3
"""Run all offline analyze_micro_* and analyze_macro_* scripts (narro_v4)."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = ROOT / ".venv" / "bin" / "python"
SCRIPTS = [
    "src/analyze_macro_errors.py",
    "src/analyze_macro_metadata.py",
    "src/analyze_micro_metadata.py",
    "src/analyze_micro_errors.py",
]


def main() -> int:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    env.setdefault("NARRO_MICRO_CONFIG", "configs/micro_narro_v4.json")
    env.setdefault("NARRO_BART_FORCE_CPU", "1")
    env.setdefault("REGRESSION_FORCE_CPU", "1")

    py = PY if PY.is_file() else Path(sys.executable)
    for rel in SCRIPTS:
        path = ROOT / rel
        print(f"\n{'=' * 60}\n▶ {rel}\n{'=' * 60}")
        rc = subprocess.call([str(py), str(path)], cwd=str(ROOT), env=env)
        if rc != 0:
            print(f"❌ 失败: {rel} (exit {rc})")
            return rc
    print("\n✅ 全部分析完成")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
