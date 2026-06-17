"""后台批量评估 worker。"""
from __future__ import annotations

import io
import json
import threading
from typing import Any

import pandas as pd

from evaluation_service import EvaluationService
from evaluation_store import create_batch_job, update_batch_job
from logging_config import setup_logging

logger = setup_logging()
_active_jobs: set[int] = set()
_jobs_lock = threading.Lock()


MAX_BATCH_BYTES = 5 * 1024 * 1024
MAX_BATCH_ROWS = 500


def parse_batch_csv(raw: bytes) -> pd.DataFrame:
    if len(raw) > MAX_BATCH_BYTES:
        raise ValueError(f"CSV 超过 {MAX_BATCH_BYTES // (1024 * 1024)}MB 上限")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("gbk", errors="replace")
    df = pd.read_csv(io.StringIO(text))
    if len(df) > MAX_BATCH_ROWS:
        raise ValueError(f"CSV 超过 {MAX_BATCH_ROWS} 行上限")
    if "text" not in df.columns and "Text" in df.columns:
        df = df.rename(columns={"Text": "text"})
    if "text" not in df.columns:
        df = df.rename(columns={df.columns[0]: "text"})
    return df


def run_batch_job(job_id: int, df: pd.DataFrame) -> None:
    svc = EvaluationService.get()
    results: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    try:
        update_batch_job(job_id, status="running")
        svc.load()
        for idx, row in df.iterrows():
            try:
                text_val = str(row["text"]).strip()
                age = int(pd.to_numeric(row["age"], errors="coerce") or 5)
                lb = int(pd.to_numeric(row.get("left_behind", 0), errors="coerce") or 0)
                story = None
                if "story_type" in row.index and pd.notna(row.get("story_type")):
                    story = str(row["story_type"]).strip().lower()
                tt = None
                if "task_type" in row.index and pd.notna(row.get("task_type")):
                    tt = str(row["task_type"]).strip()
                if len(text_val) < 5:
                    errors.append({"row": int(idx), "error": "文本过短"})
                    update_batch_job(job_id, failed_rows=len(errors))
                    continue
                cid = str(row.get("child_id", "") or "").strip() if "child_id" in row.index else ""
                cname = str(row.get("child_name", "") or "").strip() if "child_name" in row.index else ""
                cclass = str(row.get("class_name", "") or "").strip() if "class_name" in row.index else ""
                out = svc.evaluate_one(
                    text_val,
                    age,
                    lb,
                    story_type=story,
                    task_type=tt,
                    child_id=cid,
                    child_name=cname,
                    class_name=cclass,
                    source="web_batch_async",
                )
                out["row"] = int(idx)
                results.append(out)
                update_batch_job(job_id, completed_rows=len(results), failed_rows=len(errors))
            except Exception as e:
                errors.append({"row": int(idx), "error": str(e)})
                update_batch_job(job_id, failed_rows=len(errors))
        summary = {
            "summary_csv": _results_to_csv(results),
            "results": results,
            "total_rows": len(df),
            "completed": len(results),
        }
        update_batch_job(
            job_id,
            status="completed",
            completed_rows=len(results),
            failed_rows=len(errors),
            summary_json=json.dumps(summary, ensure_ascii=False),
            errors_json=json.dumps(errors, ensure_ascii=False),
        )
        logger.info("批量任务 %s 完成 %s/%s", job_id, len(results), len(df))
    except Exception as e:
        logger.exception("批量任务 %s 失败", job_id)
        update_batch_job(job_id, status="failed", errors_json=json.dumps([{"error": str(e)}]))


def _results_to_csv(results: list[dict]) -> str:
    if not results:
        return "row,evaluation_id,pred_SC_Sum,micro_sum,TNW,MLU,elapsed_ms\n"
    import io

    buf = io.StringIO()
    rows = [
        {
            "row": r.get("row"),
            "evaluation_id": r.get("evaluation_id"),
            "pred_SC_Sum": r.get("regression", {}).get("pred_SC_Sum"),
            "micro_sum": r.get("microstructure", {}).get("sum"),
            "TNW": (r.get("linguistics") or {}).get("core", {}).get("TNW"),
            "MLU": (r.get("linguistics") or {}).get("core", {}).get("MLU"),
            "elapsed_ms": r.get("elapsed_ms"),
        }
        for r in results
    ]
    pd.DataFrame(rows).to_csv(buf, index=False)
    return buf.getvalue()


def enqueue_batch(filename: str, raw: bytes) -> int:
    df = parse_batch_csv(raw)
    if "age" not in df.columns:
        raise ValueError("CSV 缺少列: age")
    svc = EvaluationService.get()
    version = ""
    try:
        from paths import resolve_model_version

        version = resolve_model_version()
    except Exception:
        pass
    job_id = create_batch_job(filename, len(df), version)
    with _jobs_lock:
        _active_jobs.add(job_id)

    def _runner():
        try:
            run_batch_job(job_id, df)
        finally:
            with _jobs_lock:
                _active_jobs.discard(job_id)

    threading.Thread(target=_runner, daemon=True).start()
    return job_id
