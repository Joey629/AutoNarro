"""
micro_encoder.py
=============================
宏观 SC 回归共用：与 train_micro 对齐的 (q,c) 构造、宏观 SS 权重加载、**单次遍历**提取
Global / Hierarchical [CLS]，以及可选的 **micro 二分类概率**（完整 head：inner→ReLU→classifier→sigmoid）。

被 import
    - train_macro_xgb.py
    - train_macro_xgb.py

(q,c) 与 IST 第二段格式（**唯一真源**）
    ``qc_pairs_from_row`` 必须调用 ``train_micro.format_micro_context_segment`` 与
    ``MICRO_IST_INLINE_SEPARATOR``；禁止在本文件内再写一套「叙事 + 已知线索：…」等字符串，
    否则与宏观 SS 微调输入不一致、可复现性失效。若改训练侧格式，只改 train_micro 模块并保留此 import。

宏观 SC train/test 划分（与宏观 SS 一致）
    ``load_or_create_macro_split`` 使用 ``train_micro_shared.split_train_val_test_70_10_20``：
    **test** 与宏观 SS 训练脚本的 test（全库约 20%，按 ``story_type`` 分层）为**同一索引集合**；
    **train** 返回 train+val 合并位置（全库约 80%），供 XGB 拟合。缓存默认
    ``regression_macro_split_narro_v4_701020_seed42.npz``（勿与旧版 80/20 按行号 npz 混用）。

相对早期双遍扫描脚本的增强
    - extract_all_micro_features：每篇只 forward 一次 BERT+头，避免 global/hier 各扫一遍 df。
    - micro 概率：禁止 classifier(cls) 跳过 inner_layer；与宏观 SS 训练前向一致。
"""

from __future__ import annotations

import os

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer

import train_micro_shared as msh
import train_micro as micro
from pretrained_models import encoder_from_pretrained_kwargs, resolve_encoder_path


def qc_pairs_from_row(
    row: pd.Series,
    question_templates: dict | None = None,
    task_names: list[str] | None = None,
    ist_tasks: set[str] | None = None,
    ist_column: str = "ist_words",
) -> tuple[list[str], list[str]]:
    question_templates = question_templates or micro.QUESTION_TEMPLATES
    task_names = task_names or micro.TASK_NAMES
    ist_tasks = ist_tasks if ist_tasks is not None else micro.IST_TASKS

    text, story = row["text"], row["story_type"]
    ist = row.get(ist_column, "")
    if pd.isna(ist):
        ist = ""
    elif not isinstance(ist, str):
        ist = str(ist)

    if story not in question_templates:
        return [], []

    qs, cs = [], []
    for task in task_names:
        qs.append(question_templates[story][task])
        use_ist = bool(ist) and task in ist_tasks
        cs.append(micro.format_micro_context_segment(text, ist, use_ist))
    return qs, cs


def _forward_cls_and_micro_probs(
    model: msh.ClueAugmentedQAModel,
    tokenizer,
    qs: list[str],
    cs: list[str],
    device: torch.device,
    max_length: int,
    compute_micro: bool,
) -> tuple[np.ndarray, np.ndarray]:
    """
    一次 batch：BERT [CLS] (T,H) + 可选 sigmoid 概率 (T,) 与宏观 SS 训练一致。
    """
    enc = tokenizer(
        qs,
        cs,
        padding=True,
        truncation="only_second",
        max_length=max_length,
        return_tensors="pt",
    )
    tti = enc.get("token_type_ids")
    if tti is None:
        tti = torch.zeros_like(enc["input_ids"])
    input_ids = enc["input_ids"].to(device)
    attention_mask = enc["attention_mask"].to(device)
    tti = tti.to(device)

    bert_kwargs = dict(input_ids=input_ids, attention_mask=attention_mask)
    if getattr(model, "_pass_token_type_ids", True):
        bert_kwargs["token_type_ids"] = tti
    with torch.no_grad():
        bert_out = model.bert(**bert_kwargs)
        cls = bert_out.last_hidden_state[:, 0, :].float()
        if compute_micro:
            x = model.dropout(cls)
            x = F.relu(model.inner_layer(x))
            x = model.dropout(x)
            logits = model.classifier(x)
            micro = torch.sigmoid(logits).squeeze(-1).float().cpu().numpy()
        else:
            micro = np.zeros((cls.shape[0],), dtype=np.float32)
        cls_np = cls.cpu().numpy().astype(np.float32)
    return cls_np, micro


def _lora_kwargs_from_micro_config(config_path: str | None) -> dict:
    """与 train_micro._make_micro_model 一致，避免不同 checkpoint 的 LoRA 秩不匹配。"""
    path = (config_path or os.environ.get("NARRO_MICRO_CONFIG", "")).strip()
    if not path:
        return {}
    from micro_training_config import MicroTrainingConfig

    o = MicroTrainingConfig.from_json(path).train_options
    kw: dict = {"lora_r": o.lora_r, "lora_alpha": o.lora_alpha}
    if o.lora_target_modules:
        kw["lora_target_modules"] = o.lora_target_modules
    print(
        f"[regression 宏观 SS 编码器] LoRA 配置 ({path}): "
        f"r={o.lora_r} alpha={o.lora_alpha} targets={o.lora_target_modules}"
    )
    return kw


def load_micro_encoder(
    checkpoint_path: str,
    model_name: str | None = None,
    device: torch.device | None = None,
    micro_config_path: str | None = None,
) -> tuple[AutoTokenizer, msh.ClueAugmentedQAModel, torch.device]:
    model_name = model_name or micro.MODEL_NAME
    if device is None:
        device = msh.pick_device()
        if os.environ.get("REGRESSION_FORCE_CPU", "").lower() in ("1", "true", "yes"):
            device = torch.device("cpu")
            print("[regression 宏观 SS 编码器] REGRESSION_FORCE_CPU=1 → 使用 CPU")
    cfg_path = (micro_config_path or os.environ.get("NARRO_MICRO_CONFIG", "")).strip()
    local_pretrained = None
    trust_rc = None
    if cfg_path:
        from micro_training_config import MicroTrainingConfig

        mc = MicroTrainingConfig.from_json(cfg_path)
        local_pretrained = mc.local_pretrained_path
        trust_rc = mc.trust_remote_code
        model_name = mc.model_name or model_name
    encoder_path = resolve_encoder_path(
        model_name,
        str(local_pretrained) if local_pretrained else None,
    )
    load_kw = encoder_from_pretrained_kwargs(model_name, trust_remote_code=trust_rc)
    tokenizer = AutoTokenizer.from_pretrained(encoder_path, **load_kw)
    sep = getattr(tokenizer, "sep_token", None) or "[SEP]"
    micro.MICRO_IST_INLINE_SEPARATOR = str(sep)
    print(f"[regression 宏观 SS 编码器] {model_name} | IST sep={repr(micro.MICRO_IST_INLINE_SEPARATOR)}")
    base = AutoModel.from_pretrained(encoder_path, **load_kw)
    lora_kw = _lora_kwargs_from_micro_config(cfg_path or micro_config_path)
    model = msh.ClueAugmentedQAModel(base, use_peft=True, **lora_kw)
    # 先 CPU 加载再 .to(device)，避免 MPS 上 PEFT/embedding 出现 placeholder storage 错误
    state = msh.load_state_dict_checkpoint(checkpoint_path, map_location="cpu")
    missing, unexpected = model.load_state_dict(state, strict=False)
    if missing:
        print(f"[regression 宏观 SS 编码器] load_state_dict 未匹配键: {len(missing)} 个")
    if unexpected:
        print(f"[regression 宏观 SS 编码器] 意外键: {unexpected[:5]}...")
    model.eval()
    model.to(device)
    return tokenizer, model, device


def extract_all_micro_features(
    df: pd.DataFrame,
    model: msh.ClueAugmentedQAModel,
    tokenizer,
    device: torch.device,
    ist_column: str = "ist_words",
    max_length: int | None = None,
    compute_micro_prob: bool = True,
    desc: str = "宏观 SS 全量 [CLS]+micro",
) -> dict[str, np.ndarray | dict]:
    """
    单次遍历 df。返回：
        global (N,H), hierarchical (N,4H), micro_prob (N,15), _meta
    compute_micro_prob=False 时 micro_prob 全零（省一点点算力）。
    """
    max_length = max_length if max_length is not None else micro.MAX_LENGTH
    H = model.bert.config.hidden_size
    Tn = len(micro.TASK_NAMES)
    sl_e1, sl_e2, sl_e3 = slice(0, 5), slice(5, 10), slice(10, 15)

    og, oh, om = [], [], []
    for _, row in tqdm(df.iterrows(), total=len(df), desc=desc):
        qs, cs = qc_pairs_from_row(row, ist_column=ist_column)
        if not qs:
            og.append(np.zeros((1, H), dtype=np.float32))
            oh.append(np.zeros((1, 4 * H), dtype=np.float32))
            om.append(np.zeros((1, Tn), dtype=np.float32))
            continue
        cls_mat, micro_probs = _forward_cls_and_micro_probs(
            model, tokenizer, qs, cs, device, max_length, compute_micro_prob
        )
        g = cls_mat.mean(axis=0, keepdims=True).astype(np.float32)
        e1 = cls_mat[sl_e1].mean(axis=0, keepdims=True)
        e2 = cls_mat[sl_e2].mean(axis=0, keepdims=True)
        e3 = cls_mat[sl_e3].mean(axis=0, keepdims=True)
        gg = np.mean(np.vstack([e1, e2, e3]), axis=0, keepdims=True)
        h = np.concatenate([e1, e2, e3, gg], axis=1).astype(np.float32)
        og.append(g)
        oh.append(h)
        om.append(micro_probs.reshape(1, -1).astype(np.float32))

    return {
        "global": np.concatenate(og, axis=0),
        "hierarchical": np.concatenate(oh, axis=0),
        "micro_prob": np.concatenate(om, axis=0),
        "_meta": {"H": H, "T": Tn, "task_names": micro.TASK_NAMES},
    }


def build_regression_feature_names(
    ling_cols: list[str],
    hidden: int,
    feature_mode: str,
    use_micro_prob: bool,
) -> list[str]:
    if feature_mode == "global":
        names = [f"bert_Global_{i}" for i in range(hidden)]
    elif feature_mode == "hierarchical":
        names = (
            [f"bert_E1_{i}" for i in range(hidden)]
            + [f"bert_E2_{i}" for i in range(hidden)]
            + [f"bert_E3_{i}" for i in range(hidden)]
            + [f"bert_Global_{i}" for i in range(hidden)]
        )
    else:
        raise ValueError(feature_mode)
    if use_micro_prob:
        for t in micro.TASK_NAMES:
            names.append(f"micro_prob_{t}")
    names += list(ling_cols)
    return names


def build_regression_X(
    feats: dict[str, np.ndarray],
    ling_mat: np.ndarray,
    feature_mode: str,
    use_micro_prob: bool,
) -> np.ndarray:
    parts: list[np.ndarray] = [feats[feature_mode].astype(np.float32)]
    if use_micro_prob:
        parts.append(feats["micro_prob"].astype(np.float32))
    parts.append(ling_mat.astype(np.float32))
    return np.concatenate(parts, axis=1).astype(np.float64)


def extract_global_features_m4(
    df, model, tokenizer, device, ist_column="ist_words", max_length=None, desc="Global [CLS]",
):
    f = extract_all_micro_features(
        df, model, tokenizer, device, ist_column, max_length, compute_micro_prob=False, desc=desc
    )
    return f["global"]


def extract_hierarchical_features_m4(
    df, model, tokenizer, device, ist_column="ist_words", max_length=None, desc="Hierarchical [CLS]",
):
    f = extract_all_micro_features(
        df, model, tokenizer, device, ist_column, max_length, compute_micro_prob=False, desc=desc
    )
    return f["hierarchical"]


def bert_feature_names_global(ling_cols: list[str], hidden: int) -> list[str]:
    return build_regression_feature_names(ling_cols, hidden, "global", use_micro_prob=False)


def bert_feature_names_hierarchical(ling_cols: list[str], hidden: int) -> list[str]:
    return build_regression_feature_names(ling_cols, hidden, "hierarchical", use_micro_prob=False)


def report_xgb_feature_importance(
    model,
    feature_names: list[str],
    target_label: str,
    output_csv: str | None = None,
    top_k: int = 25,
) -> None:
    imp = np.asarray(model.feature_importances_, dtype=np.float64)
    order = np.argsort(imp)[::-1]
    rows: list[tuple[str, float]] = []
    print(f"  [XGB Feature importance] {target_label} (top {top_k}):")
    for i in order[:top_k]:
        nm = feature_names[i] if i < len(feature_names) else f"f{i}"
        print(f"    {nm}: {imp[i]:.5f}")
        rows.append((nm, float(imp[i])))
    top5 = {feature_names[i] if i < len(feature_names) else "" for i in order[:5]}
    length_proxies = {
        "TNW", "TNU", "auto_TNW", "Sentences_token", "MLU", "auto_MLU", "auto_TNU",
    }
    if top5 & length_proxies:
        print("  [提示] Top 含长度代理列 → 留意 §4.3.1；可调大 reg_lambda / 降 max_depth。")
    if output_csv:
        pd.DataFrame(rows, columns=["feature", "importance"]).to_csv(
            output_csv, index=False, encoding="utf-8-sig"
        )


def load_or_create_macro_split(
    df: pd.DataFrame,
    cache_path: str | None,
    seed: int,
    stratify_col: str = "story_type",
) -> tuple[np.ndarray, np.ndarray]:
    """
    与 ``train_micro_shared.split_train_val_test_70_10_20`` 同源划分。

    对 ``df`` 的 **当前行顺序** 赋予位置 0..n-1，分层划分后返回：
        - ``train``：train ∪ val 的位置索引（约 80%，供 XGB 训练）；
        - ``test``：test 的位置索引（约 20%，与微观 脚本 test_df **同一批样本**）。

    ``df`` 须含 ``stratify_col``（默认 ``story_type``）；划分前会先 ``reset_index(drop=True)``，
    仅位置索引写入 npz，与 ``train_macro_xgb`` 中
    ``df.iloc[tr_idx]`` 用法一致。
    """
    if cache_path:
        from paths import resolve_split_cache

        cache_path = resolve_split_cache(cache_path)
    if cache_path and os.path.isfile(cache_path):
        z = np.load(cache_path)
        tr, te = z["train"], z["test"]
        print(
            f"  [split] 已加载 {cache_path}  train+val={len(tr)} test={len(te)} "
            f"(微观 对齐 70/10/20 → XGB 用 80%/20%)"
        )
        return tr, te

    df_pos = df.reset_index(drop=True).copy()
    if "_macro_split_pos" in df_pos.columns:
        raise ValueError("df 不得包含列名 _macro_split_pos")
    df_pos["_macro_split_pos"] = np.arange(len(df_pos), dtype=np.int64)

    use_participant = os.environ.get("NARRO_SPLIT_BY_PARTICIPANT", "1").lower() in (
        "1",
        "true",
        "yes",
    )
    if use_participant:
        train_df, val_df, test_df = msh.split_train_val_test_by_participant(df_pos, seed)
    else:
        train_df, val_df, test_df = msh.split_train_val_test_70_10_20(
            df_pos, seed, stratify_col=stratify_col
        )
    tr = np.sort(
        np.concatenate(
            [train_df["_macro_split_pos"].to_numpy(), val_df["_macro_split_pos"].to_numpy()]
        )
    )
    te = np.sort(test_df["_macro_split_pos"].to_numpy())

    if cache_path:
        np.savez(cache_path, train=tr, test=te)
        print(
            f"  [split] 已写入 {cache_path}  train+val={len(tr)} test={len(te)} "
            f"(微观 对齐 70/10/20)"
        )
    return tr, te
