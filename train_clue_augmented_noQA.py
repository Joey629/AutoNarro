# train_clue_augmented_noQA.py
# 实验 A：移除自然语言问题，仅保留任务ID
# 适配：Apple M4 Pro (MPS), Batch Size=10

import pandas as pd
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
import numpy as np
from torch.optim import AdamW
from sklearn.metrics import f1_score, accuracy_score
from peft import LoraConfig, get_peft_model
import warnings

# 过滤警告
warnings.filterwarnings("ignore")

class ClueAugmentedQAModel(nn.Module):
    def __init__(self, bert_model, use_peft=True):
        super(ClueAugmentedQAModel, self).__init__()
        if use_peft:
            lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=['query', 'key', 'value'])
            self.bert = get_peft_model(bert_model, lora_config)
        else:
            self.bert = bert_model
        self.inner_layer = nn.Linear(self.bert.config.hidden_size, 768)
        self.dropout = nn.Dropout(0.5)
        self.classifier = nn.Linear(768, 1)
        
    def forward(self, input_ids, attention_mask):
        bert_output = self.bert(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:, 0, :]
        x = self.dropout(bert_output)
        x = torch.nn.functional.relu(self.inner_layer(x))
        x = self.dropout(x)
        output = self.classifier(x)
        return output

def train(model, train_dataloader, val_dataloader, epochs, lr, device, pos_weight, patience=3):
    print("\n--- 开始训练【实验A：移除问题模板】(MPS支持版) ---")
    model.to(device)
    
    # 使用传入的 pos_weight
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = AdamW(model.parameters(), lr=lr)
    
    best_f1 = -1
    patience_counter = 0

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        # 训练循环
        for batch in tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{epochs}"):
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask)
            loss = criterion(outputs, labels)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_dataloader)
        print(f"Epoch {epoch+1} 完成, 平均训练损失: {avg_loss:.4f}")
        
        print("开始在验证集上评估...")
        f1, acc, _ = evaluate(model, val_dataloader, device)
        print(f"验证集 总体F1: {f1:.4f}, 总体准确率: {acc:.4f}")
        
        if f1 > best_f1:
            best_f1 = f1
            torch.save(model.state_dict(), "model_no_question_best.pth")
            print("当前为最佳模型，权重已保存。")
            patience_counter = 0
        else:
            patience_counter += 1
            print(f"验证集 F1 未提升，Patience 计数: {patience_counter}/{patience}")
            if patience_counter >= patience:
                print(f"已连续 {patience} 轮未在验证集上取得提升，触发 Early Stopping。")
                break

def evaluate(model, test_dataloader, device):
    model.to(device)
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in tqdm(test_dataloader, desc="评估中"):
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask)
            probabilities = torch.sigmoid(outputs)
            all_preds.append(probabilities.cpu().numpy())
            all_labels.append(labels.cpu().numpy())
            
    all_preds_flat = np.concatenate(all_preds, axis=0)
    all_labels_flat = np.concatenate(all_labels, axis=0)
    all_preds_binary_flat = np.where(all_preds_flat > 0.5, 1, 0)
    
    overall_f1 = f1_score(all_labels_flat, all_preds_binary_flat, average='binary', zero_division=0)
    overall_accuracy = accuracy_score(all_labels_flat, all_preds_binary_flat)
    
    # 计算各任务详细分数
    num_tasks = 15
    num_samples = len(all_labels_flat)
    per_task_f1_scores = []

    if num_samples > 0 and num_samples % num_tasks == 0:
        num_original_samples = num_samples // num_tasks
        all_labels_reshaped = all_labels_flat.reshape(num_original_samples, num_tasks)
        all_preds_binary_reshaped = all_preds_binary_flat.reshape(num_original_samples, num_tasks)
        for i in range(num_tasks):
            task_f1 = f1_score(all_labels_reshaped[:, i], all_preds_binary_reshaped[:, i], average='binary', zero_division=0)
            per_task_f1_scores.append(task_f1)
    
    return overall_f1, overall_accuracy, per_task_f1_scores

# --- 核心改动：仅使用 Task ID，移除 Question ---
def create_dataset_no_question(df, task_names):
    expanded_texts, expanded_labels = [], []
    for index, row in df.iterrows():
        original_text = row['text']
        ist_words = row.get('ist_words', '')
        if pd.isna(ist_words): ist_words = ''

        for task_name in task_names:
            # 输入格式：任务：A2 叙事：... 线索：... (无自然语言问题)
            new_text = f"任务：{task_name} 叙事：{original_text} 已知线索：{ist_words}"
            expanded_texts.append(new_text)
            label = row[task_name]
            expanded_labels.append(label)
    return expanded_texts, expanded_labels

if __name__ == "__main__":
    file_path = 'narratives.csv'
    df = pd.read_csv(file_path)
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)
    df['ist_words'] = df.get('ist_words', pd.Series(dtype=str)).fillna('')

    print("开始划分原始数据集...")
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=42)
    TASK_NAMES = [f'A{i}' for i in range(2, 17)]
    
    print("开始为训练集生成数据 (No Question)...")
    train_texts, train_labels = create_dataset_no_question(train_df, TASK_NAMES)
    
    print("开始为测试集生成数据 (No Question)...")
    test_texts, test_labels = create_dataset_no_question(test_df, TASK_NAMES)
    
    print("开始文本分词...")
    tokenizer = AutoTokenizer.from_pretrained('hfl/chinese-roberta-wwm-ext')
    train_encodings = tokenizer(train_texts, padding=True, truncation=True, max_length=512, return_tensors='pt')
    test_encodings = tokenizer(test_texts, padding=True, truncation=True, max_length=512, return_tensors='pt')

    train_labels_t = torch.tensor(train_labels, dtype=torch.float32).reshape(-1, 1)
    test_labels_t = torch.tensor(test_labels, dtype=torch.float32).reshape(-1, 1)

    train_data = TensorDataset(train_encodings['input_ids'], train_encodings['attention_mask'], train_labels_t)
    test_data = TensorDataset(test_encodings['input_ids'], test_encodings['attention_mask'], test_labels_t)
    
    # --- 严格保持原始参数 Batch Size = 10 ---
    batch_size = 10
    train_dataloader = DataLoader(train_data, sampler=RandomSampler(train_data), batch_size=batch_size)
    test_dataloader = DataLoader(test_data, sampler=SequentialSampler(test_data), batch_size=batch_size)
    print("DataLoader 创建成功！")

    # --- 设备检测 (增加 MPS 支持) ---
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(">>> 使用设备: CUDA (NVIDIA)")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        print(">>> 使用设备: MPS (Apple Silicon M4 Pro)")
    else:
        device = torch.device("cpu")
        print(">>> 使用设备: CPU")
    # -------------------------------

    # --- 计算 pos_weight (修复 float64 报错) ---
    num_pos = np.sum(np.array(train_labels) == 1)
    num_neg = np.sum(np.array(train_labels) == 0)
    # 必须指定 dtype=torch.float32
    pos_weight = torch.tensor([num_neg / (num_pos + 1e-9)], device=device, dtype=torch.float32)
    
    bert_base = AutoModel.from_pretrained("hfl/chinese-roberta-wwm-ext")
    model = ClueAugmentedQAModel(bert_base, use_peft=True)
    
    train(model, train_dataloader, test_dataloader, epochs=15, lr=2e-5, device=device, pos_weight=pos_weight)
    
    print("\n--- 载入最佳模型进行最终评估 ---")
    final_model = ClueAugmentedQAModel(AutoModel.from_pretrained("hfl/chinese-roberta-wwm-ext"), use_peft=True)
    final_model.load_state_dict(torch.load("model_no_question_best.pth", map_location=device))
    
    final_f1, final_acc, per_task_scores = evaluate(final_model, test_dataloader, device)
    
    print("\n" + "="*40)
    print("实验A (No Question) 最终评估结果")
    print("="*40)
    print(f"最佳验证集 总体F1 分数: {final_f1:.4f}")
    print(f"最佳验证集 总体准确率: {final_acc:.4f}")
    
    # --- 打印各任务详细分数 ---
    if per_task_scores:
        print("\n--- 各任务详细 F1 分数 ---")
        for i, score in enumerate(per_task_scores):
            print(f"任务 A{i+2}: {score:.4f}")
    else:
        print("\n[警告] 未能计算各任务详细分数 (可能是样本数无法被任务数整除)。")