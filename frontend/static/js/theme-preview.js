/**
 * 测试主题切换：?theme=glass-soft | localStorage narro_theme
 */
(function () {
  const KEY = "narro_theme";
  const GLASS = "glass-soft";

  function readQueryTheme() {
    try {
      return new URLSearchParams(window.location.search).get("theme");
    } catch {
      return null;
    }
  }

  function applyTheme(name) {
    const root = document.documentElement;
    if (name === GLASS) {
      root.classList.add("narro-theme-glass-soft");
      try {
        localStorage.setItem(KEY, GLASS);
      } catch {
        /* ignore */
      }
    } else {
      root.classList.remove("narro-theme-glass-soft");
      try {
        localStorage.removeItem(KEY);
      } catch {
        /* ignore */
      }
    }
  }

  const q = readQueryTheme();
  const stored = (function () {
    try {
      return localStorage.getItem(KEY);
    } catch {
      return null;
    }
  })();
  applyTheme(q || stored);

  window.NarroThemePreview = {
    GLASS,
    isGlass() {
      return document.documentElement.classList.contains("narro-theme-glass-soft");
    },
    enableGlass() {
      applyTheme(GLASS);
      const url = new URL(window.location.href);
      url.searchParams.set("theme", GLASS);
      window.history.replaceState({}, "", url);
    },
    disableGlass() {
      applyTheme(null);
      const url = new URL(window.location.href);
      url.searchParams.delete("theme");
      window.history.replaceState({}, "", url);
    },
    wirePreviewBar() {
      const exit = document.getElementById("narroThemePreviewExit");
      if (exit) {
        exit.addEventListener("click", () => window.NarroThemePreview.disableGlass());
      }
    },
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => window.NarroThemePreview.wirePreviewBar());
  } else {
    window.NarroThemePreview.wirePreviewBar();
  }
})();
