"""健康检查、元数据、模型管理。"""
from __future__ import annotations

import json
import os
from pathlib import Path

from api.schemas import EvaluateRequest
from auth import optional_api_key, require_access
from evaluation_service import EvaluationService
from fastapi import APIRouter, Depends, HTTPException
from paths import CONFIGS_DIR, load_model_registry, narratives_csv_path
from system_metrics import runtime_info

router = APIRouter(tags=["system"])

PRODUCT_INFO_PATH = CONFIGS_DIR / "product_info.json"


def _artifact_status() -> dict:
    from paths import default_model_paths

    p = default_model_paths()
    return {
        "model_version": p.get("model_version"),
        "micro_weights": Path(p["bert_classifier_weights"]).is_file(),
        "bart_dir": Path(p["bart_model_dir"]).is_dir(),
        "xgb_e1": Path(p["auto_xgb_folder"]).joinpath("auto_xgb_model_SC_E1.joblib").is_file(),
    }


def _llm_status() -> bool:
    try:
        from llm_service import is_llm_available

        return is_llm_available()
    except Exception:
        return False


@router.get("/api/health")
def health():
    svc = EvaluationService.get()
    reg = load_model_registry()
    arts = _artifact_status()
    return {
        "status": "ok",
        "predictor_loaded": svc.is_ready,
        "predictor_error": svc.last_error,
        "product_version": json.loads(PRODUCT_INFO_PATH.read_text(encoding="utf-8")).get(
            "product_version", "POC"
        )
        if PRODUCT_INFO_PATH.is_file()
        else "POC",
        "active_model_version": reg.get("active_version"),
        "narratives_csv": narratives_csv_path().is_file(),
        "artifacts": arts,
        "runtime": runtime_info(),
        "llm_configured": _llm_status(),
        "tenant_id": os.environ.get("NARRO_TENANT_ID", "default"),
        "auth_api": True,
        "features": {"auth_api": True, "account_login": True},
    }


@router.get("/api/models")
def list_models(_: None = Depends(require_access)):
    reg = load_model_registry()
    svc = EvaluationService.get()
    return {
        "active_version": reg.get("active_version"),
        "loaded_version": svc.model_version,
        "loaded": svc.is_ready,
        "versions": [
            {"id": k, "label": v.get("label", k)} for k, v in reg.get("versions", {}).items()
        ],
    }


@router.post("/api/models/reload")
def reload_models(version: str | None = None, _: None = Depends(require_access)):
    try:
        return EvaluationService.get().reload(version=version)
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e)) from e


@router.get("/api/about")
def about(_: None = Depends(require_access)):
    if not PRODUCT_INFO_PATH.is_file():
        raise HTTPException(status_code=404, detail="缺少 configs/product_info.json")
    data = json.loads(PRODUCT_INFO_PATH.read_text(encoding="utf-8"))
    arts = _artifact_status()
    data["artifacts_ready"] = {
        "micro": arts["micro_weights"],
        "bart": arts["bart_dir"],
        "xgb": arts["xgb_e1"],
    }
    data["active_model_version"] = arts.get("model_version")
    if narratives_csv_path().is_file():
        import pandas as pd

        try:
            data["reference_corpus_rows"] = len(pd.read_csv(narratives_csv_path()))
        except Exception:
            pass
    return data


@router.get("/api/meta")
def meta(_: None = Depends(require_access)):
    from story_metadata import STORY_LABELS as SM_LABELS, TASK_BY_STORY

    about_data = about()
    return {
        "story_types": [{"id": k, "label": v} for k, v in SM_LABELS.items()],
        "story_task_rules": [
            {"story_type": k, "task_type": v, "label": SM_LABELS.get(k, k)}
            for k, v in TASK_BY_STORY.items()
        ],
        "auto_story_detection": True,
        "age_range": [4, 5, 6],
        "product": {
            "version": about_data.get("product_version"),
            "disclaimer": about_data.get("disclaimer"),
            "non_diagnostic_notice": about_data.get("non_diagnostic_notice"),
            "active_model_version": about_data.get("active_model_version"),
        },
    }


@router.post("/api/detect-story")
def detect_story(body: EvaluateRequest, _: None = Depends(require_access)):
    from story_metadata import STORY_LABELS, resolve_story_and_task

    try:
        st, tt, conf, story_inf, task_inf = resolve_story_and_task(
            body.text.strip(), story_type=body.story_type, task_type=body.task_type
        )
        return {
            "story_type": st,
            "story_label": STORY_LABELS.get(st, st),
            "task_type": tt,
            "story_inferred": story_inf,
            "task_inferred": task_inf,
            "detection_confidence": conf if story_inf else 1.0,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/api/story-stimuli")
def story_stimuli(_: None = Depends(optional_api_key)):
    path = CONFIGS_DIR / "story_stimuli.json"
    if not path.is_file():
        raise HTTPException(status_code=404, detail="未配置 story_stimuli.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


@router.get("/api/picture-books")
def picture_books(_: None = Depends(optional_api_key)):
    path = CONFIGS_DIR / "picture_books.json"
    if not path.is_file():
        raise HTTPException(status_code=404, detail="未配置 picture_books.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


@router.get("/api/llm/status")
def llm_status(_: None = Depends(require_access)):
    from llm_service import is_llm_available, load_llm_config

    cfg = load_llm_config()
    return {
        "available": is_llm_available(),
        "model": cfg.get("model", "deepseek-chat"),
        "provider": cfg.get("provider", "deepseek"),
    }


@router.get("/api/release-check")
def release_check(skip_golden: bool = False, _: None = Depends(require_access)):
    arts = _artifact_status()
    ok = arts["micro_weights"] and arts["bart_dir"] and arts["xgb_e1"]
    return {"ok": ok, "artifacts": arts, "golden_skipped": skip_golden}
