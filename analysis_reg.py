# analysis_reg.py
# [目标]：
# 1. 加载 "Run 5" 训练好的 3 个冠军 XGBoost 模型。
# 2. 对 *所有* 564 条数据进行预测。
# 3. [优化] 执行深度元数据分析，并包含以下功能：
#    a. 模型评估：计算 真实总分 vs 预测总分 的 R² 和相关性。
#    b. 推断性统计：为所有分类比较（T检验/ANOVA）和相关性（Pearson r）报告 p-value。
#    c. 对比分析：对 "真实总分 (SC_Sum)" 和 "预测总分 (pred_SC_Sum)" 分别执行所有分析。
#    d. 交互分析：添加 "年龄 x 叙事类型" 的交互分析。
# 11月版本 （问题是多处报错）

import pandas as pd
import numpy as np
from tqdm import tqdm
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib 
import warnings
# [新增] 导入统计和评估库
import scipy.stats as stats
from sklearn.metrics import r2_score

warnings.filterwarnings("ignore")

# --- Matplotlib 中文显示设置 ---
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'PingFang SC', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# =============================================================================
# --- 1. 用户配置区 ---
# =============================================================================
CONFIG = {
    # --- 核心路径 ---
    'data_path': 'narratives.csv', # 确保您的原始数据文件在这里
    'champion_model_path': 'champion_models_run5', # 存放3个 .pkl 模型的文件夹
    'analysis_output_dir': 'analysis_results_optimized', # 最终产出文件夹
    'embedding_cache_path': 'embeddings_cache_all_data.npy', # 嵌入缓存 (可选, 加速)
    
    # --- 模型配置 ---
    'model_name': 'hfl/chinese-roberta-wwm-ext', 
    'max_length': 512,
    
    # --- 特征列 ---
    'linguistic_feature_columns': [
        'TNW', 'TDW', 'TNU', 'MLU', '顺承关系', '因果关系', '转折关系', '时间关系',
        '假设关系', '并列/递进关系', 'conj_token', 'conj_type', 'Cohension',
        '关系从句', '宾语从句', '主语从句', '连动结构', '兼语结构', '描述性从句',
        '把字句', '被字句', '介词短语', '复杂状态句', '状语从句', 'Sentences_token',
        'Sentence_type', 'IS_Per', 'IS_Phy', 'IS_Con', 'IS_Emo', 'IS_Men',
        'IS_Ling', 'IS_Token', 'IS_Type'
    ],
    
    # --- 目标列 ---
    'target_columns': ['SC_E1', 'SC_E2', 'SC_E3'],
    
    # --- [优化] 元数据列 (用于新分析) ---
    'metadata_columns': {
        'age_column': 'age',
        'left_behind_column': 'left_behind',
        'story_theme_column': 'story_type',
        'narrative_type_column': 'task_type'
    },
    
    # --- [优化] 真实值与预测值列 (用于对比) ---
    'real_score_col': 'SC_Sum',
    'pred_score_col': 'pred_SC_Sum'
}

# =============================================================================
# --- 步骤 1: 特征工程 (与原脚本相同) ---
# ... (为简洁, 假设 get_text_embeddings 函数已定义并可正常工作) ...
# ... (我们将跳过 RoBERTa 嵌入的耗时步骤，直接加载数据) ...

def load_data_and_features(config):
    """
    加载原始数据，处理语言学特征中的错误值。
    (跳过了嵌入步骤，假设后续直接使用语言学特征)
    """
    print("--- 步骤 1: 加载数据和特征 ---")
    try:
        df = pd.read_csv(config['data_path'])
    except FileNotFoundError:
        print(f"错误: 未找到数据文件 {config['data_path']}")
        return None

    # [修复] 转换语言学特征为数值型，处理 '#REF!' 等错误
    for col in config['linguistic_feature_columns']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        else:
            print(f"警告: 特征列 {col} 在数据中未找到，将跳过。")
            
    # 填充 NaN (XGBoost 不接受 NaN)
    df[config['linguistic_feature_columns']] = df[config['linguistic_feature_columns']].fillna(0)
    
    print("数据加载和特征预处理完成。")
    return df

# =============================================================================
# --- 步骤 2: 加载模型并预测 (与原脚本相同) ---
# =============================================================================
def load_champion_models_and_predict(df, config):
    """
    加载3个预训练的XGBoost模型，并对数据进行预测。
    """
    print("\n--- 步骤 2: 加载模型并执行预测 ---")
    
    # 准备特征矩阵 X (仅语言学特征)
    X = df[config['linguistic_feature_columns']]
    
    results_df = df.copy()
    
    for target_col in config['target_columns']:
        model_path = os.path.join(config['champion_model_path'], f'xgb_champion_{target_col}.pkl')
        pred_col = f'pred_{target_col}'
        
        try:
            # 加载模型
            model = joblib.load(model_path)
            
            # 执行预测
            predictions = model.predict(X)
            results_df[pred_col] = predictions
            print(f"✅ 成功加载模型 {model_path} 并生成预测 {pred_col}")
            
        except FileNotFoundError:
            print(f"❌ 错误: 找不到模型文件 {model_path}。请检查路径。")
            results_df[pred_col] = np.nan
        except Exception as e:
            print(f"❌ 加载或预测 {target_col} 时出错: {e}")
            results_df[pred_col] = np.nan

    # 计算预测总分
    pred_cols = [f'pred_{col}' for col in config['target_columns']]
    results_df[config['pred_score_col']] = results_df[pred_cols].sum(axis=1)
    
    # 确保真实总分 SC_Sum 也存在 (假设它在 narratives.csv 中)
    if config['real_score_col'] not in results_df.columns:
        print(f"警告: 真实总分列 {config['real_score_col']} 不在数据中，模型评估将受限。")
        # 如果不存在，尝试从 E1, E2, E3 相加
        if all(col in results_df.columns for col in config['target_columns']):
            results_df[config['real_score_col']] = results_df[config['target_columns']].sum(axis=1)
            print(f"已通过 E1+E2+E3 创建 {config['real_score_col']}")
        
    print("所有预测已完成。")
    return results_df

# =============================================================================
# --- 步骤 3: [优化] 分类变量分析 (含 T检验/ANOVA) ---
# =============================================================================
def analyze_by_category(results_df, category_col, score_col, output_dir, plot_title, score_suffix=''):
    """
    [优化]
    1. 绘制箱线图。
    2. 执行推断性统计 (T-test 或 ANOVA) 并打印 p-value。
    3. 文件名包含 score_col 和 suffix 以区分。
    """
    print(f"\n--- 分析: {plot_title} vs {score_col}{score_suffix} ---")
    
    # 1. 描述性统计
    grouped_stats = results_df.groupby(category_col)[score_col].agg(['mean', 'std', 'count']).sort_values(by='mean', ascending=False)
    print("描述性统计 (均值, 标准差):")
    print(grouped_stats)

    # 2. 推断性统计
    groups = results_df[category_col].unique()
    group_data = [results_df[results_df[category_col] == g][score_col].dropna() for g in groups]

    stat_result = ""
    try:
        if len(groups) == 2:
            # T-检验
            t_stat, p_val = stats.ttest_ind(group_data[0], group_data[1], equal_var=False) # Welch's T-test
            stat_result = f"T-test: t = {t_stat:.3f}, p = {p_val:.4f}"
        elif len(groups) > 2:
            # ANOVA
            f_stat, p_val = stats.f_oneway(*group_data)
            stat_result = f"ANOVA: F = {f_stat:.3f}, p = {p_val:.4f}"
        print(f"统计检验结果: {stat_result}")
    except Exception as e:
        print(f"统计检验失败: {e}")

    # 3. 可视化 (箱线图)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=category_col, y=score_col, data=results_df, 
                order=grouped_stats.index) # 按均值排序
    
    full_plot_title = f'{plot_title} vs {score_col}{score_suffix}\n{stat_result}'
    plt.title(full_plot_title, fontsize=16)
    plt.ylabel(f"得分 ({score_col}{score_suffix})", fontsize=12)
    plt.xlabel(f"{plot_title}", fontsize=12)
    plt.tight_layout()
    
    # 确保文件名清晰
    plot_filename = f'{category_col}_vs_{score_col}{score_suffix}_boxplot.png'
    plot_path = os.path.join(output_dir, plot_filename)
    plt.savefig(plot_path)
    plt.close()
    print(f"图表已保存: {plot_path}")

# =============================================================================
# --- 步骤 4: [优化] 年龄分析 (含 Pearson 相关) ---
# =============================================================================
def analyze_age(results_df, age_col, score_col, output_dir, score_suffix=''):
    """
    [优化]
    1. 绘制回归散点图。
    2. 计算并报告 Pearson r 和 p-value。
    3. 文件名包含 score_col 和 suffix 以区分。
    """
    print(f"\n--- 分析: 年龄 vs {score_col}{score_suffix} ---")
    
    # 1. 统计检验 (Pearson Correlation)
    df_clean = results_df[[age_col, score_col]].dropna()
    try:
        r_val, p_val = stats.pearsonr(df_clean[age_col], df_clean[score_col])
        stat_result = f"Pearson r = {r_val:.3f}, p = {p_val:.4f}"
        print(f"统计检验结果: {stat_result}")
    except Exception as e:
        print(f"统计检验失败: {e}")
        r_val, p_val = 0, 99

    # 2. 可视化 (回归散点图)
    plt.figure(figsize=(10, 6))
    sns.regplot(x=age_col, y=score_col, data=df_clean,
                x_jitter=0.1, # 增加少量抖动以看清数据点
                scatter_kws={'alpha': 0.3})
    
    full_plot_title = f'年龄 vs {score_col}{score_suffix}\n{stat_result}'
    plt.title(full_plot_title, fontsize=16)
    plt.ylabel(f"得分 ({score_col}{score_suffix})", fontsize=12)
    plt.xlabel("年龄", fontsize=12)
    plt.tight_layout()
    
    plot_filename = f'{age_col}_vs_{score_col}{score_suffix}_scatterplot.png'
    plot_path = os.path.join(output_dir, plot_filename)
    plt.savefig(plot_path)
    plt.close()
    print(f"图表已保存: {plot_path}")

# =============================================================================
# --- 步骤 5: [新增] 模型性能评估 ---
# =============================================================================
def evaluate_model_performance(results_df, real_col, pred_col, output_dir):
    """
    [新增]
    1. 计算 R² 和 Pearson r。
    2. 绘制 真实值 vs 预测值 散点图。
    """
    print(f"\n--- 步骤 5: 模型性能评估 ({real_col} vs {pred_col}) ---")
    
    df_clean = results_df[[real_col, pred_col]].dropna()
    
    # 1. 计算指标
    try:
        r_val, p_val = stats.pearsonr(df_clean[real_col], df_clean[pred_col])
        r2_val = r2_score(df_clean[real_col], df_clean[pred_col])
        
        print(f"评估指标:")
        print(f"  Pearson r: {r_val:.4f} (p = {p_val:.4g})")
        print(f"  R-squared (R²): {r2_val:.4f}")
        stat_result = f"Pearson r = {r_val:.3f}, R² = {r2_val:.3f}"
        
    except Exception as e:
        print(f"计算评估指标失败: {e}")
        stat_result = "评估失败"

    # 2. 可视化
    plt.figure(figsize=(8, 8))
    sns.regplot(x=real_col, y=pred_col, data=df_clean,
                scatter_kws={'alpha': 0.3, 's': 20},
                line_kws={'color': 'red', 'linestyle': '--'})
    
    # 绘制完美对角线 (y=x)
    min_val = min(df_clean[real_col].min(), df_clean[pred_col].min())
    max_val = max(df_clean[real_col].max(), df_clean[pred_col].max())
    plt.plot([min_val, max_val], [min_val, max_val], 'gray', linestyle=':')
    
    full_plot_title = f'模型性能: 真实值 vs 预测值\n({stat_result})'
    plt.title(full_plot_title, fontsize=16)
    plt.xlabel(f"真实得分 ({real_col})", fontsize=12)
    plt.ylabel(f"预测得分 ({pred_col})", fontsize=12)
    plt.axis('equal') # 确保x,y轴尺度相同
    plt.tight_layout()
    
    plot_path = os.path.join(output_dir, 'model_performance_real_vs_pred_scatterplot.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"图表已保存: {plot_path}")

# =============================================================================
# --- 步骤 6: [新增] 交互分析 ---
# =============================================================================
def analyze_interaction(results_df, cat_col, cont_col, score_col, output_dir, plot_title, score_suffix=''):
    """
    [新增]
    使用 seaborn.lmplot 分析分类变量和连续变量对得分的交互影响。
    """
    print(f"\n--- 交互分析: {plot_title} vs {score_col}{score_suffix} ---")
    
    try:
        # lmplot 是 Figure-level 接口, 用法稍有不同
        g = sns.lmplot(
            data=results_df.dropna(subset=[score_col, cont_col, cat_col]),
            x=cont_col,
            y=score_col,
            hue=cat_col, # 按分类变量着色并生成不同回归线
            height=7,
            aspect=1.2,
            scatter_kws={'alpha': 0.3, 's': 20}
        )
        
        full_plot_title = f'交互分析: {plot_title}\n(按 {cat_col} 分组)'
        g.fig.suptitle(full_plot_title, y=1.03, fontsize=16)
        g.set_axis_labels(f"{cont_col}", f"得分 ({score_col}{score_suffix})")

        plot_filename = f'interaction_{cat_col}_x_{cont_col}_vs_{score_col}{score_suffix}.png'
        plot_path = os.path.join(output_dir, plot_filename)
        plt.savefig(plot_path)
        plt.close(g.fig) # 关闭 Figure
        print(f"图表已保存: {plot_path}")

    except Exception as e:
        print(f"❌ 交互分析失败: {e}")


# =============================================================================
# --- 主执行函数 ---
# =============================================================================
def main():
    print("--- 开始执行优化版分析脚本 (analysis_reg_optimized.py) ---")
    
    # 创建输出文件夹
    output_dir = CONFIG['analysis_output_dir']
    os.makedirs(output_dir, exist_ok=True)
    
    # 步骤 1: 加载数据
    df = load_data_and_features(CONFIG)
    if df is None:
        return

    # 步骤 2: 执行预测
    results_df = load_champion_models_and_predict(df, CONFIG)
    
    print(f"\n{'='*30} 预测完成，进入分析阶段 {'='*30}")

    # 步骤 5: [新增] 首先进行模型性能评估
    evaluate_model_performance(results_df, 
                               CONFIG['real_score_col'], 
                               CONFIG['pred_score_col'], 
                               output_dir)

    # 步骤 6 & 7: [优化] 对 "真实值" 和 "预测值" 分别执行所有分析
    
    # 获取元数据列名
    meta_cols = CONFIG['metadata_columns']
    age_col = meta_cols['age_column']
    
    # 定义要分析的分类变量
    categories_to_analyze = [
        (meta_cols['story_theme_column'], '叙事主题'),
        (meta_cols['narrative_type_column'], '叙事类型'),
        (meta_cols['left_behind_column'], '留守经历')
    ]
    
    # [关键优化] 循环两次：一次分析真实总分，一次分析预测总分
    scores_to_analyze = [
        (CONFIG['real_score_col'], '_真实值'),  # (列名, 文件名后缀)
        (CONFIG['pred_score_col'], '_预测值')
    ]
    
    for score_col, score_suffix in scores_to_analyze:
        
        if score_col not in results_df.columns:
            print(f"\n警告: 找不到得分列 {score_col}，跳过对它的分析。")
            continue
            
        print(f"\n{'='*20} 正在分析 {score_col} (标记为: {score_suffix}) {'='*20}")
        
        # --- 分类变量分析 (原步骤 3/4) ---
        for col, title in categories_to_analyze:
            analyze_by_category(results_df, 
                                category_col=col, 
                                score_col=score_col,
                                output_dir=output_dir, 
                                plot_title=title, 
                                score_suffix=score_suffix)
        
        # --- 年龄分析 (原步骤 5) ---
        analyze_age(results_df, 
                    age_col=age_col, 
                    score_col=score_col,
                    output_dir=output_dir, 
                    score_suffix=score_suffix)

        # --- 交互分析 (原步骤 6) ---
        analyze_interaction(results_df,
                            cat_col=meta_cols['narrative_type_column'], # 叙事类型
                            cont_col=age_col, # 年龄
                            score_col=score_col,
                            output_dir=output_dir,
                            plot_title=f"年龄与叙事类型",
                            score_suffix=score_suffix)

    # 步骤 8: 保存最终数据
    final_csv_path = os.path.join(output_dir, 'predictions_with_metadata_ALL_DATA_OPTIMIZED.csv')
    try:
        results_df.to_csv(final_csv_path, index=False, encoding='utf-8-sig')
        print(f"\n✅ 包含所有预测得分和元数据的完整数据已保存: {final_csv_path}")
    except Exception as e:
        print(f"❌ 保存最终 CSV 失败: {e}")

    print("\n--- 优化版分析脚本执行完毕 ---")

if __name__ == "__main__":
    main()