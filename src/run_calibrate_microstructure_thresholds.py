#!/usr/bin/env python3
"""
在 **训练池** 内划出校准子集（默认不触碰与 paper_statistics 相同的 20% held-out test），
对 Telling / Retelling 两组分别网格搜索 sigmoid 阈值，使 sklearn macro-F1（多标签，与 bootstrap 脚本一致）最大；
结果写入与 checkpoint 同名的 ``<stem>.calibration.json``，供 pipeline_predict_report 与 paper_statistics 自动加载。

示例：
  python run_calibrate_microstructure_thresholds.py \\
    --checkpoint best_model_20251001-111255_epoch10_macrof1_0.7067.pth \\
    --data narratives.csv
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from transformers import AutoModel, AutoTokenizer

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from calibration_microstructure_thresholds import (  # noqa: E402
    calibration_json_path_for_weights,
    DEFAULT_THRESHOLD_RETELLING,
    DEFAULT_THRESHOLD_TELLING,
    save_calibration_json,
)
from research_paper_statistics_bootstrap import (  # noqa: E402
    ClueAugmentedQAModel,
    predict_multitask_probs_m4,
)


def _row_is_telling_stratum(row: pd.Series) -> bool:
    """与 calibration_microstructure_thresholds.multitask_threshold_for_task 的分组一致（用 Telling 那一支阈值的样本）。"""
    tt = row.get("task_type")
    if tt is not None and pd.notna(tt):
        t = str(tt).strip().lower()
        if "retelling" in t or "复述" in t:
            return False
        if "telling" in t or "讲述" in t:
            return True
        return False
    st = str(row.get("story_type", "")).strip().lower()
    return st in ("goat", "bird")


def _macro_f1(probs: np.ndarray, y_true: np.ndarray, thr_t: float, thr_r: np.ndarray | float, telling_mask: np.ndarray) -> float:
    thr_row = np.where(telling_mask, thr_t, thr_r)
    thr_mat = np.repeat(thr_row[:, None], 15, axis=1)
    pred = (probs >= thr_mat).astype(int)
    return float(f1_score(y_true, pred, average="macro", zero_division=0))


def grid_search_thresholds(
    probs: np.ndarray,
    y_true: np.ndarray,
    telling_mask: np.ndarray,
    grid: np.ndarray,
) -> tuple[float, float, float]:
    has_t = bool(np.any(telling_mask))
    has_r = bool(np.any(~telling_mask))
    best_score = -1.0
    best_tt, best_tr = DEFAULT_THRESHOLD_TELLING, DEFAULT_THRESHOLD_RETELLING

    if has_t and has_r:
        for tt in grid:
            for tr in grid:
                s = _macro_f1(probs, y_true, tt, tr, telling_mask)
                if s > best_score:
                    best_score, best_tt, best_tr = s, tt, tr
    elif has_t:
        best_tr = DEFAULT_THRESHOLD_RETELLING
        for tt in grid:
            s = _macro_f1(probs, y_true, tt, best_tr, telling_mask)
            if s > best_score:
                best_score, best_tt = s, tt
    elif has_r:
        best_tt = DEFAULT_THRESHOLD_TELLING
        for tr in grid:
            s = _macro_f1(probs, y_true, best_tt, tr, telling_mask)
            if s > best_score:
                best_score, best_tr = s, tr
    else:
        best_score = 0.0

    return best_tt, best_tr, best_score


def main():
    parser = argparse.ArgumentParser(description="微观 多任务阈值：验证子集上网格搜索并写入 .calibration.json")
    parser.add_argument("--checkpoint", type=Path, required=True, help="微观 .pth 权重路径")
    parser.add_argument("--data", type=Path, default=ROOT / "narratives.csv")
    parser.add_argument("--model_name", default="hfl/chinese-roberta-wwm-ext")
    parser.add_argument("--out_json", type=Path, default=None, help="默认：与 checkpoint 同目录 <stem>.calibration.json")
    parser.add_argument(
        "--held_out_test_size",
        type=float,
        default=0.2,
        help="与 paper_statistics / regression 一致的测试比例；校准 **绝不使用** 该子集",
    )
    parser.add_argument("--held_out_seed", type=int, default=42)
    parser.add_argument(
        "--calib_fraction_of_train",
        type=float,
        default=0.15,
        help="从剩余训练池中划出该校准子集的比例",
    )
    parser.add_argument("--calib_seed", type=int, default=0)
    parser.add_argument("--grid_start", type=float, default=0.30)
    parser.add_argument("--grid_stop", type=float, default=0.70)
    parser.add_argument("--grid_step", type=float, default=0.01)
    parser.add_argument("--batch_size", type=int, default=16)
    args = parser.parse_args()

    if not args.data.is_file():
        print(f"缺少数据: {args.data}")
        sys.exit(1)
    if not args.checkpoint.is_file():
        print(f"缺少权重: {args.checkpoint}")
        sys.exit(1)

    df = pd.read_csv(args.data)
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    if "ist_words" not in df.columns:
        df["ist_words"] = ""
    df["ist_words"] = df["ist_words"].fillna("")

    task_cols = [f"A{i}" for i in range(2, 17)]
    missing = [c for c in task_cols if c not in df.columns]
    if missing:
        print(f"数据缺少列 {missing[:3]}… 需要含 A2–A16 的 CSV。")
        sys.exit(1)
    for c in task_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

    indices = df.index.values
    train_idx, held_test_idx = train_test_split(
        indices,
        test_size=args.held_out_test_size,
        random_state=args.held_out_seed,
    )
    cal_idx, _ = train_test_split(
        train_idx,
        test_size=args.calib_fraction_of_train,
        random_state=args.calib_seed,
    )
    cal_df = df.loc[sorted(cal_idx)].copy()
    n_cal = len(cal_df)
    telling_mask = np.array([_row_is_telling_stratum(row) for _, row in cal_df.iterrows()], dtype=bool)

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    bert_base = AutoModel.from_pretrained(args.model_name)
    model = ClueAugmentedQAModel(bert_base, use_peft=True)
    state = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(state, strict=False)
    model.to(device)
    model.eval()

    print(f"校准集叙事数 n={n_cal}（held-out test {args.held_out_test_size:.0%} seed={args.held_out_seed} 已排除）")
    print(f"  Telling 分层: {int(telling_mask.sum())}，Retelling 分层: {int((~telling_mask).sum())}")

    probs = predict_multitask_probs_m4(cal_df, model, tokenizer, device, batch_size=args.batch_size)
    y_true = cal_df[task_cols].values.astype(int)
    grid = np.arange(args.grid_start, args.grid_stop + args.grid_step * 0.5, args.grid_step)
    tt, tr, best_f1 = grid_search_thresholds(probs, y_true, telling_mask, grid)
    print(f"最优 macro-F1（校准集）= {best_f1:.4f}，threshold_telling={tt:.4f}, threshold_retelling={tr:.4f}")

    out_path = args.out_json or calibration_json_path_for_weights(args.checkpoint)
    save_calibration_json(
        out_path,
        checkpoint=str(args.checkpoint.resolve()),
        threshold_telling=float(tt),
        threshold_retelling=float(tr),
        metric="sklearn_f1_macro_multilabel",
        metric_value=float(best_f1),
        extra={
            "held_out_test_size": args.held_out_test_size,
            "held_out_seed": args.held_out_seed,
            "calib_fraction_of_train": args.calib_fraction_of_train,
            "calib_seed": args.calib_seed,
            "n_calibration_narratives": n_cal,
            "grid": {"start": args.grid_start, "stop": args.grid_stop, "step": args.grid_step},
        },
    )
    print(f"已写入: {out_path.resolve()}")


if __name__ == "__main__":
    import os

    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
