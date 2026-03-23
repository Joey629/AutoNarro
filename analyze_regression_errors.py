# analyze_regression_errors.py
# 用于回归模型的详细错误分析脚本
# 功能：加载保存的 XGBoost 模型，在测试集上进行预测，并筛选出预测误差最大的样本进行分析。

import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
from peft import LoraConfig, get_peft_model
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os
import joblib
import warnings

warnings.filterwarnings("ignore")

# ==============================================================================
# --- 1. 用户配置区 ---
# ==============================================================================
CONFIG = {
    'data_path': 'narratives.csv',
    'model_name': 'hfl/chinese-roberta-wwm-ext', 
    
    # --- [用户必须修改] BERT 模型路径 (用于特征提取) ---
    'champion_model_path': 'best_model_20251001-111255_epoch10_macrof1_0.7067.pth',
    
    # --- [用户必须修改] 保存了 XGBoost 模型的文件夹路径 ---
    # 这是运行 regression_analysis_final.py 后生成的文件夹，例如: 'champion_models_best_model_...'
    'xgb_models_dir': 'champion_models_best_model_20251001-111255_epoch10_macrof1_0.7067',
    
    # --- 分析配置 ---
    'target_variables': ['SC_E1', 'SC_E2', 'SC_E3'],
    'top_n_errors': 20, # 每个任务保存误差最大的前 20 个样本
    
    # --- 语言学特征列 (需与训练脚本完全一致) ---
    'linguistic_feature_columns': [
        'IS_Per', 'IS_Phy', 'IS_Con', 'IS_Emo', 'IS_Men', 'IS_Ling', 'IS_Token', 
        'IS_Type', 'TNW', 'TDW', 'TNU', 'MLU', '顺承关系', '因果关系', 
        '转折关系', '时间关系', '假设关系', '并列/递进关系', 'conj_token', 'conj_type', 
        '关系从句', '宾语从句', '主语从句', '连动结构', '兼语结构', 
        '描述性从句', '把字句', '被字句', '介词短语', '复杂状态句', '状语从句', 
        'Sentences_token', 'Sentence_type', 'PPVT', 'MINT', 'Forward', 'Backward'
    ]
}

# ==============================================================================
# --- 2. 核心组件 (必须与训练脚本一致) ---
# ==============================================================================
QUESTION_TEMPLATES = {
    'cat': { 'A2': "第一个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A3': "在追蝴蝶的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A4': "为了抓蝴蝶，小猫采取了什么行动？", 'A5': "小猫抓蝴蝶的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在抓蝴蝶失败后，猫和蝴蝶各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。", 'A8': "在拿球的事件中，男孩想要达成的目标或打算做的事情是什么？", 'A9': "为了拿回球，男孩采取了什么行动？", 'A10': "男孩拿球的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在拿回球后，男孩的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A13': "在关于鱼的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A14': "为了得到鱼，小猫采取了什么行动？", 'A15': "小猫拿鱼的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在得到鱼后，小猫的情绪反应是什么？", },
    'dog': { 'A2': "第一个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A3': "在追老鼠的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A4': "为了抓老鼠，小狗采取了什么行动？", 'A5': "小狗抓老鼠的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在抓老鼠失败后，小狗和老鼠各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。", 'A8': "在关于气球的事件中，男孩想要达成的目标或打算做的事情是什么？", 'A9': "为了拿回气球，男孩采取了什么行动？", 'A10': "男孩拿气球的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在拿回球后，男孩的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A13': "在关于香肠的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A14': "为了得到香肠，小狗采取了什么行动？", 'A15': "小狗拿香肠的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在得到香肠后，小狗的情绪反应是什么？", },
    'bird': { 'A2': "第一个事件的起因是什么？这包括鸟妈妈或小鸟的感受、想法或所看到的情境。", 'A3': "在喂食的事件中，鸟妈妈想要达成的目标或打算做的事情是什么？", 'A4': "为了喂小鸟，鸟妈妈采取了什么行动？", 'A5': "鸟妈妈找食物的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在喂食成功后，鸟妈妈和小鸟各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A8': "在抓小鸟的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A9': "为了抓小鸟，小猫采取了什么行动？", 'A10': "小猫抓小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在小猫抓到小鸟后，小猫和小鸟各自的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A13': "在救小鸟的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A14': "为了救小鸟，小狗采取了什么行动？", 'A15': "小鸟救小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。", "A16": "在小鸟获救后，小狗、小猫、小鸟和鸟妈妈各自的情绪反应是什么？", },
    'goat': { 'A2': "第一个事件的起因是什么？这包括小羊或羊妈妈的感受、想法或所看到的情境。", 'A3': "在救小羊的事件中，羊妈妈想要达成的目标或打算做的事情是什么？", 'A4': "为了救小羊，羊妈妈采取了什么行动？", 'A5': "羊妈妈救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在小羊获救后，羊妈妈和小羊各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括狐狸的感受、想法或他所看到的情境。", 'A8': "在抓小羊的事件中，狐狸想要达成的目标或打算做的事情是什么？", 'A9': "为了抓小羊，狐狸采取了什么行动？", 'A10': "狐狸抓小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在狐狸抓到小羊后，狐狸和小羊各自的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小鸟的感受、想法或他所看到的情境。", 'A13': "在救小鳥的事件中，小鸟想要达成的目标或打算做的事情是什么？", 'A14': "为了救小羊，小鸟采取了什么行动？", 'A15': "小鸟救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", "A16": "在小羊被小鸟救下后，小鸟、狐狸、小羊和羊妈妈各自的情绪反应是什么？", }
}

class ClueAugmentedQAModel(nn.Module):
    def __init__(self, bert_model, use_peft=True):
        super(ClueAugmentedQAModel, self).__init__()
        if use_peft:
            lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=['query', 'key', 'value'])
            self.bert = get_peft_model(bert_model, lora_config)
        else:
            self.bert = bert_model
    def forward(self, input_ids, attention_mask):
        return self.bert(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:, 0, :]

# ==============================================================================
# --- 3. 特征提取函数 ---
# ==============================================================================
def extract_global_features(df, model, tokenizer, device):
    print("\n--- 提取测试集特征: 全局平均策略 (用于 E1, E3) ---")
    model.to(device); model.eval()
    TASK_NAMES = [f'A{i}' for i in range(2, 17)]
    final_embeddings = []
    for index, row in tqdm(df.iterrows(), total=len(df), desc="Extracting Global"):
        prompts = []
        original_text, story_type = row['text'], row['story_type']
        ist_words = row.get('ist_words', '') if not pd.isna(row.get('ist_words', '')) else ''
        for task_name in TASK_NAMES:
            question = QUESTION_TEMPLATES[story_type][task_name]
            prompts.append(f"问题：{question} 叙事：{original_text} 已知线索：{ist_words}")
        inputs = tokenizer(prompts, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
        with torch.no_grad():
            prompt_embeddings = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
        final_embeddings.append(torch.mean(prompt_embeddings, dim=0, keepdim=True).cpu().numpy())
    return np.concatenate(final_embeddings, axis=0)

def extract_hierarchical_features(df, model, tokenizer, device):
    print("\n--- 提取测试集特征: 层次化策略 (用于 E2) ---")
    model.to(device); model.eval()
    TASK_NAMES_E1 = [f'A{i}' for i in range(2, 7)]
    TASK_NAMES_E2 = [f'A{i}' for i in range(7, 12)]
    TASK_NAMES_E3 = [f'A{i}' for i in range(12, 17)]
    final_embeddings = []
    
    def get_mean_embedding(prompts_list, device):
        if not prompts_list: return torch.zeros((1, model.bert.config.hidden_size), device=device)
        inputs = tokenizer(prompts_list, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
        with torch.no_grad(): prompt_embeddings = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
        return torch.mean(prompt_embeddings, dim=0, keepdim=True)

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Extracting Hierarchical"):
        original_text, story_type = row['text'], row['story_type']
        ist_words = row.get('ist_words', '') if not pd.isna(row.get('ist_words', '')) else ''
        
        prompts_E1 = [f"问题：{QUESTION_TEMPLATES[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}" for t in TASK_NAMES_E1]
        prompts_E2 = [f"问题：{QUESTION_TEMPLATES[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}" for t in TASK_NAMES_E2]
        prompts_E3 = [f"问题：{QUESTION_TEMPLATES[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}" for t in TASK_NAMES_E3]

        emb_E1 = get_mean_embedding(prompts_E1, device)
        emb_E2 = get_mean_embedding(prompts_E2, device)
        emb_E3 = get_mean_embedding(prompts_E3, device)
        emb_Global = torch.mean(torch.stack([emb_E1, emb_E2, emb_E3]), dim=0)
        final_embeddings.append(torch.cat([emb_E1, emb_E2, emb_E3, emb_Global], dim=1).cpu().numpy())
    return np.concatenate(final_embeddings, axis=0)

# ==============================================================================
# --- 4. 错误分析主程序 ---
# ==============================================================================
if __name__ == "__main__":
    if not os.path.exists(CONFIG['xgb_models_dir']):
        print(f"❌ 错误: 找不到 XGBoost 模型文件夹 '{CONFIG['xgb_models_dir']}'。请修改 CONFIG['xgb_models_dir']。")
        exit()

    # --- 1. 数据准备 (仅保留测试集) ---
    print("--- 1. 加载数据并复现测试集划分 ---")
    df = pd.read_csv(CONFIG['data_path'])
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)
    
    # 使用相同的 random_state=42 进行划分，只取测试集部分
    _, test_df = train_test_split(df, test_size=0.2, random_state=42)
    print(f"测试集大小: {len(test_df)} 条样本")

    if torch.backends.mps.is_available(): device = torch.device("mps")
    else: device = torch.device("cpu")

    # --- 2. 提取特征 ---
    # 需要加载 BERT 来提取特征，因为训练时没有保存测试集的特征
    print("\n--- 2. 加载 BERT 模型以提取特征 ---")
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
    bert_base = AutoModel.from_pretrained(CONFIG['model_name'])
    model = ClueAugmentedQAModel(bert_base, use_peft=True)
    try:
        model.load_state_dict(torch.load(CONFIG['champion_model_path'], map_location=device), strict=False)
    except FileNotFoundError:
        print(f"错误: BERT 模型权重 '{CONFIG['champion_model_path']}' 未找到。")
        exit()

    # 提取语言学特征
    existing_linguistic_cols = [col for col in CONFIG['linguistic_feature_columns'] if col in test_df.columns]
    for col in existing_linguistic_cols:
        test_df[col] = pd.to_numeric(test_df[col], errors='coerce').fillna(0)
    linguistic_features = test_df[existing_linguistic_cols].values

    # 提取 BERT 特征
    bert_global = extract_global_features(test_df, model, tokenizer, device)
    bert_hierarchical = extract_hierarchical_features(test_df, model, tokenizer, device)
    
    X_test_global = np.concatenate([bert_global, linguistic_features], axis=1)
    X_test_hierarchical = np.concatenate([bert_hierarchical, linguistic_features], axis=1)

    # --- 3. 加载 XGBoost 模型并预测 ---
    print("\n--- 3. 加载 XGBoost 模型进行预测与错误分析 ---")
    
    # 准备结果存储文件夹
    output_dir = f"regression_error_analysis_{CONFIG['xgb_models_dir']}"
    os.makedirs(output_dir, exist_ok=True)
    
    # 创建基础结果 DataFrame
    results_df = test_df.copy()
    
    for target in CONFIG['target_variables']:
        print(f"\n正在分析目标: {target} ...")
        
        # 加载模型
        model_path = os.path.join(CONFIG['xgb_models_dir'], f"xgb_model_{target}.joblib")
        if not os.path.exists(model_path):
            print(f"  ⚠️ 警告: 找不到模型文件 {model_path}，跳过。")
            continue
            
        xgb_model = joblib.load(model_path)
        
        # 选择特征 (SC_E2 用 hierarchical, 其他用 global)
        if target == 'SC_E2':
            X_input = X_test_hierarchical
        else:
            X_input = X_test_global
            
        # 预测
        y_pred = xgb_model.predict(X_input)
        y_true = results_df[target].values
        
        # 存储结果
        col_pred = f'{target}_pred'
        col_resid = f'{target}_residual'
        results_df[col_pred] = y_pred
        results_df[col_resid] = y_true - y_pred # 正值表示模型低估(Under)，负值表示模型高估(Over)
        
        # 计算误差统计
        mse = mean_squared_error(y_true, y_pred)
        print(f"  {target} 测试集 MSE: {mse:.4f}")
        
        # --- 筛选 Worst Errors ---
        # 1. 严重低估 (Under-prediction): 真实值远大于预测值 (Residual 最正)
        top_under = results_df.nlargest(CONFIG['top_n_errors'], col_resid)
        under_filename = os.path.join(output_dir, f"{target}_worst_under_predictions.csv")
        
        # 2. 严重高估 (Over-prediction): 预测值远大于真实值 (Residual 最负)
        top_over = results_df.nsmallest(CONFIG['top_n_errors'], col_resid)
        over_filename = os.path.join(output_dir, f"{target}_worst_over_predictions.csv")
        
        # 定义输出列 (只保留关键信息)
        out_cols = ['text', 'story_type', target, col_pred, col_resid] + existing_linguistic_cols[:5]
        
        top_under[out_cols].to_csv(under_filename, index=False, encoding='utf-8-sig')
        top_over[out_cols].to_csv(over_filename, index=False, encoding='utf-8-sig')
        
        print(f"  - 已保存严重低估样本至: {under_filename}")
        print(f"  - 已保存严重高估样本至: {over_filename}")

    print(f"\n✅ 分析完成！所有报告已生成在 '{output_dir}' 文件夹中。")