"""
宏观 SS 训练实验配置：JSON 驱动编码器对照（如 DeBERTa-v3 vs RoBERTa-wwm-ext）。
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

from paths import CONFIGS_DIR, REPO_ROOT


@dataclass
class M4TrainOptions:
    """可选训练配方；未在 JSON 中指定时与历史默认行为一致。"""

    weight_decay: float = 0.0
    warmup_ratio: float = 0.0
    head_learning_rate: float | None = None
    lora_learning_rate: float | None = None
    lora_r: int = 8
    lora_alpha: int = 16
    lora_target_modules: list[str] | None = None
    max_grad_norm: float = 1.0

    @classmethod
    def from_training_dict(cls, tr: dict[str, Any]) -> M4TrainOptions:
        lora = tr.get("lora") or {}
        opt = tr.get("optimizer") or {}
        targets = lora.get("target_modules")
        if isinstance(targets, str):
            targets = [s.strip() for s in targets.split(",") if s.strip()]
        elif targets is not None:
            targets = list(targets)
        return cls(
            weight_decay=float(opt.get("weight_decay", 0.0)),
            warmup_ratio=float(opt.get("warmup_ratio", 0.0)),
            head_learning_rate=(
                float(opt["head_learning_rate"])
                if opt.get("head_learning_rate") is not None
                else None
            ),
            lora_learning_rate=(
                float(opt["lora_learning_rate"])
                if opt.get("lora_learning_rate") is not None
                else None
            ),
            lora_r=int(lora.get("r", 8)),
            lora_alpha=int(lora.get("alpha", 16)),
            lora_target_modules=targets,
            max_grad_norm=float(opt.get("max_grad_norm", 1.0)),
        )

    def apply_lora_env(self) -> None:
        if self.lora_target_modules:
            os.environ["NARRO_LORA_TARGETS"] = ",".join(self.lora_target_modules)

    def describe(self, base_lr: float) -> str:
        parts = [f"wd={self.weight_decay}", f"warmup={self.warmup_ratio}"]
        if self.head_learning_rate is not None:
            ll = self.lora_learning_rate if self.lora_learning_rate is not None else base_lr
            parts.append(f"lr_head={self.head_learning_rate} lr_lora={ll} lr_base={base_lr}")
        else:
            parts.append(f"lr={base_lr}")
        parts.append(f"LoRA r={self.lora_r} alpha={self.lora_alpha}")
        if self.lora_target_modules:
            parts.append(f"targets={self.lora_target_modules}")
        return " | ".join(parts)


@dataclass
class MicroTrainingConfig:
    id: str
    label: str
    model_name: str
    local_pretrained_path: Path | None
    checkpoint_out: Path
    cv_prefix: str
    metrics_log: Path
    seed: int
    n_splits: int
    epochs: int
    batch_size: int
    learning_rate: float
    patience: int
    max_length: int
    split_by_participant: bool
    ist_separator: str  # "auto" or explicit token string
    trust_remote_code: bool
    train_options: M4TrainOptions
    config_path: Path
    comparison: dict[str, Any]
    raw: dict[str, Any]

    @classmethod
    def from_json(cls, path: str | Path) -> MicroTrainingConfig:
        config_path = Path(path)
        if not config_path.is_absolute():
            config_path = REPO_ROOT / config_path
        blob = json.loads(config_path.read_text(encoding="utf-8"))
        enc = blob.get("encoder", {})
        tr = blob.get("training", {})
        out = blob.get("outputs", {})

        def _resolve(p: str) -> Path:
            pp = Path(p)
            return pp if pp.is_absolute() else REPO_ROOT / pp

        train_opts = M4TrainOptions.from_training_dict(tr)

        return cls(
            id=str(blob.get("id", config_path.stem)),
            label=str(blob.get("label", blob.get("id", ""))),
            model_name=str(enc.get("model_name", "hfl/chinese-roberta-wwm-ext")),
            local_pretrained_path=(
                _resolve(enc["local_path"])
                if enc.get("local_path")
                else None
            ),
            checkpoint_out=_resolve(out.get("checkpoint", f"models/M4_{config_path.stem}.pth")),
            cv_prefix=str(out.get("cv_checkpoint_prefix", "M4_cv_fold_")),
            metrics_log=_resolve(out.get("metrics_log", f"data/logs/{config_path.stem}_metrics.json")),
            seed=int(tr.get("seed", 42)),
            n_splits=int(tr.get("n_splits", 5)),
            epochs=int(tr.get("epochs", 15)),
            batch_size=int(tr.get("batch_size", 10)),
            learning_rate=float(tr.get("learning_rate", 2e-5)),
            patience=int(tr.get("patience", 3)),
            max_length=int(tr.get("max_length", 512)),
            split_by_participant=bool(tr.get("split_by_participant", True)),
            ist_separator=str(enc.get("ist_inline_separator", "auto")),
            trust_remote_code=bool(enc.get("trust_remote_code", False)),
            train_options=train_opts,
            config_path=config_path,
            comparison=dict(blob.get("comparison", {})),
            raw=blob,
        )

    def resolve_ist_separator(self, tokenizer) -> str:
        if self.ist_separator == "auto":
            sep = getattr(tokenizer, "sep_token", None) or "[SEP]"
            return str(sep)
        return self.ist_separator

    def write_results(
        self,
        *,
        cv_fold_f1: list[float],
        test_macro_f1: float,
        test_accuracy: float,
        per_task_f1: dict[str, float],
        ist_separator_used: str,
    ) -> None:
        blob = dict(self.raw)
        results = dict(blob.get("results", {}))
        results["cv_fold_f1"] = [round(x, 4) for x in cv_fold_f1]
        results["cv_mean"] = round(float(sum(cv_fold_f1) / len(cv_fold_f1)), 4) if cv_fold_f1 else None
        results["cv_sd"] = (
            round(float(np.std(cv_fold_f1, ddof=1)), 4) if len(cv_fold_f1) > 1 else 0.0
        )
        results["test_macro_f1"] = round(test_macro_f1, 4)
        results["test_accuracy"] = round(test_accuracy, 4)
        results["per_task_f1"] = {k: round(v, 4) for k, v in per_task_f1.items()}
        results["ist_separator_used"] = ist_separator_used
        results["trained_at"] = datetime.now(timezone.utc).isoformat()
        blob["results"] = results
        self.config_path.write_text(
            json.dumps(blob, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        self.metrics_log.parent.mkdir(parents=True, exist_ok=True)
        self.metrics_log.write_text(json.dumps(blob, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def default_ablation_config_path() -> Path:
    return CONFIGS_DIR / "micro_narro_v4.json"
