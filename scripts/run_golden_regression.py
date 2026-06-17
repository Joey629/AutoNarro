#!/usr/bin/env python3
"""
POC 黄金样本回归：有效叙事检查 SC/微观区间；拒评样本检查 insufficient 且无 SC。

  PYTHONPATH=src python scripts/run_golden_regression.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

from paths import default_model_paths
from pipeline_predict_report import AutomatedNarrativePredictor


def in_range(val, bounds) -> bool:
    if val is None:
        return False
    lo, hi = bounds
    return lo <= float(val) <= hi


def main() -> int:
    cfg_path = ROOT / "configs" / "golden_samples.json"
    samples = json.loads(cfg_path.read_text(encoding="utf-8"))["samples"]
    print(f"加载模型…（共 {len(samples)} 条黄金样本）")
    os.environ.setdefault("NARRO_BART_FORCE_CPU", "1")
    predictor = AutomatedNarrativePredictor(default_model_paths())
    failed = 0
    for s in samples:
        _, reg, tasks, _, quality = predictor.predict(
            s["text"],
            s["story_type"],
            s["age"],
            s["left_behind"],
            task_type=s.get("task_type"),
        )
        exp = s["expect"]
        sc = reg.get("pred_SC_Sum")
        micro = tasks.get("pred_MultiTask_Sum")
        if micro is not None:
            micro = int(micro)

        ok = True
        msgs = []

        exp_q = exp.get("quality_status")
        if exp_q and quality.get("status") != exp_q:
            ok = False
            msgs.append(f"quality={quality.get('status')} expect {exp_q}")

        if exp_q == "insufficient":
            if sc is not None:
                ok = False
                msgs.append(f"SC_Sum should be null got {sc}")
            exp_micro = exp.get("micro_sum")
            if exp_micro is None and micro is not None:
                ok = False
                msgs.append(f"micro should be null got {micro}")
        else:
            if "pred_SC_Sum" in exp and exp["pred_SC_Sum"] is not None:
                if not in_range(sc, exp["pred_SC_Sum"]):
                    ok = False
                    msgs.append(f"SC_Sum={sc} not in {exp['pred_SC_Sum']}")
            if "micro_sum" in exp and exp["micro_sum"] is not None:
                bounds = exp["micro_sum"]
                if micro is None or not (bounds[0] <= micro <= bounds[1]):
                    ok = False
                    msgs.append(f"micro={micro} not in {bounds}")

        status = "PASS" if ok else "FAIL"
        if not ok:
            failed += 1
        extra = f" quality={quality.get('status')}" if quality else ""
        print(
            f"  [{status}] {s['id']}: SC_Sum={sc} micro={micro}{extra}"
            + (f" — {'; '.join(msgs)}" if msgs else "")
        )
    print(f"\n结果: {len(samples) - failed}/{len(samples)} 通过")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
