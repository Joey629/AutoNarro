# 训练与产物（Narro v4）

对齐 MAIN 框架：**宏观 SS** = 故事结构（A2–A16）；**宏观 SC** = 情节完整性（SC_E1–E3 / SC_Sum）。

## 训练流水线

1. BART：`scripts/train_bart.py` → `models/bart_narro_v4/`
2. 宏观 SS：`scripts/train_micro.py` → `models/micro_narro_v4.pth`（`configs/micro_narro_v4.json`）
3. 宏观 SC（XGB）：`scripts/train_macro.py` → `models/macro_xgb_narro_v4/`

推理 / Web：`src/pipeline_predict_report.py`，版本见 `configs/model_registry.json`。

## 源码模块（`src/`）

| 模块 | 职责 |
|------|------|
| `bart_train.py` / `bart_infer.py` | BART 训练与推理 |
| `train_micro.py` / `train_micro_shared.py` | 宏观 SS（故事结构 A2–A16）训练 |
| `micro_encoder.py` | 宏观 SS 编码与宏观 SC 特征提取 |
| `train_macro_xgb.py` | 宏观 SC（XGB）训练 |
| `pipeline_predict_report.py` | 端到端预测与报告 |

## 详细步骤

见 [docs/TRAINING.md](docs/TRAINING.md)。
