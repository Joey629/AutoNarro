/**
 * Narro 前端共享 UI 工具（XSS 安全、鉴权下载、提示）。
 */
(function () {
  function escapeHtml(s) {
    return String(s ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function apiHeadersFromStorage() {
    const key = localStorage.getItem("narro_api_key") || "";
    const h = { "Content-Type": "application/json" };
    if (key) h["X-API-Key"] = key;
    const session = localStorage.getItem("narro_session_token");
    if (session) h.Authorization = `Bearer ${session}`;
    return h;
  }

  async function downloadWithAuth(apiBase, path) {
    const res = await fetch(`${apiBase}${path}`, { headers: apiHeadersFromStorage() });
    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      throw new Error(data.detail || `HTTP ${res.status}`);
    }
    const blob = await res.blob();
    const cd = res.headers.get("Content-Disposition") || "";
    const m = /filename="?([^";]+)"?/.exec(cd);
    const name = m ? m[1] : "download";
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = name;
    a.click();
    URL.revokeObjectURL(url);
  }

  function showNarroBanner(message, { variant = "info", timeoutMs = 6000 } = {}) {
    let root = document.getElementById("narroBannerRoot");
    if (!root) {
      root = document.createElement("div");
      root.id = "narroBannerRoot";
      root.className = "narro-banner-root";
      root.setAttribute("role", "status");
      root.setAttribute("aria-live", "polite");
      document.body.appendChild(root);
    }
    const el = document.createElement("div");
    el.className = `narro-banner narro-banner-${variant}`;
    el.textContent = message;
    root.appendChild(el);
    setTimeout(() => el.remove(), timeoutMs);
  }

  /** MAIN 框架：A2–A16 仅显示编码（A2、A3…），不替换为其它文案 */
  function ssTaskLabel(id) {
    return id ? String(id) : "";
  }

  window.NarroUI = {
    escapeHtml,
    downloadWithAuth,
    showNarroBanner,
    ssTaskLabel,
    /** @deprecated 使用 ssTaskLabel */
    microTaskLabel: ssTaskLabel,
  };
})();
