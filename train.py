# ======================================================================================
# train_unified_final.py
# 最終統一版腳本
# --------------------------------------------------------------------------------------
# 本腳本為最終的、最穩健的版本，整合了所有優化策略和評估指標。
# 其數據加載邏輯經過特殊設計，可以安全地處理兩種情況：
#   1. 欄位乾淨的CSV文件（僅包含文本和A2-A16標籤）。
#   2. 包含任意多餘無關欄位的複雜CSV文件。
# 您只需使用這一個腳本，即可應對您的兩種數據集。
# ======================================================================================

# 1. 導入所需庫
# ==============================================================================
import pandas as pd
import torch
import torch.nn as nn
import numpy as np
import warnings
import os
import random
from sklearn.model_selection import KFold
from torch.utils.data import TensorDataset, DataLoader, SequentialSampler, RandomSampler
from transformers import AutoTokenizer, AutoModel, get_linear_schedule_with_warmup
from torch.optim import AdamW
import torch.nn.functional as F
from tqdm import tqdm
from sklearn.metrics import f1_score, fbeta_score, accuracy_score, precision_score, recall_score, mean_squared_error
from scipy.stats import pearsonr
from peft import LoraConfig, get_peft_model

warnings.filterwarnings("ignore")

# ==============================================================================
# 0. 最終超參數配置 (Final Hyperparameter Configuration)
# ==============================================================================
CONFIG = {
    # --- 核心模型與數據 ---
    "model_name": "hfl/chinese-bert-wwm-ext",
    "data_path": "narratives.csv",  # 將您的數據文件命名為這個，或修改此路徑
    
    # --- 訓練超參數 ---
    "epochs": 15,
    "lr": 2e-5,
    "weight_decay": 0.01,
    "batch_size": 10,
    "gradient_accumulation_steps": 2, # 有效批大小為 10 * 2 = 20
    "max_length": 512,
    "dropout_rate": 0.3,
    "warmup_ratio": 0.1,
    
    # --- 核心優化策略 ---
    "loss_function": "bce",  # 預設為最穩定的'bce'。如果您確認Focal Loss在新數據上穩定，可以改回'focal'
    "f_beta": 0.5,           # beta < 1.0, 优化时更侧重精确率
    
    # --- K-Fold 與 早停 ---
    "n_splits": 5,
    "early_stopping_patience": 3,
    
    # --- 數據不平衡處理 ---
    "max_pos_weight": 20.0,

    # --- LoRA 參數 ---
    "lora_r": 16,
    "lora_alpha": 32,
    
    # --- 環境參數 ---
    "seed": 42,
    "device": torch.device("cuda" if torch.cuda.is_available() else "cpu"),
}

# ==============================================================================
# 1. Focal Loss 實現 (Focal Loss Implementation)
# ==============================================================================
class FocalLoss(nn.Module):
    def __init__(self, alpha=0.25, gamma=2, reduction='mean', pos_weight=None):
        super(FocalLoss, self).__init__()
        self.alpha = alpha; self.gamma = gamma; self.reduction = reduction; self.pos_weight = pos_weight
    def forward(self, inputs, targets):
        bce_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction='none', pos_weight=self.pos_weight)
        p = torch.sigmoid(inputs)
        pt = p * targets + (1 - p) * (1 - targets)
        epsilon = 1e-9
        pt = torch.clamp(pt, min=epsilon, max=1.0 - epsilon)
        alpha_factor = self.alpha * targets + (1 - self.alpha) * (1 - targets)
        focal_term = (1.0 - pt).pow(self.gamma)
        loss = alpha_factor * focal_term * bce_loss
        return loss.mean() if self.reduction == 'mean' else loss.sum()

# ==============================================================================
# 2. 輔助函數 (Utility Functions) & 模型定義 (Model Definition)
# ==============================================================================
def set_seed(seed_value):
    random.seed(seed_value); np.random.seed(seed_value); torch.manual_seed(seed_value)
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(seed_value); torch.backends.cudnn.deterministic = True; torch.backends.cudnn.benchmark = False

class MultiClassifier(nn.Module):
    def __init__(self, config):
        super(MultiClassifier, self).__init__()
        bert_model = AutoModel.from_pretrained(config['model_name'])
        lora_config = LoraConfig(r=config['lora_r'], lora_alpha=config['lora_alpha'], lora_dropout=0.1, target_modules=['query', 'key', 'value'])
        self.bert = get_peft_model(bert_model, lora_config)
        self.inner_layer = nn.Linear(self.bert.config.hidden_size, self.bert.config.hidden_size)
        self.dropout = nn.Dropout(config['dropout_rate'])
        self.classifiers = nn.ModuleList([nn.Linear(self.bert.config.hidden_size, 1) for _ in range(15)])
    
    def forward(self, input_ids, attention_mask):
        bert_output = self.bert(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        attention_mask_expanded = attention_mask.unsqueeze(-1).expand(bert_output.size()).float()
        sum_embeddings = torch.sum(bert_output * attention_mask_expanded, 1)
        sum_mask = torch.clamp(attention_mask_expanded.sum(1), min=1e-9)
        pooled_output = sum_embeddings / sum_mask
        x = self.dropout(pooled_output); x = F.relu(self.inner_layer(x)); x = self.dropout(x)
        return torch.stack([self.classifiers[i](x) for i in range(15)], dim=1)

# ==============================================================================
# 3. 數據加載與預處理 (Data Loading & Preprocessing) - [核心魯棒邏輯]
# ==============================================================================
def load_and_preprocess_data(config, tokenizer):
    print("--- 1. 加載和預處理數據 (統一魯棒版) ---")
    
    label_columns = [f'A{i}' for i in range(2, 17)]
    try:
        csv_columns = pd.read_csv(config['data_path'], nrows=0).columns
        text_column = csv_columns[0]
        required_columns = [text_column] + label_columns
        
        # 檢查所需欄位是否存在
        if not all(col in csv_columns for col in required_columns):
            print(f"錯誤: CSV文件 '{config['data_path']}' 中缺少必要的欄位。")
            print(f"需要的欄位: {required_columns}")
            return None, None, None, None

    except FileNotFoundError:
        print(f"錯誤: 找不到數據文件 '{config['data_path']}'")
        return None, None, None, None
    except Exception as e:
        print(f"讀取CSV文件時出錯: {e}")
        return None, None, None, None

    print(f"將只讀取以下欄位: {required_columns}")
    df = pd.read_csv(config['data_path'], usecols=required_columns)
    
    df.rename(columns={text_column: 'text'}, inplace=True)

    for col in label_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        df[col] = df[col].astype(int)

    texts = df['text'].astype(str).tolist()
    labels_np = df[label_columns].values
    
    num_neg = (labels_np == 0).sum(axis=0)
    num_pos = (labels_np == 1).sum(axis=0)
    epsilon = 1e-9
    pos_weight_np = num_neg / (num_pos + epsilon) 
    pos_weight_np = np.clip(pos_weight_np, a_min=1.0, a_max=config['max_pos_weight'])
    pos_weight_tensor = torch.tensor(pos_weight_np, dtype=torch.float32)
    print("計算出的pos_weight:", pos_weight_tensor)
    
    encoded_data = tokenizer(texts, padding=True, truncation=True, max_length=config['max_length'], return_tensors='pt')
    print(f"數據加載完成。樣本數: {len(texts)}")
    return encoded_data['input_ids'], encoded_data['attention_mask'], torch.tensor(labels_np, dtype=torch.float32), pos_weight_tensor

# ==============================================================================
# 4. 評估與訓練函數 (Evaluation & Training Functions) - [包含RMSE和Pearson's r]
# ==============================================================================
def find_best_thresholds(y_true, y_proba, beta=1.0):
    best_thresholds = np.zeros(y_true.shape[1])
    for i in range(y_true.shape[1]):
        best_f_score = -1
        for threshold in np.arange(0.1, 0.9, 0.01):
            preds = (y_proba[:, i] > threshold).astype(int)
            f_score = fbeta_score(y_true[:, i], preds, beta=beta, zero_division=0)
            if f_score > best_f_score:
                best_f_score = f_score; best_thresholds[i] = threshold
    return best_thresholds

def evaluate(model, dataloader, device, beta=1.0, best_thresholds=None):
    model.to(device); model.eval()
    all_probs, all_labels_list = [], []
    with torch.no_grad():
        for batch in dataloader:
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask).squeeze(2)
            all_probs.append(torch.sigmoid(outputs).cpu().numpy())
            all_labels_list.append(labels.cpu().numpy())
    all_probs = np.concatenate(all_probs, axis=0)
    all_labels = np.concatenate(all_labels_list, axis=0).astype(int)

    if best_thresholds is None:
        best_thresholds = find_best_thresholds(all_labels, all_probs, beta=beta)
    
    all_preds = (all_probs > best_thresholds).astype(int)
    
    predicted_scores = np.sum(all_preds, axis=1)
    actual_scores = np.sum(all_labels, axis=1)
    
    rmse = np.sqrt(mean_squared_error(actual_scores, predicted_scores))
    
    if np.std(actual_scores) > 0 and np.std(predicted_scores) > 0:
        pearson_r, _ = pearsonr(actual_scores, predicted_scores)
    else:
        pearson_r = 0.0

    per_task_f1 = f1_score(all_labels, all_preds, average=None, zero_division=0)
    
    avg_metrics = {
        "rmse": rmse,
        "pearson_r": pearson_r,
        "macro_f_beta": np.mean(fbeta_score(all_labels, all_preds, beta=beta, average=None, zero_division=0)),
        "macro_f1": np.mean(per_task_f1),
        "macro_precision": np.mean(precision_score(all_labels, all_preds, average=None, zero_division=0)),
        "macro_recall": np.mean(recall_score(all_labels, all_preds, average=None, zero_division=0)),
    }
    per_task_metrics = {"f1": per_task_f1}
    return avg_metrics, best_thresholds, per_task_metrics

def train_one_fold(config, fold, train_dataloader, val_dataloader, pos_weight):
    print(f"\n--- [Fold {fold+1}/{config['n_splits']}] 開始訓練 ---")
    model = MultiClassifier(config); model.to(config['device'])
    if config['loss_function'] == 'focal':
        criterion = FocalLoss(pos_weight=pos_weight.to(config['device'])); print("使用 Focal Loss")
    else:
        criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight.to(config['device'])); print("使用 BCEWithLogitsLoss")
    optimizer = AdamW(model.parameters(), lr=config['lr'], weight_decay=config['weight_decay'])
    total_steps = len(train_dataloader) // config['gradient_accumulation_steps'] * config['epochs']
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=int(total_steps * config['warmup_ratio']), num_training_steps=total_steps)
    best_eval_score = -1; best_thresholds = None; patience_counter = 0
    weights_path = f"fold_{fold+1}_best_weights.pth"
    for epoch in range(config['epochs']):
        model.train(); total_loss = 0; optimizer.zero_grad()
        for step, batch in enumerate(tqdm(train_dataloader, desc=f"Fold {fold+1} Epoch {epoch+1}", leave=False)):
            input_ids, attention_mask, labels = [b.to(config['device']) for b in batch]
            outputs = model(input_ids, attention_mask).squeeze(2)
            loss = criterion(outputs, labels) / config['gradient_accumulation_steps']
            if torch.isnan(loss): print("\n錯誤: 損失值為NaN，訓練中斷。"); return None, None
            loss.backward()
            if (step + 1) % config['gradient_accumulation_steps'] == 0:
                nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step(); scheduler.step(); optimizer.zero_grad()
            total_loss += loss.item() * config['gradient_accumulation_steps']
        print(f"Epoch {epoch+1} 完成, 平均訓練損失: {total_loss / len(train_dataloader):.4f}")
        avg_metrics, current_thresholds, _ = evaluate(model, val_dataloader, config['device'], beta=config['f_beta'])
        eval_score = avg_metrics['macro_f_beta']
        print(f"驗證集 -> F-beta: {eval_score:.4f} | P: {avg_metrics['macro_precision']:.4f} | R: {avg_metrics['macro_recall']:.4f} | RMSE: {avg_metrics['rmse']:.4f} | Pearson's r: {avg_metrics['pearson_r']:.4f}")
        if eval_score > best_eval_score:
            best_eval_score = eval_score; best_thresholds = current_thresholds; patience_counter = 0
            torch.save(model.state_dict(), weights_path); print(f"Fold {fold+1} 找到更優模型 (F-beta: {best_eval_score:.4f})，權重和閾值已更新。")
        else:
            patience_counter += 1
            if patience_counter >= config['early_stopping_patience']: print(f"驗證集F-beta連續{patience_counter}輪未提升，觸發早停。"); break
    print(f"\n--- [Fold {fold+1}] 訓練完成，加載最佳模型 ---")
    model.load_state_dict(torch.load(weights_path))
    final_avg_metrics, _, final_per_task_metrics = evaluate(model, val_dataloader, config['device'], beta=config['f_beta'], best_thresholds=best_thresholds)
    os.remove(weights_path)
    return final_avg_metrics, final_per_task_metrics

# ==============================================================================
# 5. 主執行流程 (Main Execution)
# ==============================================================================
if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    set_seed(CONFIG['seed'])
    print(f"使用設備: {CONFIG['device']}")
    print(f"使用最終基線配置: {CONFIG}")
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
    all_input_ids, all_attention_mask, all_labels, pos_weight = load_and_preprocess_data(CONFIG, tokenizer)
    if all_input_ids is not None:
        dataset = TensorDataset(all_input_ids, all_attention_mask, all_labels)
        kf = KFold(n_splits=CONFIG['n_splits'], shuffle=True, random_state=CONFIG['seed'])
        all_folds_avg_metrics, all_folds_per_task_metrics = [], []
        print(f"\n--- 2. 開始 {CONFIG['n_splits']}-折交叉驗證 ---")
        for fold, (train_idx, val_idx) in enumerate(kf.split(dataset)):
            train_subset = torch.utils.data.Subset(dataset, train_idx); val_subset = torch.utils.data.Subset(dataset, val_idx)
            train_dataloader = DataLoader(train_subset, sampler=RandomSampler(train_subset), batch_size=CONFIG['batch_size'])
            val_dataloader = DataLoader(val_subset, sampler=SequentialSampler(val_subset), batch_size=CONFIG['batch_size'])
            avg_metrics, per_task_metrics = train_one_fold(CONFIG, fold, train_dataloader, val_dataloader, pos_weight)
            if avg_metrics and per_task_metrics:
                all_folds_avg_metrics.append(avg_metrics); all_folds_per_task_metrics.append(per_task_metrics)
        if all_folds_avg_metrics:
            print("\n\n--- 交叉驗證最終評估結果 (所有折的平均指標) ---")
            summary = {metric: [m[metric] for m in all_folds_avg_metrics] for metric in all_folds_avg_metrics[0]}
            print("指標            |  平均值   |  標準差"); print("----------------|-----------|-----------")
            for metric, values in summary.items():
                print(f"{metric.upper():<15} |  {np.mean(values):.4f}   |  {np.std(values):.4f}")
        if all_folds_per_task_metrics:
            print("\n\n--- 交叉驗證最終評估結果 (各任務平均F1分數) ---")
            per_task_f1_matrix = np.array([m['f1'] for m in all_folds_per_task_metrics])
            mean_f1_per_task = np.mean(per_task_f1_matrix, axis=0)
            print("任務 | 平均 F1 分數"); print("-----|--------------")
            for i, mean_f1 in enumerate(mean_f1_per_task):
                print(f"A{i+2:<3} | {mean_f1:.4f}")