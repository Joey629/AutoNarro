# bart_infer.py
# [目标]：加载训练好的 BART (Seq2Seq) 线索模型，与 bart_train 一致：
#   - predict_ist_words：decode(skip_special_tokens=False) + cleanup_bart_structured_decode，
#     保留 [IS_*] 标签并与 BARTStructuredPredictor 输出格式一致
#   - predict_ist_analyzed：面向「儿童叙述 → IST 词项 + 六类之一 + 频次」的自动化接口
#     （解析训练目标格式 `[IS_*] 词 (n) ...`；并在叙述上用 Jieba 重算出现次数）
#
# 词表与 features_automated / 训练侧 EXPERT_KEYWORD_DB 对齐（单一真源）。

from __future__ import annotations

import csv
import os
import re
import sys
import warnings
from collections import defaultdict
from pathlib import Path

import jieba
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

try:
    from features_automated import EXPERT_KEYWORD_DB
except ImportError:
    EXPERT_KEYWORD_DB = {}

warnings.filterwarnings("ignore")

DEFAULT_BART_MODEL_DIR = "./models/bart_narro_v4"
# 须与 bart_train.INPUT_PREFIX 一致
IST_INPUT_PREFIX = "线索提取："
# 训练验证 compute_metrics、Trainer generation、推理端统一，避免训推不一致
BART_IST_GEN_MAX_LENGTH = 128
BART_IST_GEN_NUM_BEAMS = 6


def _matplotlib_or_xgboost_loaded() -> bool:
    return "matplotlib" in sys.modules or "xgboost" in sys.modules


def _pick_bart_device() -> torch.device:
    """选 BART 推理设备。macOS 上若在 matplotlib/xgboost 之后加载权重，MPS 易段错误。"""
    env = os.environ.get("NARRO_BART_FORCE_CPU", "").lower()
    if env in ("1", "true", "yes"):
        return torch.device("cpu")
    if env not in ("0", "false", "no") and os.environ.get(
        "REGRESSION_FORCE_CPU", ""
    ).lower() in ("1", "true", "yes"):
        return torch.device("cpu")
    if env not in ("0", "false", "no") and _matplotlib_or_xgboost_loaded():
        if torch.backends.mps.is_available():
            return torch.device("cpu")
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")

_TAG_SPLIT_RE = re.compile(r"(\[(?:IS_[A-Za-z]+|Unclassified)\])")
_PAIR_RE = re.compile(r"([\u4e00-\u9fa5]+)\s*\((\d+)\)")


def cleanup_bart_structured_decode(raw_text: str, tokenizer) -> str:
    """
    与 bart_train.BARTStructuredPredictor._cleanup_output 一致。
    generate 后须 skip_special_tokens=False，否则会丢掉 [IS_*] 等 additional_special_tokens；
    再手动去掉 pad/eos 等，并规整括号与中文字符间空格。
    """
    special_tokens_to_remove = [
        tokenizer.pad_token,
        tokenizer.sep_token,
        tokenizer.cls_token,
        tokenizer.eos_token,
        tokenizer.bos_token,
    ]
    special_tokens_to_remove = [t for t in special_tokens_to_remove if t is not None]

    cleaned_text = raw_text
    for token in special_tokens_to_remove:
        cleaned_text = cleaned_text.replace(token, "")

    text = re.sub(r"\s+\]", "]", cleaned_text)
    text = re.sub(r"\[\s+", "[", text)
    text = re.sub(r"\(\s*(\d+)\s*[)）]\s*", r"(\1)", text)
    text = re.sub(r"([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])", r"\1\2", text)
    text = re.sub(r"([\u4e00-\u9fa5])\s+\(", r"\1(", text)
    text = re.sub(r"\]([\u4e00-\u9fa5])", r"] \1", text)
    text = re.sub(r"\)\[", r") [", text)
    return text.strip()


def _build_word_to_ist_category() -> dict[str, str]:
    m: dict[str, str] = {}
    for category, keywords in EXPERT_KEYWORD_DB.items():
        for kw in keywords:
            m[kw] = category
    return m


WORD_TO_IST_CATEGORY = _build_word_to_ist_category()


def parse_structured_ist_string(raw: str) -> list[dict]:
    """
    解析与 create_structured_target 对称的 BART 输出，如：
    [IS_Emo] 难过 (2) [IS_Men] 想 (1)
    返回条目列表：category（如 IS_Emo）、word、bart_count（模型目标中的整数，可为 None）。
    """
    if not isinstance(raw, str) or not raw.strip():
        return []
    s = raw.strip()
    parts = _TAG_SPLIT_RE.split(s)
    out: list[dict] = []

    head = parts[0].strip()
    if head:
        for w, c in _PAIR_RE.findall(head):
            out.append({"category": "Unclassified", "word": w, "bart_count": int(c)})

    i = 1
    while i < len(parts):
        tag = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        m = re.match(r"\[((?:IS_[A-Za-z]+)|Unclassified)\]", tag)
        cat = m.group(1) if m else "Unclassified"
        for w, c in _PAIR_RE.findall(body):
            out.append({"category": cat, "word": w, "bart_count": int(c)})
        i += 2

    return out


def _fallback_entries_from_flat_string(raw: str) -> list[dict]:
    """无方括号结构时：对生成串分词，命中关键词表的词视为 IST 项（无 bart 侧频次）。"""
    if not isinstance(raw, str) or not raw.strip():
        return []
    seen: set[tuple[str, str]] = set()
    out: list[dict] = []
    for tok in jieba.lcut(raw.strip()):
        cat = WORD_TO_IST_CATEGORY.get(tok)
        if not cat:
            continue
        key = (cat, tok)
        if key in seen:
            continue
        seen.add(key)
        out.append({"category": cat, "word": tok, "bart_count": None})
    return out


def count_ist_token_in_narrative(narrative: str, token: str) -> int:
    """在儿童叙述中按 Jieba 词界统计 token 出现次数（与词表型 IST 一致）。"""
    if not narrative or not token:
        return 0
    return sum(1 for t in jieba.lcut(narrative) if t == token)


def structured_string_to_count_map(s: str) -> dict[tuple[str, str], int]:
    """结构化目标/预测串 → (category, word) → 次数（与导出 CSV 语义一致）。"""
    m: dict[tuple[str, str], int] = {}
    for it in parse_structured_ist_string(s):
        bc = it.get("bart_count")
        if bc is None:
            continue
        k = (str(it["category"]), str(it["word"]))
        m[k] = m.get(k, 0) + int(bc)
    return m


def ist_metrics_accumulate_from_maps(
    e_map: dict[tuple[str, str], int],
    p_map: dict[tuple[str, str], int],
) -> tuple[int, int, int, int]:
    """单条叙事：返回 tp, fp, fn, word_matched_mass (W_TP)。"""
    tp = fp = fn = 0
    keys = set(e_map) | set(p_map)
    for k in keys:
        e = int(e_map.get(k, 0))
        p = int(p_map.get(k, 0))
        tp += min(e, p)
        fp += max(0, p - e)
        fn += max(0, e - p)
    e_by_w: dict[str, int] = defaultdict(int)
    p_by_w: dict[str, int] = defaultdict(int)
    for (c, w), v in e_map.items():
        e_by_w[w] += v
    for (c, w), v in p_map.items():
        p_by_w[w] += v
    w_tp = 0
    for w in set(e_by_w) | set(p_by_w):
        w_tp += min(e_by_w[w], p_by_w[w])
    return tp, fp, fn, w_tp


def make_structured_ist_compute_metrics(tokenizer):
    """
    Seq2SeqTrainer.compute_metrics：按预留集相同定义计算 structured_f1，
    用于 load_best_model_at_end。金标从 eval_preds 的 labels 解码，保证
    evaluate(val) / evaluate(test) 与当前子集对齐（勿闭包固定 val 列表）。
    """
    import numpy as np

    def compute_metrics(eval_preds):
        preds, labels = eval_preds
        if preds is None or labels is None:
            return {}
        preds = np.asarray(preds)
        labels = np.asarray(labels)
        if preds.ndim == 1:
            preds = preds.reshape(1, -1)
        if labels.ndim == 1:
            labels = labels.reshape(1, -1)
        pad_id = tokenizer.pad_token_id
        tp = fp = fn = w_tp = 0
        n = min(len(preds), len(labels))
        for i in range(n):
            lab = labels[i].flatten()
            lab = lab[lab != -100]
            gold_ids = [int(x) for x in lab if int(x) >= 0]
            gold_raw = tokenizer.decode(
                gold_ids,
                skip_special_tokens=False,
                clean_up_tokenization_spaces=False,
            )
            gold_clean = cleanup_bart_structured_decode(gold_raw, tokenizer)
            e_map = structured_string_to_count_map(gold_clean.strip())

            ids = preds[i].flatten()
            mask = np.ones_like(ids, dtype=bool)
            mask &= ids != -100
            if pad_id is not None:
                mask &= ids != pad_id
            ids = ids[mask]
            id_list = [int(x) for x in ids if int(x) >= 0]
            raw = tokenizer.decode(
                id_list,
                skip_special_tokens=False,
                clean_up_tokenization_spaces=False,
            )
            pred_clean = cleanup_bart_structured_decode(raw, tokenizer)
            p_map = structured_string_to_count_map(pred_clean)
            tpi, fpi, fni, wtpi = ist_metrics_accumulate_from_maps(e_map, p_map)
            tp += tpi
            fp += fpi
            fn += fni
            w_tp += wtpi
        denom_p = tp + fp
        denom_r = tp + fn
        precision = float(tp / denom_p) if denom_p > 0 else 0.0
        recall = float(tp / denom_r) if denom_r > 0 else 0.0
        if precision + recall <= 0:
            f1 = 0.0
        else:
            f1 = float(2 * precision * recall / (precision + recall))
        cat_acc = float(100.0 * tp / w_tp) if w_tp > 0 else 0.0
        return {
            "structured_f1": f1,
            "structured_precision": precision,
            "structured_recall": recall,
            "structured_cat_acc": cat_acc,
        }

    return compute_metrics


def compute_bart_holdout_ist_word_metrics(
    word_counts_csv: str | Path,
) -> dict[str, float | int]:
    """
    由 bart_train 导出的 bart_test_ist_word_counts.csv 计算预留集词项级指标。

    词项键为 (ist_category, word)，带专家/模型侧出现次数。逐条叙事聚合后：
    - TP = Σ min(专家次数, 预测次数)；FP = Σ max(0, 预测−专家)；FN = Σ max(0, 专家−预测)。
    - 精确率 = TP/(TP+FP)，召回率 = TP/(TP+FN)，F1 为调和平均。
    - 词形对齐质量 W_TP = 对每个词形 w，min(专家总次数, 预测总次数) 之和（跨类别）。
    - 类别分配准确率 (%) = 100 × TP / W_TP（词形可被预测覆盖时，(类别,词) 同时正确的比例）。
    """
    path = Path(word_counts_csv)
    by_nid: dict[str, list[dict[str, str]]] = defaultdict(list)
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            by_nid[str(row["narrative_id"])].append(row)

    tp = fp = fn = 0
    w_tp = 0

    for rows in by_nid.values():
        e_map: dict[tuple[str, str], int] = {}
        p_map: dict[tuple[str, str], int] = {}
        for row in rows:
            cat = str(row["ist_category"])
            w = str(row["word"])
            e = int(row["expert_bart_count"])
            p = int(row["predicted_bart_count"])
            key = (cat, w)
            e_map[key] = e
            p_map[key] = p
        tpi, fpi, fni, wtpi = ist_metrics_accumulate_from_maps(e_map, p_map)
        tp += tpi
        fp += fpi
        fn += fni
        w_tp += wtpi

    denom_p = tp + fp
    denom_r = tp + fn
    precision = tp / denom_p if denom_p > 0 else float("nan")
    recall = tp / denom_r if denom_r > 0 else float("nan")
    if precision != precision or recall != recall or (precision + recall) == 0:
        f1 = float("nan")
    else:
        f1 = 2 * precision * recall / (precision + recall)

    cat_acc_pct = (100.0 * tp / w_tp) if w_tp > 0 else float("nan")

    return {
        "tp": int(tp),
        "fp": int(fp),
        "fn": int(fn),
        "word_matched_mass_w_tp": int(w_tp),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "category_assignment_accuracy_pct": float(cat_acc_pct),
    }


def read_bart_training_log_epoch_row(
    training_log_csv: str | Path, epoch: int
) -> dict[str, float | None]:
    """读取 BartEpochCsvCallback 写出的 CSV 中指定 epoch 的 train_loss / eval_loss。"""
    path = Path(training_log_csv)
    if not path.is_file():
        return {"train_loss": None, "eval_loss": None}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                ep = int(round(float(row.get("epoch", 0))))
            except (TypeError, ValueError):
                continue
            if ep != epoch:
                continue
            tl_raw = (row.get("train_loss") or "").strip()
            el_raw = (row.get("eval_loss") or "").strip()
            train_loss = float(tl_raw) if tl_raw else None
            eval_loss: float | None = None
            if el_raw:
                try:
                    eval_loss = float(el_raw)
                except ValueError:
                    eval_loss = None
            return {"train_loss": train_loss, "eval_loss": eval_loss}
    return {"train_loss": None, "eval_loss": None}


def format_bart_holdout_paper_summary_zh(
    wm: dict[str, float | int],
    test_loss: float | None,
    ep20: dict[str, float | None],
    *,
    paper_overrides: dict[str, float] | None = None,
) -> str:
    """生成可直接写入论文的中文结果句（占位符已填数）。

    paper_overrides: 若提供 precision/recall/f1/category_assignment_accuracy_pct，
    则覆盖 wm 中对应项（用于与 Trainer.evaluate(test) 的 test_structured_* 一致）。
    """

    def fmt4(x: float) -> str:
        if x != x:
            return "—"
        return f"{x:.4f}"

    def fmt_pct(x: float) -> str:
        if x != x:
            return "—"
        return f"{x:.2f}"

    tr = ep20.get("train_loss")
    ev = ep20.get("eval_loss")
    tr_s = f"{tr:.4f}" if tr is not None else "—"
    ev_s = f"{ev:.4f}" if ev is not None else "—"
    tl_s = f"{test_loss:.6f}" if test_loss is not None else "—"

    po = paper_overrides or {}
    p = float(po.get("precision", wm["precision"]))
    r = float(po.get("recall", wm["recall"]))
    f1v = float(po.get("f1", wm["f1"]))
    ca = float(
        po.get("category_assignment_accuracy_pct", wm["category_assignment_accuracy_pct"])
    )

    return (
        "在预留数据集上，词元级精确率达到 {}，召回率达到 {}，F1 值达到 {}。"
        "正确识别的词元中，类别分配准确率为 {}%。"
        "预留测试损失为 {}（第 20 个训练轮的训练损失为 {}，验证损失为 {}）。".format(
            fmt4(p), fmt4(r), fmt4(f1v), fmt_pct(ca), tl_s, tr_s, ev_s
        )
    )


class BARTCuePredictor:
    def __init__(self, model_dir=None):
        """
        加载训练好的 BART 模型 和 tokenizer。

        Args:
            model_dir (str): 包含 config.json 与权重（pytorch_model.bin / model.safetensors）的目录。
                默认 models/bart_narro_v4（与 bart_train 默认保存路径一致）。
        """
        if model_dir is None:
            model_dir = DEFAULT_BART_MODEL_DIR
        print(f"--- [模块B] 正在从 '{model_dir}' 加载 BART 线索提取模型 ---")
        self.model_dir = model_dir
        self.device = _pick_bart_device()
        if self.device.type == "cpu" and (
            _matplotlib_or_xgboost_loaded() or os.environ.get("NARRO_BART_FORCE_CPU")
        ):
            print(
                "  [BART] 使用 CPU（规避 macOS MPS 段错误；"
                "NARRO_BART_FORCE_CPU=0 且在 matplotlib 之前加载时可试 MPS）"
            )

        try:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_dir).to(
                self.device
            )
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
            print("  [✓] BART 模型加载成功。")
        except Exception as e:
            print(f"❌ 错误: 加载 BART 模型失败。请确保 '{model_dir}' 路径正确。")
            print(
                "  请先运行 'bart_train.py' 来训练并保存 BART 模型。"
            )
            print(f"  {e}")
            raise

    def predict_ist_words(self, text: str) -> str:
        """为一段新文本生成结构化 IST 串（含 [IS_*]、已去 pad/eos 并规整空格/括号）。"""
        preprocess_text = f"{IST_INPUT_PREFIX}{text}"

        self.model.eval()
        with torch.no_grad():
            inputs = self.tokenizer(
                preprocess_text,
                return_tensors="pt",
                max_length=512,
                truncation=True,
            ).to(self.device)

            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=BART_IST_GEN_MAX_LENGTH,
                num_beams=BART_IST_GEN_NUM_BEAMS,
                early_stopping=True,
            )

            predicted_text = self.tokenizer.decode(
                outputs[0],
                skip_special_tokens=False,
                clean_up_tokenization_spaces=False,
            )

        return cleanup_bart_structured_decode(predicted_text, self.tokenizer)

    def predict_ist_analyzed(self, narrative: str) -> dict:
        """
        自动化 IST 分析：叙述文本 → BART 生成 → 解析六类 IST（+ Unclassified）下的词项，
        并给出 (1) 目标格式中的 bart_count（若可解析）(2) 在叙述中的 Jieba 词频。

        Returns:
            dict:
              - raw_output: str
              - structured_format_detected: bool  （是否出现 [IS_*] / [Unclassified]）
              - items: list[{category, word, bart_count, count_in_narrative}]
              - by_category: {category: [同上字段的字典...]}
              - ist_words_flat: str  空格连接词项，供仍吃「扁平 ist 串」的旧代码使用
        """
        raw = self.predict_ist_words(narrative)
        structured = "[IS_" in raw or "[Unclassified]" in raw
        items = parse_structured_ist_string(raw)
        if not items:
            items = _fallback_entries_from_flat_string(raw)

        for e in items:
            e["count_in_narrative"] = count_ist_token_in_narrative(narrative, e["word"])

        by_category: dict[str, list[dict]] = {}
        for e in items:
            by_category.setdefault(e["category"], []).append(
                {
                    "word": e["word"],
                    "bart_count": e["bart_count"],
                    "count_in_narrative": e["count_in_narrative"],
                }
            )

        flat_tokens = []
        for e in items:
            w = e["word"]
            if w and w not in flat_tokens:
                flat_tokens.append(w)
        ist_words_flat = " ".join(flat_tokens)

        return {
            "raw_output": raw,
            "structured_format_detected": structured and bool(_PAIR_RE.search(raw)),
            "items": items,
            "by_category": by_category,
            "ist_words_flat": ist_words_flat,
        }


# 兼容旧代码中的类名
BartPredictor = BARTCuePredictor

if __name__ == "__main__":
    new_narrative_text = "小猫想抓蝴蝶。它跳了起来，但是没有抓到。小猫很难过。"

    print("--- 演示 BART 预测器 (模块 B) ---")

    try:
        bart_model = BARTCuePredictor()
        print(f"\n输入文本: {new_narrative_text}")
        predicted_clues = bart_model.predict_ist_words(new_narrative_text)
        print(f"原始生成串: {predicted_clues}")

        analyzed = bart_model.predict_ist_analyzed(new_narrative_text)
        print("\n--- predict_ist_analyzed（六类 IST + 叙述内词频）---")
        print(f"structured_format_detected: {analyzed['structured_format_detected']}")
        for it in analyzed["items"]:
            print(
                f"  [{it['category']}] {it['word']!r}  "
                f"bart_count={it['bart_count']}  narrative_count={it['count_in_narrative']}"
            )
        print(f"ist_words_flat: {analyzed['ist_words_flat']!r}")
    except Exception as e:
        print("\n--- 演示失败 ---")
        print(f"错误: {e}")
