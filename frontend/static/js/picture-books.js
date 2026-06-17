/**
 * 绘本学习 · 原创电子绘本（与讲故事 MAIN 图卡无关）
 */
(function () {
  const BOOK_SOURCES = ["/api/picture-books", "/static/picture_books.json"];

  const state = {
    catalogOrder: [],
    books: null,
    currentKey: null,
    pageIndex: 0,
  };

  function $(id) {
    return document.getElementById(id);
  }

  function escapeHtml(s) {
    return window.NarroUI?.escapeHtml?.(s) ?? String(s ?? "");
  }

  async function loadCatalog() {
    if (state.books) return { books: state.books, catalogOrder: state.catalogOrder };
    let lastErr = null;
    for (const url of BOOK_SOURCES) {
      try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        if (data?.books) {
          state.books = data.books;
          state.catalogOrder =
            data.catalog_order || Object.keys(data.books);
          return { books: state.books, catalogOrder: state.catalogOrder };
        }
      } catch (e) {
        lastErr = e;
      }
    }
    throw lastErr || new Error("无法加载绘本目录");
  }

  function showLibrary() {
    $("picturebooksLibrary")?.classList.remove("hidden");
    const reader = $("picturebooksReader");
    reader?.classList.add("hidden");
    reader?.setAttribute("aria-hidden", "true");
    state.currentKey = null;
    state.pageIndex = 0;
  }

  function showReader() {
    $("picturebooksLibrary")?.classList.add("hidden");
    const reader = $("picturebooksReader");
    reader?.classList.remove("hidden");
    reader?.setAttribute("aria-hidden", "false");
  }

  function bookDef(key) {
    return state.books?.[key] || null;
  }

  function renderGrid() {
    const grid = $("picturebooksGrid");
    if (!grid || !state.books) return;
    const keys = state.catalogOrder.filter((k) => state.books[k]);
    const cards = keys.map((key) => {
      const def = state.books[key];
      const cover = def.panels?.[0]?.image || "";
      const pages = def.panels?.length || 0;
      const tag = (def.tags && def.tags[0]) || def.subtitle || "";
      const meta = [def.age_hint, `${pages} 页`].filter(Boolean).join(" · ");
      return `
        <article class="picturebooks-card" role="listitem">
          <button type="button" class="picturebooks-card-btn" data-book-key="${escapeHtml(key)}" aria-label="打开绘本：${escapeHtml(def.label)}">
            <div class="picturebooks-card-cover picturebooks-card-cover--illustrated">
              <img src="${escapeHtml(cover)}" alt="" loading="lazy" />
              ${tag ? `<span class="picturebooks-card-badge">${escapeHtml(tag)}</span>` : ""}
            </div>
            <div class="picturebooks-card-body">
              <h3 class="picturebooks-card-title">${escapeHtml(def.label)}</h3>
              <p class="picturebooks-card-meta">${escapeHtml(meta || "点击阅读")}</p>
            </div>
          </button>
        </article>`;
    });
    grid.innerHTML = cards.join("");
    grid.querySelectorAll("[data-book-key]").forEach((btn) => {
      btn.addEventListener("click", () => openReader(btn.dataset.bookKey));
    });
  }

  function renderReaderPage() {
    const def = bookDef(state.currentKey);
    const panels = def?.panels || [];
    if (!panels.length) return;

    const idx = Math.max(0, Math.min(state.pageIndex, panels.length - 1));
    state.pageIndex = idx;
    const p = panels[idx];

    const img = $("picturebooksPageImg");
    if (img) {
      img.src = p.image || "";
      img.alt = (p.caption || `${def.label} 第 ${idx + 1} 页`).trim();
    }

    const cap = $("picturebooksCaption");
    if (cap) cap.textContent = (p.caption || "").trim() || "（请根据画面讲给孩子听）";

    const ind = $("picturebooksPageIndicator");
    if (ind) ind.textContent = `${idx + 1} / ${panels.length}`;

    if ($("picturebooksReaderTitle")) {
      $("picturebooksReaderTitle").textContent = def.label || "绘本";
    }
    const meta = $("picturebooksReaderMeta");
    if (meta) {
      const parts = [def.subtitle, def.age_hint].filter(Boolean);
      meta.textContent = parts.join(" · ");
    }

    const prev = $("picturebooksPrevBtn");
    const next = $("picturebooksNextBtn");
    if (prev) prev.disabled = idx <= 0;
    if (next) next.disabled = idx >= panels.length - 1;

    const dots = $("picturebooksDots");
    if (dots) {
      dots.innerHTML = panels
        .map(
          (_, i) =>
            `<button type="button" class="picturebooks-dot${i === idx ? " is-active" : ""}" data-page="${i}" role="tab" aria-selected="${i === idx ? "true" : "false"}" aria-label="第 ${i + 1} 页"></button>`
        )
        .join("");
      dots.querySelectorAll("[data-page]").forEach((dot) => {
        dot.addEventListener("click", () => {
          state.pageIndex = Number(dot.dataset.page) || 0;
          renderReaderPage();
        });
      });
    }
  }

  function openReader(bookKey) {
    if (!bookDef(bookKey)) return;
    state.currentKey = bookKey;
    state.pageIndex = 0;
    showReader();
    renderReaderPage();
  }

  function stepPage(delta) {
    const panels = bookDef(state.currentKey)?.panels || [];
    if (!panels.length) return;
    state.pageIndex = Math.max(0, Math.min(state.pageIndex + delta, panels.length - 1));
    renderReaderPage();
  }

  async function onTabShown() {
    const loading = $("picturebooksLoading");
    const errEl = $("picturebooksError");
    const grid = $("picturebooksGrid");
    loading?.classList.remove("hidden");
    errEl?.classList.add("hidden");
    grid?.classList.add("hidden");

    try {
      await loadCatalog();
      renderGrid();
      grid?.classList.remove("hidden");
      if (!state.currentKey) showLibrary();
      else renderReaderPage();
    } catch (e) {
      if (errEl) {
        errEl.textContent = `绘本加载失败：${e.message || "未知错误"}`;
        errEl.classList.remove("hidden");
      }
    } finally {
      loading?.classList.add("hidden");
    }
  }

  function bindUi() {
    $("picturebooksBackBtn")?.addEventListener("click", showLibrary);
    $("picturebooksPrevBtn")?.addEventListener("click", () => stepPage(-1));
    $("picturebooksNextBtn")?.addEventListener("click", () => stepPage(1));
    $("picturebooksPracticeBtn")?.addEventListener("click", () => {
      window.__narroSwitchTab?.("session");
    });

    document.addEventListener("keydown", (e) => {
      const reader = $("picturebooksReader");
      if (!reader || reader.classList.contains("hidden")) return;
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        stepPage(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        stepPage(1);
      } else if (e.key === "Escape") {
        showLibrary();
      }
    });

    let touchStartX = 0;
    const stage = document.querySelector(".picturebooks-stage");
    stage?.addEventListener(
      "touchstart",
      (e) => {
        touchStartX = e.changedTouches[0]?.clientX ?? 0;
      },
      { passive: true }
    );
    stage?.addEventListener(
      "touchend",
      (e) => {
        const dx = (e.changedTouches[0]?.clientX ?? 0) - touchStartX;
        if (Math.abs(dx) < 48) return;
        if (dx < 0) stepPage(1);
        else stepPage(-1);
      },
      { passive: true }
    );
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindUi);
  } else {
    bindUi();
  }

  window.NarroPictureBooks = { onTabShown, openReader, showLibrary };
})();
