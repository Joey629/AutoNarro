"""批量评估任务。"""
from __future__ import annotations

from auth import require_access
from evaluation_service import EvaluationService
from evaluation_store import get_batch_job
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from job_worker import enqueue_batch

router = APIRouter(tags=["batch"])


@router.post("/api/batch")
async def batch_enqueue(file: UploadFile = File(...), _: None = Depends(require_access)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="请上传 CSV 文件")
    raw = await file.read()
    try:
        job_id = enqueue_batch(file.filename, raw)
        return {"ok": True, "job_id": job_id, "status": "queued"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail="批量任务提交失败") from e


@router.post("/api/batch/sync")
async def batch_sync(file: UploadFile = File(...), _: None = Depends(require_access)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="请上传 CSV 文件")
    from evaluation_store import create_batch_job
    from job_worker import parse_batch_csv, run_batch_job

    raw = await file.read()
    df = parse_batch_csv(raw)
    job_id = create_batch_job(
        file.filename, len(df), EvaluationService.get().model_version or ""
    )
    run_batch_job(job_id, df)
    job = get_batch_job(job_id)
    return job


@router.get("/api/batch/{job_id}")
def batch_status(job_id: int, _: None = Depends(require_access)):
    job = get_batch_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="任务不存在")
    return job
