"""运行时资源指标（健康检查用）。"""
from __future__ import annotations

import os
import platform


def memory_stats() -> dict:
    out = {"rss_mb": None, "vms_mb": None, "system_total_mb": None, "system_available_mb": None}
    try:
        import psutil

        p = psutil.Process(os.getpid())
        mi = p.memory_info()
        out["rss_mb"] = round(mi.rss / 1024 / 1024, 1)
        out["vms_mb"] = round(mi.vms / 1024 / 1024, 1)
        vm = psutil.virtual_memory()
        out["system_total_mb"] = round(vm.total / 1024 / 1024, 1)
        out["system_available_mb"] = round(vm.available / 1024 / 1024, 1)
    except ImportError:
        pass
    return out


def runtime_info() -> dict:
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "memory": memory_stats(),
    }
