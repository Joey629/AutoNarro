"""管理后台：园所概览、成长趋势、筛查预警。"""
from __future__ import annotations

import json
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import pandas as pd

RULES_PATH = Path(__file__).resolve().parents[1] / "configs" / "screening_rules.json"


def _db_path() -> Path:
    from paths import DATA_DIR

    return DATA_DIR / "evaluations.db"


def _load_all_evaluations(limit: int = 2000) -> list[dict]:
    from evaluation_store import init_db
    from tenant import current_tenant_id
    import json as _json

    init_db()
    tid = current_tenant_id()
    with sqlite3.connect(_db_path()) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT * FROM evaluations
            WHERE tenant_id = ?
            ORDER BY id DESC LIMIT ?
            """,
            (tid, limit),
        ).fetchall()
    out = []
    for r in rows:
        reg = _json.loads(r["regression_json"] or "{}")
        sc_agreement = reg.get("sc_agreement") or {}
        micro = _json.loads(r["microstructure_json"] or "{}")
        ling = _json.loads(r["linguistic_json"] or "{}") if "linguistic_json" in r.keys() else {}
        failed = [t["id"] for t in micro.get("tasks", []) if not t.get("value")]
        core = ling.get("core") or {}
        ps = None
        if "parent_survey_json" in r.keys() and (r["parent_survey_json"] or "").strip():
            try:
                ps = _json.loads(r["parent_survey_json"])
            except _json.JSONDecodeError:
                ps = None
        out.append(
            {
                "id": r["id"],
                "created_at": r["created_at"],
                "child_id": r["child_id"] if "child_id" in r.keys() else "",
                "child_name": r["child_name"] if "child_name" in r.keys() else "",
                "class_name": r["class_name"] if "class_name" in r.keys() else "",
                "age": r["age"],
                "story_type": r["story_type"],
                "pred_SC_Sum": reg.get("pred_SC_Sum"),
                "sc_dual_review": bool(sc_agreement.get("flag_review")),
                "sc_agreement_message": sc_agreement.get("message"),
                "micro_sum": micro.get("sum"),
                "TNW": core.get("TNW"),
                "MLU": core.get("MLU"),
                "linguistics": ling,
                "failed_tasks": failed,
                "parent_survey": ps,
                "coach_mode": r["coach_mode"] if "coach_mode" in r.keys() else "free",
                "user_id": int(r["user_id"]) if "user_id" in r.keys() and r["user_id"] is not None else 0,
            }
        )
    return out


def _expert_norms_by_age_story() -> dict[tuple, dict]:
    """预计算 narratives.csv 专家常模均值。"""
    from paths import narratives_csv_path
    from benchmark_norms import ensure_expert_norm_columns, EXPERT_MACRO_SUM_COL, EXPERT_MICRO_SUM_COL

    p = narratives_csv_path()
    if not p.is_file():
        return {}
    df = pd.read_csv(p)
    if df.columns[0].lower() not in ("text", "narrative"):
        df = df.rename(columns={df.columns[0]: "text"})
    df = ensure_expert_norm_columns(df)
    norms = {}
    for (age, st), g in df.groupby(["age", "story_type"]):
        norms[(int(age), str(st))] = {
            "SC_Sum": float(g[EXPERT_MACRO_SUM_COL].mean()) if EXPERT_MACRO_SUM_COL in g else None,
            "micro_sum": float(g[EXPERT_MICRO_SUM_COL].mean()) if EXPERT_MICRO_SUM_COL in g else None,
            "TNW": float(g["TNW"].mean()) if "TNW" in g else None,
            "MLU": float(g["MLU"].mean()) if "MLU" in g else None,
            "n": len(g),
        }
    return norms


def compute_alerts(rows: list[dict], norms: dict) -> list[dict]:
    rules = json.loads(RULES_PATH.read_text(encoding="utf-8")) if RULES_PATH.is_file() else {"alerts": []}
    alerts_out = []
    fired: dict[int, set[str]] = defaultdict(set)

    for row in rows:
        age, st = row.get("age"), row.get("story_type")
        norm = norms.get((age, st), {})
        sc = row.get("pred_SC_Sum")
        micro = row.get("micro_sum")
        core = (row.get("linguistics") or {}).get("core") or {}
        tnw, mlu = core.get("TNW"), core.get("MLU")

        for rule in rules.get("alerts", []):
            if rule.get("requires"):
                continue
            rid = rule.get("id")
            if not rid:
                continue
            hit = False
            op = rule.get("op")
            if op == "lte" and micro is not None:
                hit = micro <= rule.get("value", 5)
            elif op == "below_ratio" and sc is not None and norm.get("SC_Sum"):
                hit = sc < norm["SC_Sum"] * rule.get("ratio", 0.75)
            elif op == "below_ratio" and rule.get("field") == "TNW" and tnw and norm.get("TNW"):
                hit = tnw < norm["TNW"] * rule.get("ratio", 0.7)
            elif op == "below_ratio" and rule.get("field") == "MLU" and mlu and norm.get("MLU"):
                hit = mlu < norm["MLU"] * rule.get("ratio", 0.75)
            elif op == "flag_true" and rule.get("field") == "sc_dual_review":
                hit = bool(row.get("sc_dual_review"))
            if hit:
                fired[row["id"]].add(rid)
                alerts_out.append(
                    {
                        "evaluation_id": row["id"],
                        "child_id": row.get("child_id"),
                        "child_name": row.get("child_name"),
                        "class_name": row.get("class_name"),
                        "alert_id": rid,
                        "label": rule.get("label", rid),
                        "severity": "high" if rid in ("suspected_delay", "low_macro_vs_norm", "sc_dual_disagreement") else "medium",
                    }
                )

        for rule in rules.get("alerts", []):
            req = rule.get("requires")
            if req and all(r in fired[row["id"]] for r in req):
                alerts_out.append(
                    {
                        "evaluation_id": row["id"],
                        "child_id": row.get("child_id"),
                        "child_name": row.get("child_name"),
                        "class_name": row.get("class_name"),
                        "alert_id": rule["id"],
                        "label": rule.get("label"),
                        "severity": "high",
                    }
                )
    return alerts_out


def child_growth_series(child_id: str) -> dict[str, Any]:
    from evaluation_store import list_child_timeline

    items = list_child_timeline(child_id, limit=200)
    if not items:
        return {"child_id": child_id, "points": [], "trend": "unknown"}

    points = []
    for it in reversed(items):
        points.append(
            {
                "date": (it.get("created_at") or "")[:10],
                "evaluation_id": it["id"],
                "pred_SC_Sum": it.get("pred_SC_Sum"),
                "micro_sum": it.get("micro_sum"),
            }
        )
    sc_vals = [p["pred_SC_Sum"] for p in points if p["pred_SC_Sum"] is not None]
    trend = "steady"
    if len(sc_vals) >= 2:
        delta = sc_vals[-1] - sc_vals[0]
        if delta > 0.5:
            trend = "up"
        elif delta < -0.5:
            trend = "down"
        if sc_vals[-1] is not None and sc_vals[-1] < 4:
            trend = "warning"

    return {"child_id": child_id, "points": points, "trend": trend, "trend_label": _trend_label(trend)}


def _trend_label(t: str) -> str:
    return {
        "up": "上升",
        "down": "下降",
        "steady": "平稳",
        "warning": "预警",
        "unknown": "数据不足",
    }.get(t, t)


def admin_overview(class_name: Optional[str] = None) -> dict[str, Any]:
    rows = _load_all_evaluations()
    if class_name:
        rows = [r for r in rows if (r.get("class_name") or "") == class_name]
    norms = _expert_norms_by_age_story()
    alerts = compute_alerts(rows, norms)

    sc_list = [r["pred_SC_Sum"] for r in rows if r.get("pred_SC_Sum") is not None]
    micro_list = [r["micro_sum"] for r in rows if r.get("micro_sum") is not None]

    weak_tasks: dict[str, int] = defaultdict(int)
    for r in rows:
        for t in r.get("failed_tasks") or []:
            weak_tasks[t] += 1

    children = {}
    for r in rows:
        cid = r.get("child_id") or f"anon_{r['id']}"
        if cid not in children:
            children[cid] = {
                "child_id": r.get("child_id"),
                "child_name": r.get("child_name"),
                "class_name": r.get("class_name"),
                "n_evaluations": 0,
                "last_SC_Sum": None,
                "flagged": False,
            }
        children[cid]["n_evaluations"] += 1
        children[cid]["last_SC_Sum"] = r.get("pred_SC_Sum")

    alert_child_ids = {a["child_id"] for a in alerts if a.get("child_id")}
    for cid, c in children.items():
        if c.get("child_id") in alert_child_ids:
            c["flagged"] = True

    return {
        "total_evaluations": len(rows),
        "total_children": len(children),
        "sc_mean": round(sum(sc_list) / len(sc_list), 2) if sc_list else None,
        "micro_mean": round(sum(micro_list) / len(micro_list), 2) if micro_list else None,
        "alerts_count": len(alerts),
        "alerts": alerts[:50],
        "children": sorted(children.values(), key=lambda x: (x.get("flagged", False), x.get("child_id") or ""), reverse=True),
        "distribution": {
            "pred_SC_Sum": sc_list[:200],
            "micro_sum": micro_list[:200],
        },
        "weak_ss_tasks": dict(sorted(weak_tasks.items(), key=lambda x: -x[1])[:10]),
        "weak_micro_tasks": dict(sorted(weak_tasks.items(), key=lambda x: -x[1])[:10]),
    }


def list_children(class_name: Optional[str] = None) -> list[dict]:
    ov = admin_overview(class_name)
    return ov.get("children", [])


def user_insights(
    limit: int = 200,
    *,
    user_id: int | None = None,
    child_id: str | None = None,
) -> dict[str, Any]:
    """家长端：汇总评估，呈现长期进步与筛查告警。"""
    rows = _load_all_evaluations(limit=limit)
    if user_id and user_id > 0:
        rows = [r for r in rows if int(r.get("user_id") or 0) == user_id]
    if child_id:
        cid = child_id.strip()
        rows = [r for r in rows if (r.get("child_id") or "").strip() == cid]
    norms = _expert_norms_by_age_story()
    alerts = compute_alerts(rows, norms)

    chrono = sorted(rows, key=lambda r: r.get("created_at") or "")
    points = [
        {
            "date": (r.get("created_at") or "")[:10],
            "created_at": r.get("created_at"),
            "evaluation_id": r["id"],
            "story_type": r.get("story_type"),
            "pred_SC_Sum": r.get("pred_SC_Sum"),
            "micro_sum": r.get("micro_sum"),
            "TNW": r.get("TNW"),
            "MLU": r.get("MLU"),
            "parent_composite": (r.get("parent_survey") or {}).get("composite"),
        }
        for r in chrono
    ]

    sc_vals = [p["pred_SC_Sum"] for p in points if p["pred_SC_Sum"] is not None]
    micro_vals = [p["micro_sum"] for p in points if p["micro_sum"] is not None]
    trend = "unknown"
    if len(sc_vals) >= 2:
        delta = sc_vals[-1] - sc_vals[0]
        if delta > 0.5:
            trend = "up"
        elif delta < -0.5:
            trend = "down"
        else:
            trend = "steady"
        if sc_vals[-1] is not None and sc_vals[-1] < 4:
            trend = "warning"
    elif len(sc_vals) == 1 and sc_vals[0] is not None and sc_vals[0] < 4:
        trend = "warning"

    weak_tasks: dict[str, int] = defaultdict(int)
    for r in rows:
        for t in r.get("failed_tasks") or []:
            weak_tasks[t] += 1

    seen_alert: set[tuple] = set()
    unique_alerts = []
    for a in alerts:
        key = (a.get("alert_id"), a.get("evaluation_id"))
        if key in seen_alert:
            continue
        seen_alert.add(key)
        unique_alerts.append(a)

    # 按故事主题汇总
    by_story: dict[str, dict] = defaultdict(lambda: {"count": 0, "sc_sum": 0.0, "ss_sum": 0.0, "n_sc": 0, "n_ss": 0})
    for r in rows:
        st = r.get("story_type") or "unknown"
        by_story[st]["count"] += 1
        if r.get("pred_SC_Sum") is not None:
            by_story[st]["sc_sum"] += float(r["pred_SC_Sum"])
            by_story[st]["n_sc"] += 1
        if r.get("micro_sum") is not None:
            by_story[st]["ss_sum"] += float(r["micro_sum"])
            by_story[st]["n_ss"] += 1
    story_labels = {"cat": "小猫", "dog": "小狗", "bird": "小鸟", "goat": "小羊"}
    by_story_out = []
    for st, v in by_story.items():
        by_story_out.append(
            {
                "story_type": st,
                "label": story_labels.get(st, st),
                "count": v["count"],
                "sc_mean": round(v["sc_sum"] / v["n_sc"], 2) if v["n_sc"] else None,
                "ss_mean": round(v["ss_sum"] / v["n_ss"], 2) if v["n_ss"] else None,
            }
        )
    by_story_out.sort(key=lambda x: -x["count"])

    # 评估间隔（天）
    intervals: list[int] = []
    for i in range(1, len(chrono)):
        try:
            t0 = datetime.fromisoformat((chrono[i - 1].get("created_at") or "").replace("Z", "+00:00"))
            t1 = datetime.fromisoformat((chrono[i].get("created_at") or "").replace("Z", "+00:00"))
            intervals.append(max(0, (t1 - t0).days))
        except ValueError:
            continue
    avg_interval = round(sum(intervals) / len(intervals), 1) if intervals else None

    # 家长问卷汇总
    parent_scores = [
        (r.get("parent_survey") or {}).get("composite")
        for r in rows
        if (r.get("parent_survey") or {}).get("composite") is not None
    ]
    guided_count = sum(1 for r in rows if (r.get("coach_mode") or "") == "guided")

    return {
        "evaluation_count": len(rows),
        "alerts_count": len(unique_alerts),
        "alerts": unique_alerts[:30],
        "growth": {
            "points": points,
            "trend": trend,
            "trend_label": _trend_label(trend),
        },
        "sc_first": sc_vals[0] if sc_vals else None,
        "sc_last": sc_vals[-1] if sc_vals else None,
        "sc_delta": round(sc_vals[-1] - sc_vals[0], 2) if len(sc_vals) >= 2 else None,
        "micro_first": micro_vals[0] if micro_vals else None,
        "micro_last": micro_vals[-1] if micro_vals else None,
        "micro_delta": round(micro_vals[-1] - micro_vals[0], 2) if len(micro_vals) >= 2 else None,
        "micro_mean": round(sum(micro_vals) / len(micro_vals), 2) if micro_vals else None,
        "tnw_last": points[-1].get("TNW") if points else None,
        "mlu_last": points[-1].get("MLU") if points else None,
        "weak_ss_tasks": dict(sorted(weak_tasks.items(), key=lambda x: -x[1])[:12]),
        "weak_micro_tasks": dict(sorted(weak_tasks.items(), key=lambda x: -x[1])[:12]),
        "by_story": by_story_out,
        "avg_interval_days": avg_interval,
        "parent_survey_count": len(parent_scores),
        "parent_composite_mean": round(sum(parent_scores) / len(parent_scores), 2)
        if parent_scores
        else None,
        "guided_session_count": guided_count,
    }
