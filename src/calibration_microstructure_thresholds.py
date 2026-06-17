"""
多任务 BERT（微观）sigmoid 二值化阈值：默认值、与 checkpoint 同目录的 JSON 版本化、按行阈值矩阵。

与 pipeline_predict_report / research_paper_statistics_bootstrap 共用同一套 task_type + story_type 规则。
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

DEFAULT_THRESHOLD_TELLING = 0.52
DEFAULT_THRESHOLD_RETELLING = 0.58


def calibration_json_path_for_weights(weights_path: str | Path) -> Path:
    p = Path(weights_path).resolve()
    return p.parent / f"{p.stem}.calibration.json"


def load_calibration_json(path: str | Path) -> dict[str, Any] | None:
    path = Path(path)
    if not path.is_file():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def resolve_thresholds(
    bert_weights_path: str | Path,
    explicit_json: str | Path | None = None,
) -> tuple[float, float, str]:
    """
    返回 (threshold_telling, threshold_retelling, source_label)。
    优先顺序：显式 JSON → 与 .pth 同 stem 的 .calibration.json → 默认常数。
    """
    if explicit_json is not None and str(explicit_json).strip():
        data = load_calibration_json(explicit_json)
        if data:
            return (
                float(data["threshold_telling"]),
                float(data["threshold_retelling"]),
                f"json:{Path(explicit_json).resolve()}",
            )
    sibling = calibration_json_path_for_weights(bert_weights_path)
    data = load_calibration_json(sibling)
    if data:
        return (
            float(data["threshold_telling"]),
            float(data["threshold_retelling"]),
            f"json:{sibling}",
        )
    return (
        DEFAULT_THRESHOLD_TELLING,
        DEFAULT_THRESHOLD_RETELLING,
        "defaults",
    )


def multitask_threshold_for_task(
    task_type,
    story_type,
    telling: float | None = None,
    retelling: float | None = None,
) -> float:
    t_t = DEFAULT_THRESHOLD_TELLING if telling is None else telling
    t_r = DEFAULT_THRESHOLD_RETELLING if retelling is None else retelling
    if task_type is not None and pd.notna(task_type):
        t = str(task_type).strip().lower()
        if "retelling" in t or "复述" in t:
            return t_r
        if "telling" in t or "讲述" in t:
            return t_t
        return t_r
    st = str(story_type).strip().lower() if story_type is not None and pd.notna(story_type) else ""
    return t_t if st in ("goat", "bird") else t_r


def build_per_row_threshold_matrix(
    df: pd.DataFrame,
    telling: float | None = None,
    retelling: float | None = None,
) -> np.ndarray:
    """(n_samples, 15)，每行 15 个任务共用该行叙事对应的阈值。"""
    n = len(df)
    mat = np.zeros((n, 15), dtype=np.float64)
    for i, (_, row) in enumerate(df.iterrows()):
        thr = multitask_threshold_for_task(row.get("task_type"), row.get("story_type"), telling, retelling)
        mat[i, :] = thr
    return mat


def save_calibration_json(
    path: str | Path,
    *,
    checkpoint: str,
    threshold_telling: float,
    threshold_retelling: float,
    metric: str,
    metric_value: float,
    extra: dict[str, Any] | None = None,
) -> None:
    path = Path(path)
    payload: dict[str, Any] = {
        "schema_version": 1,
        "checkpoint": str(Path(checkpoint).resolve()),
        "threshold_telling": threshold_telling,
        "threshold_retelling": threshold_retelling,
        "metric": metric,
        "metric_value_on_calibration_set": metric_value,
    }
    if extra:
        payload["calibration_run"] = extra
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
