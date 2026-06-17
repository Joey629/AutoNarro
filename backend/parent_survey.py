"""家长李克特问卷：配置加载与和模型分对照。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "parent_likert.json"


def load_likert_config() -> dict[str, Any]:
    if not CONFIG_PATH.is_file():
        return {"questions": [], "scale_labels": []}
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def score_survey(answers: dict[str, int]) -> dict[str, Any]:
    """answers: question_id -> 1..5"""
    cfg = load_likert_config()
    items = []
    for q in cfg.get("questions", []):
        qid = q["id"]
        raw = answers.get(qid)
        if raw is None:
            continue
        v = max(1, min(5, int(raw)))
        if q.get("reverse"):
            v = 6 - v
        items.append({"id": qid, "value": v, "text": q.get("text", qid)})
    if not items:
        return {"composite": None, "items": [], "n_answered": 0}
    composite = round(sum(i["value"] for i in items) / len(items), 2)
    return {"composite": composite, "items": items, "n_answered": len(items)}


def triangulation_note(
    survey: dict[str, Any],
    *,
    micro_sum: Optional[int],
    pred_sc_sum: Optional[float],
) -> str:
    """生成家长自评与模型分的简短对照说明。"""
    comp = survey.get("composite")
    if comp is None:
        return "尚未填写家长观察问卷。"
    parts = [f"家长综合观察 {comp}/5"]
    if micro_sum is not None:
        ss_norm = round(micro_sum / 15 * 5, 1)
        gap = round(comp - ss_norm, 1)
        if abs(gap) <= 0.8:
            parts.append(f"与宏观 SS（换算约 {ss_norm}/5）较为一致")
        elif gap > 0.8:
            parts.append(f"高于本次宏观 SS（{micro_sum}/15），可关注是否任务难度或紧张影响发挥")
        else:
            parts.append(f"低于本次宏观 SS（{micro_sum}/15），模型捕捉到较多结构要素，可鼓励日常多讲")
    if pred_sc_sum is not None:
        parts.append(f"宏观 SC {pred_sc_sum}")
    return "；".join(parts) + "。"
