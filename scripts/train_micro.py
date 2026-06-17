#!/usr/bin/env python3
"""重训 Narro v4 微观模型（QiDeBERTa + LoRA）。

  PYTHONPATH=src python scripts/download_deberta_pretrained.py
  PYTHONPATH=src python scripts/train_micro.py
  PYTHONPATH=src python scripts/train_micro.py --skip-smoke

见 docs/TRAINING.md。
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "micro_narro_v4.json"


def _hf_env() -> dict[str, str]:
    sys.path.insert(0, str(ROOT / "src"))
    from pretrained_models import configure_hf_hub

    env = os.environ.copy()
    configure_hf_hub()
    env.update(os.environ)
    env.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "120")
    return env


def _smoke(config_path: Path) -> int:
    sys.path.insert(0, str(ROOT / "src"))
    from pretrained_models import resolve_encoder_path

    enc = json.loads(config_path.read_text(encoding="utf-8")).get("encoder", {})
    model_name = enc.get("model_name", "Morton-Li/QiDeBERTa-base")
    local = enc.get("local_path", "").strip() or None
    load_path = resolve_encoder_path(model_name, local)
    print(f"加载 {load_path} …")
    import torch
    from transformers import AutoModel, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(load_path, trust_remote_code=True)
    m = AutoModel.from_pretrained(load_path, trust_remote_code=True)
    inp = tok("小猫想抓蝴蝶。", return_tensors="pt")
    with torch.no_grad():
        out = m(**inp)
    print("OK hidden", tuple(out.last_hidden_state.shape))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-smoke", action="store_true")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    args = parser.parse_args()

    cfg_path = ROOT / args.config
    env = _hf_env()
    env["PYTHONPATH"] = str(ROOT / "src")
    env["NARRO_MICRO_CONFIG"] = str(cfg_path)
    os.chdir(ROOT)

    if not args.skip_smoke:
        print("=== 1/2 编码器冒烟 ===")
        try:
            if _smoke(cfg_path) != 0:
                return 1
        except Exception as e:
            print("失败:", e)
            print("请先: PYTHONPATH=src python scripts/download_deberta_pretrained.py")
            return 1

    print("\n=== 2/2 微观训练 ===")
    r = subprocess.run(
        [
            sys.executable,
            str(ROOT / "src" / "train_micro.py"),
            "--config",
            str(cfg_path),
        ],
        env=env,
    )
    if r.returncode == 0:
        print(f"\n完成。指标见 {cfg_path}")
    return r.returncode


if __name__ == "__main__":
    raise SystemExit(main())
