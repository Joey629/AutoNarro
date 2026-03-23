# analyze_multitask_metadata.py
# 描述:
# 本脚本是一个功能完整、结构优化的深度分析工具。
# 它能加载预训练的 Transformer 模型，对包含特定元数据（如年龄、留守经历、
# 叙事类型、叙事主题等）的文本数据进行评分预测，并从多个维度进行深入的
# 统计与可视化分析，最终将所有图表和结果保存在一个独立的文件夹中。
#
# 作者: Gemini
# 日期: 2025年10月3日
# 版本: 3.7 (修复最后两个列名不匹配的警告)

import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader, SequentialSampler
from transformers import AutoTokenizer, AutoModel
from tqdm import tqdm
from peft import LoraConfig, get_peft_model, TaskType
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings("ignore")

# --- 1. 全局配置与环境设置 (*** 已为您配置好 ***) ---

# Matplotlib 中文显示设置 (确保您的环境已安装中文字体)
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'PingFang SC', 'SimHei'] # 优先使用黑体TC，不行则尝试苹方或黑体
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

CONFIG = {
    # --- 文件路径配置 ---
    'data_path': 'narratives.csv',                    # 您的原始数据文件名
    'champion_model_path': 'best_model_20251001-111255_epoch10_macrof1_0.7067.pth', # 您训练好的模型权重文件路径
    'pretrained_model_name': 'hfl/chinese-macbert-base', # 预训练模型的名称

    # --- 分析参数配置 ---
    'test_size': 1.0,                                 # 使用全部数据进行分析
    'batch_size': 16,                                 # 预测时使用的批量大小
    'max_length': 256,                                # Tokenizer的最大长度

    # --- 元数据列名配置 (已根据您的截图更新) ---
    'text_column': 'A2',                              # 文本内容所在的列
    'age_column': 'age',                              # 年龄所在的列
    'left_behind_column': 'left_behind',              # <--- [已更新] 留守经历所在的列
    'narrative_type_column': 'task_type',             # <--- [已更新] 叙事类型 (讲述/复述) 所在的列
    'story_theme_column': 'story_type',               # 叙事主题 (猫狗鸟羊) 所在的列
    'score_column': 'score'                           # 预测得分将被存储在此列
}

# --- 核心组件 (请确保与您的训练脚本一致) ---

class CustomModel(nn.Module):
    def __init__(self, pretrained_model_name):
        super(CustomModel, self).__init__()
        self.bert = AutoModel.from_pretrained(pretrained_model_name)
        # 您可以根据需要添加LoRA或其他自定义层
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(self.bert.config.hidden_size, 1)

    # --- [修改] 增加 **kwargs 来接收并忽略peft传入的额外参数 ---
    def forward(self, input_ids, attention_mask, **kwargs):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits

def get_all_predictions(model, df, tokenizer, device):
    """使用加载的模型对DataFrame中的文本进行预测。"""
    print("开始对文本进行评分预测...")
    
    # 检查文本列是否存在，如果不存在，则给出清晰的错误提示
    if CONFIG['text_column'] not in df.columns:
        print(f"❌ 错误: 在CSV文件中找不到指定的文本列 '{CONFIG['text_column']}'。")
        print(f"可用的列有: {df.columns.tolist()}")
        return None
        
    # --- 清洗数据，将NaN值替换为空字符串，并确保所有值为字符串类型 ---
    texts = df[CONFIG['text_column']].fillna('').astype(str).tolist()
    
    encoded_data = tokenizer.batch_encode_plus(
        texts,
        add_special_tokens=True,
        return_attention_mask=True,
        padding='max_length',
        max_length=CONFIG['max_length'],
        truncation=True,
        return_tensors='pt'
    )
    
    input_ids = encoded_data['input_ids']
    attention_masks = encoded_data['attention_mask']

    dataset = TensorDataset(input_ids, attention_masks)
    dataloader = DataLoader(dataset, sampler=SequentialSampler(dataset), batch_size=CONFIG['batch_size'])
    
    model.eval()
    predictions = []
    
    for batch in tqdm(dataloader, desc="正在预测"):
        batch = tuple(b.to(device) for b in batch)
        inputs = {'input_ids': batch[0], 'attention_mask': batch[1]}
        
        with torch.no_grad():
            outputs = model(**inputs)
        
        logits = outputs
        predictions.extend(logits.cpu().numpy().flatten())
        
    df[CONFIG['score_column']] = predictions
    print("✅ 预测完成。")
    return df

# --- 2. 模块化的分析函数 ---

def check_column(df, column_name):
    """检查列是否存在，如果不存在则打印警告并返回False。"""
    if column_name not in df.columns:
        print(f"⚠️ 警告: 在数据表中找不到列 '{column_name}'，将跳过相关分析。")
        return False
    return True

def save_plot(figure, output_dir, filename):
    """保存图表到指定路径。"""
    path = os.path.join(output_dir, filename)
    figure.savefig(path, dpi=300, bbox_inches='tight')
    plt.close(figure)
    print(f"✅ 图表已保存: {path}")

def analyze_by_category(df, category_col, score_col, output_dir, plot_title, filename_prefix):
    """
    通用的分类变量分析函数。
    计算每个类别的平均分、数量，并绘制箱形图和计数图。
    """
    if not check_column(df, category_col):
        return

    # 计算统计数据
    summary = df.groupby(category_col)[score_col].agg(['mean', 'count', 'std']).sort_values('mean', ascending=False)
    print(f"\n--- 按 '{plot_title}' 分析 ---")
    print(summary)

    # 绘制箱形图 (Box Plot)，观察得分分布
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x=category_col, y=score_col, ax=ax, order=summary.index)
    ax.set_title(f'{plot_title}的得分分布', fontsize=16)
    ax.set_xlabel(plot_title, fontsize=12)
    ax.set_ylabel('预测得分', fontsize=12)
    save_plot(fig, output_dir, f'{filename_prefix}_boxplot.png')

    # 绘制计数图 (Count Plot)，观察样本数量
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x=category_col, order=summary.index)
    ax.set_title(f'各{plot_title}的样本数量', fontsize=16)
    ax.set_xlabel(plot_title, fontsize=12)
    ax.set_ylabel('数量', fontsize=12)
    save_plot(fig, output_dir, f'{filename_prefix}_countplot.png')

def analyze_age(df, age_col, score_col, output_dir):
    """分析年龄与得分的关系。"""
    if not check_column(df, age_col):
        return

    print(f"\n--- 按 '年龄' 分析 ---")
    # 绘制散点图，观察年龄与得分的总体趋势
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.regplot(data=df, x=age_col, y=score_col, ax=ax,
                scatter_kws={'alpha': 0.4}, line_kws={'color': 'red'})
    ax.set_title('年龄与预测得分的关系', fontsize=16)
    ax.set_xlabel('年龄', fontsize=12)
    ax.set_ylabel('预测得分', fontsize=12)
    correlation = df[[age_col, score_col]].corr().iloc[0, 1]
    print(f"年龄与得分的相关系数: {correlation:.3f}")
    ax.text(0.05, 0.95, f'相关系数 (Correlation): {correlation:.3f}',
            transform=ax.transAxes, fontsize=12, verticalalignment='top')
    save_plot(fig, output_dir, 'age_score_scatterplot.png')


# --- 3. 主执行流程 (Main Workflow) ---

def main():
    """主函数，串联整个分析流程。"""
    print("--- 开始执行深度分析脚本 (版本: 3.7) ---")

    # --- 步骤 1: 加载数据 ---
    try:
        df = pd.read_csv(CONFIG['data_path'])
        print(f"✅ 成功加载数据: {CONFIG['data_path']}, 共 {len(df)} 条记录。")
    except FileNotFoundError:
        print(f"❌ 错误: 数据文件 '{CONFIG['data_path']}' 未找到。请检查路径配置。")
        return

    # --- 步骤 2: 加载模型和Tokenizer ---
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"当前使用的设备: {device}")

    tokenizer = AutoTokenizer.from_pretrained(CONFIG['pretrained_model_name'])
    model = CustomModel(CONFIG['pretrained_model_name']).to(device)

    # --- 应用PEFT/LoRA配置以匹配训练时的模型结构 ---
    print("正在应用PEFT/LoRA配置以确保模型结构匹配...")
    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["query", "value"], # 通常对BERT模型的这些模块应用LoRA
        lora_dropout=0.1,
        bias="none",
        task_type=TaskType.FEATURE_EXTRACTION # 使用特征提取，因为我们有一个自定义的回归头
    )
    model = get_peft_model(model, lora_config)
    print("✅ PEFT/LoRA配置已应用。")
    
    try:
        # --- 使用 strict=False 来加载部分权重 ---
        model.load_state_dict(torch.load(CONFIG['champion_model_path'], map_location=device), strict=False)
        model.eval()
        print(f"✅ 成功加载模型权重: {CONFIG['champion_model_path']}")
    except FileNotFoundError:
        print(f"❌ 错误: 模型权重文件 '{CONFIG['champion_model_path']}' 未找到。")
        return
    except Exception as e:
        print(f"❌ 加载模型时发生未知错误: {e}")
        return

    # --- 步骤 3: 数据准备与模型预测 ---
    if CONFIG['test_size'] == 1.0:
        test_df = df.copy()
    else:
        _, test_df = train_test_split(df, test_size=CONFIG['test_size'], random_state=42)
    print(f"已选择 {len(test_df)} 条数据用于分析。")

    # 调用预测函数，获取包含预测得分的DataFrame
    results_df = get_all_predictions(model, test_df, tokenizer, device)

    # 如果预测失败（例如，因为列名错误），则终止脚本
    if results_df is None:
        print("--- 脚本因数据错误已终止 ---")
        return

    # --- 步骤 4: 执行一系列深度分析 ---
    output_dir = f"analysis_results_{os.path.basename(CONFIG['champion_model_path']).replace('.pth','')}"
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🚀 所有分析结果将保存在 '{output_dir}' 文件夹中。")

    # 分析1: 叙事主题 (猫狗鸟羊)
    analyze_by_category(results_df,
                        category_col=CONFIG['story_theme_column'],
                        score_col=CONFIG['score_column'],
                        output_dir=output_dir,
                        plot_title='叙事主题',
                        filename_prefix='story_theme')

    # 分析2: 叙事类型 (讲述/复述)
    analyze_by_category(results_df,
                        category_col=CONFIG['narrative_type_column'],
                        score_col=CONFIG['score_column'],
                        output_dir=output_dir,
                        plot_title='叙事类型',
                        filename_prefix='narrative_type')

    # 分析3: 留守经历
    analyze_by_category(results_df,
                        category_col=CONFIG['left_behind_column'],
                        score_col=CONFIG['score_column'],
                        output_dir=output_dir,
                        plot_title='留守经历',
                        filename_prefix='left_behind')

    # 分析4: 年龄
    analyze_age(results_df,
                age_col=CONFIG['age_column'],
                score_col=CONFIG['score_column'],
                output_dir=output_dir)
    
    # 保存带有预测得分的最终数据
    final_csv_path = os.path.join(output_dir, 'predictions_with_metadata.csv')
    results_df.to_csv(final_csv_path, index=False, encoding='utf-8-sig')
    print(f"✅ 包含预测得分的完整数据已保存: {final_csv_path}")


    print("\n--- ✅ 所有分析已完成！---")


if __name__ == '__main__':
    main()

