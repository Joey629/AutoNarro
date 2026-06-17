"""异步评估：先建记录再写入结果。"""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def eval_db(monkeypatch):
    with tempfile.TemporaryDirectory() as tmp:
        data_dir = Path(tmp)
        db_path = data_dir / "evaluations.db"
        monkeypatch.setenv("NARRO_TENANT_ID", "tenant-a")
        monkeypatch.setattr("paths.DATA_DIR", data_dir)
        monkeypatch.setattr("evaluation_store._db_path", lambda: db_path)
        from evaluation_store import init_db

        init_db()
        yield db_path


def test_pending_then_complete(eval_db):
    from evaluation_store import (
        complete_evaluation,
        create_pending_evaluation,
        get_evaluation,
        update_evaluation_status,
    )

    eid = create_pending_evaluation(
        source="test",
        text="小猫想抓蝴蝶。它跳了起来但是没有抓到。",
        story_type="cat",
        task_type="Telling",
        age=5,
        left_behind=0,
    )
    row = get_evaluation(eid)
    assert row is not None
    assert row["status"] == "pending"
    assert row["text"].startswith("小猫")

    update_evaluation_status(eid, "analyzing", "正在分析叙事与打分…")
    row = get_evaluation(eid)
    assert row["status"] == "analyzing"

    complete_evaluation(
        eid,
        predicted_ist_words="蝴蝶",
        report_text="report",
        regression={"pred_SC_Sum": 5.0},
        microstructure={"sum": 8, "tasks": [], "max": 15},
        linguistics={},
        parent_summary="摘要",
        benchmark_source="test",
        elapsed_ms=100,
        model_version="narro_v4",
    )
    done = get_evaluation(eid)
    assert done["status"] == "completed"
    assert done["regression"]["pred_SC_Sum"] == 5.0
    assert done["report_text"] == "report"
