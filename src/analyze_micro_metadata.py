# analyze_micro_metadata.py
# 在 train_micro 协议下：多任务 15 头推理，叙事级分数 = 15 个任务 sigmoid 概率的均值；
# 元数据图表与 analyze_macro_metadata.py（analyze_macro_core）对齐：
#   同一套 boxplot / 年龄散点 / age×task_type 交互（lmplot）：金标 MT_Sum 与模型 Σp̂（pred_MT_sum_expected）
#   均为 0–15 量纲，且可设 metadata_shared_y_lim 统一纵轴；叙事级仍保留 score / pred_MT_mean（0–1）列供其它用途。
#   另：专家微观结构项数之和 MT_Sum（0–15）与模型「期望项数」Σp̂（= pred_MT_mean×15）的散点图，
#   对齐回归侧 scatter_SC_Sum_real_vs_pred_test.png（预留测试集上真值–预测关系）。
#   另：15 叙事要素（A2–A16）逐任务准确率「矩阵」热力图（3×5），标示天花板（默认≥90%）与地板（默认≤40%）区间，
#   并导出 per_task_accuracy_*.csv。
#   另：run_subgroup_performance_metrics → subgroup_multitask_metrics_*.csv（按 age / task_type / story_theme / 交叉 的
#   macro-F1、R²(MT_Sum vs Σp̂)、15 头平均准确率、MAE/r，审稿子组性能）。

import os
import warnings

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np
import pandas as pd
import seaborn as sns
import torch
from scipy.stats import pearsonr
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
from sklearn.metrics import f1_score, r2_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer

import config_analysis_output_paths as arp
import micro_encoder as rfe
import train_micro_shared as msh
import train_micro as micro
from analyze_macro_core import (
    _analyze_age_scatter,
    _analyze_by_category,
    _analyze_interaction,
)

warnings.filterwarnings("ignore")

plt.rcParams["font.sans-serif"] = [
    "Heiti TC",
    "PingFang SC",
    "SimHei",
    "Arial Unicode MS",
    "sans-serif",
]
plt.rcParams["axes.unicode_minus"] = False

CONFIG = {
    "data_path": micro.FILE_PATH,
    "micro_weights": "models/micro_narro_v4.pth",
    "model_name": micro.MODEL_NAME,
    "batch_size": 16,
    # 与 analyze_macro_metadata 的 metadata_subset='test' 一致：默认与宏观回归同源 test 索引
    "eval_split": "micro_test",  # 'all' | 'micro_test' | float in (0,1) 随机 test 比例
    "split_cache": "regression_macro_split_narro_v4_701020_seed42.npz",
    "age_column": "age",
    "left_behind_column": "left_behind",
    "narrative_type_column": "task_type",
    "story_theme_column": "story_type",
    # 叙事级连续分（15 任务 sigmoid 均值）；另写入 pred_MT_mean 与回归 pred_SC_Sum 命名习惯一致
    "score_column": "score",
    "pred_score_column": "pred_MT_mean",
    "true_score_column": "MT_Sum",
    "output_dir": arp.OUTPUT_ANALYZE_MULTITASK_METADATA,
    "run_countplots": True,
    # 专家 MT_Sum vs 模型 Σp̂（与宏观回归 real-vs-pred 散点同角色）
    "run_expert_vs_pred_scatter": True,
    "expected_sum_column": "pred_MT_sum_expected",
    # 元数据箱线/年龄/交互图：预测侧用 pred_MT_sum_expected（Σp̂，0–15）与 MT_Sum 同量纲；统一 ylim 便于并排比较
    "metadata_shared_y_lim": (0.0, 15.0),  # None 则纵轴随数据自动缩放
    # 15 头逐任务准确率矩阵（与叙事级推理同一次 forward）
    "run_task_accuracy_matrix": True,
    "per_task_prob_threshold": 0.5,
    "task_acc_ceiling": 0.90,
    "task_acc_floor": 0.40,
    # 审稿补充：年龄 / 任务类型 / 交叉 下的多任务指标（见 subgroup_multitask_metrics_*.csv）
    "run_subgroup_performance_metrics": True,
    "run_manifest_script": "analyze_micro_metadata",
}


def _select_eval_df(df: pd.DataFrame) -> pd.DataFrame:
    es = CONFIG["eval_split"]
    if es == "all":
        out = df
    elif es == "micro_test":
        _, te_idx = rfe.load_or_create_macro_split(
            df, CONFIG.get("split_cache") or None, micro.SEED
        )
        out = df.iloc[te_idx]
    elif isinstance(es, float) and 0 < es < 1:
        _, out = train_test_split(df, test_size=es, random_state=micro.SEED)
    else:
        raise ValueError("CONFIG['eval_split'] 须为 'all' | 'micro_test' | (0,1) 的 float")
    return out.reset_index(drop=True)


def _build_pairs(df: pd.DataFrame):
    qs, cs, row_pos = [], [], []
    for ri, row in df.iterrows():
        story = row["story_type"]
        if story not in micro.QUESTION_TEMPLATES:
            continue
        ist = row.get("ist_words", "")
        if pd.isna(ist):
            ist = ""
        elif not isinstance(ist, str):
            ist = str(ist)
        text = row["text"]
        for task in micro.TASK_NAMES:
            qs.append(micro.QUESTION_TEMPLATES[story][task])
            use_ist = bool(ist) and task in micro.IST_TASKS
            cs.append(micro.format_micro_context_segment(text, ist, use_ist))
            row_pos.append(ri)
    return qs, cs, np.asarray(row_pos, dtype=np.int64)


def _run_multitask_inference(
    df: pd.DataFrame, model, tokenizer, device
) -> tuple[np.ndarray | None, np.ndarray | None]:
    qs, cs, rpos = _build_pairs(df)
    if not qs:
        return None, None
    probs = _predict_probs(
        model, tokenizer, device, qs, cs, CONFIG["batch_size"]
    )
    return probs, rpos


def _predict_probs(model, tokenizer, device, qs, cs, batch_size: int) -> np.ndarray:
    out = []
    n = len(qs)
    for start in tqdm(range(0, n, batch_size), desc="多任务预测"):
        qb = qs[start : start + batch_size]
        cb = cs[start : start + batch_size]
        enc = tokenizer(
            qb,
            cb,
            padding=True,
            truncation="only_second",
            max_length=micro.MAX_LENGTH,
            return_tensors="pt",
        )
        tti = enc.get("token_type_ids")
        if tti is None:
            tti = torch.zeros_like(enc["input_ids"])
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)
        tti = tti.to(device)
        with torch.no_grad():
            logits = model(input_ids, attention_mask, tti)
        out.extend(torch.sigmoid(logits).squeeze(-1).float().cpu().numpy().tolist())
    return np.asarray(out, dtype=np.float64)


def _fill_mean_task_score(df: pd.DataFrame, probs: np.ndarray, rpos: np.ndarray) -> pd.DataFrame:
    df = df.copy()
    n = len(df)
    df[CONFIG["score_column"]] = np.nan
    icol = df.columns.get_loc(CONFIG["score_column"])
    for ri in range(n):
        mask = rpos == ri
        if np.any(mask):
            df.iloc[ri, icol] = float(np.mean(probs[mask]))
    return df


def _attach_mean_task_score(df: pd.DataFrame, model, tokenizer, device) -> pd.DataFrame:
    probs, rpos = _run_multitask_inference(df, model, tokenizer, device)
    if probs is None:
        print("⚠️ 无有效 (q,c) 样本（检查 story_type）")
        out = df.copy()
        out[CONFIG["score_column"]] = np.nan
        return out
    return _fill_mean_task_score(df, probs, rpos)


def _per_task_accuracy(
    df: pd.DataFrame,
    probs: np.ndarray,
    rpos: np.ndarray,
    threshold: float,
) -> pd.DataFrame:
    """逐叙事、按 TASK_NAMES 顺序与 probs 对齐，统计各任务准确率。"""
    n_tasks = len(micro.TASK_NAMES)
    correct = np.zeros(n_tasks, dtype=np.int64)
    total = np.zeros(n_tasks, dtype=np.int64)
    for idx, p in enumerate(probs):
        ri = int(rpos[idx])
        ti = idx % n_tasks
        task = micro.TASK_NAMES[ti]
        if task not in df.columns:
            continue
        y_raw = df.iloc[ri][task]
        yn = pd.to_numeric(y_raw, errors="coerce")
        yt = 1 if (not pd.isna(yn) and int(round(float(yn))) == 1) else 0
        yp = 1 if float(p) >= threshold else 0
        total[ti] += 1
        if yt == yp:
            correct[ti] += 1
    acc = (correct / np.maximum(total, 1)).astype(np.float64)
    rows = []
    ceil_ = float(CONFIG.get("task_acc_ceiling", 0.90))
    floor_ = float(CONFIG.get("task_acc_floor", 0.40))
    for i, t in enumerate(micro.TASK_NAMES):
        a = acc[i] if total[i] > 0 else np.nan
        if total[i] == 0:
            zone = "no_data"
        elif a >= ceil_:
            zone = "ceiling"
        elif a <= floor_:
            zone = "floor"
        else:
            zone = "mid"
        rows.append(
            {
                "task": t,
                "accuracy": a,
                "n": int(total[i]),
                "correct": int(correct[i]),
                "zone": zone,
            }
        )
    return pd.DataFrame(rows)


def _subgroup_multitask_row_metrics(
    df: pd.DataFrame,
    probs: np.ndarray,
    rpos: np.ndarray,
    threshold: float,
    row_idx: pd.Index,
    true_col: str,
    exp_col: str,
) -> dict:
    """同一子组内：15 任务 macro-F1（与主评估 τ 一致）、MT_Sum vs Σp̂ 的 R²、15 头平均准确率、MAE / Pearson r。

    仅计入「15 个 (q,c) 预测齐全」的叙事，与叙事级 macro-F1 定义一致。
    """
    row_set = sorted({int(i) for i in row_idx})
    n_tasks = len(micro.TASK_NAMES)
    task_names = micro.TASK_NAMES
    Yt_list: list[list[int]] = []
    Yp_list: list[np.ndarray] = []
    valid_rows: list[int] = []
    for ri in row_set:
        m = rpos == ri
        if int(m.sum()) != n_tasks:
            continue
        pvec = probs[m]
        if pvec.shape[0] != n_tasks:
            continue
        yt_row: list[int] = []
        bad = False
        for task in task_names:
            if task not in df.columns:
                bad = True
                break
            y_raw = df.iloc[ri][task]
            yn = pd.to_numeric(y_raw, errors="coerce")
            yt = 1 if (not pd.isna(yn) and int(round(float(yn))) == 1) else 0
            yt_row.append(yt)
        if bad:
            continue
        Yt_list.append(yt_row)
        Yp_list.append((pvec >= threshold).astype(np.int64))
        valid_rows.append(ri)
    if not valid_rows:
        return {
            "n_narratives": 0,
            "macro_mean_accuracy_15_tasks": np.nan,
            "macro_F1_15_tasks": np.nan,
            "R2_MT_Sum_vs_sum_p_hat": np.nan,
            "MT_Sum_MAE_vs_pred_sum_expected": np.nan,
            "MT_Sum_Pearson_r_vs_pred_sum_exp": np.nan,
        }
    Yt = np.asarray(Yt_list, dtype=np.int64)
    Yp = np.asarray(Yp_list, dtype=np.int64)
    macro_acc = float(np.mean((Yt == Yp).mean(axis=0)))
    macro_f1 = float(f1_score(Yt, Yp, average="macro", zero_division=0))
    part = df.loc[valid_rows, [true_col, exp_col]].dropna()
    mae = (
        float(np.mean(np.abs(part[true_col] - part[exp_col]))) if len(part) else np.nan
    )
    pr = np.nan
    if len(part) >= 3:
        try:
            pr, _ = pearsonr(part[true_col], part[exp_col])
        except Exception:
            pass
    r2_mt = np.nan
    if len(part) >= 2:
        try:
            r2_mt = float(r2_score(part[true_col], part[exp_col]))
        except Exception:
            pass
    return {
        "n_narratives": len(valid_rows),
        "macro_mean_accuracy_15_tasks": macro_acc,
        "macro_F1_15_tasks": macro_f1,
        "R2_MT_Sum_vs_sum_p_hat": r2_mt,
        "MT_Sum_MAE_vs_pred_sum_expected": mae,
        "MT_Sum_Pearson_r_vs_pred_sum_exp": pr,
    }


def write_subgroup_multitask_performance(
    df: pd.DataFrame,
    probs: np.ndarray,
    rpos: np.ndarray,
    threshold: float,
    meta: dict,
    out_dir: str,
    tag: str,
) -> None:
    """审稿补充：按 age / task_type / story_theme / 交叉 分层报告 macro-F1 与 MT_Sum–Σp̂ R² 等。"""
    true_col = CONFIG["true_score_column"]
    exp_col = CONFIG.get("expected_sum_column", "pred_MT_sum_expected")
    age_col = meta["age_column"]
    tt_col = meta["narrative_type_column"]
    st_col = meta.get("story_theme_column")
    need = [true_col, exp_col, age_col, tt_col]
    if st_col and st_col in df.columns:
        need.append(st_col)
    for c in (true_col, exp_col, age_col, tt_col):
        if c not in df.columns:
            print(f"[subgroup multitask] 缺少列 {c}，跳过")
            return
    rows: list[dict] = []
    sub = df[need].dropna(subset=[true_col, exp_col])
    for k, g in sub.groupby(age_col, dropna=False):
        mm = _subgroup_multitask_row_metrics(
            df, probs, rpos, threshold, g.index, true_col, exp_col
        )
        rows.append({"stratum": "age", "level": str(k), **mm})
    for k, g in sub.groupby(tt_col, dropna=False):
        mm = _subgroup_multitask_row_metrics(
            df, probs, rpos, threshold, g.index, true_col, exp_col
        )
        rows.append({"stratum": "task_type", "level": str(k), **mm})
    if st_col and st_col in sub.columns:
        for k, g in sub.groupby(st_col, dropna=False):
            mm = _subgroup_multitask_row_metrics(
                df, probs, rpos, threshold, g.index, true_col, exp_col
            )
            rows.append({"stratum": "story_theme", "level": str(k), **mm})
    for k, g in sub.groupby([age_col, tt_col], dropna=False):
        mm = _subgroup_multitask_row_metrics(
            df, probs, rpos, threshold, g.index, true_col, exp_col
        )
        lvl = " | ".join(str(x) for x in k) if isinstance(k, tuple) else str(k)
        rows.append({"stratum": "age_x_task_type", "level": lvl, **mm})
    out_df = pd.DataFrame(rows)
    path = os.path.join(out_dir, f"subgroup_multitask_metrics_{tag}.csv")
    out_df.to_csv(path, index=False, encoding="utf-8-sig")
    print("\n--- Subgroup multitask performance — held-out ---")
    print(out_df.to_string(index=False))
    print(f"✅ {path}")


def plot_microstructure_task_matrix(per_task_df: pd.DataFrame, out_dir: str) -> None:
    """
    3×5 矩阵热力图：展示 A2–A16 在评估子集上的分类准确率异质性；
    配色强调高准确率（结构透明/天花板）与低准确率（深层加工/地板）。
    """
    if not CONFIG.get("run_task_accuracy_matrix", True):
        return
    tag = _eval_split_tag()
    acc_map = dict(zip(per_task_df["task"], per_task_df["accuracy"]))
    n_tasks = len(micro.TASK_NAMES)
    acc_arr = np.array([acc_map.get(t, np.nan) for t in micro.TASK_NAMES], dtype=np.float64).reshape(
        3, 5
    )
    annot = np.empty((3, 5), dtype=object)
    for i in range(3):
        for j in range(5):
            t = micro.TASK_NAMES[i * 5 + j]
            a = acc_arr[i, j]
            if np.isnan(a):
                annot[i, j] = f"{t}\n—"
            else:
                annot[i, j] = f"{t}\n{a * 100:.1f}%"

    ceil_ = float(CONFIG.get("task_acc_ceiling", 0.90))
    floor_ = float(CONFIG.get("task_acc_floor", 0.40))
    fig, ax = plt.subplots(figsize=(11, 6.2))
    cmap = LinearSegmentedColormap.from_list(
        "acc_rgy",
        ["#c0392b", "#f39c12", "#f1c40f", "#27ae60"],
        N=256,
    )
    sns.heatmap(
        acc_arr,
        annot=annot,
        fmt="",
        cmap=cmap,
        vmin=0.0,
        vmax=1.0,
        linewidths=1.2,
        linecolor="white",
        cbar_kws={"label": f"Accuracy (τ={CONFIG.get('per_task_prob_threshold', 0.5):g})"},
        ax=ax,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("")
    ax.set_ylabel("")
    n_narr = int(per_task_df["n"].max()) if len(per_task_df) and per_task_df["n"].max() > 0 else 0
    ax.set_title(
        "Multitask microstructure: per-element accuracy (A2–A16)\n"
        f"Held-out subset n={n_narr} narratives · green≈ceiling (≥{ceil_ * 100:.0f}%) · red≈floor (≤{floor_ * 100:.0f}%)",
        fontsize=12,
    )
    legend_elems = [
        Patch(facecolor="#27ae60", edgecolor="gray", label=f"Ceiling ≥{ceil_ * 100:.0f}%"),
        Patch(facecolor="#f1c40f", edgecolor="gray", label="Mid"),
        Patch(facecolor="#c0392b", edgecolor="gray", label=f"Floor ≤{floor_ * 100:.0f}%"),
    ]
    fig.legend(
        handles=legend_elems,
        loc="lower center",
        ncol=3,
        bbox_to_anchor=(0.5, -0.02),
        fontsize=9,
        frameon=False,
    )
    plt.tight_layout(rect=(0, 0.06, 1, 1))
    path = os.path.join(out_dir, f"microstructure_task_accuracy_matrix_{tag}.png")
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"✅ 15 要素准确率矩阵: {path}")

    csv_path = os.path.join(out_dir, f"per_task_accuracy_{tag}.csv")
    per_task_df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"✅ 逐任务准确率表: {csv_path}")
    print("\n--- Per-task accuracy (A2–A16) ---")
    print(per_task_df.to_string(index=False))


def check_column(df, column_name):
    if column_name not in df.columns:
        print(f"⚠️ 缺少列 '{column_name}'，跳过相关分析。")
        return False
    return True


def save_plot(figure, output_dir, filename):
    path = os.path.join(output_dir, filename)
    figure.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(figure)
    print(f"✅ 图表: {path}")


def _mt_sum_labels(df: pd.DataFrame) -> pd.Series:
    cols = [c for c in micro.TASK_NAMES if c in df.columns]
    if not cols:
        return pd.Series(np.nan, index=df.index)
    return df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).sum(axis=1)


def _eval_split_tag() -> str:
    es = CONFIG["eval_split"]
    if es == "micro_test":
        return "test"
    if es == "all":
        return "all"
    if isinstance(es, float):
        return f"holdout_{es:.2f}".replace(".", "p")
    return str(es)


def plot_expert_vs_model_expected_sum(
    df: pd.DataFrame,
    true_col: str,
    expected_col: str,
    out_dir: str,
) -> None:
    """
    专家标注：15 个微观结构二值标签之和 MT_Sum ∈ [0,15]。
    模型侧：同一 15 头上 sigmoid 之和 Σp̂（expected_col，由 pred_MT_mean×15 写入），与 MT_Sum 同量纲。
    （若论文中 n 与脚本差 1，多为某行 story 不在模板中未计入叙事级分数；图中 n 为散点有效对数。）
    """
    if not CONFIG.get("run_expert_vs_pred_scatter", True):
        return
    if true_col not in df.columns or expected_col not in df.columns:
        return
    sub = df.dropna(subset=[true_col, expected_col])
    if len(sub) < 3:
        print("⚠️ 有效样本不足，跳过专家–模型散点图。")
        return
    y_true = sub[true_col].to_numpy(dtype=np.float64)
    y_pred = sub[expected_col].to_numpy(dtype=np.float64)
    tag = _eval_split_tag()
    path = os.path.join(out_dir, f"scatter_MT_Sum_expert_vs_pred_expected_{tag}.png")
    dfp = pd.DataFrame({"expert_MT_Sum": y_true, "model_sum_p_hat": y_pred})
    plt.figure(figsize=(7, 7))
    sns.regplot(
        data=dfp,
        x="expert_MT_Sum",
        y="model_sum_p_hat",
        scatter_kws={"alpha": 0.35, "s": 22},
    )
    y_lim = CONFIG.get("metadata_shared_y_lim")
    if y_lim is not None:
        plt.xlim(y_lim)
        plt.ylim(y_lim)
        lo, hi = float(y_lim[0]), float(y_lim[1])
    else:
        lo = min(float(y_true.min()), float(y_pred.min()))
        hi = max(float(y_true.max()), float(y_pred.max()))
    plt.plot([lo, hi], [lo, hi], "k:", lw=1, label="y = x")
    r2 = r2_score(y_true, y_pred)
    r, _ = pearsonr(y_true, y_pred)
    plt.title(
        f"Expert MT_Sum vs model Σp̂ (held-out subset, n={len(sub)})\n"
        f"R²={r2:.4f}, Pearson r={r:.4f}"
    )
    plt.xlabel("Expert MT_Sum (sum of 15 binary cues, 0–15)")
    plt.ylabel("Model Σp̂ (sum of 15 sigmoid probabilities, 0–15)")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"✅ 专家–模型微观结构对应散点: {path}")


def _countplot_by_category(df, category_col, output_dir, plot_title, filename_prefix):
    if not check_column(df, category_col):
        return
    vc = df[category_col].value_counts()
    if vc.empty:
        return
    order = vc.index.tolist()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x=category_col, order=order, ax=ax)
    ax.set_title(f"各{plot_title}样本量", fontsize=16)
    save_plot(fig, output_dir, f"{filename_prefix}_countplot.png")


def run_metadata_plots_aligned(results_df: pd.DataFrame, out_dir: str, meta: dict) -> None:
    """与 regression核心同一套绘图；预测侧用 Σp̂ 列与 MT_Sum 同 0–15 纵轴。"""
    sfx_real = "_true"
    sfx_pred = "_pred"
    exp_col = CONFIG.get("expected_sum_column", "pred_MT_sum_expected")
    y_lim = CONFIG.get("metadata_shared_y_lim")
    for score_col, sfx in [
        (CONFIG["true_score_column"], sfx_real),
        (exp_col, sfx_pred),
    ]:
        if score_col not in results_df.columns:
            continue
        for key, title in [
            (meta["story_theme_column"], "Story theme"),
            (meta["narrative_type_column"], "Narrative type"),
            (meta["left_behind_column"], "Left-behind"),
        ]:
            _analyze_by_category(
                results_df, key, score_col, out_dir, title, sfx, y_lim=y_lim
            )
        _analyze_age_scatter(
            results_df, meta["age_column"], score_col, out_dir, sfx, y_lim=y_lim
        )
        _analyze_interaction(
            results_df,
            meta["narrative_type_column"],
            meta["age_column"],
            score_col,
            out_dir,
            sfx,
            y_lim=y_lim,
        )


def main():
    ckpt = CONFIG["micro_weights"]
    if not ckpt or not os.path.isfile(ckpt):
        print(f"❌ 未找到权重: {ckpt}")
        return

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    msh.set_seed(micro.SEED)
    device = msh.pick_device()

    df = pd.read_csv(CONFIG["data_path"])
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    df["ist_words"] = df.get("ist_words", pd.Series(dtype=str)).fillna("")
    if "story_type" not in df.columns:
        print("❌ 缺少 story_type")
        return
    msh.coerce_task_label_columns(df, micro.TASK_NAMES)

    eval_df = _select_eval_df(df)
    print(f"分析子集 eval_split={CONFIG['eval_split']!r}, n={len(eval_df)}")

    tokenizer = AutoTokenizer.from_pretrained(CONFIG["model_name"])
    base = AutoModel.from_pretrained(CONFIG["model_name"])
    model = msh.ClueAugmentedQAModel(base, use_peft=True)
    model.load_state_dict(msh.load_state_dict_checkpoint(ckpt, map_location=device), strict=False)
    model.to(device)
    model.eval()

    probs, rpos = _run_multitask_inference(eval_df, model, tokenizer, device)
    if probs is None:
        print("⚠️ 无有效 (q,c) 样本（检查 story_type），终止。")
        return
    results_df = _fill_mean_task_score(eval_df, probs, rpos)
    thr = float(CONFIG.get("per_task_prob_threshold", 0.5))
    per_task_df = _per_task_accuracy(results_df, probs, rpos, thr)
    sc = CONFIG["score_column"]
    pred_col = CONFIG["pred_score_column"]
    true_col = CONFIG["true_score_column"]
    n_scored = results_df[sc].notna().sum()
    print(f"✅ 已写入叙事级 {sc}（15 任务概率均值）: {n_scored}/{len(results_df)} 条")

    results_df[true_col] = _mt_sum_labels(results_df)
    results_df[pred_col] = results_df[sc]
    exp_col = CONFIG.get("expected_sum_column", "pred_MT_sum_expected")
    results_df[exp_col] = pd.to_numeric(results_df[pred_col], errors="coerce") * 15.0

    out_dir = CONFIG.get("output_dir") or arp.OUTPUT_ANALYZE_MULTITASK_METADATA
    os.makedirs(out_dir, exist_ok=True)

    meta = {
        "age_column": CONFIG["age_column"],
        "left_behind_column": CONFIG["left_behind_column"],
        "story_theme_column": CONFIG["story_theme_column"],
        "narrative_type_column": CONFIG["narrative_type_column"],
    }
    run_metadata_plots_aligned(results_df, out_dir, meta)

    if CONFIG.get("run_subgroup_performance_metrics", True):
        write_subgroup_multitask_performance(
            results_df, probs, rpos, thr, meta, out_dir, _eval_split_tag()
        )

    plot_expert_vs_model_expected_sum(results_df, true_col, exp_col, out_dir)

    if CONFIG.get("run_task_accuracy_matrix", True):
        plot_microstructure_task_matrix(per_task_df, out_dir)

    if CONFIG.get("run_countplots", True):
        _countplot_by_category(
            results_df, meta["story_theme_column"], out_dir, "叙事主题", "story_theme"
        )
        _countplot_by_category(
            results_df, meta["narrative_type_column"], out_dir, "叙事类型", "narrative_type"
        )
        _countplot_by_category(
            results_df, meta["left_behind_column"], out_dir, "留守", "left_behind"
        )

    csv_path = os.path.join(out_dir, "predictions_with_metadata.csv")
    results_df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"✅ CSV: {csv_path}")

    pd.DataFrame(
        [
            {
                "script": CONFIG["run_manifest_script"],
                "micro_checkpoint": ckpt,
                "eval_split": CONFIG["eval_split"],
                "split_cache": CONFIG.get("split_cache"),
                "true_score_column": true_col,
                "pred_score_column": pred_col,
                "expected_sum_column": exp_col,
                "per_task_prob_threshold": thr,
                "task_acc_ceiling": CONFIG.get("task_acc_ceiling"),
                "task_acc_floor": CONFIG.get("task_acc_floor"),
                "metadata_shared_y_lim": str(CONFIG.get("metadata_shared_y_lim")),
                "output_dir": out_dir,
                "run_subgroup_performance_metrics": CONFIG.get(
                    "run_subgroup_performance_metrics", False
                ),
            }
        ]
    ).to_csv(os.path.join(out_dir, "run_manifest.csv"), index=False)
    print(f"✅ 完成 → {out_dir}")


if __name__ == "__main__":
    main()
