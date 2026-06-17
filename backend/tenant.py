"""部署级租户标识（单进程单租户；多园所可配置不同 NARRO_TENANT_ID）。"""
from __future__ import annotations

import os


def current_tenant_id() -> str:
    tid = os.environ.get("NARRO_TENANT_ID", "default").strip()
    return tid or "default"
