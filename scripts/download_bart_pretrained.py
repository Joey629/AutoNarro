#!/usr/bin/env python3
"""
将 BART 预训练基座下载到 configs 中 encoder.local_path（默认 models/pretrained/bart-chinese-uer/）。

推荐（二选一）：

  # A. 有代理（Clash 等 7890）
  export http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890
  unset HF_TOKEN HF_ENDPOINT
  PYTHONPATH=src python scripts/download_bart_pretrained.py

  # B. 无代理，用国内镜像
  unset HF_TOKEN http_proxy https_proxy HTTP_PROXY HTTPS_PROXY
  export HF_ENDPOINT=https://hf-mirror.com
  PYTHONPATH=src python scripts/download_bart_pretrained.py

说明：勿用 transformers.from_pretrained 直拉（会无视镜像、直连 huggingface.co 导致超时）。
本脚本使用 huggingface_hub.snapshot_download，与 download_deberta_pretrained.py 一致。
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description="下载 BART 预训练基座到 models/pretrained/")
    parser.add_argument(
        "--config",
        default="configs/bart_narro_v4.json",
        help="实验 JSON（encoder.model_name / local_path）",
    )
    args = parser.parse_args()

    from bart_training_config import BartTrainingConfig
    from pretrained_models import (
        _proxy_configured,
        configure_hf_hub,
        default_local_pretrained_dir,
        download_model_snapshot,
        resolve_encoder_path,
    )

    configure_hf_hub()
    cfg = BartTrainingConfig.from_json(ROOT / args.config)
    target = cfg.local_pretrained_path or default_local_pretrained_dir(cfg.model_name)

    if target.is_dir() and (target / "config.json").is_file():
        print(f"已存在本地权重: {target}")
        print("完成:", resolve_encoder_path(cfg.model_name, str(target)))
        return 0

    endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
    print(f"模型: {cfg.model_name}")
    if _proxy_configured() and endpoint.rstrip("/").endswith("hf-mirror.com"):
        print("\n警告: 同时设置了代理与 HF_ENDPOINT=hf-mirror，易失败。")
        print("  建议: unset HF_ENDPOINT 后重试（走代理访问 huggingface.co）\n")

    try:
        download_model_snapshot(cfg.model_name, target)
    except Exception as e:
        print("\n下载失败:", e)
        print("\n常见处理：")
        print("  1) 开代理: export http_proxy=http://127.0.0.1:7890 https_proxy=... && unset HF_ENDPOINT HF_TOKEN")
        print("  2) 镜像:   unset 所有 proxy && export HF_ENDPOINT=https://hf-mirror.com")
        print("  3) 手动:   hf download uer/bart-base-chinese-cluecorpussmall \\")
        print(f"             --local-dir {target}")
        return 1

    print("\n完成:", resolve_encoder_path(cfg.model_name, str(target)))
    rel = target.relative_to(ROOT) if target.is_relative_to(ROOT) else target
    print(f"  configs 中 local_path 应为: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
