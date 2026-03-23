# regression_analysis_final.py
# [目标]：
# 1. 训练 "Run 5" (Dynamic_Best_Of) 的冠军回归策略。
# 2. 在 20% 的测试集上评估并报告 R² 分数。
# 3. [新] 将训练好的 3 个 XGBoost 模型保存到硬盘。

import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
from peft import LoraConfig, get_peft_model
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import os
from collections import Counter
import warnings
import joblib # [新] 导入 joblib

warnings.filterwarnings("ignore")

# --- Matplotlib 中文显示设置 ---
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

# ==============================================================================
# --- 1. 用户配置区 ---
# ==============================================================================
CONFIG = {
    'data_path': 'narratives.csv',
    'model_name': 'hfl/chinese-roberta-wwm-ext', 
    'champion_model_path': 'best_model_20251001-111255_epoch10_macrof1_0.7067.pth',
    'target_variables': ['SC_E1', 'SC_E2', 'SC_E3'], 
    'linguistic_feature_columns': [
        'IS_Per', 'IS_Phy', 'IS_Con', 'IS_Emo', 'IS_Men', 'IS_Ling', 'IS_Token', 
        'IS_Type', 'TNW', 'TDW', 'TNU', 'MLU', '顺承关系', '因果关系', 
        '转折关系', '时间关系', '假设关系', '并列/递进关系', 'conj_token', 'conj_type', 
        '关系从句', '宾语从句', '主语从句', '连动结构', '兼语结构', 
        '描述性从句', '把字句', '被字句', '介词短语', '复杂状态句', '状语从句', 
        'Sentences_token', 'Sentence_type', 'PPVT', 'MINT', 'Forward', 'Backward'
    ],
}

# ==============================================================================
# --- 2. 核心组件 (BERT) ---
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
# --- 3. 特征提取函数 (与 Run 5 脚本一致) ---
# ==============================================================================

# 策略 1: 全局平均 (适用于 E1, E3)
def extract_global_features(df, model, tokenizer, device):
    print("\n--- 步骤1a: 正在提取丰富的深度语义特征 (全局平均策略) ---")
    model.to(device); model.eval()
    
    TASK_NAMES = [f'A{i}' for i in range(2, 17)] # A2-A16
    final_embeddings = []

    for index, row in tqdm(df.iterrows(), total=len(df), desc="逐篇叙事提取特征中 (Global)"):
        prompts = []
        original_text, story_type = row['text'], row['story_type']
        ist_words = row.get('ist_words', '')
        if pd.isna(ist_words): ist_words = ''
        for task_name in TASK_NAMES:
            question = QUESTION_TEMPLATES[story_type][task_name]
            prompts.append(f"问题：{question} 叙事：{original_text} 已知线索：{ist_words}")
            
        inputs = tokenizer(prompts, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
        with torch.no_grad():
            prompt_embeddings = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
        
        mean_embedding = torch.mean(prompt_embeddings, dim=0, keepdim=True)
        final_embeddings.append(mean_embedding.cpu().numpy())
        
    return np.concatenate(final_embeddings, axis=0)

# 策略 2: 层次化 (适用于 E2)
def extract_hierarchical_features(df, model, tokenizer, device):
    print("\n--- 步骤1b: 正在提取丰富的深度语义特征 (层次化策略) ---")
    model.to(device); model.eval()
    
    TASK_NAMES_E1 = [f'A{i}' for i in range(2, 7)]
    TASK_NAMES_E2 = [f'A{i}' for i in range(7, 12)]
    TASK_NAMES_E3 = [f'A{i}' for i in range(12, 17)]
    
    final_embeddings = []

    def get_mean_embedding(prompts_list, device):
        if not prompts_list:
            return torch.zeros((1, model.bert.config.hidden_size), device=device) 
        
        inputs = tokenizer(prompts_list, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
        with torch.no_grad():
            prompt_embeddings = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
        mean_embedding = torch.mean(prompt_embeddings, dim=0, keepdim=True)
        return mean_embedding

    for index, row in tqdm(df.iterrows(), total=len(df), desc="逐篇叙事提取特征中 (Hierarchical)"):
        original_text, story_type = row['text'], row['story_type']
        ist_words = row.get('ist_words', '')
        if pd.isna(ist_words): ist_words = ''
        
        prompts_E1 = []
        for task_name in TASK_NAMES_E1:
            question = QUESTION_TEMPLATES[story_type][task_name]
            prompts_E1.append(f"问题：{question} 叙事：{original_text} 已知线索：{ist_words}")
            
        prompts_E2 = []
        for task_name in TASK_NAMES_E2:
            question = QUESTION_TEMPLATES[story_type][task_name]
            prompts_E2.append(f"问题：{question} 叙事：{original_text} 已知线索：{ist_words}")

        prompts_E3 = []
        for task_name in TASK_NAMES_E3:
            question = QUESTION_TEMPLATES[story_type][task_name]
            prompts_E3.append(f"问题：{question} 叙事：{original_text} 已知线索：{ist_words}")

        emb_E1 = get_mean_embedding(prompts_E1, device)
        emb_E2 = get_mean_embedding(prompts_E2, device)
        emb_E3 = get_mean_embedding(prompts_E3, device)
        emb_Global = torch.mean(torch.stack([emb_E1, emb_E2, emb_E3]), dim=0)
        
        # (1, 3072) = (1, 768) + (1, 768) + (1, 768) + (1, 768)
        final_emb = torch.cat([emb_E1, emb_E2, emb_E3, emb_Global], dim=1)
        final_embeddings.append(final_emb.cpu().numpy())
        
    return np.concatenate(final_embeddings, axis=0)

# ==============================================================================
# --- 5. [已重构] 回归分析主流程 ---
# ==============================================================================
if __name__ == "__main__":
    
    # --- 1. 数据与模型加载 ---
    print("--- 步骤1: 加载数据与模型 ---")
    try:
        df = pd.read_csv(CONFIG['data_path'])
    except FileNotFoundError:
        print(f"❌ 错误: 数据文件 '{CONFIG['data_path']}' 未找到。")
        exit()
        
    # [!! 修复 !!] 重命名第一列为 'text'
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)
        
    if torch.backends.mps.is_available(): device = torch.device("mps")
    else: device = torch.device("cpu")
    
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
    bert_base = AutoModel.from_pretrained(CONFIG['model_name'])
    
    model = ClueAugmentedQAModel(bert_base, use_peft=True)
    
    try:
        print(f"正在加载模型权重: {CONFIG['champion_model_path']}")
        state_dict = torch.load(CONFIG['champion_model_path'], map_location=device)
        model.load_state_dict(state_dict, strict=False)
    except FileNotFoundError:
        print(f"❌ 错误: 模型权重文件 '{CONFIG['champion_model_path']}' 未找到。")
        exit()

    # --- 2. 特征工程 ---
    print("\n--- 步骤2: 正在提取所有特征 ---")
    
    # 2.1 提取两种 BERT 特征
    bert_features_global = extract_global_features(df, model, tokenizer, device)
    bert_features_hierarchical = extract_hierarchical_features(df, model, tokenizer, device)
    
    # 2.2 准备语言学特征
    existing_linguistic_cols = [col for col in CONFIG['linguistic_feature_columns'] if col in df.columns]
    print(f"找到 {len(existing_linguistic_cols)} 个语言学特征 (例如: {existing_linguistic_cols[0]}, {existing_linguistic_cols[1]})")
    
    all_target_cols = CONFIG['target_variables'] + ['SC_Sum']
    all_feature_cols = existing_linguistic_cols + all_target_cols
    
    for col in all_feature_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
    linguistic_features = df[existing_linguistic_cols].values
    
    # 2.3 准备两种完整的特征集
    X_full_global = np.concatenate([bert_features_global, linguistic_features], axis=1)
    X_full_hierarchical = np.concatenate([bert_features_hierarchical, linguistic_features], axis=1)
    
    # 2.4 准备特征名称列表
    bert_dim = model.bert.config.hidden_size # 768
    feature_names_global = [f'bert_Global_{i}' for i in range(bert_dim)] + existing_linguistic_cols
    feature_names_hierarchical = (
        [f'bert_E1_{i}' for i in range(bert_dim)] +
        [f'bert_E2_{i}' for i in range(bert_dim)] +
        [f'bert_E3_{i}' for i in range(bert_dim)] +
        [f'bert_Global_{i}' for i in range(bert_dim)] +
        existing_linguistic_cols
    )
    
    # 2.5 准备所有目标的 y 值
    df_y = df[all_target_cols]
    
    # --- 3. 划分数据 (80% 训练, 20% 测试) ---
    print("\n--- 步骤3: 划分训练集与测试集 (80/20) ---")
    
    indices = df.index.values
    train_indices, test_indices = train_test_split(indices, test_size=0.2, random_state=42)
    
    y_train_df = df_y.iloc[train_indices]
    y_test_df = df_y.iloc[test_indices]
    
    X_train_g, X_test_g = X_full_global[train_indices], X_full_global[test_indices]
    X_train_h, X_test_h = X_full_hierarchical[train_indices], X_full_hierarchical[test_indices]


    # --- 4. 循环为 E1, E2, E3 训练回归模型 ---
    print("\n--- 步骤4: 训练“动态特征”回归模型 ---")
    
    output_dir = f"champion_models_{CONFIG['champion_model_path'].replace('.pth','')}"
    os.makedirs(output_dir, exist_ok=True)
    
    performance_summary = []
    test_predictions = {} # 存储 pred_E1, pred_E2, pred_E3

    for target_variable in CONFIG['target_variables']: # 只循环 E1, E2, E3
        print(f"\n{'='*25} 正在为目标: {target_variable} {'='*25}")
        
        y_train = y_train_df[target_variable].values
        y_test = y_test_df[target_variable].values
        
        # [动态特征选择]
        if target_variable == 'SC_E2':
            print("  [策略] 使用 '层次化' 特征 (E1+E2+E3+Global)")
            X_train = X_train_h
            X_test = X_test_h
            feature_names = feature_names_hierarchical
        else:
            print(f"  [策略] 为 {target_variable} 使用 '全局平均' 特征")
            X_train = X_train_g
            X_test = X_test_g
            feature_names = feature_names_global

        # 训练模型
        xgb_reg = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42, n_jobs=-1)
        xgb_reg.fit(X_train, y_train)
        
        # [新] 保存这个训练好的模型
        model_filename = f"xgb_model_{target_variable}.joblib"
        joblib.dump(xgb_reg, os.path.join(output_dir, model_filename))
        print(f"  [保存] 冠军模型已保存到: {output_dir}/{model_filename}")

        # 评估并存储预测
        y_pred = xgb_reg.predict(X_test)
        test_predictions[target_variable] = y_pred
        
        mse = mean_squared_error(y_test, y_pred); r2 = r2_score(y_test, y_pred)
        print(f"  [动态特征] 均方误差 (MSE): {mse:.4f}, R-squared (R²): {r2:.4f}")
        performance_summary.append({'预测目标': target_variable, 'MSE': mse, 'R-squared': r2, 'Accuracy (rounded)': np.nan})
        
    # --- 5. 推导和评估 SC_Sum ---
    print(f"\n{'='*25} 正在推导和评估: SC_Sum {'='*25}")
    
    y_pred_Sum = test_predictions['SC_E1'] + test_predictions['SC_E2'] + test_predictions['SC_E3']
    y_true_Sum = y_test_df['SC_Sum'].values
    
    r2_sum = r2_score(y_true_Sum, y_pred_Sum)
    mse_sum = mean_squared_error(y_true_Sum, y_pred_Sum)
    print(f"  [推导] 均方误差 (MSE): {mse_sum:.4f}, R-squared (R²): {r2_sum:.4f}")

    y_true_Sum_int = y_true_Sum.astype(int)
    y_pred_Sum_rounded = np.round(y_pred_Sum).astype(int)
    
    acc_sum = accuracy_score(y_true_Sum_int, y_pred_Sum_rounded)
    print(f"  [推导] 四舍五入准确率 (Accuracy): {acc_sum:.4f}")

    performance_summary.append({
        '预测目标': 'SC_Sum (推导)',
        'MSE': mse_sum,
        'R-squared': r2_sum,
        'Accuracy (rounded)': acc_sum
    })
    
    # --- 6. 生成总结报告 ---
    print("\n--- 步骤5: 生成性能报告 ---")
    
    performance_df = pd.DataFrame(performance_summary)
    print("\n--- 回归性能总结 (SC_Sum_Derived_Dynamic_Best_Of) ---")
    
    try:
        import tabulate
        print(performance_df.to_markdown(index=False, floatfmt=".4f"))
    except ImportError:
        print("警告: 'tabulate' 未安装, 采用普通文本格式输出。建议执行: pip install tabulate")
        print(performance_df.to_string(index=False, float_format="%.4f"))
        
    performance_df.to_csv(os.path.join(output_dir, "summary_performance.csv"), index=False)

    print(f"\n--- ✅ 训练完成！请检查 '{output_dir}' 文件夹。 ---")