# analyze_micro_errors.py
# 多任务（A2–A16）错误分析：与 train_micro / train_micro_shared 对齐（问法、IST 仅 A6/A11/A16、</s> 衔接、LoRA-[CLS] 头）。
# 划分与 analyze_micro_metadata / analyze_regression_* 一致：micro_test + 同源 npz。
# 输出目录默认与脚本同名，见 config_analysis_output_paths.py。

import os
import warnings

import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer

import config_analysis_output_paths as arp
import micro_encoder as rfe
import train_micro_shared as msh
import train_micro as micro

warnings.filterwarnings("ignore")

CONFIG = {
    "data_path": micro.FILE_PATH,
    "model_name": micro.MODEL_NAME,
    "micro_weights": "models/micro_narro_v4.pth",
    "batch_size": 16,
    "eval_split": "micro_test",
    "split_cache": "regression_macro_split_narro_v4_701020_seed42.npz",
    "tasks_to_analyze": ["A6", "A11", "A13", "A16"],
    "output_dir": arp.OUTPUT_ANALYZE_MULTITASK_ERRORS,
    "run_manifest_script": "analyze_micro_errors",
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


def _build_expanded_pairs(test_df: pd.DataFrame):
    qs, cs, row_ix, task_names = [], [], [], []
    for ri, row in test_df.iterrows():
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
            row_ix.append(ri)
            task_names.append(task)
    return qs, cs, row_ix, task_names


def _predict_in_batches(model, tokenizer, device, qs, cs, batch_size: int):
    probs = []
    n = len(qs)
    for start in tqdm(range(0, n, batch_size), desc="模型预测"):
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
        probs.extend(torch.sigmoid(logits).squeeze(-1).float().cpu().numpy().tolist())
    return np.array(probs, dtype=np.float64)


if __name__ == "__main__":
    path = CONFIG["micro_weights"]
    if not path or path.endswith("PASTE_YOUR_BEST_MODEL_FILENAME_HERE.pth"):
        print("请设置 CONFIG['micro_weights'] 为实际 .pth 路径。")
        raise SystemExit(1)
    if not os.path.isfile(path):
        print(f"找不到权重: {path}")
        raise SystemExit(1)

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    msh.set_seed(micro.SEED)
    device = msh.pick_device()

    df = pd.read_csv(CONFIG["data_path"])
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    df["ist_words"] = df.get("ist_words", pd.Series(dtype=str)).fillna("")
    if "story_type" not in df.columns:
        raise SystemExit("缺少列 story_type")
    msh.coerce_task_label_columns(df, micro.TASK_NAMES)

    test_df = _select_eval_df(df)
    print(
        f"评估子集: {CONFIG['eval_split']} → n={len(test_df)} "
        f"(问法/IST 与 train_micro 一致)"
    )

    qs, cs, row_ix, task_col = _build_expanded_pairs(test_df)
    if not qs:
        raise SystemExit("无有效样本（检查 story_type 是否在 QUESTION_TEMPLATES 中）")

    tokenizer = AutoTokenizer.from_pretrained(CONFIG["model_name"])
    base = AutoModel.from_pretrained(CONFIG["model_name"])
    model = msh.ClueAugmentedQAModel(base, use_peft=True)
    state = msh.load_state_dict_checkpoint(path, map_location=device)
    model.load_state_dict(state, strict=False)
    model.to(device)
    model.eval()

    all_probs = _predict_in_batches(
        model, tokenizer, device, qs, cs, CONFIG["batch_size"]
    )
    pred_bin = (all_probs > 0.5).astype(int)

    # 便于阅读的「完整输入」摘要（非模型真实 token 拼接，仅 CSV 追溯用）
    full_input_text = [f"Q: {q} || C: {c}" for q, c in zip(qs, cs)]

    results_df = pd.DataFrame(
        {
            "row_pos": row_ix,
            "task": task_col,
            "predicted_prob": all_probs,
            "predicted_label": pred_bin,
            "full_input_text": full_input_text,
        }
    )
    merged_df = results_df.merge(
        test_df.reset_index(drop=True),
        left_on="row_pos",
        right_index=True,
        how="left",
    )

    out_dir = CONFIG.get("output_dir") or arp.OUTPUT_ANALYZE_MULTITASK_ERRORS
    os.makedirs(out_dir, exist_ok=True)
    print(f"\n--- 筛选错误样本 → {out_dir} ---")

    for task_name in CONFIG["tasks_to_analyze"]:
        print(f"\n--- 任务: {task_name} ---")
        task_df = merged_df[merged_df["task"] == task_name].copy()
        if task_df.empty:
            print("  无样本")
            continue
        task_df["true_label"] = task_df[task_name]
        err = task_df[task_df["true_label"] != task_df["predicted_label"]]
        if err.empty:
            print("  无错误样本")
            continue
        fp_df = err[err["predicted_label"] == 1]
        fn_df = err[err["predicted_label"] == 0]
        cols = [
            "story_type",
            "text",
            "ist_words",
            "true_label",
            "predicted_label",
            "predicted_prob",
            "full_input_text",
        ]
        if not fp_df.empty:
            fp_path = os.path.join(out_dir, f"{task_name}_false_positives.csv")
            fp_df[cols].to_csv(fp_path, index=False, encoding="utf-8-sig")
            print(f"  FP: {len(fp_df)} → {fp_path}")
        if not fn_df.empty:
            fn_path = os.path.join(out_dir, f"{task_name}_false_negatives.csv")
            fn_df[cols].to_csv(fn_path, index=False, encoding="utf-8-sig")
            print(f"  FN: {len(fn_df)} → {fn_path}")

    pd.DataFrame(
        [
            {
                "script": CONFIG["run_manifest_script"],
                "micro_weights": path,
                "eval_split": CONFIG["eval_split"],
                "split_cache": CONFIG.get("split_cache"),
                "tasks_to_analyze": ",".join(CONFIG["tasks_to_analyze"]),
                "n_eval_narratives": len(test_df),
                "output_dir": out_dir,
            }
        ]
    ).to_csv(os.path.join(out_dir, "run_manifest.csv"), index=False)
    print(f"\n✅ run_manifest.csv → {out_dir}")
    print("\n完成。")
