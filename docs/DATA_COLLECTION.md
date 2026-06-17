# 数据扩充指南（短期 +1000 条）

当前 POC 的瓶颈是 **标注样本量与分布**，不是前端或部署。扩充数据时请优先保证字段完整、协议一致。

## 必需字段（与 `data/narratives.csv` 对齐）

| 列 | 说明 |
|----|------|
| `text` | 儿童叙事全文（录音转写或听写） |
| `age` | 4 / 5 / 6 |
| `story_type` | `cat` / `dog` / `bird` / `goat` |
| `task_type` | `Telling` 或 `Retelling`（与故事绑定规则一致） |
| `left_behind` | 0 / 1 |
| `participant_id` | **强烈建议**：同一儿童固定 ID，便于按人划分 train/test |
| `SC_E1`, `SC_E2`, `SC_E3` 或 `SC_Sum` | 专家宏观 SC（情节完整性） |
| `A2`–`A16` | 专家宏观 SS 0/1（故事结构；或可由汇总表导入） |

可选：`child_id`、`class_name`（园所试点）、`gender`、采集日期。

## 质量要求

1. **拒绝极短无效样本进入训练集**（如仅「你好」）—— 这类应作为「拒评」对照，不写入 `narratives.csv` 主表，或单独 `data/rejected_samples.csv`。
2. **每条叙事建议 ≥2 句、≥20 字（去空格）**，与 `configs/narrative_quality_rules.json` 一致。
3. **四故事 + 讲述/复述** 尽量均衡；避免 90% 来自同一主题。
4. **双标注**：至少 10% 双评 + 不一致复核，用于报告 ICC / Cohen’s κ（投资与论文均需）。

## 推荐目录结构

```text
data/
  narratives.csv              # 主库（合并后）
  incoming/
    batch_2025_xx.csv         # 你每次提供的增量
  rejected_samples.csv        # 极短/无效（可选，用于质量门测试）
```

## 提供给我（仓库维护）时

1. CSV 编码 **UTF-8**，首行英文列名与上表一致。  
2. 附 **1 页数据说明**：来源（哪家园所）、采集方式、标注者资质、伦理批件号（如有）。  
3. 说明是否包含 **同一儿童多次测评**（纵向）。  
4. 不要提交含真实姓名的文件到公开 git；可用 `participant_id` 脱敏。

## 数据到位后的工程步骤

```bash
# 合并校验（可自行写脚本或交给我）
PYTHONPATH=src python scripts/validate_narratives_csv.py   # 待增

# 重训（见 docs/TRAINING.md）
PYTHONPATH=src python scripts/train_micro.py --skip-smoke
PYTHONPATH=src python scripts/train_bart.py --skip-smoke
PYTHONPATH=src python scripts/train_macro.py

# 发布门禁
PYTHONPATH=src python scripts/run_golden_regression.py
PYTHONPATH=src python scripts/check_release.py
```

## 1000 条如何分配（建议）

| 用途 | 比例 | 说明 |
|------|------|------|
| 训练 + 常模更新 | ~80% | 合并进 `narratives.csv` 后重训 |
| 独立 test holdout | ~15% | **按 participant_id 锁定**，永不参与训练 |
| 对抗/拒评集 | ~5% | 极短、乱输入，只用于质量门与回归测试 |

目标：test 集 **n≥150** 且四层（年龄×故事×任务）均有样本后，宏观 SC R² 与宏观 SS F1 才具有稳定可比性。
