# 模型文件（勿提交 git）

| 文件 / 目录 | 模型 |
|-------------|------|
| `bart_narro_v4/` | **uer/bart-base-chinese** 微调 → 生成叙事线索 |
| `micro_narro_v4.pth` | **Morton-Li/QiDeBERTa-base** LoRA 微调 → **宏观 SS**（故事结构 A2–A16，15 项） |
| `macro_xgb_narro_v4/` | **XGBoost** → **宏观 SC**（情节完整性 SC_E1–E3） |
| `pretrained/qideberta-base/` | QiDeBERTa 预训练（训练宏观 SS 前下载） |
| `pretrained/bart-chinese-uer/` | BART 预训练（训练线索前下载） |

对齐 MAIN：SS = 故事语法数量维度；SC = GAO 情节完整性维度。

配置：`configs/model_registry.json`
