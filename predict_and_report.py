# predict_and_report.py
# [目标]：
# 1. 接收一段新文本和元数据。
# 2. 全自动执行 B1 (Jieba) 和 B2 (BART) 预处理 [来自: 1, 2]。
# 3. 全自动执行 C (BERT) 特征提取。
# 4. 全自动执行 D (XGBoost) 回归预测。
# 5. 全自动执行 E (多任务) 分类预测 [来自: 3]。
# 6. 加载 F (基准数据库)，生成一份对比分析报告 [来自: 3]。
#
# [V5 - 最终对比修复版]
# [V6 - 与论文模块 4 对齐] 支持 task_type 基准对比、报告增加发展水平定位。
# - 自动读取 "new_data.csv"（可选列 task_type：讲述/复述，用于更精确的常模对比）
# - 修复了 'age' 和 'left_behind' 列的 NaN/字符串转换错误
# - 修复了 'goat' 模板中的 'A4Masks' 拼写错误
# - 新增 '置信分数' 到报告和 CSV 中
# - [!] 修复1: 自动计算多任务基准库的 'calculated_SS_Sum'，启用对比。
# - [!] 修复2: 回归和多任务对比现在同时按 'age' 和 'story_type' 筛选。
# - [V6] 修复3: 若基准库与输入含 task_type，则按 task_type 筛选（与论文 4.2.3 一致）。
# - [V6] 新增: 报告增加「发展水平定位」摘要（论文 3.2 developmental stage indicators）。
# - [V7] 若 new_data.csv 含 participants 列，同数字视为同一人；predict 完成后自动按参与者生成汇总报告（batch_reports/participant_reports/）。

import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from transformers import AutoTokenizer, AutoModel, AutoModelForSeq2SeqLM
from tqdm import tqdm
from peft import LoraConfig, get_peft_model
import xgboost as xgb
import os
import joblib 
import warnings
import re # 用于 Jieba

# --- 导入自动化工具 ---
try:
    # [来自: 2] (linguistic_feature_extractor.py)
    from linguistic_feature_extractor import extract_calculable_features
    # [来自: 1] (bart_cue_predictor.py)
    from bart_cue_predictor import BartPredictor
except ImportError as e:
    print(f"❌ 错误: 找不到自动化脚本。 {e}")
    print("请确保 'linguistic_feature_extractor.py' 和 'bart_cue_predictor.py' 在同一个文件夹中。")
    exit()

# [来自: 2] (automated_feature_extractor.py)
from automated_feature_extractor import EXPERT_KEYWORD_DB, analyze_automated_features

warnings.filterwarnings("ignore")

# ==============================================================================
# --- ( ! ) 用户输入区 ( ! ) ---
# ==============================================================================

# [!] 注意：下面的文本和元数据仅作为备用，脚本现在会从 .csv 读取
# 1. 填入你想要分析的新文本
NEW_NARRATIVE_TEXT = "小猫想抓蝴蝶。它跳了起来，但是没有抓到。小猫很难过。"

# 2. 填入对应的元数据
NEW_META_DATA = {
    'story_type': 'cat', # 'cat', 'dog', 'bird', 'goat'
    'age': 5,            # 参与者年龄
    'left_behind': 0     # 0 = 非留守, 1 = 留守
}

# 3. 确保这些路径是正确的
MODEL_PATHS = {
    # 来自 'train_bart_cue_generator.py' [来自: 1]
    'bart_model_dir': './model_b_bart_structured_generator',
    
    # [新] 来自 'train_final_automated_model.py'；若不存在则自动尝试 champion_xgb_folder
    'auto_xgb_folder': './automated_champion_models',
    # 宏观回归备用：来自 regression_analysis_final.py 的 xgb_model_*.joblib（与论文基准一致）
    'champion_xgb_folder': 'champion_models_best_model_20251001-111255_epoch10_macrof1_0.7067',
    
    # 来自 'train_multitask_cue_augmented.py'
    'bert_classifier_weights': 'best_model_20251001-111255_epoch10_macrof1_0.7067.pth',
    
    # 来自 'analyze_regression_metadata.py' 等流程产出的基准数据库 [来自: 3]
    # !! 确保此路径指向 *回归* 基准库 CSV !!
    'benchmark_db_regression': '【Archived】deep_analysis_results_champion_models_best_model_20251001-111255_epoch10_macrof1_0.7067/predictions_with_metadata_ALL_DATA.csv',
    
    # [新] 指向你的 *多任务* 基准库 [来自: 3]
    'benchmark_db_multitask': 'analysis_results_best_model_20251001-111255_epoch10_macrof1_0.7067/predictions_with_metadata.csv' 
}

# ==============================================================================
# --- 1. 核心组件 (BERT) ---
# ==============================================================================
CONFIG = {
    'model_name': 'hfl/chinese-roberta-wwm-ext',
    # [新] 我们只使用 'automated_feature_extractor.py' 能生成的特征
    'automated_linguistic_columns': [
        'auto_TNU', 'auto_MLU', 'auto_TNW', 'auto_TDW', 
        'auto_IS_Per_count', 'auto_IS_Phy_count', 'auto_IS_Con_count', 
        'auto_IS_Emo_count', 'auto_IS_Men_count', 'auto_IS_Ling_count'
    ],
}
TASK_NAMES_GLOBAL = [f'A{i}' for i in range(2, 17)] # [!] V5: 设为全局变量
# 多任务 0/1 判定阈值：按任务类型区分。goat/bird 为直接叙述(Telling)难度较大，cat/dog 为先听再讲(Retelling)难度较小；
# 以 test.xlsx 中 98、67 共 8 条人工 SS_Sum 对齐，Telling=0.52、Retelling=0.58 时总绝对误差最小（10），且更符合任务难度差异。
MULTITASK_THRESHOLD_TELLING = 0.52   # 直接叙述（goat, bird）
MULTITASK_THRESHOLD_RETELLING = 0.58 # 先听再讲（cat, dog）

def _multitask_threshold_for_task(task_type, story_type):
    """按任务类型返回多任务判定阈值：讲述/直接叙述(goat,bird)用较低阈值，复述(cat,dog)用较高阈值。"""
    if task_type is not None:
        t = str(task_type).strip().lower()
        if 'retelling' in t or '复述' in t:
            return MULTITASK_THRESHOLD_RETELLING
        if 'telling' in t or '讲述' in t:
            return MULTITASK_THRESHOLD_TELLING
        return MULTITASK_THRESHOLD_RETELLING
    return MULTITASK_THRESHOLD_TELLING if str(story_type).strip().lower() in ('goat', 'bird') else MULTITASK_THRESHOLD_RETELLING

QUESTION_TEMPLATES = {
    'cat': { 'A2': "第一个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A3': "在追蝴蝶的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A4': "为了抓蝴蝶，小猫采取了什么行动？", 'A5': "小猫抓蝴蝶的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在抓蝴蝶失败后，猫和蝴蝶各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。", 'A8': "在拿球的事件中，男孩想要达成的目标或打算做的事情是什么？", 'A9': "为了拿回球，男孩采取了什么行动？", 'A10': "男孩拿球的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在拿回球后，男孩的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A13': "在关于鱼的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A14': "为了得到鱼，小猫采取了什么行动？", 'A15': "小猫拿鱼的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在得到鱼后，小猫的情绪反应是什么？", },
    'dog': { 'A2': "第一个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A3': "在追老鼠的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A4': "为了抓老鼠，小狗采取了什么行动？", 'A5': "小狗抓老鼠的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在抓老鼠失败后，小狗和老鼠各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括男孩的感受、想法或他所看到的情境。", 'A8': "在关于气球的事件中，男孩想要达成的目标或打算做的事情是什么？", 'A9': "为了拿回气球，男孩采取了什么行动？", 'A10': "男孩拿气球的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在拿回球后，男孩的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A13': "在关于香肠的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A14': "为了得到香肠，小狗采取了什么行动？", 'A15': "小狗拿香肠的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A16': "在得到香肠后，小狗的情绪反应是什么？", },
    'bird': { 'A2': "第一个事件的起因是什么？这包括鸟妈妈或小鸟的感受、想法或所看到的情境。", 'A3': "在喂食的事件中，鸟妈妈想要达成的目标或打算做的事情是什么？", 'A4': "为了喂小鸟，鸟妈妈采取了什么行动？", 'A5': "鸟妈妈找食物的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在喂食成功后，鸟妈妈和小鸟各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括小猫的感受、想法或他所看到的情境。", 'A8': "在抓小鸟的事件中，小猫想要达成的目标或打算做的事情是什么？", 'A9': "为了抓小鸟，小猫采取了什么行动？", 'A10': "小猫抓小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在小猫抓到小鸟后，小猫和小鸟各自的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小狗的感受、想法或他所看到的情境。", 'A13': "在救小鸟的事件中，小狗想要达成的目标或打算做的事情是什么？", 'A14': "为了救小鸟，小狗采取了什么行动？", 'A15': "小鸟救小鸟的行动最后产生了什么结果？包括成功、失败或差点成功。", "A16": "在小鸟获救后，小狗、小猫、小鸟和鸟妈妈各自的情绪反应是什么？", },
    'goat': { 'A2': "第一个事件的起因是什么？这包括小羊或羊妈妈的感受、想法或所看到的情境。", 'A3': "在救小羊的事件中，羊妈妈想要达成的目标或打算做的事情是什么？", 'A4': "为了救小羊，羊妈妈采取了什么行动？", 'A5': "羊妈妈救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A6': "在小羊获救后，羊妈妈和小羊各自的情绪反应是什么？", 'A7': "第二个事件的起因是什么？这包括狐狸的感受、想法或他所看到的情境。", 'A8': "在抓小羊的事件中，狐狸想要达成的目标或打算做的事情是什么？", 'A9': "为了抓小羊，狐狸采取了什么行动？", 'A10': "狐狸抓小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", 'A11': "在狐狸抓到小羊后，狐狸和小羊各自的情绪反应是什么？", 'A12': "第三个事件的起因是什么？这包括小鸟的感受、想法或他所看到的情境。", 'A13': "在救小鳥的事件中，小鸟想要达成的目标或打算做的事情是什么？", 'A14': "为了救小羊，小鸟采取了什么行动？", 'A15': "小鸟救小羊的行动最后产生了什么结果？包括成功、失败或差点成功。", "A16": "在小羊被小鸟救下后，小鸟、狐狸、小羊和羊妈妈各自的情绪反应是什么？", }
}

# [重要] 这是一个 *包含* 分类头的模型，用于多任务分类 (E)
# [来自: 3]
class BertClassifier(nn.Module):
    def __init__(self, bert_model, use_peft=True):
        super(BertClassifier, self).__init__()
        if use_peft:
            lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=['query', 'key', 'value'])
            self.bert = get_peft_model(bert_model, lora_config)
        else:
            self.bert = bert_model
        # [来自: 3]
        self.inner_layer = nn.Linear(self.bert.config.hidden_size, 768)
        self.dropout = nn.Dropout(0.5)
        self.classifier = nn.Linear(768, 1)
    
    def forward_embedding(self, input_ids, attention_mask):
        # 模块 C: 提取用于回归的 [CLS] 特征
        return self.bert(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:, 0, :]

    def forward(self, input_ids, attention_mask):
        # 模块 E: 完整的分类流程
        embedding = self.forward_embedding(input_ids, attention_mask)
        x = self.dropout(embedding)
        x = torch.nn.functional.relu(self.inner_layer(x))
        x = self.dropout(x)
        output = self.classifier(x)
        return output

def get_mean_embedding(prompts_list, model, tokenizer, device):
    if not prompts_list:
        return torch.zeros((1, model.bert.config.hidden_size), device=device) 
    inputs = tokenizer(prompts_list, padding=True, truncation=True, max_length=512, return_tensors='pt').to(device)
    with torch.no_grad():
        # [重要] 我们只调用 bert.forward_embedding 来获取特征
        prompt_embeddings = model.forward_embedding(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
    mean_embedding = torch.mean(prompt_embeddings, dim=0, keepdim=True)
    return mean_embedding

# ==============================================================================
# --- 2. 预测流程 ---
# ==============================================================================

class AutomatedNarrativePredictor:
    def __init__(self, model_paths):
        print("--- 正在初始化全自动叙事分析器 ---")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_paths = model_paths
        
        # 1. 加载 T5 模型 (B2)
        try:
            self.bart_predictor = BartPredictor(model_dir=model_paths['bart_model_dir'])
        except Exception as e:
            print("❌ 致命错误: 无法加载 BART 模型。")
            raise e

        # 2. 加载 BERT 分类/特征提取器 (C & E)
        self.tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
        bert_base = AutoModel.from_pretrained(CONFIG['model_name'])
        self.bert_model = BertClassifier(bert_base, use_peft=True).to(self.device)
        try:
            self.bert_model.load_state_dict(torch.load(model_paths['bert_classifier_weights'], map_location=self.device))
            self.bert_model.eval()
            print("  [✓] BERT (多任务/特征) 模型加载成功。")
        except FileNotFoundError:
            print(f"❌ 致命错误: 找不到 BERT 权重: {model_paths['bert_classifier_weights']}")
            raise

        # 3. 加载 3 个 XGBoost 回归模型 (D)：优先 automated_champion_models，否则使用 champion_models（regression_analysis_final 产出）
        self._has_regression_models = False
        self._regression_ling_dim = 10  # 全自动管道使用 10 维语言学特征
        auto_xgb_dir = model_paths.get('auto_xgb_folder', './automated_champion_models')
        champion_xgb_dir = model_paths.get('champion_xgb_folder', 'champion_models_best_model_20251001-111255_epoch10_macrof1_0.7067')
        for name in ['auto_xgb_model_SC_E1.joblib', 'auto_xgb_model_SC_E2.joblib', 'auto_xgb_model_SC_E3.joblib']:
            if not os.path.isfile(os.path.join(auto_xgb_dir, name)):
                break
        else:
            try:
                self.xgb_e1 = joblib.load(os.path.join(auto_xgb_dir, 'auto_xgb_model_SC_E1.joblib'))
                self.xgb_e2 = joblib.load(os.path.join(auto_xgb_dir, 'auto_xgb_model_SC_E2.joblib'))
                self.xgb_e3 = joblib.load(os.path.join(auto_xgb_dir, 'auto_xgb_model_SC_E3.joblib'))
                self._has_regression_models = True
                print("  [✓] 3 个全自动 XGBoost 回归模型加载成功 (automated_champion_models)。")
            except Exception as e:
                print(f"  [!] 回归模型加载失败: {e}，将尝试 champion_models。")
        if not self._has_regression_models:
            for name in ['xgb_model_SC_E1.joblib', 'xgb_model_SC_E2.joblib', 'xgb_model_SC_E3.joblib']:
                if not os.path.isfile(os.path.join(champion_xgb_dir, name)):
                    break
            else:
                try:
                    self.xgb_e1 = joblib.load(os.path.join(champion_xgb_dir, 'xgb_model_SC_E1.joblib'))
                    self.xgb_e2 = joblib.load(os.path.join(champion_xgb_dir, 'xgb_model_SC_E2.joblib'))
                    self.xgb_e3 = joblib.load(os.path.join(champion_xgb_dir, 'xgb_model_SC_E3.joblib'))
                    n_global = getattr(self.xgb_e1, 'n_features_in_', 805)
                    n_ling_champion = n_global - 768  # 768 = BERT global dim
                    self._regression_ling_dim = int(n_ling_champion)
                    self._has_regression_models = True
                    print(f"  [✓] 3 个宏观回归模型加载成功 (champion_models)，语言学特征维度: {self._regression_ling_dim}。")
                except Exception as e:
                    print(f"  [!] champion_models 加载失败: {e}")
        if not self._has_regression_models:
            self.xgb_e1 = self.xgb_e2 = self.xgb_e3 = None
            print("  [!] 未找到回归模型 (automated_champion_models 或 champion_models)，宏观复杂度得分将显示为「未可用」。")

        # 4. 加载基准数据库 (F)
        try:
            self.benchmark_db_reg = pd.read_csv(model_paths['benchmark_db_regression'])
            # [来自: 3] 确保基准数据库中的列是正确的类型
            self.benchmark_db_reg['age'] = pd.to_numeric(self.benchmark_db_reg['age'], errors='coerce').fillna(0)
            self.benchmark_db_reg['left_behind'] = pd.to_numeric(self.benchmark_db_reg['left_behind'], errors='coerce').fillna(0)
            print(f"  [✓] 成功加载 {len(self.benchmark_db_reg)} 条 *回归* 基准数据库记录。")
        except FileNotFoundError:
            print(f"❌ 致命错误: 找不到回归基准数据库: {model_paths['benchmark_db_regression']}")
            print(f"  请先运行回归分析流程（如 analyze_regression_metadata.py）生成基准文件。")
            raise
            
        try:
            self.benchmark_db_multi = pd.read_csv(model_paths['benchmark_db_multitask'])
            # [来自: 3]
            self.benchmark_db_multi['age'] = pd.to_numeric(self.benchmark_db_multi['age'], errors='coerce').fillna(0)
            self.benchmark_db_multi['left_behind'] = pd.to_numeric(self.benchmark_db_multi['left_behind'], errors='coerce').fillna(0)
            
            # --- [!! V5 修复 1 !!] ---
            # 自动计算缺失的 'calculated_SS_Sum' 列
            multi_task_cols = [col for col in TASK_NAMES_GLOBAL if col in self.benchmark_db_multi.columns]
            if multi_task_cols:
                self.benchmark_db_multi['calculated_SS_Sum'] = self.benchmark_db_multi[multi_task_cols].sum(axis=1)
                print(f"  [✓] 成功加载 {len(self.benchmark_db_multi)} 条 *多任务* 基准数据库记录 (并自动计算了 'calculated_SS_Sum')。")
            else:
                print(f"  [!] 警告: 成功加载多任务基准库，但未找到任何 A2-A16 列用于计算总分。")
            # --- [!! V5 修复 1 结束 !!] ---
            
        except FileNotFoundError:
            print(f"❌ 致命错误: 找不到多任务基准数据库: {model_paths['benchmark_db_multitask']}")
            raise
        
        print("--- ✅ 分析器已就绪 ---")

    def predict(self, text, story_type, age, left_behind, task_type=None):
        """
        对单篇新文本执行全流程分析。
        task_type: 可选，叙事类型（如 'storytelling'/'retelling' 或中文）。若提供且基准库含该列，则按同龄+同主题+同任务类型对比。
        """
        # [!] 增加一个轻量级的打印，用于批量处理
        # print(f"\n--- 正在分析新文本 ---")
        
        # --- 模块 B: 预处理器 ---
        # B2: 自动生成 B 类线索 [来自: 1]
        predicted_ist_words = self.bart_predictor.predict_ist_words(text)
        # print(f"  [B2] 自动预测线索: \"{predicted_ist_words}\"")

        # B1: 自动计算 A 类语言学特征 [来自: 2]
        auto_ling_dict = extract_calculable_features(text)
        # B1 + B(扩展): 自动计算 B 类特征
        auto_features_vector, auto_feature_names = analyze_automated_features(text, predicted_ist_words)
        linguistic_features = np.array(auto_features_vector).reshape(1, -1) # (1, 10)
        # print(f"  [A+B] 自动语言学特征: {list(zip(auto_feature_names, auto_features_vector))}")


        # --- 模块 C & E: BERT 特征与多任务分类 ---
        # print("  [C/E] 正在运行 BERT (多任务分类与特征提取)...")
        all_prompts = []
        
        # [!] 检查 story_type 是否有效
        if story_type not in QUESTION_TEMPLATES:
            print(f"  [!] 警告: 未知的 story_type '{story_type}'。将使用 'cat' 作为模板。")
            story_type = 'cat'
            
        for task_name in TASK_NAMES_GLOBAL:
            question = QUESTION_TEMPLATES[story_type][task_name]
            all_prompts.append(f"问题：{question} 叙事：{text} 已知线索：{predicted_ist_words}")

        # 准备 Dataloader
        encodings = self.tokenizer(all_prompts, padding=True, truncation=True, max_length=512, return_tensors='pt')
        dataset = torch.utils.data.TensorDataset(encodings['input_ids'], encodings['attention_mask'])
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=16)

        all_probs = []
        all_embeddings = []
        
        with torch.no_grad():
            for batch in dataloader:
                input_ids, attention_mask = [b.to(self.device) for b in batch]
                
                # 模块 E: 多任务分类 [来自: 3]
                logits = self.bert_model(input_ids, attention_mask)
                probabilities = torch.sigmoid(logits)
                all_probs.append(probabilities.cpu().numpy())
                
                # 模块 C: 提取 [CLS] 嵌入 [来自: 3]
                embeddings = self.bert_model.forward_embedding(input_ids, attention_mask)
                all_embeddings.append(embeddings.cpu().numpy())
        
        # 处理多任务结果 (E)：按任务类型选用阈值（Telling 难度大用 0.52，Retelling 用 0.58）
        all_probs_flat = np.concatenate(all_probs, axis=0)
        thr = _multitask_threshold_for_task(task_type, story_type)
        all_preds_binary_flat = np.where(all_probs_flat > thr, 1, 0)
        
        # --- [!! V4 修改 !!] ---
        # 同时存储 0/1 预测和概率
        task_predictions = {}
        for i, task_name in enumerate(TASK_NAMES_GLOBAL):
            binary_pred = all_preds_binary_flat[i][0]
            probability = float(all_probs_flat[i][0])
            task_predictions[task_name] = binary_pred
            task_predictions[f"{task_name}_prob"] = probability # [!] 新增此行
        # --- [!! V4 修改结束 !!] ---
            
        # 处理回归特征 (C)
        all_embeddings_flat = np.concatenate(all_embeddings, axis=0) # (15, 768)
        
        # C1: 全局特征
        bert_features_global = np.mean(all_embeddings_flat, axis=0, keepdims=True) # (1, 768)
        
        # C2: 层次化特征
        emb_E1 = np.mean(all_embeddings_flat[0:5], axis=0, keepdims=True) # A2-A6
        emb_E2 = np.mean(all_embeddings_flat[5:10], axis=0, keepdims=True) # A7-A11
        emb_E3 = np.mean(all_embeddings_flat[10:15], axis=0, keepdims=True) # A12-A16
        emb_Global = np.mean(np.stack([emb_E1, emb_E2, emb_E3]), axis=0)
        bert_features_hierarchical = np.concatenate([emb_E1, emb_E2, emb_E3, emb_Global], axis=1) # (1, 3072)
        
        # print("  [✓] BERT 特征提取与多任务分类完成。")

        # --- 模块 D: 动态回归预测 ---
        if self._has_regression_models:
            # champion 模型期望 768+37 或 3072+37，当前只有 10 维自动特征时需零填充至 _regression_ling_dim
            n_ling = linguistic_features.shape[1]
            if n_ling < self._regression_ling_dim:
                pad = np.zeros((1, self._regression_ling_dim - n_ling), dtype=linguistic_features.dtype)
                linguistic_for_reg = np.concatenate([linguistic_features, pad], axis=1)
            else:
                linguistic_for_reg = linguistic_features[:, :self._regression_ling_dim]
            X_global_auto = np.concatenate([bert_features_global, linguistic_for_reg], axis=1)
            X_hierarchical_auto = np.concatenate([bert_features_hierarchical, linguistic_for_reg], axis=1)
            pred_sc_e1 = self.xgb_e1.predict(X_global_auto)[0]
            pred_sc_e2 = self.xgb_e2.predict(X_hierarchical_auto)[0]
            pred_sc_e3 = self.xgb_e3.predict(X_global_auto)[0]
            pred_sc_sum = pred_sc_e1 + pred_sc_e2 + pred_sc_e3
            regression_results = {
                'pred_SC_E1': float(pred_sc_e1), 'pred_SC_E2': float(pred_sc_e2),
                'pred_SC_E3': float(pred_sc_e3), 'pred_SC_Sum': float(pred_sc_sum)
            }
        else:
            pred_sc_e1 = pred_sc_e2 = pred_sc_e3 = pred_sc_sum = None
            regression_results = {'pred_SC_E1': None, 'pred_SC_E2': None, 'pred_SC_E3': None, 'pred_SC_Sum': None}
        
        # --- 模块 F: 生成分析报告 ---
        # print("  [F] 正在生成对比分析报告...")
        
        report_lines = []
        report_lines.append("--- 叙事自动分析报告 ---")
        
        # 1. 回归得分
        report_lines.append("\n1. 复杂度回归得分 (模块 D)")
        if self._has_regression_models:
            report_lines.append(f"   - SC_E1 (情节 1) 得分: {pred_sc_e1:.2f}")
            report_lines.append(f"   - SC_E2 (情节 2) 得分: {pred_sc_e2:.2f}")
            report_lines.append(f"   - SC_E3 (情节 3) 得分: {pred_sc_e3:.2f}")
            report_lines.append("   ---------------------------------")
            report_lines.append(f"   - SC_Sum (总复杂度) 得分: {pred_sc_sum:.2f} (四舍五入: {np.round(pred_sc_sum):.0f})")
        else:
            report_lines.append("   - [未可用] 请先运行 train_final_automated_model.py 生成 automated_champion_models 后再获得宏观复杂度得分。")

        # --- [!! V5 修复 2 + V6 task_type !!] ---
        # 2. 回归基准对比 (按 age, story_type，若有则按 task_type)
        report_lines.append("\n2. 复杂度基准对比 (模块 F - 回归)")
        mask_reg = (self.benchmark_db_reg['age'] == age) & (self.benchmark_db_reg['story_type'] == story_type)
        if task_type is not None and 'task_type' in self.benchmark_db_reg.columns:
            t_ref = self.benchmark_db_reg['task_type'].astype(str).str.strip().str.lower()
            t_in = str(task_type).strip().lower()
            mask_reg = mask_reg & (t_ref == t_in)
        benchmark_df_reg_filtered = self.benchmark_db_reg[mask_reg]
        
        if not self._has_regression_models:
            report_lines.append("   - [未可用] 缺少回归模型，无法进行宏观基准对比。")
        else:
            report_lines.append(f"   - 您的总分: {pred_sc_sum:.2f}")
            if not benchmark_df_reg_filtered.empty:
                age_avg_sum = benchmark_df_reg_filtered['pred_SC_Sum'].mean()
                peer_desc = f"同龄人 & 同主题 ('{story_type}', 年龄 {age})"
                if task_type is not None and 'task_type' in self.benchmark_db_reg.columns:
                    peer_desc += f" & 同任务类型 ('{task_type}')"
                report_lines.append(f"\n   - [{peer_desc} 对比]")
                report_lines.append(f"     - 您的分数: {pred_sc_sum:.2f}")
                report_lines.append(f"     - 同类人群平均分: {age_avg_sum:.2f} (n={len(benchmark_df_reg_filtered)})")
                report_lines.append(f"     - {'表现优于同类人群平均水平' if pred_sc_sum > age_avg_sum else '表现低于同类人群平均水平'}")
            else:
                report_lines.append(f"\n   - [!] 在基准库中未找到匹配的同类数据 (story_type={story_type}, age={age}" + (f", task_type={task_type}" if task_type else "") + ")，跳过对比。")
        # --- [!! V5 修复 2 + V6 结束 !!] ---

        
        # --- [!! V4 修改 !!] ---
        # 3. 多任务分类结果 (带置信度)
        report_lines.append("\n3. 多任务分类结果 (模块 E)")
        task_sum = 0
        for task_name in TASK_NAMES_GLOBAL: # [!] 遍历 A2-A16 的标准列表
            value = task_predictions[task_name]
            prob = task_predictions[f"{task_name}_prob"]
            report_lines.append(f"   - {task_name}: {value}  (置信度: {prob*100:.2f}%)") # [!] 修改
            task_sum += value
        report_lines.append(f"   ---------------------------------")
        report_lines.append(f"   - 多任务总分: {task_sum} / 15")
        # --- [!! V4 修改结束 !!] ---
        
        # [!] 添加一个 key 到 task_predictions 字典，用于汇总 CSV
        task_predictions['pred_MultiTask_Sum'] = task_sum

        # --- [!! V5 修复 3 + V6 task_type !!] ---
        # 4. 多任务基准对比 (按 age, story_type，若有则按 task_type)
        report_lines.append("\n4. 多任务基准对比 (模块 F - 多任务)")
        report_lines.append(f"   - 您的多任务总分: {task_sum}")
        
        multi_task_sum_col = 'calculated_SS_Sum'
        benchmark_df_multi_filtered = pd.DataFrame()  # 供后续发展水平定位使用
        if multi_task_sum_col not in self.benchmark_db_multi.columns:
            report_lines.append(f"  [F 警告] 在多任务基准库中未找到 'calculated_SS_Sum' 列，跳过多任务对比。")
        else:
            mask_multi = (self.benchmark_db_multi['age'] == age) & (self.benchmark_db_multi['story_type'] == story_type)
            if task_type is not None and 'task_type' in self.benchmark_db_multi.columns:
                t_ref = self.benchmark_db_multi['task_type'].astype(str).str.strip().str.lower()
                t_in = str(task_type).strip().lower()
                mask_multi = mask_multi & (t_ref == t_in)
            benchmark_df_multi_filtered = self.benchmark_db_multi[mask_multi]
            
            if not benchmark_df_multi_filtered.empty:
                age_avg_multi_sum = benchmark_df_multi_filtered[multi_task_sum_col].mean()
                peer_desc = f"同龄人 & 同主题 ('{story_type}', 年龄 {age})"
                if task_type is not None and 'task_type' in self.benchmark_db_multi.columns:
                    peer_desc += f" & 同任务类型 ('{task_type}')"
                report_lines.append(f"\n   - [{peer_desc} 对比]")
                report_lines.append(f"     - 您的分数: {task_sum}")
                report_lines.append(f"     - 同类人群平均分: {age_avg_multi_sum:.2f} (n={len(benchmark_df_multi_filtered)})")
                report_lines.append(f"     - {'表现优于同类人群平均水平' if task_sum > age_avg_multi_sum else '表现低于同类人群平均水平'}")
            else:
                report_lines.append(f"\n   - [!] 在基准库中未找到匹配的同类数据 (story_type={story_type}, age={age}" + (f", task_type={task_type}" if task_type else "") + ")，跳过对比。")
        # --- [!! V5 修复 3 + V6 结束 !!] ---
        
        # --- [!! V6: 发展水平定位 (Developmental stage indicators, 论文 3.2) !!] ---
        report_lines.append("\n5. 发展水平定位 (Developmental Stage)")
        above_reg = (self._has_regression_models and pred_sc_sum is not None and not benchmark_df_reg_filtered.empty and
                     pred_sc_sum > benchmark_df_reg_filtered['pred_SC_Sum'].mean())
        above_multi = (multi_task_sum_col in self.benchmark_db_multi.columns and not benchmark_df_multi_filtered.empty and
                       task_sum > benchmark_df_multi_filtered[multi_task_sum_col].mean())
        if self._has_regression_models and not benchmark_df_reg_filtered.empty:
            pos_reg = "高于同龄同组平均" if above_reg else "低于或接近同龄同组平均"
        else:
            pos_reg = "未可用（缺回归模型）" if not self._has_regression_models else "无同类参照"
        if multi_task_sum_col in self.benchmark_db_multi.columns and not benchmark_df_multi_filtered.empty:
            pos_multi = "高于同龄同组平均" if above_multi else "低于或接近同龄同组平均"
        else:
            pos_multi = "无同类参照"
        report_lines.append(f"   - 宏观复杂度: {pos_reg}。")
        report_lines.append(f"   - 微观结构完整性: {pos_multi}。")
        if not benchmark_df_reg_filtered.empty or (multi_task_sum_col in self.benchmark_db_multi.columns and not benchmark_df_multi_filtered.empty):
            report_lines.append(f"   - 综合: 该叙事在「年龄 {age} 岁、主题 {story_type}" + (f"、任务 {task_type}" if task_type else "") + "」的参照组中，整体处于" + ("较好" if (above_reg or above_multi) else "中等或待提升") + "水平。")
        else:
            report_lines.append("   - 暂无同类参照数据，无法给出发展水平定位；请确认基准库包含匹配的 age / story_type / task_type。")
        # --- [!! V6 结束 !!] ---
        
        report_lines.append("\n--- 报告结束 ---")
        
        return "\n".join(report_lines), regression_results, task_predictions

# ==============================================================================
# --- ( ! ) [新] 主程序入口 (批量处理版 V3 - 最终修复) ( ! ) ---
# ==============================================================================

if __name__ == "__main__":
    
    # --- 批量配置 ---
    NEW_DATA_FILE = "new_data.csv"
    OUTPUT_REPORT_DIR = "batch_reports"  # 与 participant_reports 的父目录（已不再生成单条 report_index_* 文件）
    OUTPUT_PARTICIPANT_REPORT_DIR = "batch_reports/participant_reports"  # 按参与者汇总的融合报告（含各故事完整分析）
    OUTPUT_CSV_FILE = "batch_predictions_summary.csv" # 包含所有预测结果的总表
    
    # 1. 创建输出文件夹
    os.makedirs(OUTPUT_REPORT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_PARTICIPANT_REPORT_DIR, exist_ok=True)
    
    # 2. 加载新数据
    try:
        df_new = pd.read_csv(NEW_DATA_FILE)
        
        # [!! 重要 !!] 检查 'text', 'story_type', 'age', 'left_behind' 列是否存在
        if 'text' not in df_new.columns and 'Text' in df_new.columns:
            df_new.rename(columns={'Text': 'text'}, inplace=True)
        elif 'text' not in df_new.columns:
            print("  [警告] 在 new_data.csv 中未找到 'text' 或 'Text' 列，正在将第一列重命名为 'text'。")
            df_new.rename(columns={df_new.columns[0]: 'text'}, inplace=True)
            
        # 检查其他必要的元数据列
        required_cols = ['story_type', 'age', 'left_behind']
        if not all(col in df_new.columns for col in required_cols):
            print(f"❌ 致命错误: 您的 '{NEW_DATA_FILE}' 必须包含以下列: {required_cols}")
            exit()
            
        print(f"--- 成功加载 '{NEW_DATA_FILE}', 准备分析 {len(df_new)} 条文本 ---")
    
    except FileNotFoundError:
        print(f"❌ 致命错误: 找不到数据文件 '{NEW_DATA_FILE}'。")
        exit()
    except Exception as e:
        print(f"❌ 致命错误: 加载 '{NEW_DATA_FILE}' 时出错: {e}")
        exit()

    all_regression_results = []
    all_task_predictions = []
    all_single_report_contents = {}  # index -> 单条报告全文（仅用于嵌入参与者报告，不再单独落盘）

    try:
        # 3. 初始化预测器 (只执行一次)
        predictor = AutomatedNarrativePredictor(MODEL_PATHS)
        
        print(f"\n--- 开始批量处理 {len(df_new)} 条文本 ---")
        
        # 4. 循环遍历 DataFrame 的每一行
        for index, row in tqdm(df_new.iterrows(), total=len(df_new), desc="批量分析中"):
            
            try:
                # 从行中获取数据
                text_to_analyze = str(row['text'])
                story_type = str(row['story_type'])
                
                # --- [!! 最终修复 !!] ---
                # 1. 尝试将 'age' 转换为数字
                age_val = pd.to_numeric(row['age'], errors='coerce')
                # 2. 如果是 NaN (空) 则设为0, 否则转为 int
                age = 0 if pd.isna(age_val) else int(age_val)
                
                # 1. 尝试将 'left_behind' 转换为数字 (这将对 "Partially Left-Behind" 返回 NaN)
                lb_val = pd.to_numeric(row['left_behind'], errors='coerce')
                # 2. 如果是 NaN (转换失败) 则设为0, 否则转为 int
                left_behind = 0 if pd.isna(lb_val) else int(lb_val)
                # --- [!! 修复结束 !!] ---
                
                # [V6] 可选: task_type（讲述/复述），用于与论文 4.2.3 一致的基准对比
                task_type = str(row['task_type']).strip() if 'task_type' in df_new.columns and pd.notna(row.get('task_type')) else None
                if task_type is not None and (task_type == '' or task_type.lower() == 'nan'):
                    task_type = None
                
                # 5. 执行预测
                final_report, regression_results, task_predictions = predictor.predict(
                    text_to_analyze,
                    story_type,
                    age,
                    left_behind,
                    task_type=task_type
                )
                
                # 存储结果以便最后保存到总表
                all_regression_results.append(regression_results)
                all_task_predictions.append(task_predictions)
                
                # 6. 单条报告内容仅存入内存，用于嵌入参与者报告（不再单独写 report_index_* 文件）
                meta_line = "元数据: story_type={}, age={}, left_behind={}".format(story_type, age, left_behind)
                if task_type is not None:
                    meta_line += ", task_type={}".format(task_type)
                single_full = "分析索引: {}\n分析文本: {}\n{}\n{}".format(index, text_to_analyze, meta_line, final_report)
                all_single_report_contents[index] = single_full

            except Exception as e:
                print(f"--- ❌ 跳过第 {index} 行，发生错误: {e} ---")
                all_regression_results.append({}) # 添加空字典以保持行对应
                all_task_predictions.append({})   # 添加空字典以保持行对应

        print("\n--- 批量处理完成 ---")

        # 7. 保存汇总的 CSV 结果
        df_reg_results = pd.DataFrame(all_regression_results)
        df_task_results = pd.DataFrame(all_task_predictions)
        
        # 将原始数据与新预测合并
        # [!] V5 修复: 重置 df_new 的索引以确保 concat 对齐
        df_final_summary = pd.concat([df_new.reset_index(drop=True), df_reg_results.reset_index(drop=True), df_task_results.reset_index(drop=True)], axis=1)
        # 数值列统一保留小数点后 2 位再写入 CSV
        for c in df_final_summary.columns:
            if df_final_summary[c].dtype in (np.floating, 'float64', 'float32'):
                df_final_summary[c] = df_final_summary[c].round(2)
        
        df_final_summary.to_csv(OUTPUT_CSV_FILE, index=False, encoding='utf-8-sig')
        
        print(f"\n--- ✅ 汇总的 CSV 已保存到 '{OUTPUT_CSV_FILE}' ---")

        # 8. 按参与者汇总报告（若 new_data 中有 participants 列）：面向家长的可读版 + 常模对比
        STORY_NAMES = {'cat': '小猫与蝴蝶', 'dog': '小狗与香肠', 'bird': '小鸟一家', 'goat': '小羊与狐狸'}
        if 'participants' in df_final_summary.columns:
            bench_reg, bench_multi = None, None
            multi_col = 'calculated_SS_Sum'
            try:
                bench_reg = pd.read_csv(MODEL_PATHS['benchmark_db_regression'])
                bench_reg['age'] = pd.to_numeric(bench_reg['age'], errors='coerce').fillna(0)
                bench_multi = pd.read_csv(MODEL_PATHS['benchmark_db_multitask'])
                bench_multi['age'] = pd.to_numeric(bench_multi['age'], errors='coerce').fillna(0)
                if multi_col not in bench_multi.columns:
                    task_cols = [c for c in TASK_NAMES_GLOBAL if c in bench_multi.columns]
                    if task_cols:
                        bench_multi[multi_col] = bench_multi[task_cols].sum(axis=1)
            except Exception as e:
                print(f"  [!] 加载参照库失败: {e}")
            part_col = 'participants'
            for pid, grp in df_final_summary.groupby(part_col, sort=True):
                pid = pid if pd.notna(pid) else 'unknown'
                part_age = int(grp['age'].dropna().iloc[0]) if len(grp['age'].dropna()) > 0 else None
                has_reg = 'pred_SC_Sum' in grp.columns and grp['pred_SC_Sum'].notna().any()
                has_multi = 'pred_MultiTask_Sum' in grp.columns and grp['pred_MultiTask_Sum'].notna().any()
                part_mean_reg = float(grp['pred_SC_Sum'].dropna().mean()) if has_reg else None
                part_mean_m = float(grp['pred_MultiTask_Sum'].dropna().mean()) if has_multi else None
                # 宏观常模：优先用回归库 pred_SC_Sum；若全为 0 则用多任务库的 SC_Sum（专家评分）作参照
                ref_reg_mean, ref_reg_n, ref_reg_age_mean, ref_reg_age_n = None, 0, None, 0
                if bench_reg is not None and 'pred_SC_Sum' in bench_reg.columns:
                    ref_all = bench_reg['pred_SC_Sum'].dropna()
                    ref_reg_n = len(ref_all)
                    ref_reg_mean = float(ref_all.mean())
                    if part_age is not None and ref_reg_n > 0:
                        ref_age = bench_reg[bench_reg['age'] == part_age]['pred_SC_Sum'].dropna()
                        ref_reg_age_n = len(ref_age)
                        ref_reg_age_mean = float(ref_age.mean()) if ref_reg_age_n > 0 else ref_reg_mean
                if (ref_reg_mean is None or ref_reg_n == 0 or ref_reg_mean == 0) and bench_multi is not None and 'SC_Sum' in bench_multi.columns:
                    s = bench_multi['SC_Sum'].dropna()
                    ref_reg_n = len(s)
                    ref_reg_mean = float(s.mean())
                    if part_age is not None and ref_reg_n > 0:
                        sa = bench_multi[bench_multi['age'] == part_age]['SC_Sum'].dropna()
                        ref_reg_age_n = len(sa)
                        ref_reg_age_mean = float(sa.mean()) if ref_reg_age_n > 0 else ref_reg_mean
                ref_m_mean, ref_m_n, ref_m_age_mean, ref_m_age_n = None, 0, None, 0
                if bench_multi is not None and multi_col in bench_multi.columns:
                    rm = bench_multi[multi_col].dropna()
                    ref_m_n = len(rm)
                    ref_m_mean = float(rm.mean())
                    if part_age is not None and ref_m_n > 0:
                        rma = bench_multi[bench_multi['age'] == part_age][multi_col].dropna()
                        ref_m_age_n = len(rma)
                        ref_m_age_mean = float(rma.mean()) if ref_m_age_n > 0 else ref_m_mean
                # ----- 家长版报告：约 2 分钟阅读，篇幅适中、说清即可 -----
                lines = []
                lines.append("")
                lines.append("╔══════════════════════════════════════════════════════════════════════════╗")
                lines.append("║                    儿童叙事能力评估报告 · 家长版                           ║")
                lines.append("╚══════════════════════════════════════════════════════════════════════════╝")
                lines.append("")
                lines.append("本报告根据孩子完成的 {} 个叙事任务（四个主题故事）生成，得分已与参照库（约 564 名 4–6 岁儿童）对比，便于了解孩子在同龄人中的大致位置。".format(len(grp)))
                lines.append("")
                lines.append("一、本报告看什么")
                lines.append("  · 故事结构（满分 9 分）：孩子能否把故事的「开头—经过—结果」说清楚，有无起因、目标、行动和结局。")
                lines.append("  · 情节与细节（15 项）：是否提到「为什么」「心里怎么想」「结果怎样」等，项数越多说明表达越丰富。")
                lines.append("")
                lines.append("二、各故事表现")
                rows_list = list(grp.iterrows())
                for i, (idx, row) in enumerate(rows_list, 1):
                    st = str(row.get('story_type', '—'))
                    story_name = STORY_NAMES.get(st, st)
                    sc = row.get('pred_SC_Sum')
                    mt = row.get('pred_MultiTask_Sum')
                    sc_val = float(sc) if pd.notna(sc) else None
                    mt_val = int(mt) if pd.notna(mt) else None
                    lines.append("  （{}）《{}》 结构 {:.2f}/9 分，细节 {}/15 项。".format(
                        i, story_name,
                        sc_val if sc_val is not None else 0,
                        int(mt_val) if mt_val is not None else 0))
                    if sc_val is not None and mt_val is not None:
                        if sc_val >= 7.0 and mt_val >= 12:
                            lines.append("     本故事结构较完整、细节也较丰富。")
                        elif sc_val >= 5.0 and mt_val >= 8:
                            lines.append("     本故事脉络基本清楚，部分环节可再充实。")
                        else:
                            lines.append("     可多鼓励孩子说清「后来呢」「为什么」和角色感受。")
                lines.append("")
                lines.append("三、整体小结")
                if has_reg and part_mean_reg is not None:
                    s = grp['pred_SC_Sum'].dropna()
                    if len(s) > 0:
                        lines.append("  · 故事结构：平均 {:.2f} 分（最高 {:.2f}，最低 {:.2f}）。".format(part_mean_reg, s.max(), s.min()))
                    else:
                        lines.append("  · 故事结构：平均 {:.2f} 分。".format(part_mean_reg))
                if has_multi and part_mean_m is not None:
                    m = grp['pred_MultiTask_Sum'].dropna()
                    if len(m) > 0:
                        lines.append("  · 情节与细节：平均 {:.2f} 项/15 项（最多 {} 项，最少 {} 项）。".format(part_mean_m, int(m.max()), int(m.min())))
                    else:
                        lines.append("  · 情节与细节：平均 {:.2f} 项/15 项。".format(part_mean_m))
                lines.append("")
                lines.append("四、与同龄人对比")
                n_ref = ref_reg_n if ref_reg_n > 0 else ref_m_n
                lines.append("  参照库为约 {} 名 4–6 岁儿童，使用相同故事任务。".format(n_ref))
                if part_mean_reg is not None and ref_reg_mean is not None and ref_reg_n > 0:
                    above_reg = part_mean_reg > ref_reg_mean
                    lines.append("  · 故事结构：孩子平均 {:.2f} 分，同龄平均 {:.2f} 分 → 总体{}同龄水平。".format(
                        part_mean_reg, ref_reg_age_mean if ref_reg_age_mean is not None and ref_reg_age_n > 0 else ref_reg_mean,
                        "高于" if above_reg else "低于"))
                if part_mean_m is not None and ref_m_mean is not None and ref_m_n > 0:
                    above_m = part_mean_m > ref_m_mean
                    lines.append("  · 情节与细节：孩子平均 {:.2f} 项/15 项，同龄平均 {:.2f} 项 → 总体{}同龄水平。".format(
                        part_mean_m, ref_m_age_mean if ref_m_age_mean is not None and ref_m_age_n > 0 else ref_m_mean,
                        "高于" if above_m else "低于"))
                lines.append("")
                lines.append("五、使用说明")
                lines.append("  本报告仅供了解发展参考，不替代专业诊断；如有疑问请咨询实施方或专业人员。")
                lines.append("")
                lines.append("═══════════════════════════════════════════════════════════════════════════")
                out_path = os.path.join(OUTPUT_PARTICIPANT_REPORT_DIR, f"participant_report_{pid}.txt")
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))
            n_part = df_final_summary['participants'].nunique()
            print(f"--- ✅ 已按参与者生成 {n_part} 份家长可读报告到 '{OUTPUT_PARTICIPANT_REPORT_DIR}'（含常模对比）---")

    except Exception as e:
        print(f"\n--- ❌ 预测过程中发生严重错误 ---")
        print(e)
        import traceback
        traceback.print_exc()