import pandas as pd
import torch
import torch.nn as nn
import numpy as np
import warnings
import argparse
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from transformers import AutoTokenizer, AutoModel, get_linear_schedule_with_warmup
from torch.optim import AdamW
from peft import LoraConfig, get_peft_model

warnings.filterwarnings("ignore")

# ==============================================================================
# 1. 模型定义与评估函数 (这部分无需修改)
# ==============================================================================

class SingleTaskClassifier(nn.Module):
    """
    带 LoRA 的单任务分类器模型。
    """
    def __init__(self, model_name, use_peft=True):
        super(SingleTaskClassifier, self).__init__()
        bert_model = AutoModel.from_pretrained(model_name)
        
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

def evaluate_model(model, dataloader, device):
    """
    在验证集或测试集上评估模型性能。
    返回: F1 分数
    """
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Evaluating"):
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask)
            probabilities = torch.sigmoid(outputs)
            predictions = (probabilities > 0.5).cpu().numpy().astype(int)
            labels_batch = labels.cpu().numpy().astype(int)
            all_preds.append(predictions)
            all_labels.append(labels_batch)

    all_preds = np.concatenate(all_preds, axis=0)
    all_labels = np.concatenate(all_labels, axis=0)
    f1 = f1_score(all_labels, all_preds, zero_division=0)
    return f1

# ==============================================================================
# 2. 主训练流程函数 (修改以接受 task_name)
# ==============================================================================

def train_single_expert(args, task_name, texts, tokenizer):
    """
    为单个指定任务训练专家模型的主流程函数。
    """
    # --- 设备设置 ---
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # --- 数据加载与预处理 ---
    print(f"Loading labels for task: {task_name}")
    df = pd.read_csv(args.data_path) # 重新加载以确保数据清洁
    if task_name not in df.columns:
        raise ValueError(f"Error: Column '{task_name}' not found in {args.data_path}.")
    
    labels_np = df[task_name].values.reshape(-1, 1)
    
    # --- 计算类别权重 ---
    num_neg = (labels_np == 0).sum()
    num_pos = (labels_np == 1).sum()
    pos_weight_value = num_neg / num_pos if num_pos > 0 else 1.0
    pos_weight = torch.tensor([pos_weight_value], dtype=torch.float32).to(device)
    print(f"Calculated pos_weight for task {task_name}: {pos_weight_value:.4f}")

    # --- Tokenization ---
    # 文本已经被预先 tokenize，这里只编码标签
    encoded_data = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='pt')
    input_ids = encoded_data['input_ids']
    attention_mask = encoded_data['attention_mask']
    labels = torch.tensor(labels_np, dtype=torch.float32)

    # --- 数据划分与 DataLoader 创建 ---
    train_idx, val_idx = train_test_split(range(len(input_ids)), test_size=0.1, random_state=42, stratify=labels)
    
    train_data = TensorDataset(input_ids[train_idx], attention_mask[train_idx], labels[train_idx])
    val_data = TensorDataset(input_ids[val_idx], attention_mask[val_idx], labels[val_idx])
    
    train_dataloader = DataLoader(train_data, sampler=RandomSampler(train_data), batch_size=args.batch_size)
    val_dataloader = DataLoader(val_data, sampler=SequentialSampler(val_data), batch_size=args.batch_size)

    # --- 模型、优化器、损失函数和调度器初始化 ---
    print(f"\n--- Initializing model for task: {task_name} ---")
    model = SingleTaskClassifier(args.model_name, use_peft=True)
    model.to(device)
    model.bert.print_trainable_parameters()

    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = AdamW(model.parameters(), lr=args.learning_rate, eps=1e-8)
    
    total_steps = len(train_dataloader) * args.epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)
    
    scaler = torch.cuda.amp.GradScaler(enabled=torch.cuda.is_available())
    best_f1 = -1
    
    # --- 训练循环 ---
    for epoch in range(args.epochs):
        model.train()
        total_loss = 0
        for batch in tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{args.epochs}"):
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            optimizer.zero_grad()
            
            with torch.cuda.amp.autocast(enabled=torch.cuda.is_available()):
                outputs = model(input_ids, attention_mask)
                loss = criterion(outputs, labels)

            scaler.scale(loss).backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()
            total_loss += loss.item()
        
        avg_loss = total_loss / len(train_dataloader)
        print(f"Epoch {epoch+1} finished, average training loss: {avg_loss:.4f}")
        
        print("Evaluating on validation set...")
        current_f1 = evaluate_model(model, val_dataloader, device)
        print(f"Validation F1 Score: {current_f1:.4f}")
        
        if current_f1 > best_f1:
            best_f1 = current_f1
            output_path = f"{args.model_name.replace('/', '_')}_expert_{task_name}_best.pth"
            torch.save(model.state_dict(), output_path)
            print(f"Best model for {task_name} found! Weights saved to {output_path}. Best F1: {best_f1:.4f}")
    
    print(f"\nTraining for expert model {task_name} complete. Best validation F1: {best_f1:.4f}")


# ==============================================================================
# 3. 主脚本流程 (修改为循环执行任务)
# ==============================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Expert Models for a list of tasks (A6, A13, A16)")
    
    # 这些参数将应用于所有任务的训练
    parser.add_argument("--model_name", type=str, default="bert-base-chinese", help="Name of the pretrained model from Hugging Face.")
    parser.add_argument("--data_path", type=str, default="narratives.csv", help="Path to the training data CSV file.")
    parser.add_argument("--epochs", type=int, default=20, help="Number of training epochs for each task.")
    parser.add_argument("--batch_size", type=int, default=10, help="Training batch size for each task.")
    parser.add_argument("--learning_rate", type=float, default=2e-5, help="Learning rate for the optimizer for each task.")

    args = parser.parse_args()
    
    # 核心修改：定义要训练的任务列表
    tasks_to_train = ["A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14", "A15", "A16"]
    
    # 优化：预先加载文本和分词器，避免在循环中重复操作
    print("Pre-loading text data and tokenizer...")
    main_df = pd.read_csv(args.data_path)
    texts = main_df[main_df.columns[1]].astype(str).tolist()
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    
    # 循环遍历任务列表，为每个任务训练一个模型
    for task in tasks_to_train:
        print(f"\n{'='*30} Starting Training for Task: {task} {'='*30}")
        # 调用训练函数，传入当前任务的名称
        train_single_expert(args, task_name=task, texts=texts, tokenizer=tokenizer)
        print(f"\n{'='*30} Finished Training for Task: {task} {'='*30}")

    print("\nAll expert models have been trained successfully!")