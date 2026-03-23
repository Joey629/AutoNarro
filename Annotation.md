# 项目脚本说明 (Annotation)

本仓库为儿童叙事能力自动评估流水线，包含：**多任务微观结构分类（A2–A16）**、**宏观结构复杂度回归（SC_E1/E2/E3/Sum）**、**线索生成（BART）** 与 **预测/报告（new_data → 家长版报告）**。以下为各脚本用途简介。

---

## 一、预测与报告（上线使用）

| 脚本 | 说明 |
|------|------|
| **predict_and_report.py** | **主入口**。读取 `new_data.csv`，对每条叙事执行：BART 线索生成 + Jieba 自动特征 + BERT 多任务分类 + XGBoost 宏观回归；输出单条数值、常模对比，并可按 `participants` 汇总生成家长版简明报告（约 2 分钟阅读）。支持按任务类型（讲述/复述）使用不同多任务阈值（Telling 0.52 / Retelling 0.58）。 |

---

## 二、训练脚本

### 2.1 多任务分类（微观结构 A2–A16）

| 脚本 | 说明 |
|------|------|
| **train.py** | 统一多任务训练脚本（K 折、F-beta、最优阈值等），输出 BERT+LoRA 权重（如 `best_model_*.pth`），供预测与错误分析使用。 |
| **train_single.py** | 单任务学习：对 A2–A16 中某一任务单独训练一个分类器，用于对比或消融。 |
| **train_clue_augmented_model.py** | 线索增强多任务训练（最终版）：输入为「问题模板 + BART/线索词」，与当前 predict 使用的模板一致，产出多任务权重。 |
| **train_clue_augmented_noQA.py** | 实验变体 A：仅保留任务 ID，移除自然语言问题，用于消融。 |
| **train_clue_augmented_noist.py** | 实验变体 B：保留问题模板，移除 IST（内部状态）线索词。文件名 `noist` 即 no-IST。 |

### 2.2 宏观复杂度回归（SC_E1 / SC_E2 / SC_E3 / SC_Sum）

| 脚本 | 说明 |
|------|------|
| **regression_analysis_final.py** | 使用 **narratives.csv** 中已有语言学特征列 + BERT 嵌入，训练 3 个 XGBoost 回归模型（E1/E2/E3），并保存到 `champion_models_*`。需预计算语言学特征，与全自动流水线特征集不同。 |
| **train_final_automated_model.py** | **全自动**宏观回归训练：仅用 BART 线索 + `automated_feature_extractor` 的 10 维自动特征 + BERT 嵌入训练 XGBoost，输出 `automated_champion_models/auto_xgb_model_*.joblib`，供 `predict_and_report.py` 优先加载。 |

### 2.3 线索生成（BART / 模块 B）

| 脚本 | 说明 |
|------|------|
| **train_model_b_t5_generator.py** | 使用 BART-base-chinese 在 `narratives.csv` 上训练「叙事 → 线索词」的 Seq2Seq 模型，保存到 `model_b_bart_structured_generator`，供 `bart_predictor` 与全自动流水线调用。 |

---

## 三、特征与推理辅助

| 脚本 | 说明 |
|------|------|
| **linguistic_feature_extractor.py** | 基于 Jieba 的 A 类语言学特征提取（TNW、TDW、TNU、MLU、连接词、从句等），提供 `extract_calculable_features(text)`，被 `automated_feature_extractor` 调用。 |
| **automated_feature_extractor.py** | 在 A 类基础上，用 BART 生成线索串 + 关键词匹配，自动计算 6 类内部状态计数（IS_Per/Phy/Con/Emo/Men/Ling）等，输出 10 维自动特征，供全自动回归与 predict 使用。依赖 `linguistic_feature_extractor`。 |
| **bart_predictor.py** | 加载已训练的 BART 模型目录，对输入叙事生成 `predicted_ist_words` 字符串，供 BERT 多任务输入与自动特征提取使用。需先运行 `train_model_b_t5_generator.py`。 |

---

## 四、分析与错误分析

| 脚本 | 说明 |
|------|------|
| **analysis.py** | 多任务分类的元数据分析与可视化：加载多任务权重，对 narratives 预测，按年龄/留守/主题等维度做统计与图表，输出到指定文件夹。 |
| **analysis_reg.py** | 宏观复杂度回归的元数据分析：加载 XGBoost 冠军模型（需预先存在语言学特征列），全量预测，做 R²、相关性、分组检验与交互分析等。配置与 `regression_analysis_final` 所用特征列需一致。 |
| **analysis_reg_update_12.py** | 带 BERT 的回归分析完整版：用 BERT 提取 Global/Hierarchical 特征，与语言学特征拼接后加载 XGBoost 做预测与评估，产出与 `regression_analysis_final` 类似的冠军模型及分析结果。 |
| **analyze_errors.py** | 多任务分类错误分析：在测试集上预测，按任务（如 A6、A11、A13、A16）筛选错误样本并输出，便于检查误判模式。依赖与训练时一致的问题模板与权重。 |
| **analyze_errors_regression.py** | 宏观复杂度回归错误分析：加载 BERT + XGBoost，在测试集上预测 SC_E1/E2/E3，筛选误差最大的样本并保存，用于检查回归异常案例。 |

---

## 五、模型与产出文件（参考）

- **best_model_20251001-111255_epoch10_macrof1_0.7067.pth**：多任务 BERT+LoRA 权重，被 predict、回归训练、错误分析等脚本共用。
- **model_b_bart_structured_generator/**：BART 线索生成模型目录，由 `train_model_b_t5_generator.py` 产出。
- **champion_models_best_model_*/**：由 `regression_analysis_final.py` 或 `analysis_reg_update_12.py` 产出的 XGBoost 回归模型（E1/E2/E3）。
- **automated_champion_models/**：由 `train_final_automated_model.py` 产出的全自动 XGBoost 模型，predict 优先使用。
- **batch_reports/participant_reports/**：`predict_and_report.py` 按 `participants` 生成的家长版简明报告。
- **batch_predictions_summary.csv**：predict 对 `new_data.csv` 的批量预测汇总表。
