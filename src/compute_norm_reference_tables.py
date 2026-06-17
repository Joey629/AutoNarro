#!/usr/bin/env python3
"""
Appendix E — template: norm-referenced percentile tables by age × task_type.

Expects a DataFrame with (at minimum):
  - age_group: 4 / 5 / 6 (or map from raw `age`)
  - task_type: storytelling vs retelling (same strings as your corpus, e.g. Telling / Retelling)
  - micro_score: expert sum of A2–A16 present (0–15), e.g. sum of binary columns or SS_Sum
  - macro_score: expert SC_Sum (0–9)

Usage:
  python compute_norm_reference_tables.py path/to/annotated_corpus.csv

If no path given, prints column contract only.
"""
import sys
from typing import Optional

import pandas as pd

PERCENTILES = [10, 25, 50, 75, 90]
PERCENTILE_ARGS = [p / 100.0 for p in PERCENTILES]


def norm_table(df: pd.DataFrame, score_col: str) -> pd.DataFrame:
    """Per (age_group, task_type): count, mean, std, min, max, requested percentiles."""
    g = df.groupby(["age_group", "task_type"], observed=True)[score_col]
    out = g.describe(percentiles=PERCENTILE_ARGS)
    # describe uses names like 10%, 25%, ...
    return out


def try_prepare_from_benchmark(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """
    If the CSV has expert labels A2–A16, SC_Sum, age, task_type (e.g. multitask
    predictions_with_metadata.csv), build age_group / micro / macro columns.

    Norms must use **expert** columns only. In that export, `get_all_predictions`
    overwrites only the `score` column; A2–A16 and SC_Sum are left as corpus labels.
    Micro = sum of A2–A16 (15 items; Appendix E); macro = SC_Sum (0–9).
    """
    need = ["A2", "A16", "SC_Sum", "age", "task_type"]
    if not all(c in df.columns for c in need):
        return None
    micro_cols = [f"A{i}" for i in range(2, 17)]  # A2..A16
    if not all(c in df.columns for c in micro_cols):
        return None
    out = df.copy()
    out["age_group"] = pd.to_numeric(out["age"], errors="coerce").astype("Int64")
    out["micro_score"] = out[micro_cols].sum(axis=1)
    out["macro_score"] = pd.to_numeric(out["SC_Sum"], errors="coerce")
    out = out.dropna(subset=["age_group", "task_type", "micro_score", "macro_score"])
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    path = sys.argv[1]
    df = pd.read_csv(path)

    # --- adapt column names to your CSV ---
    # Example: if you have age 4/5/6 and task_type already:
    required = ["age_group", "task_type", "micro_score", "macro_score"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        prepared = try_prepare_from_benchmark(df)
        if prepared is not None:
            print(
                "Auto-mapped from benchmark-style CSV: age→age_group, "
                "sum(A2..A16)→micro_score, SC_Sum→macro_score"
            )
            df = prepared
        else:
            print("Missing columns:", missing)
            print("Available:", list(df.columns))
            print("\nMap your data, e.g.:")
            print("  df['age_group'] = df['age'].astype(int)")
            print("  df['micro_score'] = df[['A2',...,'A16']].sum(axis=1)")
            print("  df['macro_score'] = df['SC_Sum']")
            sys.exit(1)

    print("=== Micro-structural (0–15) ===")
    print(norm_table(df, "micro_score").to_string())
    print("\n=== Macro-structural SC_Sum (0–9) ===")
    print(norm_table(df, "macro_score").to_string())

    # Optional: export for thesis tables
    # norm_table(df, "micro_score").to_csv("norm_micro_by_age_task.csv")
    # norm_table(df, "macro_score").to_csv("norm_macro_by_age_task.csv")


if __name__ == "__main__":
    main()
