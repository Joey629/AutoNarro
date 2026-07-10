# analyze_macro_core.py
# 宏观回归（专家 微观编码器 + XGB）共用逻辑：特征、预测、测试集指标、误差样本、元数据图。
# 入口（仅此二脚本）：analyze_macro_errors.py | analyze_macro_metadata.py

from __future__ import annotations

import os
import warnings

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

import config_analysis_output_paths as arp
import analyze_bootstrap as aboot
import micro_encoder as rfe
import train_micro_shared as msh
import train_micro as micro
from paths import split_cache_path

warnings.filterwarnings("ignore")
plt.rcParams["font.sans-serif"] = [
    "Heiti TC",
    "PingFang SC",
    "SimHei",
    "Arial Unicode MS",
    "sans-serif",
]
plt.rcParams["axes.unicode_minus"] = False

# 默认参数；两个入口脚本用 pipeline 覆盖为 "errors" 或 "metadata"
BASE_CONFIG: dict = {
    "pipeline": "full",  # 仅直接调用本模块且未改 CONFIG 时；正常运行请用两个 analyze_* 入口
    "data_path": micro.FILE_PATH,
    "model_name": micro.MODEL_NAME,
    "micro_checkpoint": "models/micro_narro_v4.pth",
    "xgb_models_dir": None,
    "model_prefix": "auto_xgb_model",
    "feature_pipeline": "automated",  # "expert"：CSV 专家语言学列 + ist_words
    "bart_model_dir": "models/bart_narro_v4",
    "automated_linguistic_columns": [
        "auto_TNU",
        "auto_MLU",
        "auto_TNW",
        "auto_TDW",
        "auto_IS_Per_count",
        "auto_IS_Phy_count",
        "auto_IS_Con_count",
        "auto_IS_Emo_count",
        "auto_IS_Men_count",
        "auto_IS_Ling_count",
    ],
    "use_micro_prob_in_xgb": False,
    "split_cache": str(split_cache_path()),
    "split_seed": 42,
    "target_variables": ["SC_E1", "SC_E2", "SC_E3"],
    "hier_targets": {"SC_E2"},
    "linguistic_feature_columns": ["TNW", "TDW", "TNU", "MLU", "TTR"],
    "output_dir": None,
    "top_n_errors": 20,
    "export_error_csv": True,
    "metadata_subset": "test",
    "metadata_columns": {
        "age_column": "age",
        "left_behind_column": "left_behind",
        "story_theme_column": "story_type",
        "narrative_type_column": "task_type",
    },
    "run_metadata_plots": True,
    # metadata 管道是否额外写出与 errors 相同的 SC_Sum 真值–预测散点（论文「评估框架」宏观对齐图）
    "run_sc_sum_scatter_in_metadata": False,
    "sc_sum_scatter_title": "SC_Sum (test)",
    # metadata 管道：按 age / task_type / 交叉 分层写 subgroup_regression_SC_Sum_*.csv
    "run_subgroup_performance_metrics": False,
    "feature_cache_path": None,
    "run_manifest_script": "analyze_macro_core",
}


def _append_auto_ttr(ling: np.ndarray, base_cols: list[str]) -> tuple[np.ndarray, list[str]]:
    ic_nw = base_cols.index("auto_TNW")
    ic_dw = base_cols.index("auto_TDW")
    with np.errstate(divide="ignore", invalid="ignore"):
        ttr = ling[:, ic_dw] / (ling[:, ic_nw] + 1e-9)
    ttr = np.nan_to_num(ttr, nan=0.0, posinf=0.0, neginf=0.0)
    return np.hstack([ling, ttr.reshape(-1, 1)]), list(base_cols) + ["auto_TTR"]


def _build_automated_ling_matrix(df_work: pd.DataFrame, cfg: dict) -> np.ndarray:
    from features_automated import analyze_automated_features
    from tqdm import tqdm

    base_cols = list(cfg["automated_linguistic_columns"])
    rows = []
    for _, row in tqdm(df_work.iterrows(), total=len(df_work), desc="A+B features"):
        vec, _ = analyze_automated_features(
            str(row["text"]), str(row.get("predicted_ist_words", "") or "")
        )
        rows.append(vec)
    ling = np.array(rows, dtype=np.float64)
    ling, _ = _append_auto_ttr(ling, base_cols)
    return ling


def _prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    df["ist_words"] = df.get("ist_words", pd.Series(dtype=str)).fillna("")
    if "story_type" not in df.columns:
        raise ValueError("缺少列 story_type")
    msh.coerce_task_label_columns(df, micro.TASK_NAMES)
    return df


def _ensure_ttr_column(df: pd.DataFrame) -> None:
    if "TTR" in df.columns:
        return
    if "TNW" not in df.columns or "TDW" not in df.columns:
        print("[语言学] 无 TTR 且无法由 TNW/TDW 派生。")
        return
    tnw = pd.to_numeric(df["TNW"], errors="coerce").replace(0, np.nan)
    tdw = pd.to_numeric(df["TDW"], errors="coerce")
    df["TTR"] = (tdw / tnw).fillna(0.0)
    print("[语言学] 已派生 TTR ≈ TDW/TNW。")


def _safe_regression_metrics_subgroup(
    y_true: np.ndarray, y_pred: np.ndarray
) -> dict[str, float]:
    """子组样本较小时仍返回 n；相关/ R² 在 n<3 或方差为 0 时为 nan。"""
    y_true = np.asarray(y_true, dtype=np.float64).ravel()
    y_pred = np.asarray(y_pred, dtype=np.float64).ravel()
    m = np.isfinite(y_true) & np.isfinite(y_pred)
    y_true, y_pred = y_true[m], y_pred[m]
    n = int(len(y_true))
    base = {
        "n": float(n),
        "MSE": np.nan,
        "R2": np.nan,
        "Pearson_r": np.nan,
        "Spearman_rho": np.nan,
        "Acc_rounded": np.nan,
    }
    if n < 3:
        return base
    try:
        base.update(_metrics_block(y_true, y_pred))
    except Exception:
        pass
    return base


def write_subgroup_regression_performance(
    df: pd.DataFrame,
    meta: dict,
    out_dir: str,
    tag: str,
) -> None:
    """
    按年龄、任务类型、故事主题及年龄×任务交叉分层报告 SC_Sum 回归性能（审稿：子组性能可能差异显著）。
    依赖 predictions 中 SC_Sum、pred_SC_Sum 与元数据列。
    """
    yt_col, yp_col = "SC_Sum", "pred_SC_Sum"
    if yt_col not in df.columns or yp_col not in df.columns:
        print("[subgroup] 跳过：缺少 SC_Sum / pred_SC_Sum")
        return
    age_col = meta.get("age_column", "age")
    tt_col = meta.get("narrative_type_column", "task_type")
    story_col = meta.get("story_theme_column", "story_type")
    use = [yt_col, yp_col]
    if age_col in df.columns:
        use.append(age_col)
    if tt_col in df.columns:
        use.append(tt_col)
    if story_col in df.columns:
        use.append(story_col)
    sub = df[use].dropna(subset=[yt_col, yp_col])
    if sub.empty:
        return
    rows: list[dict] = []

    def append_group(stratum_name: str, key, part: pd.DataFrame) -> None:
        if part.empty:
            return
        level = (
            key
            if isinstance(key, str)
            else (" | ".join(str(x) for x in key) if isinstance(key, tuple) else str(key))
        )
        mm = _safe_regression_metrics_subgroup(
            part[yt_col].values, part[yp_col].values
        )
        rows.append({"stratum": stratum_name, "level": level, **mm})

    if age_col in sub.columns:
        for k, g in sub.groupby(age_col, dropna=False):
            append_group("age", k, g)
    if tt_col in sub.columns:
        for k, g in sub.groupby(tt_col, dropna=False):
            append_group("task_type", k, g)
    if story_col in sub.columns:
        for k, g in sub.groupby(story_col, dropna=False):
            append_group("story_theme", k, g)
    if age_col in sub.columns and tt_col in sub.columns:
        for k, g in sub.groupby([age_col, tt_col], dropna=False):
            append_group("age_x_task_type", k, g)

    out_df = pd.DataFrame(rows)
    path = os.path.join(out_dir, f"subgroup_regression_SC_Sum_{tag}.csv")
    out_df.to_csv(path, index=False, encoding="utf-8-sig")
    print("\n--- Subgroup regression performance (SC_Sum vs pred_SC_Sum) — held-out ---")
    print(out_df.to_string(index=False))
    print(f"✅ {path}")


def _metrics_block(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    pr, _ = pearsonr(y_true, y_pred)
    sp, _ = spearmanr(y_true, y_pred)
    acc = accuracy_score(y_true.astype(int), np.round(y_pred).astype(int))
    return {"MSE": mse, "R2": r2, "Pearson_r": pr, "Spearman_rho": sp, "Acc_rounded": acc}


def _plot_real_vs_pred(
    y_true: np.ndarray, y_pred: np.ndarray, title: str, path: str
) -> None:
    df_plot = pd.DataFrame({"true": y_true, "pred": y_pred})
    plt.figure(figsize=(7, 7))
    sns.regplot(data=df_plot, x="true", y="pred", scatter_kws={"alpha": 0.35, "s": 22})
    lo = min(float(y_true.min()), float(y_pred.min()))
    hi = max(float(y_true.max()), float(y_pred.max()))
    plt.plot([lo, hi], [lo, hi], "k:", lw=1)
    r2 = r2_score(y_true, y_pred)
    r, _ = pearsonr(y_true, y_pred)
    plt.title(f"{title}\nR²={r2:.4f}, r={r:.4f}")
    plt.xlabel("True")
    plt.ylabel("Predicted")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


def _analyze_by_category(
    df: pd.DataFrame,
    category_col: str,
    score_col: str,
    out_dir: str,
    plot_title: str,
    suffix: str,
    y_lim: tuple[float, float] | None = None,
) -> None:
    if category_col not in df.columns or score_col not in df.columns:
        return
    sub = df[[category_col, score_col]].dropna()
    if len(sub) < 2:
        return
    grouped = sub.groupby(category_col)[score_col].agg(["mean", "std", "count"]).sort_values(
        "mean", ascending=False
    )
    print(f"\n--- {plot_title} × {score_col}{suffix} ---\n{grouped}")
    groups = sub[category_col].unique()
    gdata = [sub.loc[sub[category_col] == g, score_col] for g in groups]
    stat_line = ""
    try:
        if len(groups) == 2:
            t_stat, p_val = stats.ttest_ind(gdata[0], gdata[1], equal_var=False)
            stat_line = f"Welch t = {t_stat:.3f}, p = {p_val:.4g}"
        elif len(groups) > 2:
            f_stat, p_val = stats.f_oneway(*gdata)
            stat_line = f"ANOVA F = {f_stat:.3f}, p = {p_val:.4g}"
        print(stat_line)
    except Exception as e:
        print(f"检验跳过: {e}")
    plt.figure(figsize=(9, 5))
    sns.boxplot(data=sub, x=category_col, y=score_col, order=grouped.index)
    plt.title(f"{plot_title} vs {score_col}{suffix}\n{stat_line}")
    plt.xticks(rotation=20, ha="right")
    if y_lim is not None:
        plt.ylim(y_lim)
    plt.tight_layout()
    fn = f"{category_col}_vs_{score_col}{suffix}_boxplot.png".replace("/", "_")
    plt.savefig(os.path.join(out_dir, fn), dpi=150)
    plt.close()


def _analyze_age_scatter(
    df: pd.DataFrame,
    age_col: str,
    score_col: str,
    out_dir: str,
    suffix: str,
    y_lim: tuple[float, float] | None = None,
) -> None:
    if age_col not in df.columns or score_col not in df.columns:
        return
    cl = df[[age_col, score_col]].dropna()
    if len(cl) < 3:
        return
    r_val, p_val = stats.pearsonr(cl[age_col], cl[score_col])
    plt.figure(figsize=(8, 5))
    sns.regplot(data=cl, x=age_col, y=score_col, scatter_kws={"alpha": 0.35})
    plt.title(f"Age vs {score_col}{suffix}\nr = {r_val:.3f}, p = {p_val:.4g}")
    if y_lim is not None:
        plt.ylim(y_lim)
    plt.tight_layout()
    fn = f"{age_col}_vs_{score_col}{suffix}_scatter.png".replace("/", "_")
    plt.savefig(os.path.join(out_dir, fn), dpi=150)
    plt.close()


def _analyze_interaction(
    df: pd.DataFrame,
    cat_col: str,
    cont_col: str,
    score_col: str,
    out_dir: str,
    suffix: str,
    y_lim: tuple[float, float] | None = None,
) -> None:
    if not all(c in df.columns for c in (cat_col, cont_col, score_col)):
        return
    sub = df.dropna(subset=[cat_col, cont_col, score_col])
    if len(sub) < 10:
        return
    try:
        g = sns.lmplot(
            data=sub,
            x=cont_col,
            y=score_col,
            hue=cat_col,
            height=6,
            aspect=1.2,
            scatter_kws={"alpha": 0.3, "s": 18},
        )
        if y_lim is not None:
            for ax in g.axes.flat:
                ax.set_ylim(y_lim)
        g.fig.suptitle(f"Interaction: {cont_col} × {cat_col} on {score_col}{suffix}", y=1.02)
        fn = f"interaction_{cat_col}_{cont_col}_{score_col}{suffix}.png".replace("/", "_")
        g.savefig(os.path.join(out_dir, fn), dpi=150)
        plt.close(g.fig)
    except Exception as e:
        print(f"交互图跳过: {e}")


def run_macro_analysis(user_config: dict | None = None) -> None:
    cfg = {**BASE_CONFIG, **(user_config or {})}
    pipeline = str(cfg["pipeline"]).lower().strip()
    if pipeline not in ("errors", "metadata", "full"):
        raise SystemExit("pipeline 须为 errors | metadata | full")

    do_errors = pipeline in ("errors", "full")
    do_metadata = pipeline in ("metadata", "full")

    if pipeline == "errors":
        subset = "test"
        print("[pipeline=errors] BERT 特征仅算测试集（与 4.1.2 held-out 一致）。")
    else:
        subset = str(cfg["metadata_subset"]).lower().strip()
        if subset not in ("test", "full"):
            raise SystemExit("metadata_subset 须为 test 或 full")

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    msh.set_seed(cfg["split_seed"])

    micro_cfg = aboot.load_micro_training_config()
    aboot.apply_micro_encoder_env(micro_cfg)
    cfg["model_name"] = micro_cfg.model_name

    ckpt = cfg["micro_checkpoint"]
    if not os.path.isfile(ckpt):
        raise SystemExit(f"❌ 缺少 微观权重: {ckpt}")

    stem = os.path.splitext(os.path.basename(ckpt))[0]
    xgb_dir = cfg["xgb_models_dir"] or "models/macro_xgb_narro_v4"

    out_dir = cfg["output_dir"]
    if not out_dir:
        if pipeline == "errors":
            out_dir = arp.OUTPUT_ANALYZE_MACRO_ERRORS
        elif pipeline == "metadata":
            out_dir = arp.OUTPUT_ANALYZE_MACRO_METADATA
        else:
            out_dir = f"macro_performance_{stem}"
    os.makedirs(out_dir, exist_ok=True)

    use_micro = cfg["use_micro_prob_in_xgb"]
    prefix = cfg["model_prefix"]

    df_all = pd.read_csv(cfg["data_path"])
    df_all = _prepare_dataframe(df_all)
    _ensure_ttr_column(df_all)

    targets = cfg["target_variables"]
    all_y_cols = targets + ["SC_Sum"]
    ling_cols = [c for c in cfg["linguistic_feature_columns"] if c in df_all.columns]
    for col in ling_cols + all_y_cols:
        if col in df_all.columns:
            df_all[col] = pd.to_numeric(df_all[col], errors="coerce").fillna(0)
    if "SC_Sum" not in df_all.columns and all(t in df_all.columns for t in targets):
        df_all["SC_Sum"] = df_all[targets].sum(axis=1)

    tr_idx, te_idx = rfe.load_or_create_macro_split(
        df_all,
        cfg.get("split_cache") or None,
        cfg["split_seed"],
    )

    if subset == "full":
        df_work = df_all.reset_index(drop=True)
        desc_bert = "full cohort"
    else:
        df_work = df_all.iloc[te_idx].reset_index(drop=True)
        desc_bert = "test only"

    cache_path = cfg.get("feature_cache_path") or ""
    feats_loaded_from_cache = False
    if cache_path and subset == "test" and os.path.isfile(cache_path):
        blob = joblib.load(cache_path)
        if blob.get("use_micro") == use_micro and np.array_equal(
            np.asarray(blob.get("te_idx")), np.asarray(te_idx)
        ):
            feats = blob["feats"]
            ling_mat = blob["ling_mat"]
            feats_loaded_from_cache = True
            print(f"[cache] 已加载 {cache_path}")

    if not feats_loaded_from_cache:
        feature_pipeline = str(cfg.get("feature_pipeline", "expert")).lower().strip()
        ist_col = "ist_words"
        if feature_pipeline == "automated":
            import bart_infer  # noqa: F401 — MPS 段错误规避（须在部分后端之前）
            from bart_infer import BARTCuePredictor
            from tqdm import tqdm

            bart_dir = cfg.get("bart_model_dir") or "models/bart_narro_v4"
            print(f"[pipeline] 自动化特征：BART → {bart_dir}")
            bart = BARTCuePredictor(model_dir=bart_dir)
            df_work = df_work.copy()
            df_work["predicted_ist_words"] = [
                bart.predict_ist_words(str(t))
                for t in tqdm(df_work["text"], desc="BART test")
            ]
            ist_col = "predicted_ist_words"
            ling_mat = _build_automated_ling_matrix(df_work, cfg)
        else:
            ling_mat = df_work[ling_cols].values.astype(np.float64)

        tok, bert, dev = rfe.load_micro_encoder(
            ckpt,
            cfg["model_name"],
            micro_config_path=os.environ.get("NARRO_MICRO_CONFIG", "configs/micro_narro_v4.json"),
        )
        print(
            f"\n--- BERT 特征 ({desc_bert}, ist={ist_col}, micro_in_XGB={use_micro}) ---"
        )
        feats = rfe.extract_all_micro_features(
            df_work,
            bert,
            tok,
            dev,
            ist_col,
            micro.MAX_LENGTH,
            True,
            desc_bert,
        )
        if cache_path and subset == "test":
            joblib.dump(
                {
                    "feats": feats,
                    "ling_mat": ling_mat,
                    "te_idx": te_idx,
                    "use_micro": use_micro,
                },
                cache_path,
            )
            print(f"[cache] 已写入 {cache_path}")

    preds: dict[str, np.ndarray] = {}
    for tv in targets:
        mode = "hierarchical" if tv in cfg["hier_targets"] else "global"
        X = rfe.build_regression_X(feats, ling_mat, mode, use_micro)
        mpath = os.path.join(xgb_dir, f"{prefix}_{tv}.joblib")
        if not os.path.isfile(mpath):
            raise SystemExit(f"❌ 缺少模型: {mpath}")
        model = joblib.load(mpath)
        preds[tv] = model.predict(X).astype(np.float64)
        print(f"[predict] {tv} X.shape={X.shape} ← {mpath}")

    results_df = df_work.copy()
    for tv in targets:
        results_df[f"pred_{tv}"] = preds[tv]
    results_df["pred_SC_Sum"] = sum(preds[t] for t in targets)

    df_test = df_all.iloc[te_idx].reset_index(drop=True)
    for col in ling_cols + all_y_cols:
        if col in df_test.columns:
            df_test[col] = pd.to_numeric(df_test[col], errors="coerce").fillna(0)
    if "SC_Sum" not in df_test.columns and all(t in df_test.columns for t in targets):
        df_test["SC_Sum"] = df_test[targets].sum(axis=1)

    if subset == "test":
        pred_e1 = preds["SC_E1"]
        pred_e2 = preds["SC_E2"]
        pred_e3 = preds["SC_E3"]
    else:
        pred_e1 = preds["SC_E1"][te_idx]
        pred_e2 = preds["SC_E2"][te_idx]
        pred_e3 = preds["SC_E3"][te_idx]

    pred_sum_test = pred_e1 + pred_e2 + pred_e3

    # 仅 metadata 管道写出，避免与 pipeline=full/errors 中 do_errors 重复落盘
    if cfg.get("run_sc_sum_scatter_in_metadata") and not do_errors:
        title = str(cfg.get("sc_sum_scatter_title") or "SC_Sum (test)")
        _plot_real_vs_pred(
            df_test["SC_Sum"].values.astype(np.float64),
            pred_sum_test.astype(np.float64),
            title,
            os.path.join(out_dir, "scatter_SC_Sum_real_vs_pred_test.png"),
        )
        print(f"[metadata] SC_Sum 真值–预测散点 → {out_dir}/scatter_SC_Sum_real_vs_pred_test.png")

    if do_errors:
        summary_rows = []
        for tv, p in [
            ("SC_E1", pred_e1),
            ("SC_E2", pred_e2),
            ("SC_E3", pred_e3),
        ]:
            m = _metrics_block(df_test[tv].values, p)
            m = {"target": tv, **m, "split": "test"}
            summary_rows.append(m)
            print(
                f"[test] {tv}  MSE={m['MSE']:.4f} R²={m['R2']:.4f} "
                f"r={m['Pearson_r']:.4f} ρ={m['Spearman_rho']:.4f} Acc={m['Acc_rounded']:.4f}"
            )
        msum = _metrics_block(df_test["SC_Sum"].values, pred_sum_test)
        msum = {"target": "SC_Sum", **msum, "split": "test"}
        summary_rows.append(msum)
        print(
            f"[test] SC_Sum  MSE={msum['MSE']:.4f} R²={msum['R2']:.4f} "
            f"r={msum['Pearson_r']:.4f} ρ={msum['Spearman_rho']:.4f} Acc={msum['Acc_rounded']:.4f}"
        )
        pd.DataFrame(summary_rows).to_csv(
            os.path.join(out_dir, "macro_performance_summary_test.csv"),
            index=False,
            encoding="utf-8-sig",
        )
        _plot_real_vs_pred(
            df_test["SC_Sum"].values,
            pred_sum_test,
            "SC_Sum (test)",
            os.path.join(out_dir, "scatter_SC_Sum_real_vs_pred_test.png"),
        )

        if cfg["export_error_csv"]:
            err_dir = os.path.join(out_dir, "error_samples")
            os.makedirs(err_dir, exist_ok=True)
            n = cfg["top_n_errors"]
            base = df_test.copy()
            base["pred_SC_E1"] = pred_e1
            base["pred_SC_E2"] = pred_e2
            base["pred_SC_E3"] = pred_e3
            for tv, pred_col, p in [
                ("SC_E1", "pred_SC_E1", pred_e1),
                ("SC_E2", "pred_SC_E2", pred_e2),
                ("SC_E3", "pred_SC_E3", pred_e3),
            ]:
                resid = base[tv].values - p
                base[f"{tv}_residual"] = resid
                ocols = ["text", "story_type", tv, pred_col, f"{tv}_residual"]
                ocols = [c for c in ocols if c in base.columns]
                base.nlargest(n, f"{tv}_residual")[ocols].to_csv(
                    os.path.join(err_dir, f"{tv}_worst_under_prediction.csv"),
                    index=False,
                    encoding="utf-8-sig",
                )
                base.nsmallest(n, f"{tv}_residual")[ocols].to_csv(
                    os.path.join(err_dir, f"{tv}_worst_over_prediction.csv"),
                    index=False,
                    encoding="utf-8-sig",
                )
            print(f"[errors] 已写入 {err_dir}")

    if do_metadata and cfg["run_metadata_plots"]:
        meta = cfg["metadata_columns"]
        sfx_real = "_true"
        sfx_pred = "_pred"
        for score_col, sfx in [
            ("SC_Sum", sfx_real),
            ("pred_SC_Sum", sfx_pred),
        ]:
            if score_col not in results_df.columns:
                continue
            for key, title in [
                (meta["story_theme_column"], "Story theme"),
                (meta["narrative_type_column"], "Narrative type"),
                (meta["left_behind_column"], "Left-behind"),
            ]:
                _analyze_by_category(results_df, key, score_col, out_dir, title, sfx)
            _analyze_age_scatter(
                results_df, meta["age_column"], score_col, out_dir, sfx
            )
            _analyze_interaction(
                results_df,
                meta["narrative_type_column"],
                meta["age_column"],
                score_col,
                out_dir,
                sfx,
            )

    if do_metadata and cfg.get("run_subgroup_performance_metrics"):
        write_subgroup_regression_performance(
            results_df, cfg["metadata_columns"], out_dir, str(subset)
        )

    results_path = os.path.join(out_dir, "predictions_with_scores.csv")
    results_df.to_csv(results_path, index=False, encoding="utf-8-sig")

    pd.DataFrame(
        [
            {
                "script": cfg["run_manifest_script"],
                "micro_checkpoint": ckpt,
                "xgb_models_dir": xgb_dir,
                "model_prefix": prefix,
                "use_micro_prob_in_xgb": use_micro,
                "split_cache": cfg.get("split_cache"),
                "metadata_subset": subset,
                "pipeline": pipeline,
                "output_dir": out_dir,
                "run_sc_sum_scatter_in_metadata": cfg.get(
                    "run_sc_sum_scatter_in_metadata", False
                ),
                "sc_sum_scatter_title": cfg.get("sc_sum_scatter_title"),
                "run_subgroup_performance_metrics": cfg.get(
                    "run_subgroup_performance_metrics", False
                ),
            }
        ]
    ).to_csv(os.path.join(out_dir, "run_manifest.csv"), index=False)

    print(f"\n✅ 完成 → {out_dir}")
