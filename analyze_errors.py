# analyze_errors.py
# 多任务分类（A2–A16）错误分析：与 train_clue_augmented_model / train.py 兼容，可指定任务做详细错误分析。

import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader, SequentialSampler
from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
from peft import LoraConfig, get_peft_model
import os
import warnings
warnings.filterwarnings("ignore")

# ==============================================================================
# --- 1. 用户配置区 ---
# ==============================================================================
CONFIG = {
    'data_path': 'narratives.csv',
    'model_name': 'hfl/chinese-roberta-wwm-ext', # 确保与训练时一致
    'test_size': 0.2, # 使用20%的数据进行分析，若需全部数据设为1.0
    'batch_size': 16,
    
    # --- !!! [用户必须修改] ---
    # 请从训练脚本的输出中，复制粘贴【完整】的最佳模型文件名到这里
    'champion_model_path': 'best_model_20251001-111255_epoch10_macrof1_0.7067.pth',
    
    # --- [可选修改] ---
    'tasks_to_analyze': ['A6', 'A11', 'A13', 'A16'] # 您可以指定任何想分析的任务
}

# ==============================================================================
# --- 2. 核心组件与辅助函数 (与训练脚本完全同步) ---
# ==============================================================================
QUESTION_TEMPLATES = {
    'cat': { 'A2': "第一个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A3': "在追蝴蝶的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A4': "为了抓蝴蝶，小猫采取了什么行动？", 'A5': "小猫抓蝴蝶的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在抓蝴蝶失败后，猫和蝴蝶各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。", 'A8': "在拿球的事件中，男孩想要达成的目标或打算做的事情是什么？", 'A9': "为了拿回球，男孩采取了什么行动？", 'A10': "男孩拿球的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在拿回球后，男孩的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A13': "在关于鱼的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A14': "为了得到鱼，小猫采取了什么行动？", 'A15': "小猫拿鱼的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在得到鱼后，小猫的情绪反应是什么？", },
    'dog': { 'A2': "第一个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A3': "在追老鼠的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A4': "为了抓老鼠，小狗采取了什么行动？", 'A5': "小狗抓老鼠的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在抓老鼠失败后，小狗和老鼠各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。", 'A8': "在关于气球的事件中，男孩想要达成的目标或打算做的事情是什么？", 'A9': "为了拿回气球，男孩采取了什么行动？", 'A10': "男孩拿气球的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在拿回球后，男孩的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A13': "在关于香肠的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A14': "为了得到香肠，小狗采取了什么行动？", 'A15': "小狗拿香肠的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在得到香肠后，小狗的情绪反应是什么？", },
    'bird': { 'A2': "第一个事件的起因是什么？这包括鸟妈妈或小鸟的感受、想法或所看到的情境。", 'A3': "在喂食的事件中，鸟妈妈想要达成的目标或打算做的事情是什么？", 'A4': "为了喂小鸟，鸟妈妈采取了什么行动？", 'A5': "鸟妈妈找食物的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在喂食成功后，鸟妈妈和小鸟各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A8': "在抓小鸟的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A9': "为了抓小鸟，小猫采取了什么行动？", 'A10': "小猫抓小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在小猫抓到小鸟后，小猫和小鸟各自的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A13': "在救小鸟的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A14': "为了救小鸟，小狗采取了什么行动？", 'A15': "小鸟救小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在小鸟获救后，小狗、小猫、小鸟和鸟妈妈各自的情绪反应是什么？", },
    'goat': { 'A2': "第一个事件的起因是什么？这包括小羊或羊妈妈的感受、想法或所看到的情境。", 'A3': "在救小羊的事件中，羊妈妈想要达成的目标或打算做的事情是什么？", 'A4': "为了救小羊，羊妈妈采取了什么行动？", 'A5': "羊妈妈救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在小羊获救后，羊妈妈和小羊各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括狐狸的感受、想法或他所看到的情境。", 'A8': "在抓小羊的事件中，狐狸想要达成的目标或打算做的事情是什么？", 'A9': "为了抓小羊，狐狸采取了什么行动？", 'A10': "狐狸抓小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在狐狸抓到小羊后，狐狸和小羊各自的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小鸟的感受、想法或他所看到的情境。", 'A13': "在救小鳥的事件中，小鸟想要达成的目标或打算做的事情是什么？", 'A14': "为了救小羊，小鸟采取了什么行动？", 'A15': "小鸟救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在小羊被小鸟救下后，小鸟、狐狸、小羊和羊妈妈各自的情绪反应是什么？", }
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
        x = self.dropout(bert_output); x = torch.nn.functional.relu(self.inner_layer(x)); x = self.dropout(x)
        return self.classifier(x)
        
# ==============================================================================
# --- 3. 错误分析主流程 ---
# ==============================================================================
if __name__ == "__main__":
    if CONFIG['champion_model_path'] == 'PASTE_YOUR_BEST_MODEL_FILENAME_HERE.pth':
        print("\n错误: 请打开脚本，修改 CONFIG 中的 'champion_model_path' 为您训练得到的最佳模型文件名！")
        exit()

    # --- 数据和模型加载 ---
    df = pd.read_csv(CONFIG['data_path'])
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)
    if 'ist_words' not in df.columns: df['ist_words'] = ""
    df['ist_words'] = df['ist_words'].fillna('')
    
    TASK_NAMES = [f'A{i}' for i in range(2, 17)]
    for col in TASK_NAMES:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    if torch.backends.mps.is_available(): device = torch.device("mps")
    else: device = torch.device("cpu")

    tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
    bert_base = AutoModel.from_pretrained(CONFIG['model_name'])
    model = ClueAugmentedQAModel(bert_base, use_peft=True)
    
    try:
        model.load_state_dict(torch.load(CONFIG['champion_model_path'], map_location=device))
    except FileNotFoundError:
        print(f"错误: 模型权重文件 '{CONFIG['champion_model_path']}' 未找到。")
        exit()

    model.to(device); model.eval()

    # --- 准备测试数据 ---
    if CONFIG['test_size'] == 1.0:
        test_df = df.copy()
    else:
        _, test_df = train_test_split(df, test_size=CONFIG['test_size'], random_state=42)

    # --- 为测试集生成输入文本 ---
    print("\n--- 正在为整个测试集生成预备数据 ---")
    test_expanded_texts = []
    text_to_row_map = [] # 记录每个展开文本对应的原始行索引
    for index, row in test_df.iterrows():
        for task_name in TASK_NAMES:
            question = QUESTION_TEMPLATES[row['story_type']][task_name]
            new_text = f"问题：{question} 叙事：{row['text']} 已知线索：{row['ist_words']}"
            test_expanded_texts.append(new_text)
            text_to_row_map.append(index)

    # --- 进行预测 ---
    test_encodings = tokenizer(test_expanded_texts, padding=True, truncation=True, max_length=512, return_tensors='pt')
    test_dataset = TensorDataset(test_encodings['input_ids'], test_encodings['attention_mask'])
    test_dataloader = DataLoader(test_dataset, sampler=SequentialSampler(test_dataset), batch_size=CONFIG['batch_size'])

    all_probs = []
    with torch.no_grad():
        for batch in tqdm(test_dataloader, desc="模型预测中"):
            input_ids, attention_mask = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask)
            all_probs.extend(torch.sigmoid(outputs).cpu().numpy())
    
    all_preds_flat = np.array(all_probs).flatten()
    all_preds_binary_flat = (all_preds_flat > 0.5).astype(int)

    # --- 筛选错误样本并生成分析文件 ---
    print("\n--- 正在筛选错误样本并生成分析文件 ---")
    output_dir = f"error_analysis_{CONFIG['champion_model_path'].replace('.pth','')}"
    os.makedirs(output_dir, exist_ok=True)
    
    results = {
        'original_index': text_to_row_map,
        'full_input_text': test_expanded_texts,
        'task': [task for _ in range(len(test_df)) for task in TASK_NAMES],
        'predicted_prob': all_preds_flat,
        'predicted_label': all_preds_binary_flat
    }
    results_df = pd.DataFrame(results)
    
    # 合并原始数据信息
    merged_df = pd.merge(results_df, test_df, left_on='original_index', right_index=True)
    
    for task_name in CONFIG['tasks_to_analyze']:
        print(f"\n--- 正在处理任务: {task_name} ---")
        task_df = merged_df[merged_df['task'] == task_name]
        task_df['true_label'] = task_df[task_name]
        
        error_df = task_df[task_df['true_label'] != task_df['predicted_label']]
        
        if error_df.empty:
            print(f"任务 {task_name} 在此测试集上没有发现错误样本。")
            continue
            
        fp_df = error_df[error_df['predicted_label'] == 1]
        fn_df = error_df[error_df['predicted_label'] == 0]

        fp_filename = os.path.join(output_dir, f"{task_name}_false_positives.csv")
        fn_filename = os.path.join(output_dir, f"{task_name}_false_negatives.csv")
        
        # 定义要输出的列，使其更清晰
        output_columns = [
            'story_type', 'text', 'ist_words', 'true_label', 
            'predicted_label', 'predicted_prob', 'full_input_text'
        ]
        
        if not fp_df.empty:
            fp_df[output_columns].to_csv(fp_filename, index=False, encoding='utf-8-sig')
            print(f" - {len(fp_df)} 笔假正例 (False Positives) 已保存至: {fp_filename}")
        if not fn_df.empty:
            fn_df[output_columns].to_csv(fn_filename, index=False, encoding='utf-8-sig')
            print(f" - {len(fn_df)} 笔假反例 (False Negatives) 已保存至: {fn_filename}")

    print(f"\n\n所有错误分析报告已生成完毕，请检查 '{output_dir}' 文件夹。")