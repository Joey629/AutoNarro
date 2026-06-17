"""叙事输入质量评估与宏观分数安全边界（POC）。"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from paths import CONFIGS_DIR

_RULES_PATH = CONFIGS_DIR / "narrative_quality_rules.json"


@lru_cache(maxsize=1)
def load_quality_rules() -> dict:
    if not _RULES_PATH.is_file():
        return {}
    return json.loads(_RULES_PATH.read_text(encoding="utf-8"))


def assess_narrative_quality(text: str, core: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    返回 narrative_quality 对象：
      status: sufficient | insufficient | low_quality
      score: 0–1 粗粒度质量分
      flags: 触发的规则 id 列表
      message: 用户可见说明
    """
    rules = load_quality_rules()
    th = rules.get("thresholds", {})
    msgs = rules.get("messages", {})
    raw = (text or "").strip()
    core = core or {}

    flags: list[str] = []
    tnw = int(core.get("TNW") or 0)
    tnu = int(core.get("TNU") or 0)
    tdw = int(core.get("TDW") or 0)
    n_chars = len(re.sub(r"\s+", "", raw))

    for pat in rules.get("reject_regex", []):
        try:
            if re.match(pat, raw, flags=re.IGNORECASE):
                flags.append("reject_pattern")
                break
        except re.error:
            continue

    if n_chars < int(th.get("min_chars", 20)):
        flags.append("min_chars")
    if tnu < int(th.get("min_sentences", 2)):
        flags.append("min_sentences")
    if tnw < int(th.get("min_tnw", 8)):
        flags.append("min_tnw")
    if tdw < int(th.get("min_tdw", 4)):
        flags.append("min_tdw")

    if flags:
        hard = {"reject_pattern", "min_chars"} & set(flags)
        if hard or n_chars < 10 or tnw < 5:
            return {
                "status": "insufficient",
                "score": round(max(0.0, min(1.0, n_chars / max(int(th.get("min_chars", 20)), 1))), 3),
                "flags": flags,
                "message": msgs.get("insufficient_default", "无法评估：请完整讲述。"),
                "metrics": {"chars": n_chars, "TNW": tnw, "TNU": tnu, "TDW": tdw},
            }
        return {
            "status": "low_quality",
            "score": round(max(0.2, min(0.55, tnw / max(int(th.get("min_tnw", 8)), 1) * 0.5)), 3),
            "flags": flags,
            "message": msgs.get("low_quality_note", "讲述偏短，分数仅供参考。"),
            "metrics": {"chars": n_chars, "TNW": tnw, "TNU": tnu, "TDW": tdw},
        }

    score = min(1.0, 0.45 + 0.25 * min(tnw / 25.0, 1.0) + 0.2 * min(tnu / 6.0, 1.0) + 0.1 * min(n_chars / 80.0, 1.0))
    return {
        "status": "sufficient",
        "score": round(score, 3),
        "flags": [],
        "message": "",
        "metrics": {"chars": n_chars, "TNW": tnw, "TNU": tnu, "TDW": tdw},
    }


def apply_regression_safeguards(
    regression: dict[str, Any],
    core: dict[str, Any],
    quality: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Clip SC 并与 TNW 交叉约束；返回 (regression, quality)。"""
    rules = load_quality_rules()
    b = rules.get("regression_bounds", {})
    sc_min = float(b.get("sc_min", 0.0))
    sc_max = float(b.get("sc_max", 15.0))
    caps: list[str] = []

    out = dict(regression)
    for k in ("pred_SC_E1", "pred_SC_E2", "pred_SC_E3"):
        v = out.get(k)
        if v is not None:
            out[k] = float(max(0.0, min(sc_max / 3.0, float(v))))

    if out.get("pred_SC_E1") is not None:
        s = float(out["pred_SC_E1"]) + float(out.get("pred_SC_E2") or 0) + float(out.get("pred_SC_E3") or 0)
    else:
        s = out.get("pred_SC_Sum")
        s = float(s) if s is not None else None

    if s is None:
        return out, quality

    tnw = int(core.get("TNW") or 0)
    if tnw < int(b.get("very_low_tnw_threshold", 5)):
        cap = float(b.get("very_low_tnw_cap_sum", 1.0))
        if s > cap:
            s = cap
            caps.append("very_low_tnw")
    elif tnw < int(b.get("low_tnw_threshold", 8)) or quality.get("status") == "low_quality":
        cap = float(b.get("low_tnw_cap_sum", 3.0))
        if s > cap:
            s = cap
            caps.append("low_tnw")

    s = max(sc_min, min(sc_max, s))
    out["pred_SC_Sum"] = round(s, 4)
    q = dict(quality)
    if caps:
        q["sc_capped"] = True
        q["sc_cap_reasons"] = caps
    out["pred_SC_Sum_beta"] = True
    return out, q


def null_regression() -> dict[str, Any]:
    return {
        "pred_SC_E1": None,
        "pred_SC_E2": None,
        "pred_SC_E3": None,
        "pred_SC_Sum": None,
        "pred_SC_Sum_beta": True,
    }
