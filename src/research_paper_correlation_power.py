#!/usr/bin/env python3
"""
审稿补充：Pearson 相关的统计功效（与 G*Power「Correlation / bivariate normal」双侧检验 ρ=0 一致）
及 r 的 95% 置信区间（Fisher z 变换）。

功效采用 t 统计量 t = r√(n−2)/√(1−r²) 在 H0 下服从 t_{n−2}；在备择真相关 ρ 下服从
非中心 t，非中心参数 λ = ρ√(n−2)/√(1−ρ²)（与 R 包 pwr::pwr.r.test 一致）。

F1 的 bootstrap 95% CI：research_paper_statistics_bootstrap.py --task bootstrap；
批量 Fisher r CI（多组 r:n）与 Cohen's d / η²：research_paper_effect_sizes.py。

用法示例：
  python research_paper_correlation_power.py --n 113 --alpha 0.05 --rho 0.25 0.29
  python research_paper_correlation_power.py --n 113 --report-r 0.25 0.29
"""
from __future__ import annotations

import argparse
import math

import numpy as np
from scipy import stats


def power_pearson_correlation_twosided(
    n: int,
    rho: float,
    alpha: float = 0.05,
) -> float:
    """双侧检验 H0: ρ=0 vs H1: ρ≠0 时，在真值为 rho 下的检验功效。"""
    if n < 4:
        raise ValueError("n 至少为 4（Pearson 相关 df = n-2）")
    if not (-1 < rho < 1):
        raise ValueError("rho 须在 (-1, 1) 内")
    df = n - 2
    t_crit = float(stats.t.ppf(1 - alpha / 2, df))
    lam = rho * math.sqrt(df) / math.sqrt(1 - rho * rho)
    # P(|T| > t_crit) = P(T > t_crit) + P(T < -t_crit)
    return float(
        1.0 - stats.nct.cdf(t_crit, df, lam) + stats.nct.cdf(-t_crit, df, lam)
    )


def pearson_r_ci_fisher(
    r: float,
    n: int,
    confidence: float = 0.95,
) -> tuple[float, float]:
    """观测相关系数 r 的近似 95% CI（Fisher z，正态临界值）。"""
    if n <= 3:
        raise ValueError("Fisher 近似需要 n > 3")
    if not (-1 < r < 1):
        raise ValueError("r 须在 (-1, 1) 内")
    z = math.atanh(r)
    se = 1.0 / math.sqrt(n - 3)
    z_half = stats.norm.ppf(0.5 + confidence / 2)
    lo_z = z - z_half * se
    hi_z = z + z_half * se
    return (math.tanh(lo_z), math.tanh(hi_z))


def main() -> None:
    p = argparse.ArgumentParser(description="相关功效 + Fisher z CI（论文审稿用）")
    p.add_argument("--n", type=int, default=113, help="用于相关分析的配对样本量（如测试集叙事数）")
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument(
        "--rho",
        type=float,
        nargs="*",
        default=[0.25],
        help="备择假设下的效应量 ρ，用于事后/先验功效（G*Power 中 Correlation 的 r）",
    )
    p.add_argument(
        "--report-r",
        type=float,
        nargs="*",
        default=[],
        help="论文中报告的点估计 r，输出其 Fisher 95%% CI",
    )
    args = p.parse_args()

    print("=== Pearson 相关：双侧检验功效（与 G*Power Correlation 一致）===\n")
    print(f"N = {args.n}, α = {args.alpha}, df = {args.n - 2}\n")
    for rho in args.rho:
        powv = power_pearson_correlation_twosided(args.n, rho, args.alpha)
        print(
            f"  备择 |ρ| = {rho:.3f} 时 power ≈ {powv:.4f}  "
            f"({'≥ 0.70' if powv >= 0.70 else '< 0.70'} 相对审稿常用阈值 0.70)"
        )

    if args.report_r:
        print("\n=== 观测 r 的 95% CI（Fisher z 变换）===\n")
        for r in args.report_r:
            lo, hi = pearson_r_ci_fisher(r, args.n, confidence=0.95)
            print(f"  r = {r:.3f}, n = {args.n}  →  95% CI ≈ [{lo:.3f}, {hi:.3f}]")

    print(
        "\n[说明] Macro-F1 的 bootstrap 区间请运行：\n"
        "  python research_paper_statistics_bootstrap.py --task bootstrap --eval-split row_20pct\n"
        "（或与您正文一致的 eval_split / 阈值参数。）"
    )


if __name__ == "__main__":
    main()
