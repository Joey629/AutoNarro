"""常模参照：以 narratives.csv 专家标注为准。"""
from __future__ import annotations

from typing import Any, Optional

import pandas as pd

TASK_NAMES_GLOBAL = [f"A{i}" for i in range(2, 17)]

# 宏观 SC 常模列（专家 SC_Sum）
EXPERT_MACRO_SUM_COL = "SC_Sum"
# 宏观 SS 常模：A2–A16 之和
EXPERT_MICRO_SUM_COL = "expert_micro_sum"
# 语言学常模列（专家手工/工具统计，与语料一致）
EXPERT_LING_COLS = ("TNW", "TDW", "TNU", "MLU")


def ensure_expert_norm_columns(df: pd.DataFrame) -> pd.DataFrame:
    """在基准 DataFrame 上补齐专家常模用列。"""
    out = df.copy()
    if EXPERT_MACRO_SUM_COL not in out.columns and "pred_SC_Sum" in out.columns:
        out[EXPERT_MACRO_SUM_COL] = pd.to_numeric(out["pred_SC_Sum"], errors="coerce")
    elif EXPERT_MACRO_SUM_COL in out.columns:
        out[EXPERT_MACRO_SUM_COL] = pd.to_numeric(out[EXPERT_MACRO_SUM_COL], errors="coerce")

    task_cols = [c for c in TASK_NAMES_GLOBAL if c in out.columns]
    if task_cols:
        for c in task_cols:
            out[c] = pd.to_numeric(out[c], errors="coerce").fillna(0)
        out[EXPERT_MICRO_SUM_COL] = out[task_cols].sum(axis=1)
    return out


def filter_peer_group(
    df: pd.DataFrame,
    age: int,
    story_type: str,
    task_type: Optional[str],
) -> pd.DataFrame:
    if df.empty or "age" not in df.columns:
        return pd.DataFrame()
    mask = (df["age"] == age) & (df["story_type"] == story_type)
    if task_type and "task_type" in df.columns:
        t_ref = df["task_type"].astype(str).str.strip().str.lower()
        mask = mask & (t_ref == str(task_type).strip().lower())
    return df[mask]


def expert_peer_mean(
    df: pd.DataFrame,
    column: str,
    age: int,
    story_type: str,
    task_type: Optional[str],
) -> dict[str, Any]:
    """返回专家常模列在同龄同组中的均值。"""
    base = ensure_expert_norm_columns(df)
    sub = filter_peer_group(base, age, story_type, task_type)
    if sub.empty or column not in sub.columns:
        return {"n": 0, "mean": None, "source": "expert_narratives_csv"}
    col = pd.to_numeric(sub[column], errors="coerce").dropna()
    if col.empty:
        return {"n": 0, "mean": None, "source": "expert_narratives_csv"}
    return {
        "n": int(len(col)),
        "mean": float(col.mean()),
        "source": "expert_narratives_csv",
    }


def expert_linguistic_peer_means(
    df: pd.DataFrame,
    age: int,
    story_type: str,
    task_type: Optional[str],
) -> dict[str, Any]:
    base = ensure_expert_norm_columns(df)
    sub = filter_peer_group(base, age, story_type, task_type)
    if sub.empty:
        return {"n": 0, "averages": {}, "source": "expert_narratives_csv"}
    avgs = {}
    for k in EXPERT_LING_COLS:
        if k not in sub.columns:
            continue
        col = pd.to_numeric(sub[k], errors="coerce").dropna()
        if not col.empty:
            avgs[k] = round(float(col.mean()), 3 if k == "MLU" else 2)
    if "TNW" in avgs and "TDW" in avgs and avgs.get("TNW"):
        avgs["TTR"] = round(avgs["TDW"] / avgs["TNW"], 4)
    return {"n": int(len(sub)), "averages": avgs, "source": "expert_narratives_csv"}
