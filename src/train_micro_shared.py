# train_micro_shared.py
# M1–微观训练脚本共享逻辑（审稿对齐）：模型与设备、随机种子、标签清洗、分层划分、
# 双句 truncation=only_second、截断统计、按任务 pos_weight、BCE 训练步、步进切片评估、安全 load 权重。
# 说明：分层划分与按任务 pos_weight 会改变与旧版随机划分/标量权重的数值可比性，论文中应写明协议版本。

from __future__ import annotations

import os
import random
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from peft import LoraConfig, get_peft_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from tqdm import tqdm

from micro_training_config import M4TrainOptions


def set_seed(seed: int, deterministic: bool = False) -> None:
    """deterministic=True 时启用 cudnn deterministic（更慢，便于 CUDA 上尽量可复现）。"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def pick_device() -> torch.device:
    if torch.cuda.is_available():
        d = torch.device("cuda")
        print(f"设备: CUDA — {torch.cuda.get_device_name(0)}")
        return d
    if torch.backends.mps.is_available():
        print("设备: MPS (Apple GPU)")
        return torch.device("mps")
    print("设备: CPU（未检测到 CUDA / MPS）")
    return torch.device("cpu")


def _model_config(bert_module: nn.Module):
    cfg = getattr(bert_module, "config", None)
    if cfg is not None:
        return cfg
    base = getattr(bert_module, "base_model", None)
    return getattr(base, "config", None) if base is not None else None


def _is_deberta_family(bert_module: nn.Module) -> bool:
    cfg = _model_config(bert_module)
    if cfg is None:
        return False
    model_type = (getattr(cfg, "model_type", "") or "").lower()
    if model_type in ("deberta", "deberta-v2", "qideberta"):
        return True
    archs = getattr(cfg, "architectures", None) or []
    return any("deberta" in (a or "").lower() for a in archs)


def resolve_lora_target_modules(bert_model: nn.Module) -> list[str]:
    """
    RoBERTa/BERT: query, key, value
    DeBERTa / QiDeBERTa: query_proj, key_proj, value_proj
    """
    override = os.environ.get("NARRO_LORA_TARGETS", "").strip()
    if override:
        return [s.strip() for s in override.split(",") if s.strip()]

    deberta_targets = ["query_proj", "key_proj", "value_proj"]
    bert_targets = ["query", "key", "value"]
    suffixes = {n.split(".")[-1] for n, m in bert_model.named_modules() if isinstance(m, nn.Linear)}
    if all(t in suffixes for t in deberta_targets):
        return deberta_targets
    if all(t in suffixes for t in bert_targets):
        return bert_targets
    raise ValueError(
        f"无法推断 LoRA target_modules（已见 Linear 后缀: {sorted(suffixes)[:20]}…）。"
        "可设置 NARRO_LORA_TARGETS=query_proj,key_proj,value_proj"
    )


def _bert_hidden_size(bert_module: nn.Module) -> int:
    cfg = _model_config(bert_module)
    if cfg is None:
        raise ValueError("编码器缺少 config")
    return int(getattr(cfg, "hidden_size", None) or getattr(cfg, "d_model", 768))


def _bert_accepts_token_type_ids(bert_module: nn.Module) -> bool:
    """DeBERTa 系列 forward 不接受 token_type_ids；RoBERTa/BERT 需要。"""
    return not _is_deberta_family(bert_module)


class ClueAugmentedQAModel(nn.Module):
    """M1–微观 共用：预训练编码器 + LoRA、[CLS]、单 logit 头。"""

    def __init__(
        self,
        bert_model,
        use_peft: bool = True,
        *,
        lora_r: int = 8,
        lora_alpha: int = 16,
        lora_target_modules: list[str] | None = None,
    ):
        super().__init__()
        if use_peft:
            lora_targets = lora_target_modules or resolve_lora_target_modules(bert_model)
            print(f"[LoRA] target_modules={lora_targets} r={lora_r} alpha={lora_alpha}")
            lora_config = LoraConfig(
                r=lora_r, lora_alpha=lora_alpha, target_modules=lora_targets
            )
            self.bert = get_peft_model(bert_model, lora_config)
        else:
            self.bert = bert_model
        self._pass_token_type_ids = _bert_accepts_token_type_ids(self.bert)
        hidden = _bert_hidden_size(self.bert)
        self.inner_layer = nn.Linear(hidden, 768)
        self.dropout = nn.Dropout(0.5)
        self.classifier = nn.Linear(768, 1)

    def forward(self, input_ids, attention_mask, token_type_ids):
        kwargs = dict(input_ids=input_ids, attention_mask=attention_mask)
        if self._pass_token_type_ids:
            kwargs["token_type_ids"] = token_type_ids
        outputs = self.bert(**kwargs)
        cls_output = outputs.last_hidden_state[:, 0, :]
        x = self.dropout(cls_output)
        x = F.relu(self.inner_layer(x))
        x = self.dropout(x)
        return self.classifier(x)


def load_state_dict_checkpoint(path: str, map_location):
    """torch.save(model.state_dict()) 的纯张量文件；PyTorch 2.0+ 优先 weights_only=True 消除 FutureWarning。"""
    try:
        return torch.load(path, map_location=map_location, weights_only=True)
    except TypeError:
        return torch.load(path, map_location=map_location)


def report_truncation_stats(
    qs: list, cs: list, tokenizer, max_length: int, label: str = "样本"
) -> tuple[float, int, int]:
    """
    逐条 pair 编码（不 padding），统计 len(input_ids) >= max_length 的比例。
    触顶表示该条在 max_length 处被截断，可用于回答审稿人关于长叙事比例的问题。
    """
    # QiDeBERTa 等自定义 tokenizer 默认 return_tensors='pt'，未 padding 批量会报错
    ids_list: list = []
    for q, c in zip(qs, cs):
        enc = tokenizer(
            q,
            c,
            truncation="only_second",
            max_length=max_length,
            padding=False,
            return_tensors=None,
        )
        ids_list.append(enc["input_ids"])
    n = len(ids_list)
    if n == 0:
        print(f"[截断统计] {label}: 无样本")
        return 0.0, 0, 0
    n_at_cap = sum(1 for ids in ids_list if len(ids) >= max_length)
    frac = n_at_cap / n
    print(
        f"[截断统计] {label}: 触 max_length={max_length} 的条数 {n_at_cap}/{n} "
        f"({100.0 * frac:.2f}%) — 视为可能被截断（仅第二段优先截断策略下）"
    )
    return frac, n_at_cap, n


def coerce_task_label_columns(df: pd.DataFrame, task_names: list[str]) -> None:
    """将 A* 列转为 int；无法解析且原单元非空的记为 0 并打印警告（便于区分脏数据与真缺失）。"""
    for c in task_names:
        if c not in df.columns:
            raise ValueError(f"缺少列 {c}")
        numeric = pd.to_numeric(df[c], errors="coerce")
        bad = numeric.isna() & df[c].notna()
        n_bad = int(bad.sum())
        if n_bad:
            print(
                f"警告: 列 {c} 有 {n_bad} 个无法解析为数值的非空条目，已当作 0；"
                "若为标注缺失请在数据侧显式编码，勿依赖静默转换。"
            )
        df[c] = numeric.fillna(0).astype(int)


def split_train_val_test_by_participant(
    df: pd.DataFrame,
    seed: int,
    participant_col: str = "participant_id",
    test_ratio: float = 0.2,
    val_ratio_of_rest: float = 0.125,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    按 participant 分组划分，避免同一儿童同时出现在 train/test（推荐用于 narratives.csv）。
    若缺少 participant_col 则退回 split_train_val_test_70_10_20。
    默认约 70% / 10% / 20% 叙事条数（按 participant 组切分）。
    """
    if participant_col not in df.columns:
        print(f"警告: 无 {participant_col} 列，退回按 story_type 行级划分。")
        return split_train_val_test_70_10_20(df, seed)

    from sklearn.model_selection import GroupShuffleSplit

    groups = df[participant_col].astype(str)
    n_part = groups.nunique()
    if n_part < 5:
        print(f"警告: participant 仅 {n_part} 组，退回行级划分。")
        return split_train_val_test_70_10_20(df, seed)

    gss_test = GroupShuffleSplit(n_splits=1, test_size=test_ratio, random_state=seed)
    train_val_idx, test_idx = next(gss_test.split(df, groups=groups))
    train_val_df = df.iloc[train_val_idx]
    test_df = df.iloc[test_idx]
    gss_val = GroupShuffleSplit(n_splits=1, test_size=val_ratio_of_rest, random_state=seed + 1)
    tr_idx, val_idx = next(gss_val.split(train_val_df, groups=train_val_df[participant_col]))
    train_df = train_val_df.iloc[tr_idx].reset_index(drop=True)
    val_df = train_val_df.iloc[val_idx].reset_index(drop=True)
    test_df = test_df.reset_index(drop=True)
    print(
        f"划分(按 {participant_col}): 训练 {len(train_df)} | 验证 {len(val_df)} | 测试 {len(test_df)} "
        f"(participant 组: train={train_val_df.iloc[tr_idx][participant_col].nunique()}, "
        f"val={train_val_df.iloc[val_idx][participant_col].nunique()}, "
        f"test={test_df[participant_col].nunique()})"
    )
    return train_df, val_df, test_df


def split_train_val_test_70_10_20(
    df: pd.DataFrame, seed: int, stratify_col: str = "story_type"
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """70% / 10% / 20% 划分；优先按 stratify_col 分层，失败则退回随机划分并打印原因。"""
    try:
        train_df, rest_df = train_test_split(
            df, test_size=0.30, random_state=seed, stratify=df[stratify_col]
        )
        val_df, test_df = train_test_split(
            rest_df, test_size=2 / 3, random_state=seed, stratify=rest_df[stratify_col]
        )
    except ValueError as e:
        print(f"警告: 分层划分不可用 ({e})，退回无分层划分。")
        train_df, rest_df = train_test_split(df, test_size=0.30, random_state=seed)
        val_df, test_df = train_test_split(rest_df, test_size=2 / 3, random_state=seed)
    return (
        train_df.reset_index(drop=True),
        val_df.reset_index(drop=True),
        test_df.reset_index(drop=True),
    )


def build_pair_dataloader(
    qs: list,
    cs: list,
    lbs: list,
    task_idx: list[int],
    tokenizer,
    batch_size: int,
    shuffle: bool,
    max_length: int = 512,
    num_tasks: int = 15,
) -> DataLoader:
    enc = tokenizer(
        qs,
        cs,
        padding=True,
        truncation="only_second",
        max_length=max_length,
        return_tensors="pt",
    )
    if not (len(qs) == len(cs) == len(lbs) == len(task_idx)):
        raise ValueError("qs/cs/labels/task_idx 长度不一致")
    n = len(lbs)
    if n % num_tasks != 0:
        raise ValueError(
            f"展开样本数 {n} 不是 num_tasks={num_tasks} 的整数倍，步进切片评估将错误"
        )
    labels_t = torch.tensor(lbs, dtype=torch.float32).reshape(-1, 1)
    tid_t = torch.tensor(task_idx, dtype=torch.long)
    tti = enc.get("token_type_ids")
    if tti is None:
        tti = torch.zeros_like(enc["input_ids"])
    ds = TensorDataset(enc["input_ids"], enc["attention_mask"], tti, labels_t, tid_t)
    sampler = RandomSampler(ds) if shuffle else SequentialSampler(ds)
    return DataLoader(ds, sampler=sampler, batch_size=batch_size)


def pos_weight_per_task(
    labels: list, task_idx: list[int], num_tasks: int, device: torch.device
) -> torch.Tensor:
    """对每个任务 j 单独用 neg/pos 比（无 clip），与 STL 每对一标签框架一致。"""
    assert len(labels) == len(task_idx)
    vec = []
    for j in range(num_tasks):
        ys = [int(y) for y, t in zip(labels, task_idx) if t == j]
        if not ys:
            vec.append(1.0)
            continue
        pos = sum(ys)
        neg = len(ys) - pos
        vec.append(neg / (pos + 1e-9))
    return torch.tensor(vec, device=device, dtype=torch.float32)


def evaluate_stride_macro_f1(
    model, dataloader: DataLoader, device: torch.device, num_tasks: int
) -> tuple[float, float, list[float]]:
    """
    在 **SequentialSampler、且样本按「每条叙事连续 15 任务」展开** 的 loader 上计算 macro-F1。
    使用 labels_flat[i::num_tasks]；若将本函数用于 shuffle=True 的 DataLoader，结果无意义。
    """
    model.to(device)
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in dataloader:
            ids, mask, tti, labels, _tids = [b.to(device) for b in batch]
            logits = model(ids, mask, tti)
            all_preds.append(torch.sigmoid(logits).cpu().numpy())
            all_labels.append(labels.cpu().numpy())
    preds_flat = np.concatenate(all_preds).ravel()
    labels_flat = np.concatenate(all_labels).ravel()
    if len(labels_flat) % num_tasks != 0:
        raise RuntimeError(
            f"评估集长度 {len(labels_flat)} 不是 num_tasks={num_tasks} 的整数倍"
        )
    preds_bin = (preds_flat > 0.5).astype(int)
    per_task_f1 = []
    for i in range(num_tasks):
        t_labels = labels_flat[i::num_tasks]
        t_preds = preds_bin[i::num_tasks]
        per_task_f1.append(f1_score(t_labels, t_preds, average="binary", zero_division=0))
    return float(np.mean(per_task_f1)), float(accuracy_score(labels_flat, preds_bin)), per_task_f1


def _build_optimizer_param_groups(
    model: nn.Module, base_lr: float, opts: M4TrainOptions
) -> list[dict]:
    """分组 LR：LoRA 适配器、分类头、其余（若有）。"""
    lora_params, head_params, other_params = [], [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        if "lora_" in name:
            lora_params.append(param)
        elif name.startswith("inner_layer.") or name.startswith("classifier."):
            head_params.append(param)
        else:
            other_params.append(param)

    if opts.head_learning_rate is None:
        return [{"params": model.parameters(), "lr": base_lr}]

    lora_lr = opts.lora_learning_rate if opts.lora_learning_rate is not None else base_lr
    groups: list[dict] = []
    if lora_params:
        groups.append({"params": lora_params, "lr": lora_lr})
    if head_params:
        groups.append({"params": head_params, "lr": opts.head_learning_rate})
    if other_params:
        groups.append({"params": other_params, "lr": base_lr})
    return groups


def _linear_warmup_decay_scheduler(optimizer, num_training_steps: int, warmup_ratio: float):
    warmup_steps = max(1, int(num_training_steps * warmup_ratio))

    def lr_lambda(step: int) -> float:
        if step < warmup_steps:
            return float(step) / float(warmup_steps)
        return max(
            0.0,
            float(num_training_steps - step)
            / float(max(1, num_training_steps - warmup_steps)),
        )

    return LambdaLR(optimizer, lr_lambda)


def train_multitask_bce(
    model,
    train_loader: DataLoader,
    val_loader: DataLoader,
    epochs: int,
    lr: float,
    device: torch.device,
    pos_w_per_task: torch.Tensor,
    weights_path: str,
    patience: int,
    num_tasks: int,
    train_options: M4TrainOptions | None = None,
) -> float:
    """按 batch 内 task_id 取对应 pos_weight，对 BCE 逐样本加权后取均值。"""
    opts = train_options or M4TrainOptions()
    model.to(device)
    param_groups = _build_optimizer_param_groups(model, lr, opts)
    optimizer = AdamW(param_groups, lr=lr, weight_decay=opts.weight_decay)
    total_steps = max(epochs * len(train_loader), 1)
    scheduler = None
    if opts.warmup_ratio > 0:
        scheduler = _linear_warmup_decay_scheduler(optimizer, total_steps, opts.warmup_ratio)
    best_f1 = -1.0
    patience_counter = 0
    global_step = 0
    pw = pos_w_per_task.detach().cpu().numpy()
    print(
        f"\n开始训练 | 按任务 pos_weight ({num_tasks}): min={pw.min():.3f} max={pw.max():.3f} | "
        f"patience={patience} | {opts.describe(lr)}"
    )

    for epoch in range(epochs):
        model.train()
        total_loss = 0.0
        for batch in tqdm(train_loader, desc=f"Epoch {epoch + 1}/{epochs}", leave=False):
            ids, mask, tti, labels, tids = [b.to(device) for b in batch]
            optimizer.zero_grad()
            logits = model(ids, mask, tti)
            pw_b = pos_w_per_task[tids].unsqueeze(1)
            loss = F.binary_cross_entropy_with_logits(logits, labels, pos_weight=pw_b).mean()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), opts.max_grad_norm)
            optimizer.step()
            if scheduler is not None:
                scheduler.step()
            global_step += 1
            total_loss += loss.item()

        n_batches = max(len(train_loader), 1)
        avg_loss = total_loss / n_batches
        f1, acc, _ = evaluate_stride_macro_f1(model, val_loader, device, num_tasks)
        lr_now = optimizer.param_groups[0]["lr"]
        print(
            f"Epoch {epoch + 1}/{epochs} | 训练 Loss: {avg_loss:.4f} | "
            f"验证 Macro-F1: {f1:.4f} | 验证展平 Acc: {acc:.4f} | lr≈{lr_now:.2e}"
        )

        if f1 > best_f1:
            best_f1 = f1
            torch.save(model.state_dict(), weights_path)
            print(f"  → 最佳验证 Macro-F1 更新为 {best_f1:.4f}，已保存: {weights_path}")
            patience_counter = 0
        else:
            patience_counter += 1
            print(f"  → 验证 F1 未提升 ({patience_counter}/{patience})")
            if patience_counter >= patience:
                print(f"早停：已连续 {patience} 个 epoch 无提升。")
                break

    return best_f1
