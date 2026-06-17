# Narro 产品与技术路线图

> 面向机构试点的分阶段规划。评分链路（BART → 宏观 SS → 宏观 SC/XGB + 专家常模）与解释链路（LLM）分离。

## 阶段 A — 当前 POC（已完成 / 进行中）

- [x] 单条 / 批量评估、历史、专家常模（`narratives.csv`）
- [x] 故事自动识别 + 任务类型绑定
- [x] Jieba 语言产出指标 + 可读摘要
- [x] 儿童 ID、纵向时间线、专家 override API
- [x] DeepSeek 解释接口（需配置 API Key）
- [x] 管理后台基础：班级筛选、预警列表、成长趋势

## 阶段 B — 叙事采集体验（需求 1）

| 能力 | 方案 | 优先级 |
|------|------|--------|
| 看图讲故事 | 四则故事静态图/幻灯 + 录音提示 | P0 |
| 语音采集 | 浏览器 **Web Speech API**（中文）→ 文本填入评估框 | P0 |
| 豆包式对话助手 | 独立「讲故事」页：引导提问 + 图片切换 | P1 |
| 服务端 ASR | 讯飞 / 阿里 / Whisper API（教室噪声更稳） | P2 |

**说明：** 语音转写在本阶段以浏览器端完成为主，避免额外 GPU；评估仍走现有确定性模型。

## 阶段 C — 评估后 AI 辅导（需求 2、6）

| 能力 | 实现 |
|------|------|
| 改善建议 | `POST /api/evaluate/{id}/coach` → DeepSeek，上下文含评估结果 + 专家常模 |
| 自由追问 | `POST /api/chat`，绑定 `evaluation_id` |
| 报告润色 | 可选：用 LLM 扩写 `parent_summary`，**不修改宏观 SC/SS 分数** |

环境变量：`DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL`（默认 `https://api.deepseek.com`）

## 阶段 D — 管理后台（需求 3）

| 模块 | API | 前端 |
|------|-----|------|
| 班级 / 幼儿 | `class_name` 字段 + `/api/admin/children` | 管理后台 Tab |
| 多次测评对比 | `/api/children/{id}/timeline` + trend | 折线图（Chart.js） |
| 成长曲线 | 按月聚合宏观 SC / SS | 学期视图 P1 |
| 园所分布 | `/api/admin/overview` | 直方图 + 薄弱项 |
| 筛查预警 | `/api/admin/alerts` 规则引擎 | 红标列表 |

**预警规则（初版）：** 低于同龄专家常模 1 SD；宏观 SS ≤5/15；TNW 低于常模 30% 等（可配置 `configs/screening_rules.json`）。

## 阶段 E — 模型升级（需求 4、5）

| 替换 | 候选 | 策略 |
|------|------|------|
| BART 线索 | **mT5 / CPM-Bee / Mengzi-T5** 中文 seq2seq | 平行训练 → 线索 F1 对比 → 不优于现网不切换 |
| 宏观 SS 编码器 | **DeBERTa-v3-base-chinese** + 同 LoRA 协议 | `scripts/smoke_deberta_ablation.py` 小样本验证 |

**原则：** `model_registry.json` 多版本并存；`active_version` 仅在校准 + 黄金样本通过後切换。

## 阶段 F — 治理与合规（需求 7）

见 [MLOPS_GOVERNANCE.md](./MLOPS_GOVERNANCE.md)。
