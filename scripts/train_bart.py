#!/usr/bin/env python3
"""重训 Narro v4 BART 线索模型。

  PYTHONPATH=src python scripts/download_bart_pretrained.py
  PYTHONPATH=src python scripts/train_bart.py
  PYTHONPATH=src python scripts/train_bart.py --skip-smoke

见 docs/TRAINING.md。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "bart_narro_v4.json"
sys.path.insert(0, str(ROOT / "src"))


def _smoke(cfg) -> int:
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    hub = cfg.resolve_hub_path()
    print(f"=== 冒烟：加载 {hub} ===")
    tok = AutoTokenizer.from_pretrained(hub)
    model = AutoModelForSeq2SeqLM.from_pretrained(hub)
    print(f"OK vocab={tok.vocab_size} params={sum(p.numel() for p in model.parameters())}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--skip-smoke", action="store_true")
    args = parser.parse_args()

    from bart_training_config import BartTrainingConfig
    from bart_train import run_training

    cfg = BartTrainingConfig.from_json(ROOT / args.config)
    if not args.skip_smoke:
        r = _smoke(cfg)
        if r != 0:
            return r

    print(f"\n=== BART 训练 [{cfg.id}] ===")
    final = run_training(
        data_path=str(cfg.data_path),
        model_checkpoint=cfg.resolve_hub_path(),
        output_dir=str(cfg.model_dir),
        seed=cfg.seed,
        train_on_all=cfg.train_on_all,
        num_train_epochs=cfg.epochs,
        stratify_col=cfg.stratify_col,
    )
    if final is None:
        return 1

    metrics_path = Path(final) / "bart_test_metrics.json"
    blob = json.loads(metrics_path.read_text(encoding="utf-8"))
    cfg.write_results(blob)
    f1 = (blob.get("word_level_ist_metrics_trainer_test") or blob.get("word_level_ist_metrics") or {}).get("f1")
    print(f"\n完成 → {final}")
    print(f"  test structured F1: {f1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
