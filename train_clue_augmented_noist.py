# train_clue_augmented_noIST.py
# 实验 B：保留问题模板，移除 IST Words
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

warnings.filterwarnings("ignore")

# 问题模板 (本实验需要保留)
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
        "A15": "你觉得小猫最终成功得到鱼了吗？从哪些地方可以看出？？",
        "A16": "得到鱼后，你觉得小猫的情绪反应可能是怎样的？为什么？"
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
        "A10": "男孩最终拿回了球/气球，你认为这个结果对他意味着什么？",
        "A11": "拿回气球后，你觉得男孩的情绪可能是怎样的？为什么？",
        "A12": "第三个事件中，小狗为什么会想要得到香肠？可能是什么激发了它的行为？",
        "A13": "在关于香肠的事件中，小狗可能真正想要的是什么？",
        "A14": "小狗为了得到香肠，可能采取了哪些行动？你觉得它为什么选择这样做？",
        "A15": "小狗拿香肠的行动最终带来了什么结果？你觉得它成功了吗？",
        "A16": "你觉得小狗最终成功得到香肠了吗？从哪些地方可以看出？"
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
        "A16": "小鸟获救后，你觉得小狗、小猫、小鸟和鸟妈妈各自可能会有怎样的情绪？为什么？"
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
        "A16": "小羊被小鸟救下后，你觉得小鸟、狐狸、小羊和羊妈妈各自可能会有怎样的情绪？为什么？"
    }
}

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
    print("\n--- 开始训练【实验B：移除IST线索】(MPS支持版) ---")
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
            torch.save(model.state_dict(), "model_no_ist_best.pth")
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

# --- 核心改动：保留 Question，移除 IST Words ---
def create_dataset_no_ist(df, task_names, question_templates):
    expanded_texts, expanded_labels = [], []
    for index, row in df.iterrows():
        original_text = row['text']
        story_type = row['story_type']
        
        # 本实验不读取 ist_words

        if story_type in question_templates:
            for task_name in task_names:
                question = question_templates[story_type][task_name]
                # 输入格式：问题：... 叙事：... (没有线索)
                new_text = f"问题：{question} 叙事：{original_text}"
                expanded_texts.append(new_text)
                label = row[task_name]
                expanded_labels.append(label)
    return expanded_texts, expanded_labels

if __name__ == "__main__":
    file_path = 'narratives.csv'
    df = pd.read_csv(file_path)
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)
    # 不处理 ist_words

    print("开始划分原始数据集...")
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=42)
    TASK_NAMES = [f'A{i}' for i in range(2, 17)]
    
    print("开始为训练集生成数据 (No IST)...")
    train_texts, train_labels = create_dataset_no_ist(train_df, TASK_NAMES, QUESTION_TEMPLATES)
    
    print("开始为测试集生成数据 (No IST)...")
    test_texts, test_labels = create_dataset_no_ist(test_df, TASK_NAMES, QUESTION_TEMPLATES)
    
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
    final_model.load_state_dict(torch.load("model_no_ist_best.pth", map_location=device))
    
    final_f1, final_acc, per_task_scores = evaluate(final_model, test_dataloader, device)
    
    print("\n" + "="*40)
    print("实验B (No IST) 最终评估结果")
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