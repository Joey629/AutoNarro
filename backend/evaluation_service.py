"""评估编排层：API 与 pipeline 共用，隔离模型加载与推理。"""
from __future__ import annotations

import threading
import time
from typing import Any, Optional

from logging_config import setup_logging

logger = setup_logging()


class EvaluationService:
    """单例式评估服务：可 reload、失败后可重试加载。"""

    _instance: Optional["EvaluationService"] = None
    _inst_lock = threading.Lock()

    def __init__(self) -> None:
        self._predictor = None
        self._lock = threading.Lock()
        self._infer_lock = threading.Lock()
        self._ready = False
        self._last_error: Optional[str] = None
        self._model_version: Optional[str] = None
        self._load_count = 0

    @classmethod
    def get(cls) -> "EvaluationService":
        with cls._inst_lock:
            if cls._instance is None:
                cls._instance = EvaluationService()
            return cls._instance

    @property
    def is_ready(self) -> bool:
        return self._ready and self._predictor is not None

    @property
    def last_error(self) -> Optional[str]:
        return self._last_error

    @property
    def model_version(self) -> Optional[str]:
        return self._model_version

    def reload(self, version: str | None = None) -> dict[str, Any]:
        """卸载并重新加载模型（修复加载失败后无需重启进程）。"""
        with self._lock:
            self._predictor = None
            self._ready = False
            self._last_error = None
        return self.load(version=version, force=True)

    def load(self, version: str | None = None, force: bool = False) -> dict[str, Any]:
        if self._ready and self._predictor is not None and not force:
            return {"status": "already_loaded", "model_version": self._model_version}

        with self._lock:
            if self._ready and self._predictor is not None and not force:
                return {"status": "already_loaded", "model_version": self._model_version}
            try:
                from paths import default_model_paths
                from pipeline_predict_report import AutomatedNarrativePredictor

                import os

                paths = default_model_paths(version)
                paths["benchmark_db_regression"] = os.environ.get("NARRO_BENCHMARK_REG", "")
                paths["benchmark_db_multitask"] = os.environ.get("NARRO_BENCHMARK_MULTI", "")
                t0 = time.time()
                logger.info("开始加载模型 version=%s", paths.get("model_version"))
                self._predictor = AutomatedNarrativePredictor(paths)
                self._ready = True
                self._last_error = None
                self._model_version = paths.get("model_version")
                self._load_count += 1
                elapsed = round(time.time() - t0, 1)
                logger.info("模型加载完成 version=%s (%.1fs)", self._model_version, elapsed)
                return {
                    "status": "loaded",
                    "model_version": self._model_version,
                    "elapsed_s": elapsed,
                    "benchmark_source": getattr(self._predictor, "_benchmark_source", ""),
                }
            except Exception as e:
                self._predictor = None
                self._ready = False
                self._last_error = str(e)
                logger.exception("模型加载失败")
                raise

    def _ensure_predictor(self):
        if not self.is_ready:
            try:
                self.load()
            except Exception as e:
                raise RuntimeError(
                    f"模型未就绪: {e}。可调用 POST /api/models/reload 重试。"
                ) from e
        return self._predictor

    def _compute_evaluation(
        self,
        text: str,
        age: int,
        left_behind: int,
        story_type: Optional[str] = None,
        task_type: Optional[str] = None,
        *,
        on_status: Optional[Any] = None,
    ) -> dict[str, Any]:
        from pipeline_predict_report import TASK_NAMES_GLOBAL
        from story_metadata import resolve_story_and_task

        st, tt, det_conf, story_inf, task_inf = resolve_story_and_task(
            text, story_type=story_type, task_type=task_type
        )

        if on_status:
            on_status("loading_model", "正在加载模型（首次可能约 1–2 分钟）…")

        predictor = self._ensure_predictor()

        if on_status:
            on_status("analyzing", "正在分析叙事与打分…")

        t0 = time.time()
        with self._infer_lock:
            predicted_ist = predictor.bart_predictor.predict_ist_words(text)
            report, regression, tasks, linguistics, narrative_quality = predictor.predict(
                text,
                st,
                age,
                left_behind,
                task_type=tt,
                predicted_ist_words=predicted_ist,
            )
        linguistics = {**(linguistics or {}), "narrative_quality": narrative_quality}

        insufficient = narrative_quality.get("status") == "insufficient"
        if insufficient:
            micro = {"tasks": [], "sum": None, "max": 15, "suppressed": True}
            reg = {
                k: None
                for k in (
                    "pred_SC_E1",
                    "pred_SC_E2",
                    "pred_SC_E3",
                    "pred_SC_Sum",
                    "pred_SC_Sum_beta",
                )
            }
            reg["sc_main"] = None
            reg["sc_direct"] = None
            reg["sc_agreement"] = {"flag_review": False, "message": "叙事质量不足"}
        else:
            micro = {
                "tasks": [],
                "sum": int(tasks.get("pred_MultiTask_Sum", 0)),
                "max": 15,
            }
            for name in TASK_NAMES_GLOBAL:
                micro["tasks"].append(
                    {
                        "id": name,
                        "label": name,
                        "value": int(tasks.get(name, 0)),
                        "probability": round(float(tasks.get(f"{name}_prob", 0)), 4),
                    }
                )
            reg = {}
            for k, v in regression.items():
                if k in ("sc_main", "sc_direct", "sc_agreement"):
                    reg[k] = v
                    continue
                if not str(k).startswith("pred_SC"):
                    continue
                if k == "pred_SC_Sum_beta":
                    reg[k] = bool(v)
                elif v is None:
                    reg[k] = None
                else:
                    reg[k] = round(float(v), 2)
            if reg.get("pred_SC_Sum") is not None:
                reg.setdefault("pred_SC_Sum_beta", True)

        from benchmark_norms import (
            EXPERT_MACRO_SUM_COL,
            EXPERT_MICRO_SUM_COL,
            expert_peer_mean,
        )
        from parent_report import generate_parent_summary

        peer_macro = expert_peer_mean(
            predictor.benchmark_db_reg, EXPERT_MACRO_SUM_COL, age, st, tt
        )
        peer_micro = expert_peer_mean(
            predictor.benchmark_db_reg, EXPERT_MICRO_SUM_COL, age, st, tt
        )
        n_peer = peer_macro.get("n") or 0
        parent_summary = generate_parent_summary(
            age=age,
            regression=reg,
            microstructure=micro,
            linguistics=linguistics,
            peer_macro=peer_macro.get("mean"),
            peer_micro=peer_micro.get("mean"),
            n_peer=n_peer,
            narrative_quality=narrative_quality,
        )

        elapsed = int((time.time() - t0) * 1000)
        return {
            "story_type": st,
            "task_type": tt,
            "detection_confidence": det_conf,
            "story_inferred": story_inf,
            "task_inferred": task_inf,
            "predicted_ist_words": predicted_ist,
            "report_text": report,
            "regression": reg,
            "microstructure": micro,
            "linguistics": linguistics,
            "narrative_quality": narrative_quality,
            "parent_summary": parent_summary,
            "benchmark_source": getattr(predictor, "_benchmark_source", "unknown"),
            "elapsed_ms": elapsed,
            "peer_norms": {
                "expert_SC_Sum_mean": peer_macro.get("mean"),
                "expert_micro_sum_mean": peer_micro.get("mean"),
                "n": n_peer,
                "source": "narratives.csv",
            },
        }

    def _result_payload(
        self,
        evaluation_id: int,
        text: str,
        computed: dict[str, Any],
        *,
        child_id: str = "",
        child_name: str = "",
        class_name: str = "",
        status: str = "completed",
        status_message: str = "",
    ) -> dict[str, Any]:
        from story_metadata import STORY_LABELS

        st = computed["story_type"]
        det_conf = computed["detection_confidence"]
        story_inf = computed["story_inferred"]
        return {
            "evaluation_id": evaluation_id,
            "ok": True,
            "status": status,
            "status_message": status_message,
            "text": text,
            "story_type": st,
            "story_label": STORY_LABELS.get(st, st),
            "task_type": computed["task_type"],
            "story_inferred": story_inf,
            "task_inferred": computed["task_inferred"],
            "detection_confidence": det_conf if story_inf else 1.0,
            "report_text": computed["report_text"],
            "predicted_ist_words": computed["predicted_ist_words"],
            "regression": computed["regression"],
            "microstructure": computed["microstructure"],
            "linguistics": computed["linguistics"],
            "narrative_quality": computed["narrative_quality"],
            "parent_summary": computed["parent_summary"],
            "child_id": child_id.strip(),
            "child_name": child_name.strip(),
            "class_name": class_name.strip(),
            "peer_norms": computed["peer_norms"],
            "benchmark_source": computed["benchmark_source"],
            "elapsed_ms": computed["elapsed_ms"],
            "model_version": self._model_version,
        }

    def evaluate_one(
        self,
        text: str,
        age: int,
        left_behind: int,
        story_type: Optional[str] = None,
        task_type: Optional[str] = None,
        child_id: str = "",
        child_name: str = "",
        class_name: str = "",
        source: str = "api",
    ) -> dict[str, Any]:
        from evaluation_store import save_evaluation

        computed = self._compute_evaluation(
            text, age, left_behind, story_type=story_type, task_type=task_type
        )
        st = computed["story_type"]
        eid = save_evaluation(
            source=source,
            text=text,
            story_type=st,
            task_type=computed["task_type"],
            age=age,
            left_behind=left_behind,
            predicted_ist_words=computed["predicted_ist_words"],
            report_text=computed["report_text"],
            regression=computed["regression"],
            microstructure=computed["microstructure"],
            linguistics=computed["linguistics"],
            parent_summary=computed["parent_summary"],
            child_id=child_id.strip(),
            child_name=child_name.strip(),
            class_name=class_name.strip(),
            benchmark_source=computed["benchmark_source"],
            elapsed_ms=computed["elapsed_ms"],
            model_version=self._model_version or "",
        )
        logger.info(
            "评估完成 id=%s story=%s age=%s ms=%s",
            eid,
            st,
            age,
            computed["elapsed_ms"],
        )
        return self._result_payload(
            eid,
            text,
            computed,
            child_id=child_id,
            child_name=child_name,
            class_name=class_name,
        )

    def start_evaluation_async(
        self,
        text: str,
        age: int,
        left_behind: int,
        story_type: Optional[str] = None,
        task_type: Optional[str] = None,
        child_id: str = "",
        child_name: str = "",
        class_name: str = "",
        source: str = "web_single",
        coach_mode: str = "free",
        dialogue_log: Optional[list] = None,
    ) -> dict[str, Any]:
        """创建记录并后台推理；API 立即返回 evaluation_id。"""
        from evaluation_store import create_pending_evaluation
        from story_metadata import STORY_LABELS, resolve_story_and_task

        st, tt, det_conf, story_inf, task_inf = resolve_story_and_task(
            text, story_type=story_type, task_type=task_type
        )
        eid = create_pending_evaluation(
            source=source,
            text=text.strip(),
            story_type=st,
            task_type=tt,
            age=age,
            left_behind=left_behind,
            child_id=child_id.strip(),
            child_name=child_name.strip(),
            class_name=class_name.strip(),
            status_message="已创建记录，准备分析…",
            coach_mode=coach_mode or "free",
            dialogue_log=dialogue_log or [],
        )
        params = {
            "text": text.strip(),
            "age": age,
            "left_behind": left_behind,
            "story_type": st,
            "task_type": tt,
            "child_id": child_id.strip(),
            "child_name": child_name.strip(),
            "class_name": class_name.strip(),
        }
        thread = threading.Thread(
            target=self._run_evaluation_job,
            args=(eid, params),
            daemon=True,
            name=f"narro-eval-{eid}",
        )
        thread.start()
        logger.info("异步评估已排队 id=%s", eid)
        return {
            "evaluation_id": eid,
            "ok": True,
            "status": "pending",
            "status_message": "已创建记录，准备分析…",
            "text": text.strip(),
            "story_type": st,
            "story_label": STORY_LABELS.get(st, st),
            "task_type": tt,
            "story_inferred": story_inf,
            "task_inferred": task_inf,
            "detection_confidence": det_conf if story_inf else 1.0,
            "child_id": child_id.strip(),
            "child_name": child_name.strip(),
            "class_name": class_name.strip(),
            "model_version": self._model_version,
        }

    def _run_evaluation_job(self, evaluation_id: int, params: dict[str, Any]) -> None:
        from evaluation_store import (
            complete_evaluation,
            fail_evaluation,
            update_evaluation_status,
        )

        def on_status(status: str, message: str) -> None:
            update_evaluation_status(evaluation_id, status, message)

        try:
            on_status("pending", "排队中…")
            computed = self._compute_evaluation(
                params["text"],
                params["age"],
                params["left_behind"],
                story_type=params.get("story_type"),
                task_type=params.get("task_type"),
                on_status=on_status,
            )
            complete_evaluation(
                evaluation_id,
                predicted_ist_words=computed["predicted_ist_words"],
                report_text=computed["report_text"],
                regression=computed["regression"],
                microstructure=computed["microstructure"],
                linguistics=computed["linguistics"],
                parent_summary=computed["parent_summary"],
                benchmark_source=computed["benchmark_source"],
                elapsed_ms=computed["elapsed_ms"],
                model_version=self._model_version or "",
            )
            logger.info(
                "异步评估完成 id=%s ms=%s",
                evaluation_id,
                computed["elapsed_ms"],
            )
        except Exception as e:
            logger.exception("异步评估失败 id=%s", evaluation_id)
            fail_evaluation(
                evaluation_id,
                str(e) or "评估失败，请稍后重试",
            )
