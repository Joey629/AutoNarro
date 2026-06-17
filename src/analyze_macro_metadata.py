# analyze_macro_metadata.py
# 宏观回归 · 亚组/元数据可视化：真值 SC_Sum 与 pred_SC_Sum 在年龄、留守、主题、讲述类型上的分布与交互图；
# 并写出 predictions_with_scores.csv（子集由 metadata_subset 决定）。
# 另：与 analyze_macro_errors 相同的 SC_Sum 真值–预测散点（R²、r、y=x）可由 run_sc_sum_scatter_in_metadata 打开，
# 对应论文中宏观「评估框架」下 predicted SC_Sum 与专家真值对齐图。
# 另：run_subgroup_performance_metrics → subgroup_regression_SC_Sum_<subset>.csv（按 age / task_type / 交叉 的 MSE、R²、r 等，审稿子组性能）。
# 与 analyze_micro_metadata.py 并列；输出目录默认与脚本同名（config_analysis_output_paths）。
# 不输出测试集 MSE 表与大残差 CSV（请用 analyze_macro_errors.py）。
# 宏观回归完整结果：先 analyze_macro_errors.py，再本脚本（输出目录不同，见 config_analysis_output_paths）。
#
# 共用逻辑见 analyze_macro_core.py

import config_analysis_output_paths as arp
from analyze_macro_core import BASE_CONFIG, run_macro_analysis

CONFIG = {
    **BASE_CONFIG,
    "pipeline": "metadata",
    "run_manifest_script": "analyze_macro_metadata",
    "output_dir": arp.OUTPUT_ANALYZE_REGRESSION_METADATA,
    # "test"：与 4.1.2 同 held-out； "full"：全队列 BERT+XGB（慢，用于探索）
    "metadata_subset": "test",
    "run_metadata_plots": True,
    "run_sc_sum_scatter_in_metadata": True,
    "sc_sum_scatter_title": "SC_Sum (test)",
    # 审稿补充：各年龄组、任务类型及交叉下的 SC_Sum 回归指标
    "run_subgroup_performance_metrics": True,
}

if __name__ == "__main__":
    run_macro_analysis(CONFIG)
