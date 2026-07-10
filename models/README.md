# 模型文件（勿提交 git）

| 文件 / 目录 | 模型 |
|-------------|------|
| `bart_narro_v4/` | **uer/bart-base-chinese** 微调 → 生成叙事线索 |
| `micro_narro_v4.pth` | **Morton-Li/QiDeBERTa-base** LoRA 微调 → **宏观 SS**（故事结构 A2–A16，15 项） |
| `macro_sc_main/` | **轨 A · MAIN**：序数 XGB（含 SS 概率）→ SC_E1–E3，家长端主分数 |
| `macro_sc_direct/` | **轨 B · 直接 SC**：序数 XGB（无 SS 概率）→ 研究/筛查对照 |
| `macro_xgb_narro_v4/` | **legacy 回归**（可选回退，旧 `auto_xgb_model_SC_E*.joblib`） |
| `pretrained/qideberta-base/` | QiDeBERTa 预训练（训练宏观 SS 前下载） |
| `pretrained/bart-chinese-uer/` | BART 预训练（训练线索前下载） |

训练双轨：`NARRO_BART_FORCE_CPU=1 PYTHONPATH=src python scripts/train_macro.py`

对齐 MAIN：SS = 故事语法数量维度；SC = GAO 情节完整性维度。详见 `docs/SC_DUAL_TRACK.md`。

配置：`configs/model_registry.json`
