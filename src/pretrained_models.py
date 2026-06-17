"""
Hugging Face 预训练权重加载：镜像、超时、本地目录。

国内网络无法直连 huggingface.co 时，在运行训练前设置：

  export HF_ENDPOINT=https://hf-mirror.com

或先把模型下载到仓库内，再在 configs/micro_narro_v4.json 填写 encoder.local_path。
"""

from __future__ import annotations

import os
from pathlib import Path

from paths import MODELS_DIR, REPO_ROOT


def _proxy_configured() -> bool:
    for key in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "all_proxy"):
        if os.environ.get(key, "").strip():
            return True
    return False


def configure_hf_hub() -> None:
    """
    提高下载超时；选择 Hub 端点：
    - 已设 http(s)_proxy：走官方 huggingface.co（代理），不自动改 hf-mirror
    - 无代理且未设 HF_ENDPOINT：默认 hf-mirror.com
    """
    os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "120")
    os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "120")
    if os.environ.get("HF_ENDPOINT"):
        return
    if _proxy_configured():
        # 避免「代理 + 镜像」混用导致连不上 hf-mirror.com
        return
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")


def default_local_pretrained_dir(model_name: str) -> Path:
    safe = model_name.replace("/", "__")
    return MODELS_DIR / "pretrained" / safe


def resolve_encoder_path(model_name: str, local_path: str | Path | None = None) -> str:
    """
    返回 transformers from_pretrained 可用的路径或 repo id。
    优先：显式 local_path → 仓库 models/pretrained/<org>__<name>/ → 远程 model_name。
    """
    configure_hf_hub()

    if local_path:
        p = Path(local_path)
        if not p.is_absolute():
            p = REPO_ROOT / p
        if p.is_dir() and (p / "config.json").is_file():
            print(f"[预训练] 使用本地目录: {p}")
            return str(p)
        print(f"[预训练] 警告: local_path 无效（缺少 config.json）: {p}")

    auto = default_local_pretrained_dir(model_name)
    if auto.is_dir() and (auto / "config.json").is_file():
        print(f"[预训练] 使用本地缓存: {auto}")
        return str(auto)

    endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
    print(f"[预训练] 从 Hub 拉取: {model_name}（HF_ENDPOINT={endpoint}）")
    print("  若超时，请执行: PYTHONPATH=src python scripts/download_deberta_pretrained.py")
    return model_name


def download_model_snapshot(
    model_name: str,
    local_dir: str | Path,
    *,
    repo_type: str = "model",
) -> Path:
    """
    将 Hub 仓库完整下载到 local_dir（走 HF_ENDPOINT / 代理，不经过 transformers）。
    国内推荐：无代理时 ``HF_ENDPOINT=https://hf-mirror.com``；
    有代理时 ``unset HF_ENDPOINT`` 并设置 http_proxy/https_proxy。
    """
    configure_hf_hub()
    target = Path(local_dir)
    if not target.is_absolute():
        target = REPO_ROOT / target
    target.mkdir(parents=True, exist_ok=True)

    endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
    print(f"[预训练] snapshot_download: {model_name}")
    print(f"  → {target}")
    print(f"  HF_ENDPOINT={endpoint}")
    if _proxy_configured():
        print("  检测到代理：请确保已 unset HF_ENDPOINT（勿与 hf-mirror 混用）")
    elif "hf-mirror" in endpoint:
        print("  无代理：经 hf-mirror.com 下载")

    from huggingface_hub import snapshot_download

    snapshot_download(
        repo_id=model_name,
        local_dir=str(target),
        repo_type=repo_type,
    )
    if not (target / "config.json").is_file():
        raise FileNotFoundError(f"下载不完整，缺少 {target / 'config.json'}")
    return target


def encoder_from_pretrained_kwargs(
    model_name: str = "",
    *,
    trust_remote_code: bool | None = None,
) -> dict[str, bool]:
    """QiDeBERTa 等仓库含自定义 modeling 代码，需 trust_remote_code=True。"""
    if trust_remote_code is None:
        name = model_name.lower()
        trust_remote_code = (
            "qideberta" in name
            or os.environ.get("NARRO_TRUST_REMOTE_CODE", "").lower() in ("1", "true", "yes")
        )
    if trust_remote_code:
        return {"trust_remote_code": True}
    return {}
