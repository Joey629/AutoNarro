"""评估存储与租户隔离。"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_db(monkeypatch):
    with tempfile.TemporaryDirectory() as tmp:
        data_dir = Path(tmp)
        db_path = data_dir / "evaluations.db"
        monkeypatch.setenv("NARRO_TENANT_ID", "tenant-a")
        monkeypatch.setattr("paths.DATA_DIR", data_dir)
        monkeypatch.setattr("evaluation_store._db_path", lambda: db_path)
        from evaluation_store import init_db

        init_db()
        yield db_path


def test_save_and_list_scoped_by_tenant(temp_db, monkeypatch):
    from evaluation_store import list_evaluations, save_evaluation

    eid = save_evaluation(
        source="test",
        text="小猫想抓蝴蝶。它跳了起来但是没有抓到。蝴蝶飞走了。",
        story_type="cat",
        task_type="Telling",
        age=5,
        left_behind=0,
        predicted_ist_words="",
        report_text="report",
        regression={"pred_SC_Sum": 1.0},
        microstructure={"sum": 3, "tasks": []},
        benchmark_source="test",
        elapsed_ms=10,
        model_version="narro_v4",
    )
    items = list_evaluations(limit=10)
    assert any(i["id"] == eid for i in items)

    monkeypatch.setenv("NARRO_TENANT_ID", "tenant-b")
    assert list_evaluations(limit=10) == []
