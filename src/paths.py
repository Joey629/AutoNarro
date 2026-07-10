"""仓库根目录与模型/数据路径（产品化统一配置）。"""
from __future__ import annotations

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

try:
    from narro_env import migrate_legacy_env

    migrate_legacy_env()
except ImportError:
    pass

FRONTEND_DIR = REPO_ROOT / "frontend"
MODELS_DIR = REPO_ROOT / "models"
DATA_DIR = REPO_ROOT / "data"
CONFIGS_DIR = REPO_ROOT / "configs"
LOGS_DIR = REPO_ROOT / "data" / "logs"
MODEL_REGISTRY_PATH = CONFIGS_DIR / "model_registry.json"


def load_model_registry() -> dict:
    if not MODEL_REGISTRY_PATH.is_file():
        return {
            "active_version": "narro_v4",
            "versions": {
                "narro_v4": {
                    "label": "Narro v4",
                    "micro_weights": "models/micro_narro_v4.pth",
                    "encoder_model": "Morton-Li/QiDeBERTa-base",
                    "micro_config": "configs/micro_narro_v4.json",
                    "bart_dir": "models/bart_narro_v4",
                    "macro_xgb_dir": "models/macro_xgb_narro_v4",
                    "macro_sc_main_dir": "models/macro_sc_main",
                    "macro_sc_direct_dir": "models/macro_sc_direct",
                }
            },
        }
    return json.loads(MODEL_REGISTRY_PATH.read_text(encoding="utf-8"))


def resolve_model_version(version: str | None = None) -> str:
    reg = load_model_registry()
    v = version or os.environ.get("NARRO_MODEL_VERSION") or reg.get("active_version", "narro_v4")
    if v not in reg.get("versions", {}):
        raise ValueError(f"未知模型版本: {v}，可用: {list(reg.get('versions', {}))}")
    return v


def default_model_paths(version: str | None = None) -> dict:
    reg = load_model_registry()
    v = resolve_model_version(version)
    spec = reg["versions"][v]

    def _p(rel: str) -> str:
        p = Path(rel)
        return str(p if p.is_absolute() else REPO_ROOT / p)

    micro_cfg = spec.get("micro_config")
    macro_xgb = _p(spec["macro_xgb_dir"])
    macro_sc_main = _p(spec["macro_sc_main_dir"]) if spec.get("macro_sc_main_dir") else ""
    macro_sc_direct = _p(spec["macro_sc_direct_dir"]) if spec.get("macro_sc_direct_dir") else ""
    micro_weights = _p(spec["micro_weights"])
    return {
        "model_version": v,
        "model_label": spec.get("label", v),
        "encoder_model": spec.get("encoder_model", "Morton-Li/QiDeBERTa-base"),
        "micro_config": str(REPO_ROOT / micro_cfg) if micro_cfg else os.environ.get("NARRO_MICRO_CONFIG", "").strip() or None,
        "bart_model_dir": _p(spec["bart_dir"]),
        "macro_xgb_dir": macro_xgb,
        "macro_sc_main_dir": macro_sc_main,
        "macro_sc_direct_dir": macro_sc_direct,
        "auto_xgb_folder": macro_xgb,
        "micro_weights": micro_weights,
        "bert_classifier_weights": micro_weights,
        "bert_multitask_calibration_json": _p(spec["micro_calibration_json"])
        if spec.get("micro_calibration_json")
        else None,
        "benchmark_db_regression": os.environ.get("NARRO_BENCHMARK_REG", ""),
        "benchmark_db_multitask": os.environ.get("NARRO_BENCHMARK_MULTI", ""),
    }


def narratives_csv_path() -> Path:
    return DATA_DIR / "narratives.csv"


def split_cache_path(name: str = "regression_macro_split_narro_v4_701020_seed42.npz") -> Path:
    return DATA_DIR / name


def resolve_split_cache(cache_path: str | None) -> str | None:
    """将 split 缓存解析为绝对路径；优先 ``data/``，兼容仓库根目录旧副本。"""
    if not cache_path:
        return None
    p = Path(cache_path)
    if p.is_file():
        return str(p.resolve())
    candidates = [DATA_DIR / p.name, REPO_ROOT / p, REPO_ROOT / p.name]
    for c in candidates:
        if c.is_file():
            return str(c.resolve())
    return str((DATA_DIR / p.name) if not p.is_absolute() else p)
