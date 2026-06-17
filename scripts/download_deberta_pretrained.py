#!/usr/bin/env python3
"""
将 微观编码器（默认 Morton-Li/QiDeBERTa-base）下载到 models/pretrained/qideberta-base/。

  cd Narro
  export http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890   # 如需代理
  unset HF_TOKEN
  PYTHONPATH=src python scripts/download_deberta_pretrained.py

模型 ID 默认读 configs/micro_narro_v4.json → encoder.model_name。
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
M4_CONFIG = ROOT / "configs" / "micro_narro_v4.json"
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)


def _model_id_from_config() -> str:
    if M4_CONFIG.is_file():
        enc = json.loads(M4_CONFIG.read_text(encoding="utf-8")).get("encoder", {})
        name = enc.get("model_name", "").strip()
        if name:
            return name
    return "Morton-Li/QiDeBERTa-base"


MODEL_ID = os.environ.get("NARRO_DEBERTA_MODEL") or _model_id_from_config()


def _repo_exists(model_id: str) -> bool:
    from huggingface_hub import HfApi

    from pretrained_models import configure_hf_hub

    configure_hf_hub()
    api = HfApi()
    try:
        api.model_info(model_id)
        return True
    except Exception as e:
        err = str(e).lower()
        if "not found" in err or "401" in err or "404" in err:
            return False
        raise


def main() -> int:
    from pretrained_models import configure_hf_hub, default_local_pretrained_dir

    from pretrained_models import _proxy_configured

    configure_hf_hub()
    target = default_local_pretrained_dir(MODEL_ID)
    target.mkdir(parents=True, exist_ok=True)
    endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
    print(f"下载 {MODEL_ID} → {target}")
    print(f"HF_ENDPOINT={endpoint}")
    if _proxy_configured():
        print("检测到代理：经 huggingface.co 下载（请勿同时 export HF_ENDPOINT=hf-mirror）")
    elif endpoint.endswith("hf-mirror.com"):
        print("无代理：使用 hf-mirror.com；若失败请开代理后 unset HF_ENDPOINT 再试")

    if os.environ.get("HF_TOKEN"):
        print("警告: 已设置 HF_TOKEN，若报 401 可先执行 unset HF_TOKEN")

    if not _repo_exists(MODEL_ID):
        print(f"\n错误: Hugging Face 上找不到公开仓库 «{MODEL_ID}»。")
        print("  详见 docs/TRAINING.md")
        return 1

    try:
        from huggingface_hub import snapshot_download

        snapshot_download(repo_id=MODEL_ID, local_dir=str(target))
    except Exception as e:
        print("huggingface_hub 下载失败:", e)
        print("\n可手动（代理示例）:")
        print("  export http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890")
        print("  unset HF_TOKEN HF_ENDPOINT")
        print(f"  hf download {MODEL_ID} --local-dir {target}")
        return 1

    if not (target / "config.json").is_file():
        print("下载不完整：缺少 config.json")
        return 1

    rel = target.relative_to(ROOT) if target.is_relative_to(ROOT) else target
    print(f"\n完成。configs/micro_narro_v4.json 中 local_path 应为: models/pretrained/{rel.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
