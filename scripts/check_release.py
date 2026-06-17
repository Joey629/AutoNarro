#!/usr/bin/env python3
"""
发布前检查：模型文件存在 + 黄金样本回归。

  PYTHONPATH=src python scripts/check_release.py
  PYTHONPATH=src python scripts/check_release.py --skip-golden   # 仅检查文件
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)


def check_artifacts() -> bool:
    from paths import default_model_paths, load_model_registry

    reg = load_model_registry()
    paths = default_model_paths()
    ok = True
    for key in ("bert_classifier_weights", "bart_model_dir", "auto_xgb_folder"):
        p = Path(paths[key])
        exists = p.is_file() or p.is_dir()
        print(f"  [{'OK' if exists else 'MISS'}] {key}: {p}")
        ok = ok and exists
    print(f"  活跃版本: {reg.get('active_version')} ({paths.get('model_label')})")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-golden", action="store_true")
    args = parser.parse_args()
    print("=== 产物检查 ===")
    if not check_artifacts():
        return 1
    if args.skip_golden:
        print("跳过黄金样本（--skip-golden）")
        return 0
    print("\n=== 黄金样本回归 ===")
    import subprocess

    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_golden_regression.py")],
        cwd=str(ROOT),
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
    )
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
