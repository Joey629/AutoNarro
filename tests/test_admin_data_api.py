"""管理员会话与平台数据 API。"""
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

os.environ.pop("NARRO_API_KEY", None)
os.environ.pop("NARRO_REQUIRE_API_KEY", None)
os.environ.pop("NARRO_ADMIN_EMAILS", None)

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


def _login(client: TestClient, email: str, password: str) -> str:
    res = client.post(
        "/api/auth/enter",
        json={"email": email, "password": password, "display_name": ""},
    )
    assert res.status_code == 200, res.text
    return res.json()["token"]


def test_builtin_admin_login_and_data_access(client: TestClient):
    user_token = _login(client, f"user-{uuid.uuid4().hex[:8]}@example.com", "secretpass")
    admin_token = _login(client, "admin", "123456")

    denied = client.get(
        "/api/admin/users",
        headers={"Authorization": f"Bearer {user_token}"},
    )
    assert denied.status_code == 403

    users = client.get(
        "/api/admin/users",
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert users.status_code == 200, users.text
    assert len(users.json()["items"]) >= 2

    me = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert me.status_code == 200
    assert me.json()["user"]["is_admin"] is True
    assert me.json()["user"]["email"] == "admin"
