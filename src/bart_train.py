"""
bart_train.py — BART 结构化线索生成（模型 B）：save_pretrained 输出与全自动管线
（bart_infer.BARTCuePredictor / train_macro_xgb）一致。
推理侧若需「六类 IST + 词项 + 叙述内词频」，请用 bart_infer.predict_ist_analyzed（解析 [IS_*] 词 (n) 目标格式）。

默认按 train_micro_shared 的 70/10/20 划分、验证集 **结构化 IST 词项 F1**（与预留集口径一致）选最优、epoch CSV 日志；
输入前缀 INPUT_PREFIX 与 BARTCuePredictor 一致。全量灌模: --train_on_all。

训练结束（非 --train_on_all）时自动：在 held-out test（约 20%，与微观 同 70/10/20，n≈113/564）上
  - 用 Trainer 计算 test_loss，打印并写入 bart_test_metrics.json；
  - 对 test 每条叙述调用 predict_ist_analyzed（内部等价先生成再解析），导出：
      * bart_test_ist_word_counts.csv
        列：narrative_id, ist_category, word, expert_bart_count, predicted_bart_count
      * bart_test_ist_strings.csv
        列：narrative_id, ist_words（CSV 原始专家字段）, predict_ist_words（predict_ist_words() 原始生成串）
  - bart_test_metrics.json 另含 word_level_ist_metrics（词项级 P/R/F1、类别分配准确率）、
    training_epoch_20（第 20 轮 train/eval loss）与 paper_summary_zh（论文用中文句）。
  - 已有 CSV 时可单独运行：--holdout_word_metrics（不重跑模型）。
"""
import csv
import json
import os
import random
import re
import warnings
import pathlib
import argparse
import sys
from datetime import datetime

import numpy as np
import pandas as pd
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq,
    TrainerCallback,
)

from bart_infer import (
    BART_IST_GEN_MAX_LENGTH,
    BART_IST_GEN_NUM_BEAMS,
    cleanup_bart_structured_decode,
    make_structured_ist_compute_metrics,
)

warnings.filterwarnings("ignore")

# Hub 下载超时（校园网/跨境）
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "120")

# ==============================================================================
# --- ( ! ) 全局配置 ( ! ) ---
# ==============================================================================
MODEL_CHECKPOINT = "fnlp/bart-base-chinese"
from paths import MODELS_DIR, narratives_csv_path

DATA_PATH = str(narratives_csv_path())
DEFAULT_MODEL_DIR = str(MODELS_DIR / "bart_narro_v4")
# 与 bart_infer.BARTCuePredictor 默认目录一致，避免训推分布不一致
INPUT_PREFIX = "线索提取："
DEFAULT_SEED = 42


def _align_bart_generation_config(model) -> None:
    """
    与训练/推理一致（beam=6）；修复 uer 等底座 generation_config 中
    early_stopping=True 但 num_beams=1 导致 save_pretrained 校验失败。
    """
    gc = model.generation_config
    gc.max_length = BART_IST_GEN_MAX_LENGTH
    gc.num_beams = BART_IST_GEN_NUM_BEAMS
    gc.early_stopping = BART_IST_GEN_NUM_BEAMS > 1
    for attr in ("num_beam_groups",):
        if hasattr(gc, attr) and getattr(gc, attr, 1) > gc.num_beams:
            setattr(gc, attr, gc.num_beams)


# ==============================================================================
# --- ( ! ) 您的“标准答案” ( ! ) ---
# ==============================================================================
EXPERT_KEYWORD_DB = {
    # IS_Per: 感知状态词
    'IS_Per': ['看到', '看见', '听见', '听到', '闻到', '尝到', '看'],
    # IS_Phy: 生理状态词
    'IS_Phy': ['饿', '渴', '累', '困', '痛', '发抖','酸',],
    # IS_Con: 意识词
    'IS_Con': ['活着', '醒着', '睡着', '死了', '清醒', '昏迷'],
    # IS_Emo: 情感词
    'IS_Emo': ['高兴', '开心', '快乐', '兴奋', '得意', '笑', '有趣', 
               '难过', '伤心', '哭', '害怕', '紧张', '担心', '着急', 
               '生气', '惊讶', '奇怪', '无聊', '满意', '吓', '痛苦','失望',],
    # IS_Men: 心理动词
    'IS_Men': ['想', '想要','觉得', '感觉','认为', '惊奇', '忘记', '知道', '愿意', '决定','计划',],
    # IS_Ling: 语言动词/表达动词
    'IS_Ling': ['说', '告诉', '问', '回答', '喊', '叫', '警告', ],
}

def build_lookup_map(keyword_db):
    lookup_map = {}
    for category, keywords in keyword_db.items():
        for keyword in keywords:
            if keyword in lookup_map:
                print(f"警告: 关键词 '{keyword}' 在 {lookup_map[keyword]} 和 {category} 中重复！")
            lookup_map[keyword] = category
    return lookup_map

WORD_TO_CATEGORY_MAP = build_lookup_map(EXPERT_KEYWORD_DB)

# ==============================================================================
# --- ( ! ) 核心函数 ( ! ) ---
# ==============================================================================

def create_structured_target(ist_words_string):
    """
    将原始 ist_words 字符串（如 "看到（4） 想（1）"）
    转换为带标签的训练目标（如 "[IS_Per] 看到 (4) [IS_Men] 想 (1)"）。
    """
    if not isinstance(ist_words_string, str):
        return ""

    clean_str = ist_words_string.replace(" ", "")
    matches = re.findall(r"([\u4e00-\u9fa5]+)[（(](\d+)[）)]", clean_str)
    
    classified = {
        'IS_Per': [], 'IS_Phy': [], 'IS_Con': [],
        'IS_Emo': [], 'IS_Men': [], 'IS_Ling': []
    }
    unclassified = []

    for word, count in matches:
        category = WORD_TO_CATEGORY_MAP.get(word)
        result_entry = f"{word} ({count})" 
        
        if category:
            classified[category].append(result_entry)
        else:
            unclassified.append(result_entry)
            
    final_target_parts = []
    for category, items in classified.items():
        if items:
            final_target_parts.append(f"[{category}] {' '.join(items)}")
            
    if unclassified:
        final_target_parts.append(f"[Unclassified] {' '.join(unclassified)}")

    return " ".join(final_target_parts)


def expert_ist_entries(ist_words_string: str) -> list[dict]:
    """
    解析专家 ist_words（与 create_structured_target 同一词表分类）。
    返回 [{"ist_category": "IS_Per"|..., "word": str, "count": int}, ...]
    支持全角/半角括号中的次数。
    """
    if not isinstance(ist_words_string, str) or not str(ist_words_string).strip():
        return []
    clean_str = str(ist_words_string).replace(" ", "")
    matches = re.findall(r"([\u4e00-\u9fa5]+)[（(](\d+)[）)]", clean_str)
    rows: list[dict] = []
    for word, count_s in matches:
        cat = WORD_TO_CATEGORY_MAP.get(word)
        if not cat:
            cat = "Unclassified"
        rows.append({"ist_category": cat, "word": word, "count": int(count_s)})
    return rows


def _paper_overrides_from_trainer_eval(m: dict | None) -> dict[str, float] | None:
    """Trainer.evaluate(test) 返回 dict 中的 test_structured_* → 论文句用 P/R/F1/类别准确率。"""
    if not m:
        return None
    keys = (
        "test_structured_precision",
        "test_structured_recall",
        "test_structured_f1",
        "test_structured_cat_acc",
    )
    if not all(k in m and m[k] is not None for k in keys):
        return None
    return {
        "precision": float(m["test_structured_precision"]),
        "recall": float(m["test_structured_recall"]),
        "f1": float(m["test_structured_f1"]),
        "category_assignment_accuracy_pct": float(m["test_structured_cat_acc"]),
    }


def _json_safe(obj):
    """trainer.evaluate 返回值可能含 numpy 标量，写入 JSON 前转换。"""
    if isinstance(obj, float) and (obj != obj or obj in (float("inf"), float("-inf"))):
        return None
    if isinstance(obj, dict):
        return {str(k): _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_json_safe(v) for v in obj]
    if isinstance(obj, (np.floating, np.integer)):
        return float(obj) if isinstance(obj, np.floating) else int(obj)
    return obj


def export_bart_holdout_test_artifacts(
    test_df: pd.DataFrame,
    model_dir: pathlib.Path,
    test_metrics: dict | None,
    seed: int,
    *,
    preserve_metrics_blob: dict | None = None,
    trainer_eval_for_paper: dict | None = None,
) -> None:
    """
    test_df 须含列：narrative_id, input_text, ist_words。
    写出 JSON + 两个 CSV 到 model_dir。
    """
    model_dir = pathlib.Path(model_dir).resolve()
    model_dir.mkdir(parents=True, exist_ok=True)

    raw_block = {}
    if preserve_metrics_blob and isinstance(
        preserve_metrics_blob.get("test_metrics_raw"), dict
    ):
        raw_block = preserve_metrics_blob["test_metrics_raw"]
    elif test_metrics:
        raw_block = _json_safe(test_metrics)

    summary = {
        "test_loss": float(test_metrics["test_loss"])
        if test_metrics and "test_loss" in test_metrics
        else (
            float(preserve_metrics_blob["test_loss"])
            if preserve_metrics_blob
            and preserve_metrics_blob.get("test_loss") is not None
            else None
        ),
        "test_metrics_raw": raw_block,
        "n_test": int(len(test_df)),
        "seed": int(seed),
        "model_dir": str(model_dir),
        "artifacts": {
            "word_level_csv": "bart_test_ist_word_counts.csv",
            "narrative_level_csv": "bart_test_ist_strings.csv",
            "metrics_json": "bart_test_metrics.json",
        },
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }

    # 延迟导入，避免仅 --predict 时拉 transformers 训练栈
    from bart_infer import (
        BARTCuePredictor,
        compute_bart_holdout_ist_word_metrics,
        format_bart_holdout_paper_summary_zh,
        read_bart_training_log_epoch_row,
        structured_string_to_count_map,
    )

    predictor = BARTCuePredictor(str(model_dir))

    count_rows: list[dict] = []
    string_rows: list[dict] = []

    for _, row in test_df.iterrows():
        nid = str(row["narrative_id"])
        text = str(row["input_text"])
        expert_raw = row["ist_words"] if isinstance(row["ist_words"], str) else ""
        expert_list = expert_ist_entries(expert_raw)
        analyzed = predictor.predict_ist_analyzed(text)

        e_map: dict[tuple[str, str], int] = {}
        for e in expert_list:
            k = (e["ist_category"], e["word"])
            e_map[k] = e_map.get(k, 0) + int(e["count"])

        # 与 Trainer.compute_metrics / make_structured_ist_compute_metrics 一致：只统计
        # 能从 raw 结构化串解析出的 (类别,词)+bart_count，不用 Jieba 回填的叙述词频。
        p_map = structured_string_to_count_map(analyzed.get("raw_output", ""))

        keys = set(e_map) | set(p_map)
        for cat, w in sorted(keys):
            count_rows.append(
                {
                    "narrative_id": nid,
                    "ist_category": cat,
                    "word": w,
                    "expert_bart_count": int(e_map.get((cat, w), 0)),
                    "predicted_bart_count": int(p_map.get((cat, w), 0)),
                }
            )

        # raw_output 与 BARTCuePredictor.predict_ist_words(text) 返回值一致（同一次 generate）
        string_rows.append(
            {
                "narrative_id": nid,
                "ist_words": expert_raw,
                "predict_ist_words": analyzed.get("raw_output", ""),
            }
        )

    pd.DataFrame(count_rows).to_csv(
        model_dir / "bart_test_ist_word_counts.csv",
        index=False,
        encoding="utf-8-sig",
    )
    pd.DataFrame(string_rows).to_csv(
        model_dir / "bart_test_ist_strings.csv",
        index=False,
        encoding="utf-8-sig",
    )

    wc_csv = model_dir / "bart_test_ist_word_counts.csv"
    wm = compute_bart_holdout_ist_word_metrics(wc_csv)
    log_p = pathlib.Path(str(model_dir) + "_training_log.csv")
    ep20 = read_bart_training_log_epoch_row(log_p, 20)
    tl = summary.get("test_loss")
    tl_f = float(tl) if tl is not None else None
    summary["word_level_ist_metrics"] = wm
    summary["word_level_ist_metrics_note"] = (
        "词项=(ist_category, word)，按叙事内 min(专家次数,预测次数) 累计 TP；"
        "预测侧次数仅来自 BART 原始串 parse（与验证集 structured_f1 口径一致），"
        "不含 Jieba 叙述词频回填；类别分配准确率=TP/W_TP。"
    )
    paper_po = _paper_overrides_from_trainer_eval(trainer_eval_for_paper)
    if paper_po is None and isinstance(raw_block, dict):
        paper_po = _paper_overrides_from_trainer_eval(raw_block)
    summary["paper_word_metrics_source"] = (
        "trainer_evaluate_test" if paper_po is not None else "export_csv_parse"
    )
    if paper_po is not None:
        summary["word_level_ist_metrics_trainer_test"] = paper_po.copy()
    summary["training_epoch_20"] = ep20
    summary["paper_summary_zh"] = format_bart_holdout_paper_summary_zh(
        wm, tl_f, ep20, paper_overrides=paper_po
    )
    with open(model_dir / "bart_test_metrics.json", "w", encoding="utf-8") as f:
        json.dump(_json_safe(summary), f, ensure_ascii=False, indent=2)

    tl = summary.get("test_loss")
    tl_s = f"{tl:.6f}" if tl is not None else "n/a"
    print(
        f"[BART] held-out test 导出完成（test_loss={tl_s}）→ {model_dir}\n"
        f"      · bart_test_metrics.json\n"
        f"      · bart_test_ist_word_counts.csv（{len(count_rows)} 行词项级）\n"
        f"      · bart_test_ist_strings.csv（{len(string_rows)} 条：ist_words vs predict_ist_words）\n"
        f"      · 论文用摘要（paper_summary_zh）已写入 JSON。\n"
        f"---\n{summary['paper_summary_zh']}"
    )


def run_holdout_word_metrics_only(model_dir: pathlib.Path) -> None:
    """不加载 BART：仅由已有 CSV + 训练日志 +（可选）JSON 中的 test_loss 更新论文指标。"""
    model_dir = pathlib.Path(model_dir).resolve()
    wc = model_dir / "bart_test_ist_word_counts.csv"
    if not wc.is_file():
        print(f"错误: 缺少 {wc}。请先 --train 或 --export_test_only。")
        sys.exit(1)
    from bart_infer import (
        compute_bart_holdout_ist_word_metrics,
        format_bart_holdout_paper_summary_zh,
        read_bart_training_log_epoch_row,
    )

    wm = compute_bart_holdout_ist_word_metrics(wc)
    log_p = pathlib.Path(str(model_dir) + "_training_log.csv")
    ep20 = read_bart_training_log_epoch_row(log_p, 20)
    metrics_path = model_dir / "bart_test_metrics.json"
    blob: dict = {}
    if metrics_path.is_file():
        with open(metrics_path, encoding="utf-8") as f:
            blob = json.load(f)
    tl = blob.get("test_loss")
    tl_f = float(tl) if tl is not None else None
    blob["word_level_ist_metrics"] = wm
    blob["word_level_ist_metrics_note"] = (
        "词项=(ist_category, word)，按叙事内 min(专家次数,预测次数) 累计 TP；"
        "预测侧次数仅来自 BART 原始串 parse（与验证集 structured_f1 口径一致），"
        "不含 Jieba 叙述词频回填；类别分配准确率=TP/W_TP。"
    )
    raw_block = blob.get("test_metrics_raw")
    paper_po = _paper_overrides_from_trainer_eval(
        raw_block if isinstance(raw_block, dict) else None
    )
    blob["paper_word_metrics_source"] = (
        "trainer_evaluate_test" if paper_po is not None else "export_csv_parse"
    )
    if paper_po is not None:
        blob["word_level_ist_metrics_trainer_test"] = paper_po.copy()
    blob["training_epoch_20"] = ep20
    blob["paper_summary_zh"] = format_bart_holdout_paper_summary_zh(
        wm, tl_f, ep20, paper_overrides=paper_po
    )
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(_json_safe(blob), f, ensure_ascii=False, indent=2)
    print(blob["paper_summary_zh"])


def _report_target_token_stats(tokenizer, texts, max_len: int, split_name: str) -> None:
    """训练前诊断：有多少 target 会被 max_target_length 截断。"""
    n_over, worst = 0, 0
    for s in texts:
        s = s or ""
        L = len(tokenizer.encode(s, add_special_tokens=True))
        worst = max(worst, L)
        if L > max_len:
            n_over += 1
    n = len(texts)
    print(
        f"[BART] target token 长度 ({split_name}): max={worst} | len>{max_len}: {n_over}/{n}"
    )


class BartAlignGenerationConfigCallback(TrainerCallback):
    """评估/存盘前恢复 beam 与 early_stopping，避免 Trainer 临时改 generation_config 导致 save 失败。"""

    def on_save(self, args, state, control, **kwargs):
        model = kwargs.get("model")
        if model is not None:
            _align_bart_generation_config(model)
        return control

    def on_evaluate(self, args, state, control, **kwargs):
        model = kwargs.get("model")
        if model is not None:
            _align_bart_generation_config(model)
        return control


class BartEpochCsvCallback(TrainerCallback):
    """按 epoch 将 train/eval loss 追加到 CSV（与 train_bart_v2 思路一致）。"""

    def __init__(self, csv_path: pathlib.Path):
        self.csv_path = csv_path
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(
                [
                    "epoch",
                    "train_loss",
                    "eval_loss",
                    "eval_structured_f1",
                    "timestamp",
                ]
            )

    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        if not metrics or "eval_loss" not in metrics:
            return
        train_loss = None
        for log in reversed(state.log_history):
            if "loss" in log and "eval_loss" not in log:
                train_loss = log.get("loss")
                break
        ts = datetime.now().strftime("%H:%M:%S")
        sf = metrics.get("eval_structured_f1")
        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(
                [
                    int(max(1, round(state.epoch))),
                    train_loss if train_loss is not None else "",
                    metrics["eval_loss"],
                    sf if sf is not None else "",
                    ts,
                ]
            )


def _prepare_bart_dataframe(
    data_path: str | pathlib.Path, stratify_col: str = "story_type"
) -> pd.DataFrame | None:
    """读 CSV → input_text / target_text / ist_words / narrative_id（+ 分层列若存在）。"""
    print(f"正在加载数据: {data_path}")
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"错误: '{data_path}' 文件未找到。请确保该文件在同一目录下。")
        return None

    first_col = df.columns[0]
    if first_col != "Text":
        df.rename(columns={first_col: "Text"}, inplace=True)
    if "ist_words" not in df.columns:
        print("错误: CSV 缺少列 ist_words。")
        return None

    if "participant_id" in df.columns:
        df["narrative_id"] = df["participant_id"].astype(str)
    else:
        df["narrative_id"] = [f"narrative_{i}" for i in range(len(df))]

    df["ist_words"] = df["ist_words"].fillna("")

    print("开始构建新的“结构化”训练目标...")
    df["target_text"] = df["ist_words"].apply(create_structured_target)

    df.rename(columns={"Text": "input_text"}, inplace=True)

    keep_cols = ["input_text", "target_text", "ist_words", "narrative_id"]
    if stratify_col in df.columns:
        keep_cols.append(stratify_col)
    df = df[keep_cols].copy()
    print(
        f"数据加载完毕。共 {len(df)} 条样本（narrative_id；分层列 {stratify_col!r}: "
        f"{'有' if stratify_col in df.columns else '无'}）。"
    )
    return df


def _split_train_val_test_bart(
    df: pd.DataFrame, seed: int, stratify_col: str
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    from sklearn.model_selection import train_test_split
    from train_micro_shared import split_train_val_test_70_10_20

    if stratify_col not in df.columns:
        print(
            f"警告: 缺少列 '{stratify_col}'，无法分层；退回 sklearn 随机 70/10/20。"
        )
        tr, rest = train_test_split(
            df, test_size=0.30, random_state=seed, shuffle=True
        )
        val_df, test_df = train_test_split(
            rest, test_size=2 / 3, random_state=seed, shuffle=True
        )
        return tr.reset_index(drop=True), val_df.reset_index(drop=True), test_df.reset_index(
            drop=True
        )
    return split_train_val_test_70_10_20(df, seed, stratify_col=stratify_col)


def run_export_test_only(
    data_path: str | pathlib.Path,
    model_dir: pathlib.Path,
    seed: int,
    stratify_col: str,
) -> None:
    """
    已有权重时：按与训练相同的划分得到 test_df，写出词项级 CSV + ist_words vs predict_ist_words；
    test_loss 优先读 model_dir/bart_test_metrics.json（若无则 JSON 中 test_loss 为空，仅导出预测）。
    """
    df = _prepare_bart_dataframe(data_path, stratify_col)
    if df is None:
        raise SystemExit(1)
    _, _, test_df = _split_train_val_test_bart(df, seed, stratify_col)
    print(
        f"[BART] --export_test_only: test n={len(test_df)}（与 --train 默认划分一致）"
    )
    metrics_path = pathlib.Path(model_dir).resolve() / "bart_test_metrics.json"
    test_metrics: dict = {}
    full_blob: dict | None = None
    if metrics_path.is_file():
        with open(metrics_path, encoding="utf-8") as f:
            full_blob = json.load(f)
        if full_blob.get("test_loss") is not None:
            test_metrics["test_loss"] = float(full_blob["test_loss"])
        print(f"[BART] 已读入既有 test_loss: {test_metrics.get('test_loss', 'n/a')}")
    else:
        print(
            "[BART] 未找到 bart_test_metrics.json；导出 CSV 时 JSON 中 test_loss 将为 null。"
        )
    export_bart_holdout_test_artifacts(
        test_df,
        pathlib.Path(model_dir).resolve(),
        test_metrics or None,
        seed,
        preserve_metrics_blob=full_blob,
        trainer_eval_for_paper=(
            full_blob.get("test_metrics_raw") if full_blob else None
        ),
    )


def run_training(
    data_path,
    model_checkpoint,
    output_dir,
    *,
    seed: int = DEFAULT_SEED,
    train_on_all: bool = False,
    num_train_epochs: int = 20,
    stratify_col: str = "story_type",
):
    """
    模型 B（BART-base）训练：默认 70/10/20 划分、验证集上选最优、save_pretrained 与全自动管线一致。
    """
    from train_micro_shared import set_seed

    set_seed(seed)

    print(f"开始加载分词器: {model_checkpoint}")
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    
    new_tokens = ['[IS_Per]', '[IS_Phy]', '[IS_Con]', '[IS_Emo]', '[IS_Men]', '[IS_Ling]', '[Unclassified]']
    tokenizer.add_special_tokens({'additional_special_tokens': new_tokens})
    print(f"已将 {len(new_tokens)} 个新类别标签添加到分词器中。")

    df = _prepare_bart_dataframe(data_path, stratify_col)
    if df is None:
        return None

    max_input_length = 512
    max_target_length = 128

    if train_on_all:
        train_df = df
        val_df = None
        test_df = None
        print("[BART] --train_on_all：在 100% 数据上训练（无验证集早停/选优）。")
    else:
        train_df, val_df, test_df = _split_train_val_test_bart(df, seed, stratify_col)
        print(
            f"[BART] 划分: train={len(train_df)} | val={len(val_df)} | test={len(test_df)} "
            f"(与 M1–微观 脚本相同的 70/10/20 协议)"
        )

    _report_target_token_stats(
        tokenizer, train_df["target_text"].tolist(), max_target_length, "train"
    )
    if val_df is not None:
        _report_target_token_stats(
            tokenizer, val_df["target_text"].tolist(), max_target_length, "val"
        )

    def preprocess_function(examples):
        prefixed = [INPUT_PREFIX + str(x) for x in examples["input_text"]]
        model_inputs = tokenizer(
            prefixed,
            max_length=max_input_length,
            truncation=True,
            padding="max_length",
        )
        with tokenizer.as_target_tokenizer():
            labels = tokenizer(
                examples["target_text"],
                max_length=max_target_length,
                truncation=True,
                padding="max_length",
            )
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    print("开始对数据集进行分词和预处理...")
    train_ds = Dataset.from_pandas(train_df[["input_text", "target_text"]])
    tokenized_train_dataset = train_ds.map(
        preprocess_function, batched=True, num_proc=4
    )
    tokenized_eval_dataset = None
    tokenized_test_dataset = None
    if val_df is not None:
        tokenized_eval_dataset = Dataset.from_pandas(
            val_df[["input_text", "target_text"]]
        ).map(preprocess_function, batched=True, num_proc=4)
        tokenized_test_dataset = Dataset.from_pandas(
            test_df[["input_text", "target_text"]]
        ).map(preprocess_function, batched=True, num_proc=4)
    print("预处理完成。")


    print(f"开始加载预训练模型: {model_checkpoint}")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    model.resize_token_embeddings(len(tokenizer))
    _align_bart_generation_config(model)

    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    print(f"训练设备: {device}")

    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    use_eval = tokenized_eval_dataset is not None
    log_csv = pathlib.Path(str(output_dir) + "_training_log.csv")
    callbacks: list[TrainerCallback] = [BartAlignGenerationConfigCallback()]
    if use_eval:
        callbacks.append(BartEpochCsvCallback(log_csv))

    compute_metrics_fn = None
    if use_eval:
        compute_metrics_fn = make_structured_ist_compute_metrics(tokenizer)

    arg_kw = dict(
        output_dir=f"{output_dir}_output",
        seed=seed,
        num_train_epochs=num_train_epochs,
        learning_rate=3e-5,
        warmup_ratio=0.1,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        weight_decay=0.01,
        max_grad_norm=1.0,
        predict_with_generate=True,
        logging_steps=50,
        fp16=torch.cuda.is_available(),
        generation_max_length=BART_IST_GEN_MAX_LENGTH,
        generation_num_beams=BART_IST_GEN_NUM_BEAMS,
    )
    try:
        import inspect

        sig = inspect.signature(Seq2SeqTrainingArguments.__init__)
        if "use_mps_device" in sig.parameters:
            arg_kw["use_mps_device"] = device == "mps"
    except (TypeError, ValueError):
        pass
    if use_eval:
        arg_kw.update(
            {
                "eval_strategy": "epoch",
                "save_strategy": "epoch",
                "load_best_model_at_end": True,
                "metric_for_best_model": "eval_structured_f1",
                "greater_is_better": True,
                "save_total_limit": 3,
            }
        )
    else:
        arg_kw.update(
            {
                "eval_strategy": "no",
                "save_strategy": "steps",
                "load_best_model_at_end": False,
                "save_total_limit": 2,
            }
        )

    training_args = Seq2SeqTrainingArguments(**arg_kw)

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_eval_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
        callbacks=callbacks,
        compute_metrics=compute_metrics_fn,
    )

    if use_eval:
        print(
            f"\n--- 开始训练 {training_args.num_train_epochs} epoch；"
            f"验证集按结构化 IST 词项 F1（与预留集口径一致）选最优 checkpoint；"
            f"beam={BART_IST_GEN_NUM_BEAMS} max_len={BART_IST_GEN_MAX_LENGTH}；"
            f"日志 CSV: {log_csv.resolve()} ---"
        )
    else:
        print(f"\n--- 开始训练 {training_args.num_train_epochs} epoch（全量数据，无验证） ---")

    trainer.train()
    print("--- 训练完成 ---")

    test_metrics: dict = {}
    if use_eval and tokenized_test_dataset is not None:
        test_metrics = trainer.evaluate(
            tokenized_test_dataset, metric_key_prefix="test"
        )
        if isinstance(test_metrics, dict) and "test_loss" in test_metrics:
            tl = float(test_metrics["test_loss"])
            print(f"[BART] held-out test loss (自动生成): {tl:.6f}")
        else:
            print(f"[BART] test evaluate: {test_metrics}")

    _align_bart_generation_config(trainer.model)
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    final_path = pathlib.Path(output_dir).resolve()
    print(f"\n最终的 '模型B' 已保存到: {final_path}")

    if use_eval and test_df is not None and len(test_df) > 0:
        export_bart_holdout_test_artifacts(
            test_df,
            final_path,
            test_metrics if test_metrics else None,
            seed,
            trainer_eval_for_paper=test_metrics,
        )

    return final_path


class BARTStructuredPredictor:
    """
    命令行/本地试跑用：加载 save_pretrained 目录，与 BARTCuePredictor 同权重格式。
    """
    def __init__(self, model_path):
        self.model_path = str(model_path) 
        print(f"\n--- 加载 '模型B' 从: {self.model_path} ---")
        
        try:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path, local_files_only=True)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, local_files_only=True)
        except OSError:
            print(f"错误: 找不到已训练的模型 '{self.model_path}'。")
            print("请先使用 --train 标志运行脚本来训练和保存模型。")
            sys.exit(1) 

        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
            
        self.model.to(self.device)
        self.model.eval()
        
        self.max_target_length = BART_IST_GEN_MAX_LENGTH
        print(f"模型已成功加载到: {self.device}")
        
    def _cleanup_output(self, raw_text):
        """与 BARTCuePredictor.predict_ist_words 共用同一后处理。"""
        return cleanup_bart_structured_decode(raw_text, self.tokenizer)


    def predict(self, text_input):
        """
        对单个文本输入进行预测
        """
        print(f"\n--- 正在预测新文本 ---")
        print(f"输入: {text_input[:100].replace(chr(10), ' ')}...")

        src = text_input
        if not str(src).startswith(INPUT_PREFIX):
            src = INPUT_PREFIX + str(src)

        inputs = self.tokenizer(
            src,
            return_tensors="pt",
            max_length=512,
            truncation=True,
        ).to(self.device)
        
        with torch.no_grad():
            output_sequences = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=BART_IST_GEN_MAX_LENGTH,
                num_beams=BART_IST_GEN_NUM_BEAMS,
                early_stopping=True,
            )
        
        raw_prediction = self.tokenizer.decode(
            output_sequences[0], 
            skip_special_tokens=False 
        )
        
        predicted_structured_text = self._cleanup_output(raw_prediction)
        
        print("\n--- '模型B' 智能预测结果 ---")
        print(f"预测的结构化线索: {predicted_structured_text}")
        return predicted_structured_text


# ==============================================================================
# --- ( ! ) 主程序入口 ( ! ) ---
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="训练或运行 '模型B' (智能分类版)")
    
    parser.add_argument(
        "--train",
        action="store_true", 
        help="启用训练模式，开始训练模型。"
    )
    
    parser.add_argument(
        "--predict",
        type=str, 
        metavar="TEXT_TO_PREDICT",
        help="启用预测模式，并对提供的文本进行预测。"
    )
    
    parser.add_argument(
        "--model_dir",
        type=pathlib.Path, 
        default=DEFAULT_MODEL_DIR,
        help=f"模型保存或加载的文件夹路径 (默认: {DEFAULT_MODEL_DIR})"
    )
    parser.add_argument(
        "--config",
        type=pathlib.Path,
        default=None,
        help="BART 训练 JSON（如 configs/bart_narro_v4.json）；与 --train 联用覆盖编码器与输出目录",
    )

    parser.add_argument(
        "--data_path",
        type=pathlib.Path,
        default=DATA_PATH,
        help=f"训练数据 .csv 文件的路径 (默认: {DATA_PATH})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"随机种子，与 M 系列脚本一致时建议 {DEFAULT_SEED}",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=30,
        help="训练轮数（默认 30；配合验证集 structured F1 选优）",
    )
    parser.add_argument(
        "--train_on_all",
        action="store_true",
        help="不使用 70/10/20 划分，在全量数据上训练（无验证选优；适合最终部署灌模）",
    )
    parser.add_argument(
        "--stratify_col",
        type=str,
        default="story_type",
        help="分层划分列名（默认 story_type；缺失时退回随机划分）",
    )
    parser.add_argument(
        "--export_test_only",
        action="store_true",
        help="不训练：用已有权重对 held-out test 批量 predict_ist_analyzed 并写 CSV；"
        "test_loss 沿用 model_dir/bart_test_metrics.json（若存在）。",
    )
    parser.add_argument(
        "--holdout_word_metrics",
        action="store_true",
        help="不训练：据 bart_test_ist_word_counts.csv 与 *_training_log.csv 计算词项级 P/R/F1 等，"
        "并写入/更新 bart_test_metrics.json（paper_summary_zh）。",
    )

    args = parser.parse_args()

    if args.train and args.export_test_only:
        print("错误: --train 与 --export_test_only 不能同时使用。")
        sys.exit(1)
    if args.train and args.holdout_word_metrics:
        print("错误: --train 与 --holdout_word_metrics 不能同时使用。")
        sys.exit(1)
    if args.export_test_only and args.holdout_word_metrics:
        print("错误: --export_test_only 与 --holdout_word_metrics 不能同时使用。")
        sys.exit(1)

    def _has_bart_weights(d: pathlib.Path) -> bool:
        d = d.resolve()
        if not (d / "config.json").is_file():
            return False
        return (d / "model.safetensors").is_file() or (d / "pytorch_model.bin").is_file()

    if args.holdout_word_metrics:
        run_holdout_word_metrics_only(args.model_dir)
        print("[!] --holdout_word_metrics 完成。")
        return

    # --- 仅导出 test 预测（需已有权重）---
    if args.export_test_only:
        if not _has_bart_weights(args.model_dir):
            print(
                f"错误: '{args.model_dir}' 缺少 config.json + model.safetensors（或 pytorch_model.bin）。"
                "请先 --train，或检查 --model_dir。"
            )
            sys.exit(1)
        run_export_test_only(
            args.data_path, args.model_dir, args.seed, args.stratify_col
        )
        print("[!] --export_test_only 完成。")
        return

    # --- 训练模式 ---
    if args.train:
        print(f"[!] 启动训练模式...")
        model_checkpoint = MODEL_CHECKPOINT
        model_dir = args.model_dir
        data_path = args.data_path
        seed = args.seed
        epochs = args.epochs
        train_on_all = args.train_on_all
        stratify_col = args.stratify_col
        bart_cfg = None

        if args.config is not None:
            from bart_training_config import BartTrainingConfig

            bart_cfg = BartTrainingConfig.from_json(args.config)
            model_checkpoint = bart_cfg.resolve_hub_path()
            model_dir = bart_cfg.model_dir
            data_path = bart_cfg.data_path
            seed = bart_cfg.seed
            epochs = bart_cfg.epochs
            train_on_all = bart_cfg.train_on_all
            stratify_col = bart_cfg.stratify_col
            print(f"[BART] 实验配置: {bart_cfg.id} — {bart_cfg.label}")
            print(f"  编码器: {bart_cfg.model_name} → {model_checkpoint}")
            print(f"  输出: {model_dir}")

        final = run_training(
            data_path=str(data_path),
            model_checkpoint=model_checkpoint,
            output_dir=str(model_dir),
            seed=seed,
            train_on_all=train_on_all,
            num_train_epochs=epochs,
            stratify_col=stratify_col,
        )
        if bart_cfg is not None and final is not None:
            metrics_path = pathlib.Path(final) / "bart_test_metrics.json"
            if metrics_path.is_file():
                blob = json.loads(metrics_path.read_text(encoding="utf-8"))
                bart_cfg.write_results(blob)
                print(f"[BART] 指标已写入 {bart_cfg.config_path}")
        print("[!] 训练完成。")
        
    # --- 预测模式 ---
    if args.predict:
        print(f"[!] 启动预测模式...")
        
        if not args.model_dir.exists():
            print(f"错误: 找不到模型目录 '{args.model_dir}'。")
            print("请先使用 --train 标志运行脚本来训练和保存模型。")
            sys.exit(1)
            
        predictor = BARTStructuredPredictor(args.model_dir)
        predictor.predict(args.predict)
        
    # --- 无操作 ---
    if not args.train and not args.predict:
        print("未指定操作。")
        print(
            "请使用 --train 训练，--predict '文本' 试跑，--export_test_only 仅导出 test CSV，"
            "或 --holdout_word_metrics 由已有 CSV 更新论文指标。"
        )
        parser.print_help()


if __name__ == "__main__":
    main()