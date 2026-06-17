# 宏观 SC 双轨方案（MAIN 流水线 vs 直接预测）

## 结论摘要

| 轨道 | 角色 | 模型形态 | 是否替代 SS |
|------|------|----------|-------------|
| **A · MAIN** | 家长可见主评估 | SS（A2–A16）+ 分幕 SC_E1–E3 **序数分类**，SC_Sum = 三幕之和 | 否，SS 必保留 |
| **B · 直接 SC** | 研究/筛查/一致性 | 整段文本 → SC_Sum（或 E1–E3）的 **独立头** | 不输入 SS 预测，仅对比 |

**是否放弃当前 SC 回归（XGB `reg:squarederror`）？**  
→ **是，作为 MAIN 轨的生产方案应放弃**；可暂时保留旧权重作 **B 轨基线** 或离线对照，直到 B 轨新模型训好。

---

## 轨道 A：MAIN 自动化流水线（主产品）

```
正文 + BART 线索
  → 宏观 SS（QiDeBERTa，A2–A16）
  → 按幕切段 + 幕级特征 + SS 概率（15 维）
  → 宏观 SC：SC_E1, SC_E2, SC_E3 各 0–3（四分类或有序回归）
  → SC_Sum = round(E1)+round(E2)+round(E3)
```

- 家长端只展示此轨 + SS 要素短板。
- 与专家 GAO 分幕评分一致，可解释。

**实施优先级（代码库）**

1. `train_macro_xgb.py`：SC_E* 改为 `multi:softprob` 或有序损失；SC_Sum 由三幕相加。
2. 特征：按幕文本 / 幕 [CLS] + `use_micro_prob_in_xgb: true`。
3. `evaluation_service` / 前端：展示三幕分 + 合计。

---

## 轨道 B：直接 SC（MAIN 之外的对照实验）

**问题**：不经过 SS，仅凭整段叙述能否预测专家 SC？

- **可行**（有监督信号就能学），但**不可解释**，也不符合 MAIN 向家长解释「结构短板」的目标。
- 用途：
  - 与 A 轨 **对比**（相关、偏差、分歧样本）；
  - **筛查**：|SC_A − SC_B| 或分歧大 → 提示「建议人工复核」；
  - 论文/方法学：**SS 是否必要** 的实证。

**推荐实现（适合本项目）**

| 方案 | 优点 | 缺点 |
|------|------|------|
| **B1 · 保留 XGB，仅全文特征** | 改动小，训练快 | 与旧回归同质，需改目标为序数 |
| **B2 · DeBERTa 上增加 SC 头（多任务）** | 与 SS 共享编码器，部署一次 forward | 与 A 轨耦合，「非 SS」需在推理时 **关闭 SS 条件** 或单独 checkpoint |
| **B3 · 独立小模型（仅 SC）** | 概念最干净，真正「无 SS」 | 多一套权重与推理路径 |

**建议**：短期 **B1**（全文语言学 + 全局 [CLS] → 序数 SC_Sum）作对照；中期 **B3** 若 B1 与 A 轨相关性高但分歧样本有价值，再训独立 `sc_direct` 模型。

不在 UI 主卡片展示 B 轨分数；仅在：

- 管理/研究视图、
- 评估详情「专业对照」折叠区、
- 或 `evaluation` JSON 字段 `sc_direct` / `sc_main_delta`。

---

## 数据与评估记录

每次评估建议存储：

```json
{
  "sc_main": { "E1": 2, "E2": 1, "E3": 2, "sum": 5 },
  "sc_direct": { "sum": 4.2, "sum_rounded": 4 },
  "sc_agreement": { "delta": 1, "flag_review": false }
}
```

`flag_review`: 例如 `|sum_main - sum_direct| >= 2` 或分幕任一幕差 ≥ 2。

---

## 与现有 `macro_xgb_narro_v4` 的关系

- 目录名可保留；**MAIN 轨** 改为序数模型后另存 `macro_sc_main/` 或版本 `narro_v4_sc_ordinal`。
- 当前回归 joblib 标记为 **legacy / sc_direct_baseline**，仅用于双轨对照实验，不写入家长报告主文案。
