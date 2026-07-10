#!/usr/bin/env python3
"""
学术论文统计：任务1（5折CV 的 SD）与任务2（held-out 测试集上的 Bootstrap 95% CI）。

审稿补充（Pearson 相关功效 + r 的 Fisher 95% CI）：见 research_paper_correlation_power.py。

任务1 —— 仓库内未发现训练日志中的逐折 macro F1。请将从实验记录中抄录的折分数写入
  configs/ablation_cv_fold_f1.json（见 configs/ablation_cv_fold_f1.example.json），然后运行：
  python research_paper_statistics_bootstrap.py --task cv_sd

任务2 —— 默认 ``--eval-split row_10pct``：逐行 90%/10% 测试集（与 train_micro 一致,
  seed=42）；``--eval-split row_20pct`` 为 80%/20%（n_test≈113）。Bootstrap 在 held-out 叙事上有放回抽样。

  （1）Micro：微观问法与 **train_micro.QUESTION_TEMPLATES** 一致；阈值可用
      ``--thr-telling`` / ``--thr-retelling`` 或 calibration JSON。
  （2）Macro：若 ``--xgb-dir`` 含 ``auto_xgb_model_*.joblib``，则用 **微观问法** 抽 BERT（与
      ``train_macro_xgb`` 训练一致）+ BART 在线线索 + ``analyze_automated_features`` 的 10 维特征；
      否则用 champion ``xgb_model_*.joblib`` + CSV 中专家语言学列（维数须与模型一致）。

用法：
  python research_paper_statistics_bootstrap.py --task bootstrap
  python research_paper_statistics_bootstrap.py --task bootstrap --eval-split row_10pct --thr-telling 0.5 --thr-retelling 0.51
  python research_paper_statistics_bootstrap.py --task bootstrap --eval-split row_20pct
  python research_paper_statistics_bootstrap.py --task cv_sd
  python research_paper_statistics_bootstrap.py --task all
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from peft import LoraConfig, get_peft_model
from sklearn.metrics import f1_score, r2_score
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, SequentialSampler, TensorDataset
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer

from calibration_microstructure_thresholds import build_per_row_threshold_matrix, resolve_thresholds
from train_micro import QUESTION_TEMPLATES as QUESTION_TEMPLATES_M4

# ---------------------------------------------------------------------------
# 默认路径（与 model_registry narro_v4 / analyze_micro_errors.py 对齐）
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
DEFAULT_DATA = ROOT.parent / "data" / "narratives.csv"
# 若 narratives.csv 无 A2–A16，可改用带专家标签的导出（与全量语料行序一致时，划分与主实验一致）
FALLBACK_LABELED = (
    ROOT
    / "analysis_results_best_model_20251001-111255_epoch10_macrof1_0.7067"
    / "predictions_with_metadata.csv"
)
DEFAULT_MICRO_WEIGHTS = ROOT / "models" / "micro_narro_v4.pth"
DEFAULT_XGB_DIR = ROOT / "models" / "macro_xgb_narro_v4"
FALLBACK_XGB_DIR = DEFAULT_XGB_DIR
DEFAULT_CV_JSON = ROOT / "configs" / "ablation_cv_fold_f1.json"
DEFAULT_PREDICTIONS_OUT = ROOT / "outputs" / "micro_bootstrap_testset_n113_predictions.csv"

# 与 regression_*_xgb_m4 一致：BERT 表征用于 XGB 时用 微观问法
QUESTION_TEMPLATES_REGRESSION = {
    "cat": {
        "A2": "第一个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。",
        "A3": "在追蝴蝶的事件中，小猫想要达成的目标或打算做的事情是什么？",
        "A4": "为了抓蝴蝶，小猫采取了什么行动？",
        "A5": "小猫抓蝴蝶的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A6": "在抓蝴蝶失败后，猫和蝴蝶各自的情绪反应是什么？",
        "A7": "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。",
        "A8": "在拿球的事件中，男孩想要达成的目标或打算做的事情是什么？",
        "A9": "为了拿回球，男孩采取了什么行动？",
        "A10": "男孩拿球的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A11": "在拿回球后，男孩的情绪反应是什么？",
        "A12": "第三个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。",
        "A13": "在关于鱼的事件中，小猫想要达成的目标或打算做的事情是什么？",
        "A14": "为了得到鱼，小猫采取了什么行动？",
        "A15": "小猫拿鱼的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A16": "在得到鱼后，小猫的情绪反应是什么？",
    },
    "dog": {
        "A2": "第一个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。",
        "A3": "在追老鼠的事件中，小狗想要达成的目标或打算做的事情是什么？",
        "A4": "为了抓老鼠，小狗采取了什么行动？",
        "A5": "小狗抓老鼠的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A6": "在抓老鼠失败后，小狗和老鼠各自的情绪反应是什么？",
        "A7": "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。",
        "A8": "在关于气球的事件中，男孩想要达成的目标或打算做的事情是什么？",
        "A9": "为了拿回气球，男孩采取了什么行动？",
        "A10": "男孩拿气球的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A11": "在拿回球后，男孩的情绪反应是什么？",
        "A12": "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。",
        "A13": "在关于香肠的事件中，小狗想要达成的目标或打算做的事情是什么？",
        "A14": "为了得到香肠，小狗采取了什么行动？",
        "A15": "小狗拿香肠的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A16": "在得到香肠后，小狗的情绪反应是什么？",
    },
    "bird": {
        "A2": "第一个事件的起因是什么？这包括鸟妈妈或小鸟的感受、想法或所看到的情境。",
        "A3": "在喂食的事件中，鸟妈妈想要达成的目标或打算做的事情是什么？",
        "A4": "为了喂小鸟，鸟妈妈采取了什么行动？",
        "A5": "鸟妈妈找食物的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A6": "在喂食成功后，鸟妈妈和小鸟各自的情绪反应是什么？",
        "A7": "第二个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。",
        "A8": "在抓小鸟的事件中，小猫想要达成的目标或打算做的事情是什么？",
        "A9": "为了抓小鸟，小猫采取了什么行动？",
        "A10": "小猫抓小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A11": "在小猫抓到小鸟后，小猫和小鸟各自的情绪反应是什么？",
        "A12": "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。",
        "A13": "在救小鸟的事件中，小狗想要达成的目标或打算做的事情是什么？",
        "A14": "为了救小鸟，小狗采取了什么行动？",
        "A15": "小鸟救小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A16": "在小鸟获救后，小狗、小猫、小鸟和鸟妈妈各自的情绪反应是什么？",
    },
    "goat": {
        "A2": "第一个事件的起因是什么？这包括小羊或羊妈妈的感受、想法或所看到的情境。",
        "A3": "在救小羊的事件中，羊妈妈想要达成的目标或打算做的事情是什么？",
        "A4": "为了救小羊，羊妈妈采取了什么行动？",
        "A5": "羊妈妈救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A6": "在小羊获救后，羊妈妈和小羊各自的情绪反应是什么？",
        "A7": "第二个事件的起因是什么？这包括狐狸的感受、想法或他所看到的情境。",
        "A8": "在抓小羊的事件中，狐狸想要达成的目标或打算做的事情是什么？",
        "A9": "为了抓小羊，狐狸采取了什么行动？",
        "A10": "狐狸抓小羊的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A11": "在狐狸抓到小羊后，狐狸和小羊各自的情绪反应是什么？",
        "A12": "第三个事件的起因是什么？这包括小鸟的感受、想法或他所看到的情境。",
        "A13": "在救小鳥的事件中，小鸟想要达成的目标或打算做的事情是什么？",
        "A14": "为了救小羊，小鸟采取了什么行动？",
        "A15": "小鸟救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。",
        "A16": "在小羊被小鸟救下后，小鸟、狐狸、小羊和羊妈妈各自的情绪反应是什么？",
    },
}

AUTOMATED_LINGUISTIC_COLUMNS = [
    "auto_TNU", "auto_MLU", "auto_TNW", "auto_TDW",
    "auto_IS_Per_count", "auto_IS_Phy_count", "auto_IS_Con_count",
    "auto_IS_Emo_count", "auto_IS_Men_count", "auto_IS_Ling_count",
]

LINGUISTIC_FEATURE_COLUMNS = [
    "IS_Per", "IS_Phy", "IS_Con", "IS_Emo", "IS_Men", "IS_Ling", "IS_Token",
    "IS_Type", "TNW", "TDW", "TNU", "MLU", "顺承关系", "因果关系",
    "转折关系", "时间关系", "假设关系", "并列/递进关系", "conj_token", "conj_type",
    "关系从句", "宾语从句", "主语从句", "连动结构", "兼语结构",
    "描述性从句", "把字句", "被字句", "介词短语", "复杂状态句", "状语从句",
    "Sentences_token", "Sentence_type", "PPVT", "MINT", "Forward", "Backward",
]


class ClueAugmentedQAModel(nn.Module):
    def __init__(self, bert_model, use_peft=True):
        super().__init__()
        if use_peft:
            lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=["query", "key", "value"])
            self.bert = get_peft_model(bert_model, lora_config)
        else:
            self.bert = bert_model
        self.inner_layer = nn.Linear(bert_model.config.hidden_size, 768)
        self.dropout = nn.Dropout(0.5)
        self.classifier = nn.Linear(768, 1)

    def forward(self, input_ids, attention_mask):
        bert_output = self.bert(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:, 0, :]
        x = self.dropout(bert_output)
        x = F.relu(self.inner_layer(x))
        x = self.dropout(x)
        return self.classifier(x)


def _cls_embeddings(model: ClueAugmentedQAModel, input_ids, attention_mask):
    """与 micro_encoder 一致：LoRA BERT [CLS]，不用分类头。"""
    out = model.bert(input_ids=input_ids, attention_mask=attention_mask)
    return out.last_hidden_state[:, 0, :]


def extract_global_features(df: pd.DataFrame, model, tokenizer, device):
    model.to(device)
    model.eval()
    task_names = [f"A{i}" for i in range(2, 17)]
    final_embeddings = []
    for _, row in tqdm(df.iterrows(), total=len(df), desc="BERT global (test)", leave=False):
        prompts = []
        original_text, story_type = row["text"], row["story_type"]
        ist_words = row.get("ist_words", "")
        if pd.isna(ist_words):
            ist_words = ""
        for task_name in task_names:
            question = QUESTION_TEMPLATES_REGRESSION[story_type][task_name]
            prompts.append(f"问题：{question} 叙事：{original_text} 已知线索：{ist_words}")
        inputs = tokenizer(prompts, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
        with torch.no_grad():
            prompt_embeddings = _cls_embeddings(model, inputs["input_ids"], inputs["attention_mask"])
        mean_embedding = torch.mean(prompt_embeddings, dim=0, keepdim=True)
        final_embeddings.append(mean_embedding.cpu().numpy())
    return np.concatenate(final_embeddings, axis=0)


def extract_hierarchical_features(df: pd.DataFrame, model, tokenizer, device):
    model.to(device)
    model.eval()
    task_e1 = [f"A{i}" for i in range(2, 7)]
    task_e2 = [f"A{i}" for i in range(7, 12)]
    task_e3 = [f"A{i}" for i in range(12, 17)]
    final_embeddings = []

    def mean_emb(prompts_list):
        if not prompts_list:
            return torch.zeros((1, model.bert.config.hidden_size), device=device)
        inputs = tokenizer(prompts_list, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
        with torch.no_grad():
            pe = _cls_embeddings(model, inputs["input_ids"], inputs["attention_mask"])
        return torch.mean(pe, dim=0, keepdim=True)

    for _, row in tqdm(df.iterrows(), total=len(df), desc="BERT hierarchical (test)", leave=False):
        original_text, story_type = row["text"], row["story_type"]
        ist_words = row.get("ist_words", "")
        if pd.isna(ist_words):
            ist_words = ""

        def build(tsks):
            return [
                f"问题：{QUESTION_TEMPLATES_REGRESSION[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}"
                for t in tsks
            ]

        emb_e1 = mean_emb(build(task_e1))
        emb_e2 = mean_emb(build(task_e2))
        emb_e3 = mean_emb(build(task_e3))
        emb_g = torch.mean(torch.stack([emb_e1, emb_e2, emb_e3]), dim=0)
        final_embeddings.append(torch.cat([emb_e1, emb_e2, emb_e3, emb_g], dim=1).cpu().numpy())
    return np.concatenate(final_embeddings, axis=0)


def build_automated_ling_matrix(test_df: pd.DataFrame, bart_predictor) -> np.ndarray:
    """与 train_macro_xgb 一致：BART 线索 + analyze_automated_features → (n,10)。"""
    from features_automated import analyze_automated_features

    rows = []
    for _, row in tqdm(test_df.iterrows(), total=len(test_df), desc="Auto A+B 语言学特征", leave=False):
        text = str(row["text"])
        ist = bart_predictor.predict_ist_words(text)
        vec, _ = analyze_automated_features(text, ist)
        rows.append(vec)
    return np.asarray(rows, dtype=np.float64)


def predict_multitask_probs_m4(
    test_df: pd.DataFrame,
    model: ClueAugmentedQAModel,
    tokenizer,
    device,
    batch_size: int = 16,
) -> np.ndarray:
    """返回 shape (n_test, 15) 的 sigmoid 概率（问法与 train_micro 一致）。"""
    task_names = [f"A{i}" for i in range(2, 17)]
    texts = []
    for _, row in test_df.iterrows():
        for task_name in task_names:
            q = QUESTION_TEMPLATES_M4[row["story_type"]][task_name]
            ist_words = row.get("ist_words", "")
            if pd.isna(ist_words):
                ist_words = ""
            texts.append(f"问题：{q} 叙事：{row['text']} 已知线索：{ist_words}")
    enc = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
    ds = TensorDataset(enc["input_ids"], enc["attention_mask"])
    loader = DataLoader(ds, sampler=SequentialSampler(ds), batch_size=batch_size)
    model.eval()
    probs = []
    with torch.no_grad():
        for batch in tqdm(loader, desc="微观 multitask forward", leave=False):
            input_ids, attention_mask = [b.to(device) for b in batch]
            logits = model(input_ids, attention_mask)
            probs.append(torch.sigmoid(logits).cpu().numpy())
    flat = np.concatenate(probs, axis=0).flatten()
    return flat.reshape(len(test_df), 15)


def bootstrap_ci_multilabel_macro_f1(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    n_bootstrap: int = 1000,
    seed: int = 42,
):
    """对叙事样本有放回重抽样，每次在 (n,15) 上计算 sklearn macro F1。"""
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, n)
        scores.append(f1_score(y_true[idx], y_pred[idx], average="macro", zero_division=0))
    scores = np.array(scores)
    return float(np.mean(scores)), float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))


def bootstrap_ci_r2(y_true: np.ndarray, y_pred: np.ndarray, n_bootstrap: int = 1000, seed: int = 42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, n)
        scores.append(r2_score(y_true[idx], y_pred[idx]))
    scores = np.array(scores)
    return float(np.mean(scores)), float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))


def task_cv_sd(json_path: Path):
    if not json_path.is_file():
        print(
            f"[任务1] 未找到 {json_path}。\n"
            "请复制 configs/ablation_cv_fold_f1.example.json 为 configs/ablation_cv_fold_f1.json，"
            "填入各模型 5 折的 macro F1 后重新运行：\n"
            "  python research_paper_statistics_bootstrap.py --task cv_sd"
        )
        print(
            "\n[任务1 说明] 当前仓库内无训练日志中的逐折 F1；"
            "train_multitask_ablation_*.py 与 train_micro.py 默认是单次划分而非 5 折，"
            "因此无法从现有 .pth 反推 5 折 SD。"
        )
        return

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    table_means_ref = {"M1": 0.56, "M2": 0.69, "M3": 0.75, "微观": 0.79}
    print("=== 任务1：5 折 macro F1 的均值 / SD（来自 JSON）===\n")
    for key in ["M1", "M2", "M3", "微观"]:
        block = data.get(key) or {}
        folds = block.get("fold_f1")
        if not folds or any(x is None for x in folds) or len(folds) != 5:
            print(f"{key}: fold_f1 未完整填写，跳过。")
            continue
        folds = [float(x) for x in folds]
        mean = float(np.mean(folds))
        sd = float(np.std(folds, ddof=1)) if len(folds) > 1 else 0.0
        ref = table_means_ref.get(key)
        delta = "" if ref is None else f"  (Table 1 参考 mean={ref:.2f}, Δ={mean - ref:+.4f})"
        print(f"{key}:")
        print(f"  fold F1s = {folds}")
        print(f"  mean = {mean:.4f}{delta}")
        print(f"  SD   = {sd:.4f}\n")


def task_bootstrap(
    data_path: Path,
    micro_weights: Path,
    xgb_dir: Path,
    model_name: str,
    n_bootstrap: int,
    threshold_mode: str,
    single_threshold: float,
    seed: int,
    output_predictions: Path | None,
    skip_macro_r2: bool,
    calibration_json: Path | None,
    eval_split: str,
    thr_telling_fixed: float | None,
    thr_retelling_fixed: float | None,
    bart_model_dir: Path,
):
    if not data_path.is_file():
        print(f"缺少数据文件: {data_path}")
        sys.exit(1)
    if not micro_weights.is_file():
        print(f"缺少 微观权重: {micro_weights}")
        sys.exit(1)

    df = pd.read_csv(data_path)
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    if "ist_words" not in df.columns:
        df["ist_words"] = ""
    df["ist_words"] = df["ist_words"].fillna("")

    task_cols = [f"A{i}" for i in range(2, 17)]
    missing_tasks = [c for c in task_cols if c not in df.columns]
    if missing_tasks:
        if FALLBACK_LABELED.is_file():
            print(
                f"当前数据缺少微观标签列（如 {missing_tasks[:2]}…），"
                f"改用: {FALLBACK_LABELED}"
            )
            df = pd.read_csv(FALLBACK_LABELED)
            df.rename(columns={df.columns[0]: "text"}, inplace=True)
            if "ist_words" not in df.columns:
                df["ist_words"] = ""
            df["ist_words"] = df["ist_words"].fillna("")
        else:
            print(
                "数据缺少 A2–A16，且未找到 fallback predictions_with_metadata.csv；"
                "请提供含专家微观标签的 CSV（--data）。"
            )
            sys.exit(1)
    for c in task_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

    indices = df.index.values
    if eval_split == "row_10pct":
        _, test_indices = train_test_split(indices, test_size=0.1, random_state=42)
        print(f"[任务2] 测试集划分：逐行 90%/10%（与 train_micro.py 一致, seed=42）")
    elif eval_split == "row_20pct":
        _, test_indices = train_test_split(indices, test_size=0.2, random_state=42)
        print(f"[任务2] 测试集划分：逐行 80%/20%（test_size=0.2, random_state=42）")
    else:
        print(f"未知 eval_split: {eval_split}")
        sys.exit(1)
    test_df = df.loc[test_indices].copy()
    n = len(test_df)
    print(f"  held-out 叙事 n={n}")

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    print(f"设备: {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    bert_base = AutoModel.from_pretrained(model_name)
    feat_model = ClueAugmentedQAModel(bert_base, use_peft=True)
    state = torch.load(micro_weights, map_location=device)
    feat_model.load_state_dict(state, strict=False)
    feat_model.to(device)
    feat_model.eval()

    y_true_micro = test_df[task_cols].values.astype(int)

    print("微观 多任务前向（测试集）…")
    probs = predict_multitask_probs_m4(test_df, feat_model, tokenizer, device)
    if threshold_mode == "task_specific":
        if thr_telling_fixed is not None and thr_retelling_fixed is not None:
            thr_t, thr_r = float(thr_telling_fixed), float(thr_retelling_fixed)
            thr_src = "cli_fixed"
        elif thr_telling_fixed is not None or thr_retelling_fixed is not None:
            print("请同时提供 --thr-telling 与 --thr-retelling，或二者都不提供以使用 calibration JSON / 默认。")
            sys.exit(1)
        else:
            thr_t, thr_r, thr_src = resolve_thresholds(micro_weights, calibration_json)
        thr_mat = build_per_row_threshold_matrix(test_df, thr_t, thr_r)
        print(f"二值化：任务特定阈值 ({thr_src}) Telling={thr_t:.4f}, Retelling={thr_r:.4f}")
    else:
        thr_mat = np.full_like(probs, fill_value=single_threshold, dtype=np.float64)
        print(f"二值化：单一阈值 = {single_threshold}")

    y_pred_micro = (probs >= thr_mat).astype(int)

    point_f1 = f1_score(y_true_micro, y_pred_micro, average="macro", zero_division=0)
    print(f"\n[点估计] Micro macro-F1（与上线阈值规则一致）= {point_f1:.4f}")

    mean_f1, lo_f1, hi_f1 = bootstrap_ci_multilabel_macro_f1(
        y_true_micro, y_pred_micro, n_bootstrap=n_bootstrap, seed=seed
    )
    print(
        f"Micro F1: mean={mean_f1:.4f}, 95% CI=[{lo_f1:.4f}, {hi_f1:.4f}]  "
        f"(n_bootstrap={n_bootstrap}, bootstrap_seed={seed})"
    )

    if output_predictions:
        out = pd.DataFrame(
            {
                "original_df_index": test_df.index.to_numpy(),
                "task_type": test_df["task_type"].values if "task_type" in test_df.columns else np.repeat("", n),
                "story_type": test_df["story_type"].values,
                "applied_threshold": thr_mat[:, 0],
            }
        )
        for j, c in enumerate(task_cols):
            out[f"{c}_true"] = y_true_micro[:, j]
            out[f"{c}_pred"] = y_pred_micro[:, j]
            out[f"{c}_prob"] = probs[:, j]
        output_predictions.parent.mkdir(parents=True, exist_ok=True)
        out.to_csv(output_predictions, index=False, encoding="utf-8-sig")
        print(f"\n[已保存] 测试集 n={n} 预测明细: {output_predictions}")

    if skip_macro_r2:
        print("\n[跳过] Macro R²（--skip_macro_r2），未提取 XGB 用 BERT 特征")
    else:
        print("\n提取测试集 BERT 特征（供 XGBoost；问法为正式模板 QUESTION_TEMPLATES_REGRESSION）…")
        bert_g = extract_global_features(test_df, feat_model, tokenizer, device)
        bert_h = extract_hierarchical_features(test_df, feat_model, tokenizer, device)

        auto_e1 = xgb_dir / "auto_xgb_model_SC_E1.joblib"
        if auto_e1.is_file():
            try:
                from bart_infer import BARTCuePredictor
            except ImportError as e:
                print(f"Macro 需要 BART：{e}")
                sys.exit(1)
            if not bart_model_dir.is_dir():
                print(f"缺少 BART 目录: {bart_model_dir}")
                sys.exit(1)
            print("  [Macro] 使用 auto_xgb + BART 在线线索 + 自动 A/B 语言学特征 (train_macro_xgb)")
            bart = BARTCuePredictor(model_dir=str(bart_model_dir.resolve()))
            ling = build_automated_ling_matrix(test_df, bart)
            if ling.shape[1] != len(AUTOMATED_LINGUISTIC_COLUMNS):
                print(f"自动特征维数异常: {ling.shape[1]}，期望 {len(AUTOMATED_LINGUISTIC_COLUMNS)}")
                sys.exit(1)
            e1_path = xgb_dir / "auto_xgb_model_SC_E1.joblib"
            e2_path = xgb_dir / "auto_xgb_model_SC_E2.joblib"
            e3_path = xgb_dir / "auto_xgb_model_SC_E3.joblib"
        else:
            ling_cols = [c for c in LINGUISTIC_FEATURE_COLUMNS if c in test_df.columns]
            for c in ling_cols:
                test_df[c] = pd.to_numeric(test_df[c], errors="coerce").fillna(0)
            ling = test_df[ling_cols].values.astype(np.float64)
            print(f"  [Macro] 使用 champion xgb + CSV 中专家语言学列（共 {len(ling_cols)} 列）")
            e1_path = xgb_dir / "xgb_model_SC_E1.joblib"
            e2_path = xgb_dir / "xgb_model_SC_E2.joblib"
            e3_path = xgb_dir / "xgb_model_SC_E3.joblib"

        X_g = np.concatenate([bert_g, ling], axis=1)
        X_h = np.concatenate([bert_h, ling], axis=1)

        for p in (e1_path, e2_path, e3_path):
            if not p.is_file():
                print(f"缺少 XGBoost 模型: {p}")
                sys.exit(1)

        m1 = joblib.load(e1_path)
        m2 = joblib.load(e2_path)
        m3 = joblib.load(e3_path)
        for tag, m, X in [("E1", m1, X_g), ("E2", m2, X_h), ("E3", m3, X_g)]:
            nf = getattr(m, "n_features_in_", None)
            if nf is not None and X.shape[1] != nf:
                print(
                    f"特征维数不匹配 {tag}: X 有 {X.shape[1]} 列，模型期望 {nf}。"
                    " 全自动模型请使用含 auto_xgb_model_*.joblib 的目录并确保 BART 可用；"
                    " champion 模型需要与训练时相同的专家语言学列。"
                )
                sys.exit(1)

        pred_e1 = m1.predict(X_g)
        pred_e2 = m2.predict(X_h)
        pred_e3 = m3.predict(X_g)
        y_pred_sum = pred_e1 + pred_e2 + pred_e3
        y_true_sum = pd.to_numeric(test_df["SC_Sum"], errors="coerce").fillna(0).values

        point_r2 = r2_score(y_true_sum, y_pred_sum)
        print(f"\n[点估计] Macro R² (SC_Sum) = {point_r2:.4f}")

        mean_r2, lo_r2, hi_r2 = bootstrap_ci_r2(
            y_true_sum, y_pred_sum, n_bootstrap=n_bootstrap, seed=seed + 1
        )
        print(f"Macro R²: mean={mean_r2:.4f}, 95% CI=[{lo_r2:.4f}, {hi_r2:.4f}]")

    print(
        "\n[方法学说明] 您提供的展平 + macro F1 会把 1695 个格子当成多类分类的一个向量，"
        "与「15 个二分类任务再取宏平均」不一致；本脚本采用 (n,15) 的 macro-F1 并对 **叙事** 有放回抽样。"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=["cv_sd", "bootstrap", "all"], default="all")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--micro_weights", type=Path, default=DEFAULT_MICRO_WEIGHTS)
    parser.add_argument("--xgb_dir", type=Path, default=DEFAULT_XGB_DIR)
    parser.add_argument("--model_name", default="Morton-Li/QiDeBERTa-base")
    parser.add_argument("--cv_json", type=Path, default=DEFAULT_CV_JSON)
    parser.add_argument("--n_bootstrap", type=int, default=1000)
    parser.add_argument(
        "--threshold-mode",
        choices=["task_specific", "single"],
        default="task_specific",
        help="task_specific：按行 Telling/Retelling 阈值（--thr-* 或 calibration JSON）；single：整表单一阈值",
    )
    parser.add_argument(
        "--single-threshold",
        type=float,
        default=0.5,
        help="仅当 --threshold-mode single 时使用",
    )
    parser.add_argument(
        "--output_predictions",
        type=Path,
        nargs="?",
        const=DEFAULT_PREDICTIONS_OUT,
        default=DEFAULT_PREDICTIONS_OUT,
        help="保存 n=113 的 true/pred/prob；传空路径可关闭（用 --no_output_predictions）",
    )
    parser.add_argument(
        "--no_output_predictions",
        action="store_true",
        help="不写出预测 CSV",
    )
    parser.add_argument(
        "--skip_macro_r2",
        action="store_true",
        help="跳过 XGBoost 与 Macro R²（仅算 Micro F1 + bootstrap，更快）",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--calibration-json",
        type=Path,
        default=None,
        help="多任务阈值 JSON；默认使用与 --micro_weights 同名的 <stem>.calibration.json（若存在）",
    )
    parser.add_argument(
        "--eval-split",
        choices=["row_10pct", "row_20pct"],
        default="row_10pct",
        help="row_10pct：90/10 测试（同 cue_augmented 训练脚本）；row_20pct：80/20（原 n≈113）",
    )
    parser.add_argument(
        "--thr-telling",
        type=float,
        default=None,
        help="与 --thr-retelling 同时给出时固定 Telling 阈值，跳过 JSON/默认",
    )
    parser.add_argument(
        "--thr-retelling",
        type=float,
        default=None,
        help="与 --thr-telling 同时给出时固定 Retelling 阈值",
    )
    parser.add_argument(
        "--bart-model-dir",
        type=Path,
        default=ROOT / "models" / "bart_narro_v4",
        help="Macro 使用 auto_xgb 时 BART 模型目录",
    )
    args = parser.parse_args()

    pred_out = None if args.no_output_predictions else args.output_predictions

    if args.task in ("cv_sd", "all"):
        task_cv_sd(args.cv_json)
    if args.task in ("bootstrap", "all"):
        print()
        task_bootstrap(
            args.data,
            args.micro_weights,
            args.xgb_dir,
            args.model_name,
            args.n_bootstrap,
            args.threshold_mode,
            args.single_threshold,
            args.seed,
            pred_out,
            args.skip_macro_r2,
            args.calibration_json,
            args.eval_split,
            args.thr_telling,
            args.thr_retelling,
            args.bart_model_dir,
        )


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
