# 模型治理补齐指南（外部测试集 / 数据卡 / 模型卡 / 偏见与校准）

## 1. 外部独立测试集

**目标：** 与 `narratives.csv` 训练/常模语料 **零重叠 participant**。

| 步骤 | 动作 |
|------|------|
| 1 | 新采集或合作园所提供 ≥50 篇叙事 + 专家双盲标注（A2–A16, SC_Sum, TNW…） |
| 2 | 存为 `data/holdout_external_v1.csv`，**不进入训练** |
| 3 | 脚本 `scripts/eval_holdout.py`：输出宏观 SC R²、宏观 SS macro-F1、分年龄/主题子表 |
| 4 | 发布门槛：宏观 SC R² ≥ 内部 test；宏观 SS macro-F1 下降 <3% |

## 2. 版本化数据卡（Dataset Card）

每份语料在 `data/cards/<name>.yaml` 记录：

- 来源、伦理审批、年龄分布、城乡/留守比例
- 标注者资质、一致性（Cohen's κ）
- 已知偏差（如 cat/dog 仅复述）
- 划分方式：`participant_id` 分组 seed

## 3. 模型卡（Model Card）

`configs/model_registry.json` 与各训练配置（如 `configs/micro_narro_v4.json`）含：

- 基座、训练脚本 commit、超参、指标（test + holdout）
- 适用年龄、不适用场景（方言极重、文本过短）
- 局限性：非诊断、常模仅代表参考样本

## 4. 偏见与校准

| 项 | 做法 |
|----|------|
| 亚组公平 | 按 `left_behind` / `story_type` / `age` 报告误差 |
| 阈值校准 | `calibrate_multitask_thresholds.py` 产出 per-task τ |
| 回归校准 | 分年龄绘制 pred vs expert 残差图；必要时 Platt / 分箱校正 |
| LLM 解释 | 禁止改写分数；提示词声明「非诊断」；人工抽检 10% 建议 |

## 5. 发布检查清单

```bash
PYTHONPATH=src python scripts/check_release.py
PYTHONPATH=src python scripts/eval_holdout.py   # 有 holdout 时
PYTHONPATH=src python scripts/run_golden_regression.py
```

## 6. 建议目录

```
data/
  narratives.csv          # 研发常模（勿与 holdout 混用）
  holdout_external_v1.csv # 独立测试（gitignore 或 LFS）
  cards/
models/
  cards/
configs/
  screening_rules.json
  llm_config.json         # DeepSeek（gitignore 密钥）
```
