# 文件索引（Narro 产品）

## 目录

| 目录 | 职责 |
|------|------|
| **frontend/** | SaaS 工作台；`npm run build` → `static/css/` |
| **website/** | 品牌官网 → `https://autonarro.com/` |
| **backend/** | FastAPI、`evaluation_service.py`、鉴权、批量任务 |
| **src/** | 训练与推理（`pipeline_predict_report.py`、`paths.py`） |
| **models/** | 权重（git 忽略，部署 rsync） |
| **data/** | `narratives.csv`、`evaluations.db`、`logs/` |
| **configs/** | `model_registry.json`、`micro_narro_v4.json`、`golden_samples.json` |
| **scripts/** | `check_release.py`、`train_*.py`、`run_retrain_*.sh` |

**启动：** `python run_web.py`

| URL | 说明 |
|-----|------|
| `/` | 官网 |
| `/app` | SaaS beta |

部署：[docs/DEPLOYMENT_AUTONARRO.md](docs/DEPLOYMENT_AUTONARRO.md) · 训练：[docs/TRAINING.md](docs/TRAINING.md)

## 命名约定

| 层级 | 规则 | 示例 |
|------|------|------|
| 模型产物 | `models/<组件>_narro_v4` | `micro_narro_v4.pth`, `bart_narro_v4/`, `macro_xgb_narro_v4/` |
| 预训练缓存 | `models/pretrained/<简短名>/` | `qideberta-base/`, `bart-chinese-uer/` |
| 训练脚本 | `scripts/train_<组件>.py` | `train_micro.py`, `train_bart.py`, `train_macro.py` |
| 实现模块 | `src/` 下与组件同名 | `train_micro.py`, `bart_infer.py`, `train_macro_xgb.py` |
| 离线分析 | `src/analyze_<微观\|宏观>_*.py` → 输出 `analyze_*_errors/` | `analyze_micro_errors.py` |

版本注册表：`configs/model_registry.json`（当前仅 **narro_v4**）。

## 发布检查

```bash
PYTHONPATH=src python scripts/check_release.py
```
