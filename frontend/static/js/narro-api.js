/**
 * Narro HTTP / auth helpers — shared by app.js and future feature modules.
 */
(function initNarroApi(global) {
  function resolveApiBase() {
    const meta = document.querySelector('meta[name="narro-api-base"]');
    const fromMeta = meta?.content?.trim();
    if (fromMeta) return fromMeta.replace(/\/$/, "");
    const { protocol, hostname, port } = window.location;
    if (port === "8000" || port === "") return "";
    if (hostname === "localhost" || hostname === "127.0.0.1") {
      return `${protocol}//${hostname}:8000`;
    }
    return "";
  }

  const API = resolveApiBase();
  const SESSION_KEY = "narro_session_token";

  function apiHeaders(extra = {}) {
    const h = { "Content-Type": "application/json", ...extra };
    const key = localStorage.getItem("narro_api_key");
    if (key) h["X-API-Key"] = key;
    const session = localStorage.getItem(SESSION_KEY);
    if (session) h.Authorization = `Bearer ${session}`;
    return h;
  }

  function apiAuthHeaders(extra = {}) {
    const h = { ...extra };
    const key = localStorage.getItem("narro_api_key");
    if (key) h["X-API-Key"] = key;
    const session = localStorage.getItem(SESSION_KEY);
    if (session) h.Authorization = `Bearer ${session}`;
    return h;
  }

  async function fetchJson(path, options = {}) {
    const { headers: extraHeaders, ...rest } = options;
    const url = `${API}${path}`;
    const res = await fetch(url, {
      ...rest,
      headers: apiHeaders(extraHeaders || {}),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      let detail =
        typeof data.detail === "string"
          ? data.detail
          : Array.isArray(data.detail)
            ? data.detail.map((x) => x.msg || x).join("; ")
            : data.detail
              ? JSON.stringify(data.detail)
              : "";
      if (res.status === 404 && path.startsWith("/api/auth/")) {
        detail =
          "认证接口未找到。请用项目根目录执行 python run_web.py 并访问 http://127.0.0.1:8000/platform（需重启服务以加载最新代码）。";
      }
      throw new Error(detail || `请求失败 (${res.status})`);
    }
    return data;
  }

  async function verifyAuthApiAvailable() {
    const ping = async () => {
      const res = await fetch(`${API}/api/auth/ping`, { method: "GET" });
      if (!res.ok) return false;
      const data = await res.json().catch(() => ({}));
      return data.ok === true;
    };
    const health = async () => {
      const res = await fetch(`${API}/api/health`, { method: "GET" });
      if (!res.ok) return false;
      const data = await res.json().catch(() => ({}));
      return data.auth_api === true || data.features?.auth_api === true;
    };
    for (let i = 0; i < 4; i += 1) {
      if (await ping()) return true;
      if (await health()) return true;
      await new Promise((r) => setTimeout(r, 350));
    }
    return false;
  }

  global.NarroAPI = {
    API,
    SESSION_KEY,
    apiHeaders,
    apiAuthHeaders,
    fetchJson,
    verifyAuthApiAvailable,
  };
})(window);
