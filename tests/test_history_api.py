"""历史记录重命名 / 删除 API。"""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def api_client(monkeypatch):
    with tempfile.TemporaryDirectory() as tmp:
        data_dir = Path(tmp)
        data_dir.mkdir(parents=True, exist_ok=True)
        db_path = data_dir / "evaluations.db"
        monkeypatch.setenv("NARRO_TENANT_ID", "tenant-a")
        monkeypatch.setenv("NARRO_DATA_DIR", str(data_dir))
        monkeypatch.delenv("NARRO_REQUIRE_API_KEY", raising=False)
        monkeypatch.delenv("NARRO_API_KEY", raising=False)
        monkeypatch.setattr("paths.DATA_DIR", data_dir)
        monkeypatch.setattr("evaluation_store._db_path", lambda: db_path)
        monkeypatch.setattr("account_store._db_path", lambda: db_path)
        monkeypatch.setattr("user_profile_store._db_path", lambda: db_path)
        from evaluation_store import init_db

        init_db()
        from backend.api.main import app

        yield TestClient(app)


def test_history_rename_and_delete_post(api_client: TestClient):
    from evaluation_store import save_evaluation

    reg = api_client.post(
        "/api/auth/register",
        json={
            "email": f"hist-{__import__('uuid').uuid4().hex[:8]}@example.com",
            "password": "secretpass",
            "display_name": "历史测试",
        },
    )
    assert reg.status_code == 200, reg.text
    token = reg.json()["token"]
    uid = int(reg.json()["user"]["id"])
    headers = {"Authorization": f"Bearer {token}"}

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
        user_id=uid,
    )

    r = api_client.post(f"/api/history/{eid}/rename", json={"record_label": "自定义名称"}, headers=headers)
    assert r.status_code == 200, r.text
    assert r.json()["record_label"] == "自定义名称"

    detail = api_client.get(f"/api/history/{eid}", headers=headers)
    assert detail.status_code == 200
    assert detail.json()["record_label"] == "自定义名称"

    d = api_client.post(f"/api/history/{eid}/delete", headers=headers)
    assert d.status_code == 200, d.text

    gone = api_client.get(f"/api/history/{eid}", headers=headers)
    assert gone.status_code == 404
