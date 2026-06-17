"""账户注册、登录与档案 API。"""
from __future__ import annotations

import os
import sys
import uuid
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "backend"))
sys.path.insert(0, str(_REPO / "src"))

os.environ.setdefault("NARRO_DATA_DIR", str(_REPO / "data" / "test_account_api"))
os.environ.pop("NARRO_API_KEY", None)
os.environ.pop("NARRO_REQUIRE_API_KEY", None)

from api.main import app  # noqa: E402
from evaluation_store import init_db  # noqa: E402


@pytest.fixture()
def client(tmp_path, monkeypatch):
    db_dir = tmp_path / "db"
    db_dir.mkdir()
    monkeypatch.setenv("NARRO_DATA_DIR", str(db_dir))
    init_db()
    with TestClient(app) as c:
        yield c


def test_register_login_profile_flow(client: TestClient):
    email = f"parent-{uuid.uuid4().hex[:8]}@example.com"
    reg = client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": "secretpass",
            "display_name": "小明妈妈",
        },
    )
    assert reg.status_code == 200, reg.text
    body = reg.json()
    assert body["ok"] is True
    assert body["token"]
    assert body["user"]["email"] == email
    assert body["user"]["display_name"] == "小明妈妈"
    assert body["user"]["avatar_id"] == "default"
    token = body["token"]
    headers = {"Authorization": f"Bearer {token}"}

    me = client.get("/api/auth/me", headers=headers)
    assert me.status_code == 200
    assert me.json()["user"]["display_name"] == "小明妈妈"

    put = client.post(
        "/api/profile",
        headers=headers,
        json={
            "caregiver_name": "小明妈妈",
            "child_name": "小明",
            "child_id": "c01",
            "age": 5,
            "gender": "男",
            "left_behind": 0,
            "class_name": "大一班",
            "notes": "",
        },
    )
    assert put.status_code == 200
    assert put.json()["profile"]["child_name"] == "小明"

    patch = client.patch(
        "/api/auth/account",
        headers=headers,
        json={"avatar_id": "child-boy", "display_name": "明妈"},
    )
    assert patch.status_code == 200
    assert patch.json()["user"]["avatar_id"] == "child-boy"

    logout = client.post("/api/auth/logout", headers=headers)
    assert logout.status_code == 200

    bad = client.get("/api/auth/me", headers=headers)
    assert bad.status_code == 401


def test_login_wrong_password(client: TestClient):
    client.post(
        "/api/auth/register",
        json={"email": "a@b.com", "password": "longenough", "display_name": ""},
    )
    res = client.post(
        "/api/auth/login",
        json={"email": "a@b.com", "password": "wrongone"},
    )
    assert res.status_code == 401
