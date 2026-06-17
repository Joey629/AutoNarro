/**
 * 专属练习绘本：多次评估汇总 → DeepSeek 生成 → 场景 SVG 插画
 */
(function () {
  const state = {
    status: null,
    books: [],
    currentBook: null,
    pageIndex: 0,
    busy: false,
  };

  function $(id) {
    return document.getElementById(id);
  }

  function escapeHtml(s) {
    return window.NarroUI?.escapeHtml?.(s) ?? String(s ?? "");
  }

  function apiHeaders() {
    return window.NarroUI?.apiHeadersFromStorage?.() || { "Content-Type": "application/json" };
  }

  function getChildId() {
    const p = window.__narroGetFamilyProfile?.();
    return (p?.child_id || "").trim();
  }

  function getChildName() {
    const p = window.__narroGetFamilyProfile?.();
    return (p?.child_name || "").trim();
  }

  async function fetchJson(url, opts = {}) {
    const res = await fetch(url, { ...opts, headers: { ...apiHeaders(), ...opts.headers } });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || data.message || `HTTP ${res.status}`);
    return data;
  }

  function renderStatus(st) {
    const el = $("personalizedBooksStatus");
    if (!el || !st) return;
    const cid = st.child_id || "（未填写）";
    const can = st.can_generate;
    const llm = st.llm_available;
    const n = st.completed_evaluations ?? 0;
    const need = st.min_evaluations_required ?? 2;
    el.innerHTML = `
      <p class="personalized-books-status-line"><strong>儿童 ID：</strong>${escapeHtml(cid)}</p>
      <p class="personalized-books-status-line"><strong>已完成评估：</strong>${n} 次（至少 ${need} 次可生成）</p>
      <p class="personalized-books-status-line"><strong>DeepSeek：</strong>${llm ? "已配置" : "未配置"}</p>
      <p class="personalized-books-status-line text-muted-foreground">${escapeHtml(st.image_note || "插画：内置场景图")}</p>
      ${!cid || cid === "（未填写）" ? '<p class="personalized-books-warn">请先在「个人信息」填写儿童 ID，且每次评估使用同一 ID。</p>' : ""}
      ${!can && cid ? `<p class="personalized-books-warn">评估次数不足，请先在「讲故事」多完成几次。</p>` : ""}
    `;
    const btn = $("personalizedBooksGenerateBtn");
    if (btn) btn.disabled = !can || !llm || state.busy || !st.child_id;
  }

  function renderGrid() {
    const grid = $("personalizedBooksGrid");
    if (!grid) return;
    if (!state.books.length) {
      grid.innerHTML =
        '<p class="personalized-books-empty">还没有专属绘本。满足评估次数后点击「生成专属绘本」。</p>';
      return;
    }
    grid.innerHTML = state.books
      .map((b) => {
        const cover =
          b.cover_image ||
          b.book?.pages?.[0]?.image ||
          "/static/picturebooks/scenes/sunny_park.svg";
        const skills = (b.target_skills || []).join("、");
        return `
        <article class="picturebooks-card" role="listitem">
          <button type="button" class="picturebooks-card-btn" data-book-id="${b.id}" aria-label="打开：${escapeHtml(b.title)}">
            <div class="picturebooks-card-cover picturebooks-card-cover--illustrated">
              <img src="${escapeHtml(cover)}" alt="" loading="lazy" />
              <span class="picturebooks-card-badge">专属</span>
            </div>
            <div class="picturebooks-card-body">
              <h3 class="picturebooks-card-title">${escapeHtml(b.title || "专属绘本")}</h3>
              <p class="picturebooks-card-meta">${escapeHtml(skills || "练习绘本")} · ${escapeHtml((b.evaluation_ids || []).length + " 次评估")}</p>
            </div>
          </button>
        </article>`;
      })
      .join("");
    grid.querySelectorAll("[data-book-id]").forEach((btn) => {
      btn.addEventListener("click", () => void openBook(Number(btn.dataset.bookId)));
    });
  }

  function showLibrary() {
    $("personalizedBooksLibrary")?.classList.remove("hidden");
    const reader = $("personalizedBooksReader");
    reader?.classList.add("hidden");
    reader?.setAttribute("aria-hidden", "true");
    state.currentBook = null;
    state.pageIndex = 0;
  }

  function showReader() {
    $("personalizedBooksLibrary")?.classList.add("hidden");
    const reader = $("personalizedBooksReader");
    reader?.classList.remove("hidden");
    reader?.setAttribute("aria-hidden", "false");
  }

  function renderReaderPage() {
    const book = state.currentBook?.book || state.currentBook;
    const pages = book?.pages || [];
    if (!pages.length) return;

    const idx = Math.max(0, Math.min(state.pageIndex, pages.length - 1));
    state.pageIndex = idx;
    const p = pages[idx];

    const img = $("personalizedBooksPageImg");
    if (img) {
      img.src = p.image || "";
      img.alt = (p.caption || "").trim();
    }
    if ($("personalizedBooksCaption")) {
      $("personalizedBooksCaption").textContent = (p.caption || "").trim();
    }
    if ($("personalizedBooksPageIndicator")) {
      $("personalizedBooksPageIndicator").textContent = `${idx + 1} / ${pages.length}`;
    }
    if ($("personalizedBooksReaderTitle")) {
      $("personalizedBooksReaderTitle").textContent =
        state.currentBook?.title || book?.title || "专属绘本";
    }
    if ($("personalizedBooksReaderMeta")) {
      const skills = (state.currentBook?.target_skills || book?.target_skills || []).join(" · ");
      $("personalizedBooksReaderMeta").textContent = skills ? `练习重点：${skills}` : "";
    }
    const tip = $("personalizedBooksParentTip");
    const tipText = (book?.parent_tip || "").trim();
    if (tip) {
      tip.textContent = tipText ? `💡 ${tipText}` : "";
      tip.classList.toggle("hidden", !tipText);
    }

    const prev = $("personalizedBooksPrevBtn");
    const next = $("personalizedBooksNextBtn");
    if (prev) prev.disabled = idx <= 0;
    if (next) next.disabled = idx >= pages.length - 1;

    const dots = $("personalizedBooksDots");
    if (dots) {
      dots.innerHTML = pages
        .map(
          (_, i) =>
            `<button type="button" class="picturebooks-dot${i === idx ? " is-active" : ""}" data-page="${i}" role="tab" aria-label="第 ${i + 1} 页"></button>`
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

  async function openBook(bookId) {
    const data = await fetchJson(`/api/personalized-picture-books/${bookId}`);
    state.currentBook = data;
    state.pageIndex = 0;
    showReader();
    renderReaderPage();
  }

  function stepPage(delta) {
    const pages = state.currentBook?.book?.pages || state.currentBook?.pages || [];
    if (!pages.length) return;
    state.pageIndex = Math.max(0, Math.min(state.pageIndex + delta, pages.length - 1));
    renderReaderPage();
  }

  async function refresh() {
    const errEl = $("personalizedBooksError");
    errEl?.classList.add("hidden");
    const cid = getChildId();
    if (!cid) {
      state.status = {
        child_id: "",
        completed_evaluations: 0,
        min_evaluations_required: 2,
        can_generate: false,
        llm_available: false,
        image_note: "",
        books: [],
      };
      state.books = [];
      renderStatus(state.status);
      renderGrid();
      return;
    }
    const st = await fetchJson(
      `/api/personalized-picture-books/status?child_id=${encodeURIComponent(cid)}`
    );
    state.status = st;
    state.books = st.books || [];
    renderStatus(st);
    renderGrid();
  }

  async function generate() {
    const cid = getChildId();
    if (!cid) {
      void window.openNarroAlert?.("请先在「个人信息」填写儿童 ID。", { title: "专属绘本" });
      return;
    }
    state.busy = true;
    $("personalizedBooksGenerateBtn") && ($("personalizedBooksGenerateBtn").disabled = true);
    $("personalizedBooksLoading")?.classList.remove("hidden");
    $("personalizedBooksError")?.classList.add("hidden");
    try {
      const data = await fetchJson("/api/personalized-picture-books/generate", {
        method: "POST",
        body: JSON.stringify({
          child_id: cid,
          child_name: getChildName(),
        }),
      });
      await refresh();
      if (data?.id) await openBook(data.id);
      window.NarroUI?.showNarroBanner?.("专属绘本已生成", { variant: "success" });
    } catch (e) {
      const errEl = $("personalizedBooksError");
      if (errEl) {
        errEl.textContent = e.message || "生成失败";
        errEl.classList.remove("hidden");
      }
    } finally {
      state.busy = false;
      $("personalizedBooksLoading")?.classList.add("hidden");
      renderStatus(state.status || {});
    }
  }

  async function onTabShown() {
    showLibrary();
    $("personalizedBooksLoading")?.classList.remove("hidden");
    try {
      await refresh();
    } catch (e) {
      const errEl = $("personalizedBooksError");
      if (errEl) {
        errEl.textContent = e.message || "加载失败";
        errEl.classList.remove("hidden");
      }
    } finally {
      $("personalizedBooksLoading")?.classList.add("hidden");
    }
  }

  function bindUi() {
    $("personalizedBooksGenerateBtn")?.addEventListener("click", () => void generate());
    $("personalizedBooksRefreshBtn")?.addEventListener("click", () => void refresh());
    $("personalizedBooksBackBtn")?.addEventListener("click", showLibrary);
    $("personalizedBooksPrevBtn")?.addEventListener("click", () => stepPage(-1));
    $("personalizedBooksNextBtn")?.addEventListener("click", () => stepPage(1));

    document.addEventListener("keydown", (e) => {
      const reader = $("personalizedBooksReader");
      if (!reader || reader.classList.contains("hidden")) return;
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        stepPage(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        stepPage(1);
      } else if (e.key === "Escape") showLibrary();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindUi);
  } else {
    bindUi();
  }

  window.NarroPersonalizedBooks = { onTabShown, refresh };
})();
