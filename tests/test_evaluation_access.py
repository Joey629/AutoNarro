"""评估记录按账号隔离。"""
from __future__ import annotations

import tempfile
import uuid
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from evaluation_access import evaluation_visible_to_user


def test_evaluation_visible_to_user_strict():
    user_a = {"id": 1}
    user_b = {"id": 2}
    guest = {"id": 0}

    assert evaluation_visible_to_user(1, user_a) is True
    assert evaluation_visible_to_user(2, user_a) is False
    assert evaluation_visible_to_user(0, user_a) is False
    assert evaluation_visible_to_user(None, user_a) is False

    assert evaluation_visible_to_user(2, user_b) is True
    assert evaluation_visible_to_user(1, user_b) is False

    assert evaluation_visible_to_user(0, guest) is True
    assert evaluation_visible_to_user(1, guest) is False


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


def _register(client: TestClient, label: str) -> tuple[str, int]:
    email = f"{label}-{uuid.uuid4().hex[:8]}@example.com"
    res = client.post(
        "/api/auth/register",
        json={"email": email, "password": "secretpass", "display_name": label},
    )
    assert res.status_code == 200, res.text
    body = res.json()
    return body["token"], int(body["user"]["id"])


def test_history_and_insights_isolated_by_user(api_client: TestClient):
    from evaluation_store import save_evaluation

    token_a, uid_a = _register(api_client, "user-a")
    token_b, uid_b = _register(api_client, "user-b")
    headers_a = {"Authorization": f"Bearer {token_a}"}
    headers_b = {"Authorization": f"Bearer {token_b}"}

    eid_a = save_evaluation(
        source="test",
        text="用户 A 的讲述内容。小猫想抓蝴蝶。它跳了起来但是没有抓到。",
        story_type="cat",
        task_type="Telling",
        age=5,
        left_behind=0,
        predicted_ist_words="",
        report_text="report-a",
        regression={"pred_SC_Sum": 1.0},
        microstructure={"sum": 3, "tasks": []},
        benchmark_source="test",
        elapsed_ms=10,
        model_version="narro_v4",
        user_id=uid_a,
    )
    eid_b = save_evaluation(
        source="test",
        text="用户 B 的讲述内容。小狗想吃香肠。它跑过去但是没有吃到。",
        story_type="dog",
        task_type="Telling",
        age=6,
        left_behind=0,
        predicted_ist_words="",
        report_text="report-b",
        regression={"pred_SC_Sum": 2.0},
        microstructure={"sum": 5, "tasks": []},
        benchmark_source="test",
        elapsed_ms=10,
        model_version="narro_v4",
        user_id=uid_b,
    )
    save_evaluation(
        source="test",
        text="未归属旧记录。小鸟想飞走。它拍翅膀但是没有飞起来。",
        story_type="bird",
        task_type="Telling",
        age=4,
        left_behind=0,
        predicted_ist_words="",
        report_text="report-legacy",
        regression={"pred_SC_Sum": 0.5},
        microstructure={"sum": 1, "tasks": []},
        benchmark_source="test",
        elapsed_ms=10,
        model_version="narro_v4",
        user_id=0,
    )

    list_a = api_client.get("/api/history", headers=headers_a)
    assert list_a.status_code == 200, list_a.text
    ids_a = {item["id"] for item in list_a.json()["items"]}
    assert ids_a == {eid_a}

    list_b = api_client.get("/api/history", headers=headers_b)
    assert list_b.status_code == 200, list_b.text
    ids_b = {item["id"] for item in list_b.json()["items"]}
    assert ids_b == {eid_b}

    assert api_client.get(f"/api/history/{eid_b}", headers=headers_a).status_code == 404
    assert api_client.get(f"/api/history/{eid_a}", headers=headers_b).status_code == 404

    assert api_client.get("/api/history").status_code == 401


def test_user_insights_filters_by_user_id():
    from admin_analytics import user_insights

    rows = [
        {"id": 1, "user_id": 1, "created_at": "2026-01-01", "story_type": "cat", "pred_SC_Sum": 1.0, "micro_sum": 3},
        {"id": 2, "user_id": 2, "created_at": "2026-01-02", "story_type": "dog", "pred_SC_Sum": 2.0, "micro_sum": 5},
        {"id": 3, "user_id": 0, "created_at": "2026-01-03", "story_type": "bird", "pred_SC_Sum": 0.5, "micro_sum": 1},
    ]

    def fake_load(limit=200):
        return rows

    import admin_analytics as aa

    original = aa._load_all_evaluations
    aa._load_all_evaluations = fake_load
    try:
        out_a = user_insights(user_id=1)
        out_b = user_insights(user_id=2)
    finally:
        aa._load_all_evaluations = original

    assert out_a["evaluation_count"] == 1
    assert out_a["growth"]["points"][0]["evaluation_id"] == 1
    assert out_b["evaluation_count"] == 1
    assert out_b["growth"]["points"][0]["evaluation_id"] == 2
