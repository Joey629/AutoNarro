# 项目脚本说明 (Annotation)

本仓库为儿童叙事能力自动评估流水线，包含：**多任务微观结构分类（A2–A16）**、**宏观结构复杂度回归（SC_E1/E2/E3/Sum）**、**线索生成（BART）** 与 **预测/报告（new_data → 家长版报告）**。

**命名约定（2025 起）：**  
- `train_*`：训练脚本  
- `analyze_*`：分析与错误诊断（含元数据统计）  
- `bart_cue_*`：BART 线索生成相关  
- `*_ablation_*`：多任务消融实验  

---

## 一、预测与报告（上线使用）

| 脚本 | 说明 |
|------|------|
| **predict_and_report.py** | **主入口**。读取 `new_data.csv`，对每条叙事执行：BART 线索 + Jieba 自动特征 + BERT 多任务 + XGBoost 宏观回归；常模对比；可按 `participants` 生成家长版简明报告。讲述/复述使用不同多任务阈值（Telling 0.52 / Retelling 0.58）。 |

---

## 二、训练脚本

### 2.1 多任务分类（微观结构 A2–A16）

| 脚本 | 说明 |
|------|------|
| **train.py** | 统一多任务训练（K 折、F-beta、最优阈值等），输出 BERT+LoRA 权重（如 `best_model_*.pth`）。 |
| **train_single.py** | 单任务学习：对 A2–A16 中某一任务单独训练分类器。 |
| **train_multitask_cue_augmented.py** | 线索增强多任务（与 predict 模板一致）：问题模板 + BART/线索词。 |
| **train_multitask_ablation_no_qa.py** | 消融：仅任务 ID，无自然语言问题。 |
| **train_multitask_ablation_no_ist.py** | 消融：保留问题模板，移除 IST（内部状态）线索词。 |

### 2.2 宏观复杂度回归（SC_E1 / SC_E2 / SC_E3 / SC_Sum）

| 脚本 | 说明 |
|------|------|
| **regression_analysis_final.py** | 使用 **narratives.csv** 中预计算语言学特征 + BERT 嵌入训练 3 个 XGBoost，保存到 `champion_models_*`。 |
| **train_final_automated_model.py** | 全自动回归：BART 线索 + 10 维自动特征 + BERT → `automated_champion_models/`，供 predict 优先加载。 |

### 2.3 线索生成（BART / 模块 B）

| 脚本 | 说明 |
|------|------|
| **train_bart_cue_generator.py** | 使用 BART-base-chinese 训练「叙事 → 线索词」Seq2Seq，保存到 `model_b_bart_structured_generator/`。 |

---

## 三、特征与推理辅助

| 脚本 | 说明 |
|------|------|
| **linguistic_feature_extractor.py** | Jieba A 类特征（TNW、TDW、TNU、MLU 等），`extract_calculable_features(text)`。 |
| **automated_feature_extractor.py** | A 类 + BART 线索 + 6 类内部状态计数 → 10 维自动特征。 |
| **bart_cue_predictor.py** | 加载 BART 目录，生成 `predicted_ist_words`（类名仍为 `BartPredictor`）。需先运行 `train_bart_cue_generator.py`。 |

---

## 四、分析与错误分析

| 脚本 | 说明 |
|------|------|
| **analyze_multitask_metadata.py** | 多任务预测后的元数据分析与可视化（年龄、留守、主题等）。 |
| **analyze_regression_metadata.py** | 回归冠军模型全量预测后的元数据分析（R²、分组检验、交互等）。 |
| **analyze_regression_bert_full.py** | BERT Global/Hierarchical + 语言学特征 + XGBoost 的完整回归分析流程。 |
| **analyze_multitask_errors.py** | 多任务在测试集上的错误样本筛选（可按任务指定）。 |
| **analyze_regression_errors.py** | 回归 SC_E1/E2/E3 的大误差样本分析。 |

---

## 五、模型与产出文件（参考）

- **best_model_*_macrof1_*.pth**：多任务 BERT+LoRA 权重。  
- **model_b_bart_structured_generator/**：由 **train_bart_cue_generator.py** 产出。  
- **champion_models_best_model_*/**：由 **regression_analysis_final.py** 或 **analyze_regression_bert_full.py** 产出。  
- **automated_champion_models/**：由 **train_final_automated_model.py** 产出。  
- **batch_reports/participant_reports/**：**predict_and_report.py** 生成的家长版报告。  
- **batch_predictions_summary.csv**：批量预测汇总（本地生成，默认不提交 git）。
