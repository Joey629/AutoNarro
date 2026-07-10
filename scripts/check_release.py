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
    required = ("bert_classifier_weights", "bart_model_dir")
    for key in required:
        p = Path(paths[key])
        exists = p.is_file() or p.is_dir()
        print(f"  [{'OK' if exists else 'MISS'}] {key}: {p}")
        ok = ok and exists

    # SC 双轨（MAIN + 直接）；缺任一则回退 legacy macro_xgb_narro_v4
    main_dir = Path(paths.get("macro_sc_main_dir") or "")
    direct_dir = Path(paths.get("macro_sc_direct_dir") or "")
    legacy_dir = Path(paths.get("auto_xgb_folder") or "")
    main_ok = main_dir.is_dir() and all(
        (main_dir / f"sc_main_{ep}.joblib").is_file() for ep in ("SC_E1", "SC_E2", "SC_E3")
    )
    direct_ok = direct_dir.is_dir() and all(
        (direct_dir / f"sc_direct_{ep}.joblib").is_file() for ep in ("SC_E1", "SC_E2", "SC_E3")
    )
    legacy_ok = legacy_dir.is_dir() and any(
        (legacy_dir / f"auto_xgb_model_{ep}.joblib").is_file() for ep in ("SC_E1", "SC_E2", "SC_E3")
    )
    print(f"  [{'OK' if main_ok else 'MISS'}] macro_sc_main (轨 A): {main_dir}")
    print(f"  [{'OK' if direct_ok else 'MISS'}] macro_sc_direct (轨 B): {direct_dir}")
    print(f"  [{'OK' if legacy_ok else '—'}] macro_xgb legacy 回退: {legacy_dir}")
    ok = ok and main_ok and direct_ok
    if not main_ok or not direct_ok:
        print("  [提示] 运行: NARRO_BART_FORCE_CPU=1 PYTHONPATH=src python scripts/train_macro.py")

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
