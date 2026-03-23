# train_final_automated_model.py
# [目标]：训练一个“全自动”的回归模型 (模块 D)。
# [策略]：
# 1. 导入 'bart_predictor.py' (B类) 和 'automated_feature_extractor.py' (A类+B扩展)。
# 2. 自动计算 'auto_TNU', 'auto_IS_Men_count' 和 'predicted_ist_words'。
# 3. [重要] 仅使用这些自动化特征 + BERT 特征(模块 C)来训练 XGBoost。
# 4. 保存训练好的 3 个全自动 XGBoost 模型。

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
import joblib 
import warnings

# --- [新] 导入我们的自动化工具 ---
try:
    # [来自: 2] (automated_feature_extractor.py)
    from automated_feature_extractor import analyze_automated_features
    # [来自: 1] (bart_predictor.py)
    from bart_predictor import BartPredictor
except ImportError as e:
    print(f"❌ 错误: 找不到自动化脚本。 {e}")
    print("请确保 'automated_feature_extractor.py' 和 'bart_predictor.py' 在同一个文件夹中。")
    exit()

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
    'bart_model_dir': './model_b_bart_structured_generator', # [新] 指向你训练好的 BART 模型 [来自: 1]
    'target_variables': ['SC_E1', 'SC_E2', 'SC_E3'], 
    
    # [新] 我们只使用 'automated_feature_extractor.py' 能生成的特征
    'automated_linguistic_columns': [
        'auto_TNU', 'auto_MLU', 'auto_TNW', 'auto_TDW', 
        'auto_IS_Per_count', 'auto_IS_Phy_count', 'auto_IS_Con_count', 
        'auto_IS_Emo_count', 'auto_IS_Men_count', 'auto_IS_Ling_count'
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
# [来自: 2] (回归模型使用不带头的BERT)
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
# --- 3. [已修改] 特征提取函数 ---
# ==============================================================================

# [修改] 两个 BERT 特征提取函数现在都接收 'predicted_ist_words'
def extract_global_features(df, model, tokenizer, device):
    print("\n--- 步骤1a: 正在提取丰富的深度语义特征 (全局平均策略) ---")
    model.to(device); model.eval()
    TASK_NAMES = [f'A{i}' for i in range(2, 17)]
    final_embeddings = []
    for index, row in tqdm(df.iterrows(), total=len(df), desc="逐篇叙事提取特征中 (Global)"):
        prompts = []
        original_text, story_type = row['text'], row['story_type']
        # [!! 修改 !!] 使用自动生成的 'predicted_ist_words'
        ist_words = row.get('predicted_ist_words', '') 
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
        # [!! 修改 !!] 使用自动生成的 'predicted_ist_words'
        ist_words = row.get('predicted_ist_words', '') 
        if pd.isna(ist_words): ist_words = ''
        prompts_E1 = [f"问题：{QUESTION_TEMPLATES[story_type][task_name]} 叙事：{original_text} 已知线索：{ist_words}" for task_name in TASK_NAMES_E1]
        prompts_E2 = [f"问题：{QUESTION_TEMPLATES[story_type][task_name]} 叙事：{original_text} 已知线索：{ist_words}" for task_name in TASK_NAMES_E2]
        prompts_E3 = [f"问题：{QUESTION_TEMPLATES[story_type][task_name]} 叙事：{original_text} 已知线索：{ist_words}" for task_name in TASK_NAMES_E3]
        emb_E1 = get_mean_embedding(prompts_E1, device)
        emb_E2 = get_mean_embedding(prompts_E2, device)
        emb_E3 = get_mean_embedding(prompts_E3, device)
        emb_Global = torch.mean(torch.stack([emb_E1, emb_E2, emb_E3]), dim=0)
        final_emb = torch.cat([emb_E1, emb_E2, emb_E3, emb_Global], dim=1)
        final_embeddings.append(final_emb.cpu().numpy())
    return np.concatenate(final_embeddings, axis=0)

# ==============================================================================
# --- 5. [已重构] 全自动模型训练主流程 (模块 D) ---
# ==============================================================================
if __name__ == "__main__":
    
    # --- 1. 数据与模型加载 ---
    print("--- 步骤1: 加载数据与模型 ---")
    try:
        df = pd.read_csv(CONFIG['data_path'])
    except FileNotFoundError:
        print(f"❌ 错误: 数据文件 '{CONFIG['data_path']}' 未找到。")
        exit()
        
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)
        
    if torch.backends.mps.is_available(): device = torch.device("mps")
    else: device = torch.device("cpu")
    
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
    bert_base = AutoModel.from_pretrained(CONFIG['model_name'])
    bert_model = ClueAugmentedQAModel(bert_base, use_peft=True)
    
    try:
        print(f"正在加载 BERT 模型权重: {CONFIG['champion_model_path']}")
        state_dict = torch.load(CONFIG['champion_model_path'], map_location=device)
        bert_model.load_state_dict(state_dict, strict=False)
    except FileNotFoundError:
        print(f"❌ 错误: BERT 模型权重文件 '{CONFIG['champion_model_path']}' 未找到。")
        exit()

    # --- 2. 特征工程 (全自动化) ---
    print("\n--- 步骤2: 正在执行全自动特征工程 ---")
    
    # 2.1 [新] 模块 B2: 自动生成 'predicted_ist_words' [来自: 1]
    print("  [B2] 正在自动生成 B 类线索 (predicted_ist_words)...")
    try:
        bart_predictor = BartPredictor(model_dir=CONFIG['bart_model_dir'])
    except Exception as e:
        print("  ❌ 无法加载 BART 模型。请确保已运行 'train_model_b_t5_generator.py' 并已保存模型。")
        exit()
        
    predicted_words_list = []
    for text in tqdm(df['text'], desc="生成 B 类线索"):
        predicted_words = bart_predictor.predict_ist_words(str(text)) # 确保是字符串
        predicted_words_list.append(predicted_words)
    df['predicted_ist_words'] = predicted_words_list
    print("  [✓] 成功生成 B 类线索。")

    # 2.2 [新] 模块 A+B扩展: 自动计算 A 类和 B 类语言学特征
    print("  [A+B] 正在自动计算 A 类和 B 类语言学特征 (TNU, IS_Men_count...)...")
    auto_ling_features = []
    auto_ling_names = CONFIG['automated_linguistic_columns']
    
    # 我们使用 df.apply 来并行处理，而不是 for 循环
    def process_row_features(row):
        text = row['text']
        predicted_ist_words = row['predicted_ist_words']
        # 调用“模型 A+B”
        feature_vector, _ = analyze_automated_features(text, predicted_ist_words)
        return feature_vector

    # 使用 tqdm 包装 .apply 以显示进度
    tqdm.pandas(desc="计算 A+B 类特征")
    auto_ling_features = df.progress_apply(process_row_features, axis=1)
    
    # 转换为 numpy 数组 (N, 10)
    linguistic_features = np.array(auto_ling_features.tolist())
    print(f"  [✓] 成功提取 {linguistic_features.shape[1]} 个 A+B 类特征: {auto_ling_names}")


    # 2.3 模块 C: 提取 BERT 特征 (使用 'predicted_ist_words')
    bert_features_global = extract_global_features(df, bert_model, tokenizer, device)
    bert_features_hierarchical = extract_hierarchical_features(df, bert_model, tokenizer, device)
    
    # 2.4 准备完整的 *自动化* 特征集
    X_full_global = np.concatenate([bert_features_global, linguistic_features], axis=1)
    X_full_hierarchical = np.concatenate([bert_features_hierarchical, linguistic_features], axis=1)
    
    # 2.5 准备 *自动化* 特征名称列表
    bert_dim = bert_model.bert.config.hidden_size # 768
    feature_names_global = [f'bert_Global_{i}' for i in range(bert_dim)] + auto_ling_names
    feature_names_hierarchical = (
        [f'bert_E1_{i}' for i in range(bert_dim)] +
        [f'bert_E2_{i}' for i in range(bert_dim)] +
        [f'bert_E3_{i}' for i in range(bert_dim)] +
        [f'bert_Global_{i}' for i in range(bert_dim)] +
        auto_ling_names
    )
    
    # 2.6 准备所有目标的 y 值
    all_target_cols = CONFIG['target_variables'] + ['SC_Sum']
    for col in all_target_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    df_y = df[all_target_cols]
    
    # --- 3. 划分数据 (80% 训练, 20% 测试) ---
    print("\n--- 步骤3: 划分训练集与测试集 (80/20) ---")
    
    indices = df.index.values
    train_indices, test_indices = train_test_split(indices, test_size=0.2, random_state=42)
    
    y_train_df = df_y.iloc[train_indices]
    y_test_df = df_y.iloc[test_indices]
    
    X_train_g, X_test_g = X_full_global[train_indices], X_full_global[test_indices]
    X_train_h, X_test_h = X_full_hierarchical[train_indices], X_full_hierarchical[test_indices]


    # --- 4. 训练 *全自动* 回归模型 (模块 D) ---
    print("\n--- 步骤4: 训练“全自动动态特征”回归模型 ---")
    
    output_dir = f"automated_champion_models"
    os.makedirs(output_dir, exist_ok=True)
    
    performance_summary = []
    test_predictions = {} 

    for target_variable in CONFIG['target_variables']: # 只循环 E1, E2, E3
        print(f"\n{'='*25} 正在为目标: {target_variable} {'='*25}")
        
        y_train = y_train_df[target_variable].values
        y_test = y_test_df[target_variable].values
        
        # [动态特征选择]
        if target_variable == 'SC_E2':
            print("  [策略] 使用 '层次化' 特征 + 自动化 A/B 类")
            X_train = X_train_h
            X_test = X_test_h
            feature_names = feature_names_hierarchical
        else:
            print(f"  [策略] 为 {target_variable} 使用 '全局平均' 特征 + 自动化 A/B 类")
            X_train = X_train_g
            X_test = X_test_g
            feature_names = feature_names_global

        # 训练模型
        xgb_reg = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42, n_jobs=-1)
        xgb_reg.fit(X_train, y_train)
        
        # [新] 保存这个训练好的 *全自动* 模型
        model_filename = f"auto_xgb_model_{target_variable}.joblib"
        joblib.dump(xgb_reg, os.path.join(output_dir, model_filename))
        print(f"  [保存] 全自动模型已保存到: {output_dir}/{model_filename}")

        # 评估并存储预测
        y_pred = xgb_reg.predict(X_test)
        test_predictions[target_variable] = y_pred
        
        mse = mean_squared_error(y_test, y_pred); r2 = r2_score(y_test, y_pred)
        print(f"  [全自动] 均方误差 (MSE): {mse:.4f}, R-squared (R²): {r2:.4f}")
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
    print("\n--- 回归性能总结 (Fully Automated Model) ---")
    
    try:
        import tabulate
        print(performance_df.to_markdown(index=False, floatfmt=".4f"))
    except ImportError:
        print("警告: 'tabulate' 未安装, 采用普通文本格式输出。建议执行: pip install tabulate")
        print(performance_df.to_string(index=False, float_format="%.4f"))
        
    performance_df.to_csv(os.path.join(output_dir, "summary_performance_automated.csv"), index=False)

    print(f"\n--- ✅ 训练完成！请检查 '{output_dir}' 文件夹。 ---")