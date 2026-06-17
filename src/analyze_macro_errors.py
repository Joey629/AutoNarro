# analyze_macro_errors.py
# 宏观回归 · 测试集指标 + SC_Sum 真值-预测散点 + 大残差样本 CSV（欠预测/过预测）。
# 与 analyze_micro_errors.py 并列：面向 XGB(SC_E1/E2/E3)，非多任务二分类 FP/FN。
#
# BERT 特征仅在 **微观同源测试集** 上计算（省算力、与 4.1.2 held-out 一致）。
# 元数据图 / predictions_with_scores / 子组表：再运行 analyze_macro_metadata.py。
# 共用逻辑见 analyze_macro_core.py
# 输出目录默认与脚本同名，见 config_analysis_output_paths.py。

import config_analysis_output_paths as arp
from analyze_macro_core import BASE_CONFIG, run_macro_analysis

CONFIG = {
    **BASE_CONFIG,
    "pipeline": "errors",
    "run_manifest_script": "analyze_macro_errors",
    "output_dir": arp.OUTPUT_ANALYZE_REGRESSION_ERRORS,
    # 以下为可改项（其余继承 BASE_CONFIG）
    # "micro_checkpoint": "M4_final_best_v3.pth",
    # "xgb_models_dir": None,  # None → champion_models_m4_regression_<ckpt_stem>/
    # "use_micro_prob_in_xgb": False,
    # "top_n_errors": 20,
    # "export_error_csv": True,
    # "output_dir": "custom_dir",
}

if __name__ == "__main__":
    run_macro_analysis(CONFIG)
