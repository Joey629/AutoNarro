"""鉴权 fail-closed 行为。"""
from __future__ import annotations

import os

import pytest
from auth import optional_api_key, require_api_key
from fastapi import HTTPException


def test_optional_api_key_open_when_unconfigured(monkeypatch):
    monkeypatch.delenv("NARRO_API_KEY", raising=False)
    monkeypatch.delenv("NARRO_REQUIRE_API_KEY", raising=False)
    optional_api_key(None)


def test_optional_api_key_rejects_wrong_key(monkeypatch):
    monkeypatch.setenv("NARRO_API_KEY", "secret")
    monkeypatch.delenv("NARRO_REQUIRE_API_KEY", raising=False)
    with pytest.raises(HTTPException) as exc:
        optional_api_key("wrong")
    assert exc.value.status_code == 401


def test_require_api_key_fails_when_required_but_missing_env(monkeypatch):
    monkeypatch.setenv("NARRO_REQUIRE_API_KEY", "1")
    monkeypatch.delenv("NARRO_API_KEY", raising=False)
    with pytest.raises(HTTPException) as exc:
        require_api_key(None)
    assert exc.value.status_code == 503
