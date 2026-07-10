# 训练与产物（Narro v4）

对齐 MAIN 框架：**宏观 SS** = 故事结构（A2–A16）；**宏观 SC** = 情节完整性（SC_E1–E3 / SC_Sum）。

## 当前模型栈（narro_v4）

| 模块 | 基座 / 方法 | 是否在我们数据上训练 | 说明 |
|------|-------------|-------------------|------|
| BART 线索 | `fnlp/bart-base-chinese` 等 | 是（`data/narratives.csv`） | 生成 `predicted_ist_words` |
| **宏观 SS** | **Morton-Li/QiDeBERTa-base + LoRA** | **是** | 15 头多任务；**QA 问句 + 叙事**；**IST 仅 A6/A11/A16** |
| **宏观 SC** | **双轨序数 XGB**（轨 A 含 SS 概率 + 轨 B 无 SS） | **是** | 特征 = BART 线索 + 自动化语言学 + QiDeBERTa [CLS]；0–3 四分类，SC_Sum = 三幕之和 |

注册表：`configs/model_registry.json` · 微观配置：`configs/micro_narro_v4.json` · 双轨设计：`docs/SC_DUAL_TRACK.md`

> 推理优先加载 `models/macro_sc_main/` 与 `models/macro_sc_direct/`；缺权重时回退 `models/macro_xgb_narro_v4/` legacy 回归。

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
| `sc_dual_track.py` | SC 双轨加载（MAIN / 直接 / legacy 回退） |

## 数据路径

- 训练标注：`data/narratives.csv`（本地，git 忽略）
- 划分缓存：`data/regression_macro_split_narro_v4_701020_seed42.npz`（70/10/20，按 participant_id）

## 详细步骤

见 [docs/TRAINING.md](docs/TRAINING.md)。
