#!/usr/bin/env python3
"""
审稿补充：效应量与区间（与 Results 4.2 等节对齐时可引用）。

1) 年龄相关（Age-related gains）：单因素 ANOVA（F、df、p、η²）+ 两两独立样本 t（合并方差，t、df、p）+ Cohen's d。

2) 任务类型 Retelling vs Telling：专家分与自动分的 Cohen's d（同上）。

3) 故事主题 one-way ANOVA：F、df、η² 等。

4) Pearson r 的 95% CI：Fisher z（与 research_paper_correlation_power 一致）。

默认数据：analyze_macro_metadata/predictions_with_scores.csv（held-out test，与 metadata 分析一致）。

用法：
  python research_paper_effect_sizes.py
  python research_paper_effect_sizes.py --csv path/to/predictions_with_scores.csv
  python research_paper_effect_sizes.py --fisher-rn 0.25:114 0.29:114 0.67:114 0.68:114
  python research_paper_effect_sizes.py --run-f1-bootstrap --n-bootstrap 500
"""
from __future__ import annotations

import argparse
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from research_paper_correlation_power import pearson_r_ci_fisher

ROOT = Path(__file__).resolve().parent
DEFAULT_CSV = ROOT / "analyze_macro_metadata" / "predictions_with_scores.csv"


def cohens_d_two_sample(
    x1: np.ndarray, x2: np.ndarray
) -> tuple[float, float, float, float, float, float]:
    """返回 (n1, n2, M1, M2, SD_pooled, d)，d = (M1-M2)/SD_pooled。"""
    x1 = np.asarray(x1, dtype=np.float64).ravel()
    x2 = np.asarray(x2, dtype=np.float64).ravel()
    x1 = x1[np.isfinite(x1)]
    x2 = x2[np.isfinite(x2)]
    n1, n2 = len(x1), len(x2)
    if n1 < 2 or n2 < 2:
        return (n1, n2, math.nan, math.nan, math.nan, math.nan)
    m1, m2 = float(np.mean(x1)), float(np.mean(x2))
    v1, v2 = float(np.var(x1, ddof=1)), float(np.var(x2, ddof=1))
    sp = math.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    d = (m1 - m2) / sp if sp > 1e-12 else math.nan
    return (n1, n2, m1, m2, sp, d)


def one_way_anova_age_three_groups(
    df: pd.DataFrame, age_col: str, value_col: str, age_levels: tuple[int, ...] = (4, 5, 6)
) -> dict:
    """4/5/6 岁三组 one-way ANOVA：返回 F, df1, df2, p, η² 及各组 n、M。"""
    sub = df[[age_col, value_col]].dropna()
    sub[age_col] = pd.to_numeric(sub[age_col], errors="coerce")
    sub = sub.dropna(subset=[age_col])
    groups: list[np.ndarray] = []
    ns: list[int] = []
    means: list[float] = []
    for a in age_levels:
        y = sub.loc[sub[age_col] == a, value_col].to_numpy(dtype=np.float64)
        y = y[np.isfinite(y)]
        groups.append(y)
        ns.append(len(y))
        means.append(float(np.mean(y)) if len(y) else math.nan)
    k = len([g for g in groups if len(g) > 0])
    if k < 2:
        return {
            "F": math.nan,
            "df1": math.nan,
            "df2": math.nan,
            "p": math.nan,
            "eta2": math.nan,
            "group_ns": ns,
            "group_means": means,
        }
    nonempty = [g for g in groups if len(g) >= 1]
    f_stat, p_val = stats.f_oneway(*nonempty)
    all_y = np.concatenate(nonempty)
    grand = float(np.mean(all_y))
    n_tot = len(all_y)
    ss_total = float(np.sum((all_y - grand) ** 2))
    ss_between = 0.0
    for g in nonempty:
        ss_between += len(g) * (float(np.mean(g)) - grand) ** 2
    df1 = k - 1
    df2 = n_tot - k
    eta2 = ss_between / ss_total if ss_total > 0 else math.nan
    return {
        "F": float(f_stat),
        "df1": float(df1),
        "df2": float(df2),
        "p": float(p_val),
        "eta2": float(eta2),
        "group_ns": ns,
        "group_means": means,
        "age_levels": list(age_levels),
    }


def pairwise_student_t_pooled(
    x1: np.ndarray, x2: np.ndarray
) -> tuple[float, float, float]:
    """合并方差独立样本 t：返回 (t, df, p) 双侧。"""
    x1 = np.asarray(x1, dtype=np.float64).ravel()
    x2 = np.asarray(x2, dtype=np.float64).ravel()
    x1 = x1[np.isfinite(x1)]
    x2 = x2[np.isfinite(x2)]
    n1, n2 = len(x1), len(x2)
    if n1 < 2 or n2 < 2:
        return (math.nan, math.nan, math.nan)
    m1, m2 = float(np.mean(x1)), float(np.mean(x2))
    v1, v2 = float(np.var(x1, ddof=1)), float(np.var(x2, ddof=1))
    sp2 = ((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2)
    sp = math.sqrt(sp2) if sp2 > 0 else math.nan
    if not math.isfinite(sp) or sp < 1e-12:
        return (math.nan, float(n1 + n2 - 2), math.nan)
    se = sp * math.sqrt(1.0 / n1 + 1.0 / n2)
    t_stat = (m1 - m2) / se if se > 0 else math.nan
    df = float(n1 + n2 - 2)
    p_two = float(2 * stats.t.sf(abs(t_stat), int(n1 + n2 - 2)))
    return (float(t_stat), df, p_two)


def one_way_anova_eta_squared(df: pd.DataFrame, group_col: str, value_col: str) -> dict:
    """单因素 ANOVA：η² = SS_between / SS_total。"""
    sub = df[[group_col, value_col]].dropna()
    y = sub[value_col].to_numpy(dtype=np.float64)
    g = sub[group_col].astype(str)
    grand_mean = float(np.mean(y))
    ss_total = float(np.sum((y - grand_mean) ** 2))
    ss_between = 0.0
    groups = []
    for lev in g.unique():
        part = y[g == lev]
        if len(part) < 1:
            continue
        groups.append(part)
        ss_between += len(part) * (float(np.mean(part)) - grand_mean) ** 2
    if ss_total <= 0 or len(groups) < 2:
        return {"k": len(groups), "F": math.nan, "p": math.nan, "eta2": math.nan}
    f_stat, p_val = stats.f_oneway(*groups)
    eta2 = ss_between / ss_total
    return {"k": len(groups), "F": float(f_stat), "p": float(p_val), "eta2": float(eta2)}


def parse_fisher_rn(specs: list[str]) -> list[tuple[float, int]]:
    out: list[tuple[float, int]] = []
    for s in specs:
        parts = s.replace(" ", "").split(":")
        if len(parts) != 2:
            raise ValueError(f"无效 --fisher-rn 项（需 r:n）: {s!r}")
        r, n = float(parts[0]), int(parts[1])
        out.append((r, n))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Cohen's d、η²、Fisher r CI、可选 F1 bootstrap")
    ap.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="含 age, task_type, story_type, SC_Sum, pred_SC_Sum")
    ap.add_argument(
        "--expert-col", default="SC_Sum", help="专家连续分（年龄/主题比较用）"
    )
    ap.add_argument(
        "--auto-col", default="pred_SC_Sum", help="模型宏观预测分（任务类型「自动分」）"
    )
    ap.add_argument(
        "--fisher-rn",
        type=str,
        nargs="*",
        default=["0.25:114", "0.29:114", "0.67:114", "0.68:114"],
        help="Fisher 95%% CI：每项 r:n（n 为计算该 r 时的配对样本量，请与正文一致）",
    )
    ap.add_argument(
        "--run-f1-bootstrap",
        action="store_true",
        help="子进程运行 research_paper_statistics_bootstrap（较慢，需权重与数据）",
    )
    ap.add_argument(
        "--n-bootstrap",
        type=int,
        default=1000,
        help="传给 research_paper_statistics_bootstrap 的 bootstrap 次数",
    )
    args = ap.parse_args()

    if not args.csv.is_file():
        print(f"未找到 CSV: {args.csv}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(args.csv)
    ec, ac = args.expert_col, args.auto_col
    for c in ("age", "task_type", "story_type", ec, ac):
        if c not in df.columns:
            print(f"缺少列: {c}", file=sys.stderr)
            sys.exit(1)

    df = df.copy()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    print(f"数据: {args.csv}  (n={len(df)})\n")

    # --- 1. Age-related gains：ANOVA + 两两 t（非仅相关）---
    print("=== 1. Age-related gains：年龄组（4 / 5 / 6）× 专家分 %s ===" % ec)
    ao = one_way_anova_age_three_groups(df, "age", ec, (4, 5, 6))
    al = ao.get("age_levels", [4, 5, 6])
    for i, a in enumerate(al):
        n_i = ao["group_ns"][i] if i < len(ao["group_ns"]) else 0
        m_i = ao["group_means"][i] if i < len(ao["group_means"]) else math.nan
        print(f"  {a}岁: n={n_i}, M={m_i:.4f}")
    print(
        f"\n  [单因素 ANOVA] F({int(ao['df1'])}, {int(ao['df2'])}) = {ao['F']:.4f}, "
        f"p = {ao['p']:.4g}, η² = {ao['eta2']:.4f}"
    )
    print(
        "  [两两比较：独立样本 t，合并方差，双侧 p；效应量 Cohen's d 同前式；"
        "未做多重比较校正，若报告需 Bonferroni/FDR 可在此基础上调整]"
    )
    pairs = [(4, 5), (5, 6), (4, 6)]
    for a, b in pairs:
        x1 = df.loc[df["age"] == a, ec].dropna().to_numpy(dtype=np.float64)
        x2 = df.loc[df["age"] == b, ec].dropna().to_numpy(dtype=np.float64)
        t_stat, df_t, p_t = pairwise_student_t_pooled(x1, x2)
        n1, n2, m1, m2, sp, d = cohens_d_two_sample(x1, x2)
        print(
            f"  {a}岁 vs {b}岁: t({int(df_t)}) = {t_stat:+.4f}, p = {p_t:.4g}; "
            f"d = {d:+.4f}  （t 与 d 均对应 (M_{a}−M_{b})，合并方差）"
        )

    # --- 2. 任务类型 Cohen's d ---
    print(f"\n=== 2. Retelling vs Telling：Cohen's d ===")
    r_mask = df["task_type"].astype(str) == "Retelling"
    t_mask = df["task_type"].astype(str) == "Telling"
    for name, col in [("专家分 (%s)" % ec, ec), ("自动分 (%s)" % ac, ac)]:
        x_r = df.loc[r_mask, col].dropna().to_numpy(dtype=np.float64)
        x_t = df.loc[t_mask, col].dropna().to_numpy(dtype=np.float64)
        n1, n2, m1, m2, sp, d = cohens_d_two_sample(x_r, x_t)
        print(
            f"  {name}: M_Retelling={m1:.4f}, M_Telling={m2:.4f}, "
            f"n=({n1},{n2}), SD_pooled={sp:.4f}, d = {d:+.4f}  （d = (M_Ret-M_Tell)/SD_pooled）"
        )

    # --- 3. 故事主题 η²（专家分 one-way ANOVA）---
    print(f"\n=== 3. 故事主题 one-way ANOVA（专家分 {ec}；含 F、df）===")
    an = one_way_anova_eta_squared(df, "story_type", ec)
    n_story = len(df[[ec, "story_type"]].dropna())
    df2_story = n_story - an["k"]
    print(
        f"  k={an['k']} 组, N={n_story}, F({an['k'] - 1}, {df2_story}) = {an['F']:.4f}, "
        f"p={an['p']:.4g}, η² = {an['eta2']:.4f}"
    )

    # --- 4. Fisher CI ---
    print("\n=== 4. Pearson r 的 95% CI（Fisher z: z=atanh(r), SE=1/√(n-3), 再 tanh）===")
    for r, n in parse_fisher_rn(args.fisher_rn):
        lo, hi = pearson_r_ci_fisher(r, n, confidence=0.95)
        z = math.atanh(r)
        se = 1.0 / math.sqrt(n - 3)
        print(
            f"  r = {r:.2f}, n = {n}: z = {z:.4f}, SE = {se:.4f}  →  95% CI_r ≈ [{lo:.3f}, {hi:.3f}]"
        )

    # --- 5. F1 bootstrap ---
    print("\n=== 5. Macro-F1 的 95% CI（bootstrap）===")
    if args.run_f1_bootstrap:
        cmd = [
            sys.executable,
            str(ROOT / "research_paper_statistics_bootstrap.py"),
            "--task",
            "bootstrap",
            "--eval-split",
            "row_20pct",
            "--n_bootstrap",
            str(args.n_bootstrap),
        ]
        print("运行:", " ".join(cmd))
        subprocess.run(cmd, cwd=str(ROOT), check=False)
    else:
        print(
            "未加 --run-f1-bootstrap。请在本目录执行（与正文划分/阈值一致时可改参数）：\n"
            f"  python research_paper_statistics_bootstrap.py --task bootstrap --eval-split row_20pct "
            f"--n_bootstrap {args.n_bootstrap}\n"
            "说明：row_20pct 为逐行 80/20（n_test≈113），若正文 F1 来自 macro npz 的 test（n≈114），"
            "区间以同一划分重跑 bootstrap 为准。"
        )


if __name__ == "__main__":
    main()
