"""pytest 路径与临时数据目录。"""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "backend"))

os.environ.setdefault("NARRO_TENANT_ID", "test-tenant")
