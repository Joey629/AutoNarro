"""叙事原文 Jieba 语言学指标：汇总、常模对比、报告段落。"""
from __future__ import annotations

from typing import Any, Optional

import pandas as pd

from features_jieba import LINGUISTIC_LABELS, extract_calculable_features

CORE_KEYS = ("TNW", "TDW", "TNU", "MLU", "TTR")

IS_COUNT_LABELS = {
    "auto_IS_Per_count": "感知状态词",
    "auto_IS_Phy_count": "生理状态词",
    "auto_IS_Con_count": "意识状态词",
    "auto_IS_Emo_count": "情感词",
    "auto_IS_Men_count": "心理动词",
    "auto_IS_Ling_count": "语言动词",
}


def build_linguistic_metrics(
    text: str,
    predicted_ist_words: str = "",
) -> dict[str, Any]:
    """从叙事正文（及 BART 线索）构建语言学指标包。"""
    from features_automated import extract_B_class_features

    raw = extract_calculable_features(text)
    metrics: dict[str, float | int] = {}
    for k in CORE_KEYS:
        v = float(raw.get(k, 0))
        if k == "TTR":
            metrics[k] = round(v, 4)
        elif k == "MLU":
            metrics[k] = round(v, 3)
        else:
            metrics[k] = int(v)

    b_counts = extract_B_class_features(predicted_ist_words or "")
    internal = {IS_COUNT_LABELS[k]: int(b_counts.get(k, 0)) for k in IS_COUNT_LABELS}

    return {
        "core": metrics,
        "internal_state_counts": internal,
        "source": "jieba",
    }


def _filter_benchmark(
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


def peer_linguistic_norms(
    benchmark_df: pd.DataFrame,
    age: int,
    story_type: str,
    task_type: Optional[str],
) -> dict[str, Any]:
    """常模：narratives.csv 专家标注 TNW/TDW/TNU/MLU 的同龄同组均值。"""
    from benchmark_norms import expert_linguistic_peer_means

    return expert_linguistic_peer_means(benchmark_df, age, story_type, task_type)


def format_linguistic_report_section(
    metrics: dict[str, Any],
    peer: dict[str, Any],
    age: int,
    story_type: str,
    task_type: Optional[str],
) -> list[str]:
    """生成报告中的语言学指标段落（行列表）。"""
    core = metrics.get("core", {})
    lines = [
        "\n1. 语言产出指标 (Jieba · 本次叙事自动统计；常模为专家标注语料均值)"
    ]
    for key in CORE_KEYS:
        zh, en = LINGUISTIC_LABELS[key]
        val = core.get(key)
        if val is None:
            continue
        if key == "MLU":
            disp = f"{float(val):.3f}"
        elif key == "TTR":
            disp = f"{float(val):.4f}"
        else:
            disp = str(int(val))
        lines.append(f"   - {key} ({zh}, {en}): {disp}")

    internal = metrics.get("internal_state_counts") or {}
    if any(v > 0 for v in internal.values()):
        lines.append("\n   [BART 线索 · 内部状态词检出（Jieba 匹配）]")
        for label, cnt in internal.items():
            if cnt > 0:
                lines.append(f"   - {label}: {cnt}")

    avgs = peer.get("averages") or {}
    n = peer.get("n", 0)
    if n > 0 and avgs:
        peer_desc = f"专家常模参照 (narratives.csv · 年龄 {age}, 主题 {story_type}"
        if task_type:
            peer_desc += f", {task_type}"
        peer_desc += f", n={n})"
        lines.append(f"\n   - [{peer_desc}]")
        for key in CORE_KEYS:
            if key not in avgs:
                continue
            zh, _ = LINGUISTIC_LABELS[key]
            yours = core.get(key)
            avg = avgs[key]
            if yours is None:
                continue
            yf = float(yours)
            af = float(avg)
            cmp = "高于" if yf > af else ("低于" if yf < af else "接近")
            if key in ("MLU", "TTR"):
                lines.append(f"     - {key} ({zh}): 本次 {yf:.3f} vs 常模 {af:.3f} ({cmp})")
            else:
                lines.append(f"     - {key} ({zh}): 本次 {int(yf)} vs 常模 {af:.1f} ({cmp})")
    else:
        lines.append(
            f"\n   - [!] 常模库中无匹配组 (age={age}, story_type={story_type}"
            + (f", task_type={task_type}" if task_type else "")
            + ")，跳过语言学同龄对比。"
        )
    return lines
