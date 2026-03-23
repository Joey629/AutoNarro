# analyze_regression_bert_full.py
# [目标]：
# 1. 加载 BERT 模型提取文本特征 (Global & Hierarchical)。
# 2. 拼接语言学特征，构建完整的特征矩阵。
# 3. 加载 XGBoost 冠军模型进行预测。
# 4. 生成分析报告。

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from peft import LoraConfig, get_peft_model
from tqdm import tqdm
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib 
import warnings
import scipy.stats as stats
from sklearn.metrics import r2_score

warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'PingFang SC', 'SimHei', 'Microsoft YaHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# =============================================================================
# --- 1. 用户配置区 (请仔细核对路径) ---
# =============================================================================
CONFIG = {
    # --- 基础路径 ---
    'data_path': 'narratives.csv',
    
    # [重要] 这里必须填入您训练好的 BERT 权重文件 (.pth)
    # 请确保此文件存在！根据您的文件夹名猜测如下：
    'bert_weight_path': 'best_model_20251001-111255_epoch10_macrof1_0.7067.pth',
    
    # XGBoost 模型所在的文件夹
    'champion_model_path': 'champion_models_best_model_20251001-111255_epoch10_macrof1_0.7067',
    
    'analysis_output_dir': 'analysis_results_bert_full',
    
    # 缓存路径 (提取一次后会自动保存，下次运行变快)
    'feature_cache_path': 'features_cache_full.joblib',
    
    # --- 模型配置 ---
    'model_name': 'hfl/chinese-roberta-wwm-ext', 
    'device': 'mps' if torch.backends.mps.is_available() else ('cuda' if torch.cuda.is_available() else 'cpu'),
    
    # --- 特征列 (37个) ---
    'linguistic_feature_columns': [
        'IS_Per', 'IS_Phy', 'IS_Con', 'IS_Emo', 'IS_Men', 'IS_Ling', 'IS_Token', 
        'IS_Type', 'TNW', 'TDW', 'TNU', 'MLU', '顺承关系', '因果关系', 
        '转折关系', '时间关系', '假设关系', '并列/递进关系', 'conj_token', 'conj_type', 
        '关系从句', '宾语从句', '主语从句', '连动结构', '兼语结构', 
        '描述性从句', '把字句', '被字句', '介词短语', '复杂状态句', '状语从句', 
        'Sentences_token', 'Sentence_type', 'PPVT', 'MINT', 'Forward', 'Backward'
    ],
    
    'target_columns': ['SC_E1', 'SC_E2', 'SC_E3'],
    
    'metadata_columns': {
        'age_column': 'age',
        'left_behind_column': 'left_behind',
        'story_theme_column': 'story_type',
        'narrative_type_column': 'task_type'
    },
    'real_score_col': 'SC_Sum',
    'pred_score_col': 'pred_SC_Sum'
}

# =============================================================================
# --- 2. BERT 模型定义 (必须与训练代码一致) ---
# =============================================================================
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

# =============================================================================
# --- 3. 特征提取函数 ---
# =============================================================================
def extract_global_features(df, model, tokenizer, device):
    model.to(device); model.eval()
    TASK_NAMES = [f'A{i}' for i in range(2, 17)] 
    final_embeddings = []
    
    print("  > 提取 Global 特征 (E1/E3)...")
    for index, row in tqdm(df.iterrows(), total=len(df), leave=False):
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

def extract_hierarchical_features(df, model, tokenizer, device):
    model.to(device); model.eval()
    TASK_NAMES_E1 = [f'A{i}' for i in range(2, 7)]
    TASK_NAMES_E2 = [f'A{i}' for i in range(7, 12)]
    TASK_NAMES_E3 = [f'A{i}' for i in range(12, 17)]
    final_embeddings = []

    print("  > 提取 Hierarchical 特征 (E2)...")
    def get_mean_embedding(prompts_list):
        if not prompts_list: return torch.zeros((1, model.bert.config.hidden_size), device=device)
        inputs = tokenizer(prompts_list, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
        with torch.no_grad():
            prompt_embeddings = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
        return torch.mean(prompt_embeddings, dim=0, keepdim=True)

    for index, row in tqdm(df.iterrows(), total=len(df), leave=False):
        original_text, story_type = row['text'], row['story_type']
        ist_words = row.get('ist_words', '')
        if pd.isna(ist_words): ist_words = ''
        
        # 构建 Prompt
        prompts_E1 = [f"问题：{QUESTION_TEMPLATES[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}" for t in TASK_NAMES_E1]
        prompts_E2 = [f"问题：{QUESTION_TEMPLATES[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}" for t in TASK_NAMES_E2]
        prompts_E3 = [f"问题：{QUESTION_TEMPLATES[story_type][t]} 叙事：{original_text} 已知线索：{ist_words}" for t in TASK_NAMES_E3]

        emb_E1 = get_mean_embedding(prompts_E1)
        emb_E2 = get_mean_embedding(prompts_E2)
        emb_E3 = get_mean_embedding(prompts_E3)
        emb_Global = torch.mean(torch.stack([emb_E1, emb_E2, emb_E3]), dim=0)
        
        final_emb = torch.cat([emb_E1, emb_E2, emb_E3, emb_Global], dim=1)
        final_embeddings.append(final_emb.cpu().numpy())
    return np.concatenate(final_embeddings, axis=0)

# =============================================================================
# --- 4. 主流程函数 ---
# =============================================================================
def prepare_all_features(df, config):
    # 尝试加载缓存
    if os.path.exists(config['feature_cache_path']):
        print(f"📦 发现特征缓存 {config['feature_cache_path']}，直接加载...")
        cache_data = joblib.load(config['feature_cache_path'])
        return cache_data['X_full_global'], cache_data['X_full_hierarchical']
    
    print("\n🚀 开始特征提取 (需要运行 BERT，可能需要几分钟)...")
    
    # 1. 准备语言学特征
    missing = [c for c in config['linguistic_feature_columns'] if c not in df.columns]
    if missing: 
        print(f"⚠️ 警告: 缺失语言学特征 {missing}，已补0")
        for c in missing: df[c] = 0
    for c in config['linguistic_feature_columns']:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)
    linguistic_features = df[config['linguistic_feature_columns']].values
    
    # 2. 准备 BERT
    try:
        tokenizer = AutoTokenizer.from_pretrained(config['model_name'])
        bert_base = AutoModel.from_pretrained(config['model_name'])
        model = ClueAugmentedQAModel(bert_base, use_peft=True)
        
        print(f"📥 加载 BERT 权重: {config['bert_weight_path']}")
        state_dict = torch.load(config['bert_weight_path'], map_location=config['device'])
        model.load_state_dict(state_dict, strict=False)
    except Exception as e:
        print(f"❌ BERT 模型加载失败: {e}")
        print("💡 请确认 'bert_weight_path' 指向了正确的 .pth 文件！")
        return None, None

    # 3. 提取特征
    bert_global = extract_global_features(df, model, tokenizer, config['device'])
    bert_hierarchical = extract_hierarchical_features(df, model, tokenizer, config['device'])
    
    # 4. 拼接
    X_full_global = np.concatenate([bert_global, linguistic_features], axis=1) # 768+37=805
    X_full_hierarchical = np.concatenate([bert_hierarchical, linguistic_features], axis=1) # 3072+37=3109
    
    # 5. 保存缓存
    joblib.dump({'X_full_global': X_full_global, 'X_full_hierarchical': X_full_hierarchical}, config['feature_cache_path'])
    print("💾 特征已缓存。")
    
    return X_full_global, X_full_hierarchical

def predict_and_analyze(df, X_global, X_hierarchical, config):
    results_df = df.copy()
    out_dir = config['analysis_output_dir']
    os.makedirs(out_dir, exist_ok=True)
    
    print("\n--- 开始预测 ---")
    for target_col in config['target_columns']:
        model_path = os.path.join(config['champion_model_path'], f'xgb_model_{target_col}.joblib')
        pred_col = f'pred_{target_col}'
        
        # [关键] 根据目标变量选择特征集
        if target_col == 'SC_E2':
            X_input = X_hierarchical
            print(f"  🎯 {target_col}: 使用 Hierarchical 特征 (维度 {X_input.shape[1]})")
        else:
            X_input = X_global
            print(f"  🎯 {target_col}: 使用 Global 特征 (维度 {X_input.shape[1]})")
            
        try:
            model = joblib.load(model_path)
            preds = model.predict(X_input)
            results_df[pred_col] = preds
            print(f"  ✅ {target_col} 预测成功")
        except Exception as e:
            print(f"  ❌ {target_col} 预测失败: {e}")
            results_df[pred_col] = 0

    # 计算总分
    pred_cols = [f'pred_{c}' for c in config['target_columns']]
    results_df[config['pred_score_col']] = results_df[pred_cols].sum(axis=1)
    if config['real_score_col'] not in results_df.columns:
        if all(c in results_df.columns for c in config['target_columns']):
            results_df[config['real_score_col']] = results_df[config['target_columns']].sum(axis=1)

    # 保存
    results_df.to_csv(os.path.join(out_dir, 'final_predictions.csv'), index=False, encoding='utf-8-sig')
    
    # --- 绘图与分析 ---
    print("\n--- 生成分析图表 ---")
    
    # 辅助绘图函数
    def plot_box(cat, score, title, suffix):
        if cat not in results_df.columns: return
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=cat, y=score, data=results_df)
        plt.title(f"{title} vs {score}{suffix}")
        plt.savefig(os.path.join(out_dir, f"{cat}_vs_{score}{suffix}_boxplot.png"))
        plt.close()

    def plot_scatter(x_col, y_col, title, suffix):
        if x_col not in results_df.columns: return
        df_clean = results_df.dropna(subset=[x_col, y_col])
        if len(df_clean)<2: return
        r, p = stats.pearsonr(df_clean[x_col], df_clean[y_col])
        plt.figure(figsize=(8, 6))
        sns.regplot(x=x_col, y=y_col, data=df_clean, scatter_kws={'alpha':0.3})
        plt.title(f"{title} vs {score_col}{suffix}\nr={r:.3f}, p={p:.4f}")
        plt.savefig(os.path.join(out_dir, f"{x_col}_vs_{y_col}{suffix}_scatter.png"))
        plt.close()

    targets = [(config['real_score_col'], '_真实值'), (config['pred_score_col'], '_预测值')]
    meta = config['metadata_columns']
    
    # 真实值 vs 预测值
    real = config['real_score_col']
    pred = config['pred_score_col']
    df_eval = results_df.dropna(subset=[real, pred])
    if len(df_eval) > 1:
        r2 = r2_score(df_eval[real], df_eval[pred])
        pearson_r, _ = stats.pearsonr(df_eval[real], df_eval[pred])
        print(f"📊 最终评估: R² = {r2:.4f}, Pearson r = {pearson_r:.4f}")
        plt.figure(figsize=(8,8))
        sns.scatterplot(x=real, y=pred, data=df_eval, alpha=0.5)
        plt.plot([df_eval[real].min(), df_eval[real].max()], [df_eval[real].min(), df_eval[real].max()], 'r--')
        plt.title(f"真实值 vs 预测值 (R²={r2:.3f})")
        plt.savefig(os.path.join(out_dir, "model_performance.png"))
        plt.close()

    for score_col, suffix in targets:
        if score_col not in results_df.columns: continue
        plot_box(meta['narrative_type_column'], score_col, "叙事类型", suffix)
        plot_box(meta['story_theme_column'], score_col, "叙事主题", suffix)
        plot_box(meta['left_behind_column'], score_col, "留守经历", suffix)
        plot_scatter(meta['age_column'], score_col, "年龄", suffix)
        
        # 交互分析
        try:
            g = sns.lmplot(data=results_df, x=meta['age_column'], y=score_col, hue=meta['narrative_type_column'])
            g.savefig(os.path.join(out_dir, f"interaction_age_task_{score_col}{suffix}.png"))
            plt.close()
        except: pass

    print(f"✅ 完成！结果保存在: {out_dir}")

def main():
    if not os.path.exists(CONFIG['data_path']):
        print("❌ 找不到 CSV 文件")
        return
    # 第一列如果是索引，重命名为 text (适应训练时的处理)
    df = pd.read_csv(CONFIG['data_path'])
    if 'text' not in df.columns:
        df.rename(columns={df.columns[0]: 'text'}, inplace=True)

    # 1. 准备特征 (最耗时的一步)
    X_global, X_hierarchical = prepare_all_features(df, CONFIG)
    
    if X_global is None: return # BERT 加载失败

    # 2. 预测与分析
    predict_and_analyze(df, X_global, X_hierarchical, CONFIG)

if __name__ == "__main__":
    main()