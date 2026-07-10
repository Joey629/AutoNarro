"""Offline analyze_* scripts: narro_v4 encoder path + LoRA config."""

from __future__ import annotations

import os

import pretrained_models as pm
import train_micro as micro
from micro_training_config import MicroTrainingConfig

_DEFAULT_CFG = "configs/micro_narro_v4.json"


def load_micro_training_config(path: str | None = None) -> MicroTrainingConfig:
    p = path or os.environ.get("NARRO_MICRO_CONFIG", _DEFAULT_CFG)
    return MicroTrainingConfig.from_json(p)


def apply_micro_encoder_env(cfg: MicroTrainingConfig | None = None) -> MicroTrainingConfig:
    cfg = cfg or load_micro_training_config()
    micro.MODEL_NAME = cfg.model_name
    local = cfg.local_pretrained_path
    orig = pm.resolve_encoder_path

    def resolve(model_name: str, local_path=None):
        return orig(model_name, local_path or local)

    pm.resolve_encoder_path = resolve
    try:
        import micro_encoder as me

        me.resolve_encoder_path = resolve
    except ImportError:
        pass
    return cfg


def encoder_path_and_kwargs(cfg: MicroTrainingConfig | None = None):
    cfg = apply_micro_encoder_env(cfg)
    path = pm.resolve_encoder_path(cfg.model_name, cfg.local_pretrained_path)
    kw = pm.encoder_from_pretrained_kwargs(cfg.model_name, trust_remote_code=True)
    return path, kw, cfg
