"""
BART 线索生成训练实验配置（编码器对照，JSON 驱动）。
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from paths import CONFIGS_DIR, REPO_ROOT
from pretrained_models import resolve_encoder_path


@dataclass
class BartTrainingConfig:
    id: str
    label: str
    model_name: str
    local_pretrained_path: Path | None
    model_dir: Path
    metrics_log: Path
    seed: int
    epochs: int
    train_on_all: bool
    stratify_col: str
    data_path: Path
    config_path: Path
    comparison: dict[str, Any]
    raw: dict[str, Any]

    @classmethod
    def from_json(cls, path: str | Path) -> BartTrainingConfig:
        config_path = Path(path)
        if not config_path.is_absolute():
            config_path = REPO_ROOT / config_path
        blob = json.loads(config_path.read_text(encoding="utf-8"))
        enc = blob.get("encoder", {})
        tr = blob.get("training", {})
        out = blob.get("outputs", {})
        data = blob.get("data", {})

        def _resolve(p: str) -> Path:
            pp = Path(p)
            return pp if pp.is_absolute() else REPO_ROOT / pp

        return cls(
            id=str(blob.get("id", config_path.stem)),
            label=str(blob.get("label", blob.get("id", ""))),
            model_name=str(enc.get("model_name", "fnlp/bart-base-chinese")),
            local_pretrained_path=(
                _resolve(enc["local_path"]) if enc.get("local_path") else None
            ),
            model_dir=_resolve(out.get("model_dir", f"models/BART_{config_path.stem}")),
            metrics_log=_resolve(
                out.get("metrics_log", f"data/logs/{config_path.stem}_metrics.json")
            ),
            seed=int(tr.get("seed", 42)),
            epochs=int(tr.get("epochs", 30)),
            train_on_all=bool(tr.get("train_on_all", False)),
            stratify_col=str(tr.get("stratify_col", "story_type")),
            data_path=_resolve(data.get("csv", "data/narratives.csv")),
            config_path=config_path,
            comparison=dict(blob.get("comparison", {})),
            raw=blob,
        )

    def resolve_hub_path(self) -> str:
        local = str(self.local_pretrained_path) if self.local_pretrained_path else None
        return resolve_encoder_path(self.model_name, local)

    def write_results(self, metrics_blob: dict[str, Any]) -> None:
        blob = dict(self.raw)
        results = dict(blob.get("results", {}))
        wm = metrics_blob.get("word_level_ist_metrics_trainer_test") or metrics_blob.get(
            "word_level_ist_metrics", {}
        )
        if isinstance(wm, dict):
            results["test_structured_f1"] = _round4(wm.get("f1"))
            results["test_structured_precision"] = _round4(wm.get("precision"))
            results["test_structured_recall"] = _round4(wm.get("recall"))
            results["test_structured_cat_acc"] = _round4(wm.get("category_assignment_accuracy"))
        tl = metrics_blob.get("test_loss")
        if tl is not None:
            results["test_loss"] = round(float(tl), 6)
        results["model_dir"] = str(self.model_dir)
        results["encoder_model_name"] = self.model_name
        results["trained_at"] = datetime.now(timezone.utc).isoformat()
        blob["results"] = results
        self.config_path.write_text(
            json.dumps(blob, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        self.metrics_log.parent.mkdir(parents=True, exist_ok=True)
        self.metrics_log.write_text(
            json.dumps(blob, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )


def _round4(v) -> float | None:
    if v is None:
        return None
    try:
        return round(float(v), 4)
    except (TypeError, ValueError):
        return None


def default_bart_ablation_config_path(name: str) -> Path:
    return CONFIGS_DIR / name
