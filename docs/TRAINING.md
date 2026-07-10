# Narro v4 训练（离线）

产品线默认栈见 `configs/model_registry.json`（`narro_v4`）。训练在本地/GPU 机完成，上线仅同步 `models/` 与配置。

## 权重清单

| 组件 | 路径 |
|------|------|
| 宏观 SS 模型 | `models/micro_narro_v4.pth` |
| 预训练编码器 | `models/pretrained/qideberta-base/` |
| BART 线索 | `models/bart_narro_v4/` |
| 宏观 SC（XGB） | `models/macro_sc_main/`（轨 A）+ `models/macro_sc_direct/`（轨 B） |
| legacy 回归回退 | `models/macro_xgb_narro_v4/`（可选） |

## 1. 下载预训练（仅一次）

```bash
cd /path/to/AutoNarro
source .venv/bin/activate
export PYTHONPATH=src

python scripts/download_deberta_pretrained.py
python scripts/download_bart_pretrained.py --config configs/bart_narro_v4.json
```

有 HTTP 代理时：`export http_proxy=... https_proxy=...` 并 `unset HF_ENDPOINT`。

## 2. 宏观 SS 模型（故事结构 A2–A16）

```bash
PYTHONPATH=src python scripts/train_micro.py
# 或跳过冒烟：--skip-smoke
```

配置：`configs/micro_narro_v4.json`

## 3. BART

```bash
PYTHONPATH=src python scripts/train_bart.py --skip-smoke
```

配置：`configs/bart_narro_v4.json`

## 4. 宏观 SC 双轨（序数 XGB）

需先完成 2、3。默认同时训练 **轨 A（MAIN，含 SS 概率）** 与 **轨 B（直接 SC，无 SS 概率）**：

```bash
export NARRO_BART_FORCE_CPU=1
export REGRESSION_FORCE_CPU=1   # macOS 上 BERT 特征提取建议 CPU
bash scripts/run_retrain_macro.sh
# 或 PYTHONPATH=src python scripts/train_macro.py
```

产物：

- `models/macro_sc_main/sc_main_SC_E{1,2,3}.joblib`
- `models/macro_sc_direct/sc_direct_SC_E{1,2,3}.joblib`

仅训 legacy 回归（旧行为）：`NARRO_SC_DUAL_TRAIN=0 NARRO_MACRO_OUTPUT_DIR=models/macro_xgb_narro_v4 PYTHONPATH=src python scripts/train_macro.py`

设计说明：`docs/SC_DUAL_TRACK.md`

## 5. 发布前

```bash
export NARRO_BART_FORCE_CPU=1
PYTHONPATH=src python scripts/check_release.py
```

## 论文补充分析

审稿用脚本在 `src/research_paper_*.py`（非线上路径）。SS/SC 误差分析：`src/analyze_micro_*.py`（SS）、`src/analyze_macro_*.py`（SC）。
