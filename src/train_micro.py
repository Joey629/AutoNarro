# train_micro.py
# 宏观 SS（故事结构）：QiDeBERTa-base + LoRA；每个子任务 (A2–A16) 用「问句 + 叙事正文」输入，A6/A11/A16 可带 IST 线索词。
# 共享 train_micro_shared.py（原 train_micro_v3 逻辑）。
#
# 编码器对照（如 DeBERTa-v3）：
#   PYTHONPATH=src python src/train_micro.py --config configs/micro_narro_v4.json
# 或 NARRO_MICRO_CONFIG=configs/micro_narro_v4.json

import argparse
import os
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import KFold
from transformers import AutoTokenizer, AutoModel
import warnings

import train_micro_shared as msh
from micro_training_config import MicroTrainingConfig
from pretrained_models import encoder_from_pretrained_kwargs, resolve_encoder_path

warnings.filterwarnings("ignore")

QUESTION_TEMPLATES = {
    "cat": {
        "A2": "你觉得小猫为什么会开始第一个事件？可能是什么感受、想法或情境触发了它？",
        "A3": "在追蝴蝶的过程中，你认为小猫真正想要达成的是什么？",
        "A4": "小猫为了抓蝴蝶可能尝试了哪些方式？你觉得它为什么会选择这样做？",
        "A5": "你认为小猫的这次追逐经历是成功的还是失败的？是什么让你这么觉得？",
        "A6": "抓蝴蝶失败后，你觉得猫和蝴蝶各自可能会有怎样的情绪？有哪些线索让我们这么认为？",
        "A7": "你认为男孩为什么会介入第二个事件？可能是看到了什么或感受到了什么？",
        "A8": "在拿球的过程中，男孩可能希望达成什么样的目标？",
        "A9": "男孩为了拿回球，可能采取了哪些行动？你觉得他为什么会这样做？",
        "A10": "男孩拿球的行动最终带来了什么结果？你认为这个结果对他有什么影响？",
        "A11": "拿回球后，你觉得男孩的情绪可能是怎样的？为什么？",
        "A12": "第三个事件中，小猫为什么会想要去拿鱼？可能是什么激发了它的行为？",
        "A13": "在关于鱼的事件中，小猫可能真正想要的是什么？",
        "A14": "小猫为了得到鱼，可能采取了哪些行动？你觉得它为什么选择这样做？",
        "A15": "你觉得小猫最终成功得到鱼了吗？从哪些地方可以看出？",
        "A16": "得到鱼后，你觉得小猫的情绪反应可能是怎样的？为什么？",
    },
    "dog": {
        "A2": "你认为小狗为什么会开始第一个事件？可能是怎样的感受或所见引发的？",
        "A3": "在追老鼠的过程中，小狗可能想要达成什么目标？",
        "A4": "小狗为了抓老鼠可能尝试了哪些行为？你觉得它为什么会这样做？",
        "A5": "你认为小狗的这次追逐经历是成功的还是失败的？是什么让你这么觉得？",
        "A6": "抓老鼠失败后，你觉得小狗和老鼠各自可能会有怎样的情绪？有哪些线索支持这种推测？",
        "A7": "第二个事件中，男孩为什么会想要拿回气球？可能是看到了什么或感受到了什么？",
        "A8": "在关于气球的事件中，男孩可能希望达成什么目标？",
        "A9": "男孩为了拿回气球，可能采取了哪些行动？你觉得他为什么选择这样做？",
        "A10": "男孩最终拿回了气球，你认为这个结果对他意味着什么？",
        "A11": "拿回气球后，你觉得男孩的情绪可能是怎样的？为什么？",
        "A12": "第三个事件中，小狗为什么会想要得到香肠？可能是什么激发了它的行为？",
        "A13": "在关于香肠的事件中，小狗可能真正想要的是什么？",
        "A14": "小狗为了得到香肠，可能采取了哪些行动？你觉得它为什么选择这样做？",
        "A15": "小狗拿香肠的行动最终带来了什么结果？你觉得它成功了吗？",
        "A16": "得到香肠后，你觉得小狗的情绪反应可能是怎样的？为什么？",
    },
    "bird": {
        "A2": "你认为第一个事件是如何开始的？鸟妈妈或小鸟可能感受到了什么或看到了什么？",
        "A3": "在喂食的事件中，鸟妈妈可能想要达成什么目标？",
        "A4": "鸟妈妈为了喂小鸟，可能采取了哪些行动？你觉得她为什么这样做？",
        "A5": "你认为鸟妈妈为她的小鸟找到食物了吗？这次寻找食物的过程看起来怎么样？",
        "A6": "喂食成功后，你觉得鸟妈妈和小鸟各自可能会有怎样的情绪？有哪些线索让我们这么认为？",
        "A7": "第二个事件中，小猫为什么会想要抓小鸟？可能是怎样的情境触发了它？",
        "A8": "在抓小鸟的事件中，小猫可能希望达成什么目标？",
        "A9": "小猫为了抓小鸟，可能采取了哪些行动？你觉得它为什么会这样做？",
        "A10": "你认为小猫成功抓到小鸟了吗？当时的情况是怎样的？",
        "A11": "小猫抓到小鸟后，你觉得小猫和小鸟各自可能会有怎样的情绪？为什么？",
        "A12": "第三个事件中，小狗为什么会介入救小鸟？可能是看到了什么或感受到了什么？",
        "A13": "在救小鸟的事件中，小狗可能真正想要达成的是什么？",
        "A14": "小狗为了救小鸟，可能采取了哪些行动？你觉得它为什么选择这样做？",
        "A15": "小狗救小鸟的行动最终带来了什么结果？你认为它成功了吗？",
        "A16": "小鸟获救后，你觉得小狗、小猫、小鸟和鸟妈妈各自可能会有怎样的情绪？为什么？",
    },
    "goat": {
        "A2": "你认为第一个事件是如何开始的？小羊或羊妈妈可能感受到了什么或看到了什么？",
        "A3": "在救小羊的事件中，羊妈妈可能想要达成什么目标？",
        "A4": "羊妈妈为了救小羊，可能采取了哪些行动？你觉得她为什么这样做？",
        "A5": "你认为羊妈妈成功救下小羊了吗？你是如何判断的？",
        "A6": "小羊获救后，你觉得羊妈妈和小羊各自可能会有怎样的情绪？为什么？",
        "A7": "第二个事件中，狐狸为什么会想要抓小羊？可能是怎样的情境触发了它？",
        "A8": "在抓小羊的事件中，狐狸可能希望达成什么目标？",
        "A9": "狐狸为了抓小羊，可能采取了哪些行动？你觉得它为什么会这样做？",
        "A10": "你认为狐狸成功抓到小羊了吗？从故事中你能找到什么线索？",
        "A11": "狐狸抓到小羊后，你觉得狐狸和小羊各自可能会有怎样的情绪？为什么？",
        "A12": "第三个事件中，小鸟为什么会介入救小羊？可能是看到了什么或感受到了什么？",
        "A13": "在救小羊的事件中，小鸟可能真正想要达成的是什么？",
        "A14": "小鸟为了救小羊，可能采取了哪些行动？你觉得它为什么选择这样做？",
        "A15": "小鸟救小羊的行动最终带来了什么结果？你认为它成功了吗？",
        "A16": "小羊被小鸟救下后，你觉得小鸟、狐狸、小羊和羊妈妈各自可能会有怎样的情绪？为什么？",
    },
}

TASK_NAMES = [f"A{i}" for i in range(2, 17)]
NUM_TASKS = 15
BATCH_SIZE = 10
EPOCHS = 15
LEARNING_RATE = 2e-5
PATIENCE = 3
SEED = 42
N_SPLITS = 5
MAX_LENGTH = 512

MODEL_NAME = "Morton-Li/QiDeBERTa-base"
from paths import MODELS_DIR, narratives_csv_path

FILE_PATH = str(narratives_csv_path())
IST_TASKS = {"A6", "A11", "A16"}

# 论文 §3.3：Question 与 Narrative 为两段式 encoding；语义线索属第三段语义，在 **第二段内**
# 与叙事正文用 tokenizer 的句间分界衔接（QiDeBERTa 等为 </s>，与 BERT 的 [SEP] 同角色）。
# 不再使用「已知线索：」自然语言前缀，以免与词表/注意力模式不一致。
# 若曾用旧字符串训练过 .pth，需用本格式 **重新训练 宏观 SS** 后再做宏观回归对齐。
#
# micro_encoder.qc_pairs_from_row 从本模块 import 下列符号；勿在未同步回归脚本的情况下改名或重复实现。
MICRO_IST_INLINE_SEPARATOR = "</s>"


def format_micro_context_segment(text, ist, use_ist: bool) -> str:
    """第二段（context）：无 IST 任务 = 纯叙事；IST 任务 = 叙事 + sep + 线索（无「已知线索：」）。"""
    t = "" if text is None or (isinstance(text, float) and pd.isna(text)) else str(text).strip()
    if not use_ist:
        return t
    if ist is None or (isinstance(ist, float) and pd.isna(ist)):
        ist_s = ""
    else:
        ist_s = str(ist).strip()
    if not ist_s:
        return t
    return f"{t}{MICRO_IST_INLINE_SEPARATOR}{ist_s}"


def create_expanded_dataset(df, task_names, question_templates, ist_tasks):
    questions, context_cues, labels, task_idx = [], [], [], []
    for _, row in df.iterrows():
        text, story, ist = row["text"], row["story_type"], row.get("ist_words", "")
        if pd.isna(ist):
            ist = ""
        elif not isinstance(ist, str):
            ist = str(ist)
        if story not in question_templates:
            continue
        for j, task in enumerate(task_names):
            questions.append(question_templates[story][task])
            use_ist = bool(ist) and task in ist_tasks
            context_cues.append(format_micro_context_segment(text, ist, use_ist))
            labels.append(int(row[task]))
            task_idx.append(j)
    return questions, context_cues, labels, task_idx


def _parse_args():
    p = argparse.ArgumentParser(description="宏观 SS 多任务训练（可选 JSON 实验配置）")
    p.add_argument(
        "--config",
        default=os.environ.get("NARRO_MICRO_CONFIG", "").strip() or "configs/micro_narro_v4.json",
        help="训练 JSON，默认 configs/micro_narro_v4.json",
    )
    return p.parse_args()


def _apply_training_config(cfg: MicroTrainingConfig, tokenizer) -> None:
    global MODEL_NAME, SEED, N_SPLITS, EPOCHS, BATCH_SIZE, LEARNING_RATE, PATIENCE, MAX_LENGTH
    global MICRO_IST_INLINE_SEPARATOR

    MODEL_NAME = cfg.model_name
    SEED = cfg.seed
    N_SPLITS = cfg.n_splits
    EPOCHS = cfg.epochs
    BATCH_SIZE = cfg.batch_size
    LEARNING_RATE = cfg.learning_rate
    PATIENCE = cfg.patience
    MAX_LENGTH = cfg.max_length
    MICRO_IST_INLINE_SEPARATOR = cfg.resolve_ist_separator(tokenizer)
    if cfg.split_by_participant:
        os.environ["NARRO_SPLIT_BY_PARTICIPANT"] = "1"
    print(f"[宏观 SS训练] {cfg.id}: {cfg.label}")
    print(f"  编码器: {MODEL_NAME}")
    print(f"  IST 句间符: {repr(MICRO_IST_INLINE_SEPARATOR)} (tokenizer.sep_token)")
    print(f"  输出权重: {cfg.checkpoint_out}")
    print(f"  训练配方: {cfg.train_options.describe(cfg.learning_rate)}")
    cfg.train_options.apply_lora_env()


def _make_micro_model(encoder_path: str, load_kw: dict, run_cfg: MicroTrainingConfig | None):
    base = AutoModel.from_pretrained(encoder_path, **load_kw)
    if run_cfg is None:
        return msh.ClueAugmentedQAModel(base)
    o = run_cfg.train_options
    return msh.ClueAugmentedQAModel(
        base,
        lora_r=o.lora_r,
        lora_alpha=o.lora_alpha,
        lora_target_modules=o.lora_target_modules,
    )


def _train_opts(run_cfg: MicroTrainingConfig | None):
    return run_cfg.train_options if run_cfg else None


if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    args = _parse_args()
    run_cfg = MicroTrainingConfig.from_json(args.config) if args.config else None

    msh.set_seed(run_cfg.seed if run_cfg else SEED)
    device = msh.pick_device()
    if run_cfg:
        encoder_path = resolve_encoder_path(
            run_cfg.model_name,
            str(run_cfg.local_pretrained_path) if run_cfg.local_pretrained_path else None,
        )
    else:
        encoder_path = resolve_encoder_path(MODEL_NAME)
    load_kw = encoder_from_pretrained_kwargs(
        run_cfg.model_name if run_cfg else MODEL_NAME,
        trust_remote_code=run_cfg.trust_remote_code if run_cfg else None,
    )
    if load_kw:
        print("[预训练] trust_remote_code=True（自定义 modeling 代码）")
    tokenizer = AutoTokenizer.from_pretrained(encoder_path, **load_kw)
    if run_cfg:
        _apply_training_config(run_cfg, tokenizer)
    else:
        print(f"[宏观 SS] 默认编码器: {MODEL_NAME} | IST sep: {repr(MICRO_IST_INLINE_SEPARATOR)}")

    final_path = str(run_cfg.checkpoint_out) if run_cfg else str(MODELS_DIR / "micro_narro_v4.pth")
    cv_prefix = run_cfg.cv_prefix if run_cfg else "micro_narro_v4_cv_fold_"

    df = pd.read_csv(FILE_PATH)
    df.rename(columns={df.columns[0]: "text"}, inplace=True)
    df["ist_words"] = df.get("ist_words", pd.Series(dtype=str)).fillna("")
    if "story_type" not in df.columns:
        raise SystemExit("缺少列 story_type")
    msh.coerce_task_label_columns(df, TASK_NAMES)

    use_participant = os.environ.get("NARRO_SPLIT_BY_PARTICIPANT", "1").lower() in (
        "1",
        "true",
        "yes",
    )
    if use_participant:
        print("划分数据: 70/10/20（按 participant_id 分组，推荐）")
        train_df, val_df, test_df = msh.split_train_val_test_by_participant(df, SEED)
    else:
        print("划分数据: 70/10/20（按 story_type 行级分层）")
        train_df, val_df, test_df = msh.split_train_val_test_70_10_20(df, SEED)
    print(f"训练: {len(train_df)} | 验证: {len(val_df)} | 测试: {len(test_df)}")

    _tq, _tc, _, _ = create_expanded_dataset(train_df, TASK_NAMES, QUESTION_TEMPLATES, IST_TASKS)
    msh.report_truncation_stats(_tq, _tc, tokenizer, MAX_LENGTH, label="宏观 SS train 展开池")

    kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    cv_scores = []
    print(f"\n[CV 阶段] 宏观 SS Enhanced（IST 仅 A6/A11/A16）— {N_SPLITS} 折交叉验证...")
    for fold, (t_idx, v_idx) in enumerate(kf.split(train_df)):
        tr_f, va_f = train_df.iloc[t_idx], train_df.iloc[v_idx]
        t_q, t_c, t_l, t_tid = create_expanded_dataset(tr_f, TASK_NAMES, QUESTION_TEMPLATES, IST_TASKS)
        v_q, v_c, v_l, v_tid = create_expanded_dataset(va_f, TASK_NAMES, QUESTION_TEMPLATES, IST_TASKS)

        tr_loader = msh.build_pair_dataloader(
            t_q, t_c, t_l, t_tid, tokenizer, BATCH_SIZE, True, MAX_LENGTH, NUM_TASKS
        )
        va_loader = msh.build_pair_dataloader(
            v_q, v_c, v_l, v_tid, tokenizer, BATCH_SIZE, False, MAX_LENGTH, NUM_TASKS
        )

        pos_w = msh.pos_weight_per_task(t_l, t_tid, NUM_TASKS, device)
        model = _make_micro_model(encoder_path, load_kw, run_cfg)
        score = msh.train_multitask_bce(
            model,
            tr_loader,
            va_loader,
            EPOCHS,
            LEARNING_RATE,
            device,
            pos_w,
            f"{cv_prefix}{fold}.pth",
            PATIENCE,
            NUM_TASKS,
            train_options=_train_opts(run_cfg),
        )
        cv_scores.append(score)
        print(f"Fold {fold + 1}/5 F1: {score:.4f}")

    print(f"\nCV 稳定性总结: Mean={np.mean(cv_scores):.4f}, SD={np.std(cv_scores, ddof=1):.4f}")

    print("\n[最终训练阶段] 宏观 SS — 全量 train_df，val_df 早停...")
    tr_q, tr_c, tr_l, tr_tid = create_expanded_dataset(
        train_df, TASK_NAMES, QUESTION_TEMPLATES, IST_TASKS
    )
    va_q, va_c, va_l, va_tid = create_expanded_dataset(
        val_df, TASK_NAMES, QUESTION_TEMPLATES, IST_TASKS
    )
    tr_loader = msh.build_pair_dataloader(
        tr_q, tr_c, tr_l, tr_tid, tokenizer, BATCH_SIZE, True, MAX_LENGTH, NUM_TASKS
    )
    va_loader = msh.build_pair_dataloader(
        va_q, va_c, va_l, va_tid, tokenizer, BATCH_SIZE, False, MAX_LENGTH, NUM_TASKS
    )
    pos_w = msh.pos_weight_per_task(tr_l, tr_tid, NUM_TASKS, device)
    final_model = _make_micro_model(encoder_path, load_kw, run_cfg)
    msh.train_multitask_bce(
        final_model,
        tr_loader,
        va_loader,
        EPOCHS,
        LEARNING_RATE,
        device,
        pos_w,
        final_path,
        PATIENCE,
        NUM_TASKS,
        train_options=_train_opts(run_cfg),
    )

    print("\n[测试阶段] 宏观 SS — 20% Held-out")
    te_q, te_c, te_l, te_tid = create_expanded_dataset(
        test_df, TASK_NAMES, QUESTION_TEMPLATES, IST_TASKS
    )
    test_loader = msh.build_pair_dataloader(
        te_q, te_c, te_l, te_tid, tokenizer, BATCH_SIZE, False, MAX_LENGTH, NUM_TASKS
    )
    test_model = _make_micro_model(encoder_path, load_kw, run_cfg)
    test_model.load_state_dict(msh.load_state_dict_checkpoint(final_path, map_location=device))

    f1, acc, per_task = msh.evaluate_stride_macro_f1(test_model, test_loader, device, NUM_TASKS)
    print(f"Overall Macro F1: {f1:.4f} | Accuracy: {acc:.4f}")
    per_task_map = {name: float(s) for name, s in zip(TASK_NAMES, per_task)}
    for name, s in zip(TASK_NAMES, per_task):
        mark = " ← IST" if name in IST_TASKS else ""
        print(f"  {name}: {s:.4f}{mark}")
    print(f"\n最终权重: {final_path}")

    if run_cfg:
        run_cfg.write_results(
            cv_fold_f1=cv_scores,
            test_macro_f1=float(f1),
            test_accuracy=float(acc),
            per_task_f1=per_task_map,
            ist_separator_used=MICRO_IST_INLINE_SEPARATOR,
        )
        print(f"[宏观 SS训练] 指标已写入 {run_cfg.config_path}")
        print(f"           副本: {run_cfg.metrics_log}")
        base_f1 = run_cfg.comparison.get("baseline_test_macro_f1")
        if base_f1 is not None:
            delta = float(f1) - float(base_f1)
            print(f"[宏观 SS训练] vs 基线 test macro-F1 ({base_f1}): {delta:+.4f}")
