/**
 * User / manager history list, detail, rename, delete.
 */
(function initNarroHistory(global) {
  const $ = (id) => document.getElementById(id);
  const escapeHtml =
    global.NarroUI?.escapeHtml ||
    ((s) =>
      String(s ?? "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;"));

  const { rowToRenderPayload, storyLabel } = global.NarroReport || {};
  const { isEvaluationInProgress = (s) => s && s !== "completed" && s !== "failed" } =
    global.NarroEvalStatus || {};

  let ctx = {};

  function storyPhrase(storyType) {
    if (storyType === "pn-agent") return "个人叙事Agent";
    return `${storyLabel?.(storyType) || storyType || "—"}故事`;
  }

  function formatHistoryDateShort(createdAt) {
    if (!createdAt) return "未知日期";
    const d = new Date(createdAt.replace("Z", ""));
    if (Number.isNaN(d.getTime())) return createdAt.slice(0, 10);
    return `${d.getMonth() + 1}月${d.getDate()}日`;
  }

  function formatHistoryTableLabel(r, index, total) {
    const custom = (r.record_label || "").trim();
    if (custom) return custom;
    return `第${total - index}次 · ${storyPhrase(r.story_type)} · ${formatHistoryDateShort(r.created_at)}`;
  }

  function historyRecordLabelFromDom(evalId) {
    const tableCell = document.querySelector(
      `#historyUserBody tr[data-eval-id="${evalId}"] [data-history-label]`
    );
    if (tableCell?.textContent?.trim()) return tableCell.textContent.trim();
    const row = document.querySelector(`.narro-nav-record[data-eval-id="${evalId}"]`);
    return row?.querySelector(".sidebar-nav-record-title")?.textContent?.trim() || "该记录";
  }

  function historyRecordLabel(evalId) {
    return historyRecordLabelFromDom(evalId);
  }

  function usesUserHistoryUI() {
    return !!ctx.usesUserHistoryUI?.();
  }

  function hideHistoryDetail() {
    ctx.closeNarroChatDrawer?.();
    $("historyDetailWrap")?.classList.add("hidden");
    ctx.setSelectedHistoryEvalId?.(null);
    ctx.updateHistoryAskNarroBtn?.();
    document.querySelectorAll("#historyNavItems .sidebar-nav-record-row").forEach((el) =>
      el.classList.remove("active")
    );
    document.querySelectorAll(".history-row-clickable, .history-row-manager-clickable").forEach((tr) =>
      tr.classList.remove("history-row-selected")
    );
    if (usesUserHistoryUI()) {
      const hasRows = !!$("historyUserBody")?.querySelector("tr[data-eval-id]");
      $("historyUserListWrap")?.classList.toggle("hidden", !hasRows);
      $("historyEmpty")?.classList.toggle("hidden", hasRows);
    } else {
      $("historyEmpty")?.classList.remove("hidden");
    }
  }

  function renderHistoryDetail(data, row) {
    ctx.setCurrentEvaluationId?.(data.evaluation_id);
    ctx.setSelectedHistoryEvalId?.(data.evaluation_id);
    ctx.persistLastEvaluation?.(data.evaluation_id);
    ctx.paintEvaluationUI?.(data, row, "history");
    void ctx.paintHistoryNarrativeAudio?.(row, data);
    const st = row?.status || data?.status || "completed";
    ctx.setExportEnabled?.(st === "completed" && !ctx.isPnAgentRecord?.(row));
    if (st === "completed") ctx.refreshLlmStatus?.();
    ctx.resetHistoryCoachThread?.();

    $("historyDetailWrap")?.classList.remove("hidden");
    $("historyEmpty")?.classList.add("hidden");
    if (usesUserHistoryUI()) $("historyUserListWrap")?.classList.add("hidden");
    ctx.setSidebarActive?.("history", data.evaluation_id);
    document.querySelectorAll(".history-row-clickable, .history-row-manager-clickable").forEach((tr) => {
      tr.classList.toggle("history-row-selected", String(tr.dataset.evalId) === String(data.evaluation_id));
    });
    ctx.updateHistoryAskNarroBtn?.();
    ctx.closeNarroChatDrawer?.();
    if (usesUserHistoryUI()) {
      const title = $("historyTitle")?.textContent?.trim();
      if (title && $("mainSub")) $("mainSub").textContent = title;
    }
  }

  function renderUserHistoryTable(items, { selectedId = null } = {}) {
    const wrap = $("historyUserListWrap");
    const tbody = $("historyUserBody");
    const emptyEl = $("historyEmpty");
    const detailOpen = !$("historyDetailWrap")?.classList.contains("hidden");
    if (!tbody) return;

    if (!items.length) {
      tbody.innerHTML = "";
      wrap?.classList.add("hidden");
      if (!detailOpen) emptyEl?.classList.remove("hidden");
      return;
    }

    if (!detailOpen) {
      wrap?.classList.remove("hidden");
      emptyEl?.classList.add("hidden");
    }

    const total = items.length;
    tbody.innerHTML = items
      .map((r, index) => {
        const selected = selectedId != null && String(r.id) === String(selectedId);
        const label = formatHistoryTableLabel(r, index, total);
        const type = storyPhrase(r.story_type);
        const date = formatHistoryDateShort(r.created_at);
        return `<tr class="history-row-clickable${selected ? " history-row-selected" : ""}" data-eval-id="${r.id}">
        <td class="font-medium" data-history-label>${escapeHtml(label)}</td>
        <td>${escapeHtml(type)}</td>
        <td class="whitespace-nowrap">${escapeHtml(date)}</td>
        <td class="whitespace-nowrap text-right">
          <button type="button" class="btn-outline btn-sm" data-view-eval="${r.id}">查看</button>
          <button type="button" class="btn-ghost btn-sm" data-history-table-rename="${r.id}">重命名</button>
          <button type="button" class="btn-ghost btn-sm text-destructive" data-history-table-delete="${r.id}">删除</button>
        </td>
      </tr>`;
      })
      .join("");
  }

  function bindUserHistoryTableEvents() {
    const tbody = $("historyUserBody");
    if (!tbody || tbody.dataset.bound === "1") return;
    tbody.dataset.bound = "1";

    tbody.addEventListener("click", (e) => {
      const renameBtn = e.target.closest("[data-history-table-rename]");
      if (renameBtn?.dataset.historyTableRename) {
        e.stopPropagation();
        void renameHistoryRecord(renameBtn.dataset.historyTableRename);
        return;
      }
      const deleteBtn = e.target.closest("[data-history-table-delete]");
      if (deleteBtn?.dataset.historyTableDelete) {
        e.stopPropagation();
        void deleteHistoryRecord(deleteBtn.dataset.historyTableDelete);
        return;
      }
      const viewBtn = e.target.closest("[data-view-eval]");
      if (viewBtn?.dataset.viewEval) {
        e.stopPropagation();
        void openEvaluation(viewBtn.dataset.viewEval);
        return;
      }
      const row = e.target.closest("tr.history-row-clickable[data-eval-id]");
      if (row?.dataset.evalId) void openEvaluation(row.dataset.evalId);
    });
  }

  function renderHistorySidebarNav(items, { selectedId = null } = {}) {
    const container = $("historyNavItems");
    if (!container) return;
    if (usesUserHistoryUI()) {
      container.innerHTML = "";
      return;
    }
    ctx.applyHistoryNavExpanded?.(ctx.getHistoryNavExpanded?.());
    if (!items.length) {
      container.innerHTML = '<span class="sidebar-nav-empty">暂无记录</span>';
      return;
    }
    const total = items.length;
    container.innerHTML = items
      .map((r, index) => {
        const active = selectedId != null && String(r.id) === String(selectedId);
        const label =
          (r.record_label || "").trim() ||
          `第${total - index}次 · ${storyPhrase(r.story_type)} · ${formatHistoryDateShort(r.created_at)}`;
        const hint =
          r.story_type === "pn-agent"
            ? "个人叙事Agent通话"
            : r.pred_SC_Sum != null
              ? `宏观 SC ${Number(r.pred_SC_Sum).toFixed(1)} · SS ${r.micro_sum ?? "—"}/15`
              : "";
        const tip = hint ? `${label} · ${hint}` : label;
        const pendingTag = isEvaluationInProgress(r.status)
          ? '<span class="sidebar-nav-record-pending">分析中</span>'
          : "";
        return `<div class="sidebar-nav-record-row narro-nav-record${active ? " active" : ""}" data-eval-id="${r.id}">
        <button type="button" class="sidebar-nav-item sidebar-nav-item-record" data-eval-id="${r.id}" title="${escapeHtml(tip)}">
          <span class="sidebar-nav-record-title">${escapeHtml(label)}</span>${pendingTag}
        </button>
        <button type="button" class="sidebar-nav-kebab" aria-label="更多操作" data-eval-id="${r.id}">⋮</button>
        <div class="sidebar-nav-menu hidden" role="menu">
          <button type="button" role="menuitem" data-history-menu-action="rename">重命名</button>
          <button type="button" role="menuitem" class="text-destructive" data-history-menu-action="delete">删除</button>
        </div>
      </div>`;
      })
      .join("");
  }

  async function fetchUserHistoryItems() {
    const { items } = await ctx.fetchJson("/api/history?limit=50");
    return items;
  }

  async function refreshUserHistoryNav({ highlightEvalId = null } = {}) {
    if (!usesUserHistoryUI()) return [];
    const tbody = $("historyUserBody");
    const detailOpen = !$("historyDetailWrap")?.classList.contains("hidden");
    if (tbody && !detailOpen) {
      tbody.innerHTML = `<tr><td colspan="7" class="text-muted-foreground">加载中…</td></tr>`;
    }
    try {
      const items = await fetchUserHistoryItems();
      const onHistoryTab = $("panel-history")?.classList.contains("active");
      const selectedId =
        highlightEvalId ??
        (onHistoryTab
          ? ctx.getSelectedHistoryEvalId?.() ||
            (detailOpen ? ctx.getCurrentEvaluationId?.() : null)
          : null);
      renderUserHistoryTable(items, { selectedId });
      renderHistorySidebarNav([], {});
      return items;
    } catch (e) {
      if (tbody && !detailOpen) {
        tbody.innerHTML = `<tr><td colspan="7">${escapeHtml(e.message || "加载失败")}</td></tr>`;
      }
      renderHistorySidebarNav([], {});
      return [];
    }
  }

  async function applyHistoryRecordRenamed(evalId, label) {
    await refreshUserHistoryNav({ highlightEvalId: evalId });
    const labelCell = document.querySelector(
      `#historyUserBody tr[data-eval-id="${evalId}"] [data-history-label]`
    );
    if (labelCell) labelCell.textContent = label;
    ctx.setSidebarActive?.(null, evalId);
    if (
      String(ctx.getSelectedHistoryEvalId?.()) === String(evalId) ||
      String(ctx.getCurrentEvaluationId?.()) === String(evalId)
    ) {
      if ($("mainSub")) $("mainSub").textContent = label;
      if ($("historyTitle")) $("historyTitle").textContent = label;
    }
  }

  async function applyHistoryRecordDeleted(evalId) {
    const wasViewing =
      String(ctx.getSelectedHistoryEvalId?.()) === String(evalId) ||
      String(ctx.getCurrentEvaluationId?.()) === String(evalId);

    if (String(ctx.getCurrentEvaluationId?.()) === String(evalId)) {
      ctx.setCurrentEvaluationId?.(null);
      ctx.setExportEnabled?.(false);
    }
    if (localStorage.getItem(ctx.LAST_EVAL_KEY) === String(evalId)) {
      localStorage.removeItem(ctx.LAST_EVAL_KEY);
    }

    const items = await refreshUserHistoryNav();
    if (wasViewing && $("panel-history")?.classList.contains("active")) {
      const nextId = items?.[0]?.id;
      if (nextId) {
        await openEvaluation(nextId, { silent: true });
      } else {
        hideHistoryDetail();
      }
    } else if (String(ctx.getSelectedHistoryEvalId?.()) === String(evalId)) {
      hideHistoryDetail();
    }

    if ($("panel-insights")?.classList.contains("active")) ctx.loadInsights?.();
  }

  async function renameHistoryRecord(evalId) {
    const eid = parseInt(String(evalId), 10);
    if (!eid) return;
    const current = historyRecordLabel(evalId);

    await ctx.openNarroDialog({
      title: "重命名记录",
      message: "为这条记录设置名称",
      confirmLabel: "保存",
      input: true,
      inputValue: current,
      validate: (v) => (v ? null : "名称不能为空"),
      onSubmit: async (label) => {
        await ctx.fetchJson(`/api/history/${eid}/rename`, {
          method: "POST",
          body: JSON.stringify({ record_label: label }),
        });
        await applyHistoryRecordRenamed(eid, label);
      },
    });
  }

  async function deleteHistoryRecord(evalId) {
    const eid = parseInt(String(evalId), 10);
    if (!eid) return;
    const name = historyRecordLabel(evalId);

    await ctx.openNarroDialog({
      title: "删除记录",
      message: `确定删除「${name}」？此操作不可恢复。`,
      confirmLabel: "删除",
      destructive: true,
      onSubmit: async () => {
        await ctx.fetchJson(`/api/history/${eid}/delete`, { method: "POST" });
        await applyHistoryRecordDeleted(eid);
      },
    });
  }

  async function openEvaluation(id, { silent = false } = {}) {
    const eid = parseInt(String(id), 10);
    if (!eid) return;
    try {
      const row = await ctx.fetchJson(`/api/history/${eid}`);
      const payload = rowToRenderPayload(row);

      if (usesUserHistoryUI()) {
        renderHistoryDetail(payload, row);
        $("historyEmpty")?.classList.add("hidden");
        if (isEvaluationInProgress(row.status)) {
          ctx.beginEvaluationPolling?.(eid);
        }
        requestAnimationFrame(() => ctx.scrollHistoryDetailIntoView?.());
        return;
      }

      if (row.story_type && ctx.storyStimuliData?.()?.stories?.[row.story_type]) {
        ctx.selectStory?.(row.story_type);
      }
      ctx.renderResults?.(payload);
      ctx.persistLastEvaluation?.(eid);
      if (!$("panel-evaluate")?.classList.contains("active")) {
        ctx.switchTab?.("evaluate");
      }
    } catch (e) {
      if (!silent) void ctx.openNarroAlert?.(e.message || "无法加载该条记录", { title: "记录" });
      throw e;
    }
  }

  async function loadHistory({ evalId = null } = {}) {
    const tbody = $("historyBody");
    const emptyEl = $("historyEmpty");
    const isUser = usesUserHistoryUI();
    const cols = 9;
    const reopenId =
      evalId ||
      ctx.getSelectedHistoryEvalId?.() ||
      (!$("historyDetailWrap")?.classList.contains("hidden") && ctx.getCurrentEvaluationId?.()
        ? ctx.getCurrentEvaluationId()
        : null);
    if (!reopenId) hideHistoryDetail();

    if (isUser) {
      bindUserHistoryTableEvents();
      const detailOpen = !$("historyDetailWrap")?.classList.contains("hidden");
      if (!detailOpen && $("historyUserBody")) {
        $("historyUserBody").innerHTML =
          `<tr><td colspan="4" class="text-muted-foreground">加载中…</td></tr>`;
      }
      try {
        const items = await fetchUserHistoryItems();
        renderUserHistoryTable(items, { selectedId: reopenId });
        renderHistorySidebarNav([], {});
        if (reopenId && items.some((r) => r.id === reopenId || String(r.id) === String(reopenId))) {
          await openEvaluation(reopenId, { silent: true });
        } else if (!items.length && !detailOpen) {
          $("historyUserListWrap")?.classList.add("hidden");
          emptyEl?.classList.remove("hidden");
        }
      } catch (e) {
        renderHistorySidebarNav([], {});
        if (!detailOpen && $("historyUserBody")) {
          $("historyUserBody").innerHTML =
            `<tr><td colspan="4">${escapeHtml(e.message || "加载失败")}</td></tr>`;
        }
        if (emptyEl) emptyEl.textContent = e.message || "加载失败";
        if (!detailOpen) emptyEl?.classList.remove("hidden");
      }
      return;
    }

    if (tbody) {
      tbody.innerHTML = `<tr><td colspan="${cols}" class="text-muted-foreground">加载中…</td></tr>`;
    }

    try {
      let q = "?limit=50";
      const cid = ($("historyChildFilter")?.value || "").trim();
      if (cid) q += `&child_id=${encodeURIComponent(cid)}`;
      let { items } = await ctx.fetchJson(`/api/history${q}`);
      const cls = ($("historyClassFilter")?.value || "").trim();
      if (cls) items = items.filter((r) => (r.class_name || "") === cls);

      if (!items.length) {
        tbody.innerHTML = `<tr><td colspan="${cols}" class="text-muted-foreground">暂无记录</td></tr>`;
        return;
      }
      tbody.innerHTML = items
        .map(
          (r) => `<tr class="history-row-manager-clickable" data-eval-id="${r.id}">
        <td>${r.id}</td>
        <td>${(r.created_at || "").slice(0, 19).replace("T", " ")}</td>
        <td>${escapeHtml(r.child_name || r.child_id || "—")}</td>
        <td>${r.source}</td>
        <td>${r.story_type}</td>
        <td>${r.age}</td>
        <td>${r.pred_SC_Sum != null ? Number(r.pred_SC_Sum).toFixed(2) : "—"}</td>
        <td>${r.micro_sum ?? "—"}/15</td>
        <td class="whitespace-nowrap">
          <button type="button" class="btn-outline btn-sm" data-view-eval="${r.id}">查看</button>
          <button type="button" class="btn-ghost btn-sm" data-export-txt="${r.id}">TXT</button>
          <button type="button" class="btn-ghost btn-sm" data-export-csv="${r.id}">CSV</button>
        </td>
      </tr>`
        )
        .join("");
      tbody.querySelectorAll("[data-view-eval]").forEach((b) => {
        b.addEventListener("click", (e) => {
          e.stopPropagation();
          openEvaluation(b.dataset.viewEval);
        });
      });
      tbody.querySelectorAll(".history-row-clickable, .history-row-manager-clickable").forEach((tr) => {
        tr.addEventListener("click", (e) => {
          if (e.target.closest("button")) return;
          openEvaluation(tr.dataset.evalId);
        });
      });
      if (reopenId && items.some((r) => r.id === reopenId)) {
        await openEvaluation(reopenId, { silent: true });
      }
      tbody.querySelectorAll("[data-export-txt]").forEach((b) => {
        b.addEventListener("click", () => ctx.downloadUrl?.(`/api/history/${b.dataset.exportTxt}/export?format=txt`));
      });
      tbody.querySelectorAll("[data-export-csv]").forEach((b) => {
        b.addEventListener("click", () => ctx.downloadUrl?.(`/api/history/${b.dataset.exportCsv}/export?format=csv`));
      });
    } catch (e) {
      tbody.innerHTML = `<tr><td colspan="${cols}">${e.message}</td></tr>`;
    }
  }

  function refreshHistoryClick() {
    if (usesUserHistoryUI()) {
      const reopenId =
        ctx.getSelectedHistoryEvalId?.() ||
        (!$("historyDetailWrap")?.classList.contains("hidden") ? ctx.getCurrentEvaluationId?.() : null);
      loadHistory({ evalId: reopenId });
    } else {
      loadHistory();
    }
  }

  function bindHistoryChromeEvents() {
    document.querySelectorAll(".refresh-history-btn").forEach((btn) => {
      if (btn.dataset.historyBound === "1") return;
      btn.dataset.historyBound = "1";
      btn.addEventListener("click", refreshHistoryClick);
    });
    const backBtn = $("historyBackToListBtn");
    if (backBtn && backBtn.dataset.historyBound !== "1") {
      backBtn.dataset.historyBound = "1";
      backBtn.addEventListener("click", () => {
        hideHistoryDetail();
        if ($("mainSub")) $("mainSub").textContent = ctx.TAB_TITLES?.history?.[1] || "";
        loadHistory();
      });
    }
    const filterBtn = $("historyFilterBtn");
    if (filterBtn && filterBtn.dataset.historyBound !== "1") {
      filterBtn.dataset.historyBound = "1";
      filterBtn.addEventListener("click", () => loadHistory());
    }
    const clearBtn = $("historyClearFilterBtn");
    if (clearBtn && clearBtn.dataset.historyBound !== "1") {
      clearBtn.dataset.historyBound = "1";
      clearBtn.addEventListener("click", () => {
        if ($("historyChildFilter")) $("historyChildFilter").value = "";
        if ($("historyClassFilter")) $("historyClassFilter").value = "";
        loadHistory();
      });
    }
  }

  function init(deps) {
    ctx = deps;
    bindHistoryChromeEvents();
  }

  global.NarroHistory = {
    init,
    loadHistory,
    openEvaluation,
    hideHistoryDetail,
    renderHistoryDetail,
    refreshUserHistoryNav,
    renameHistoryRecord,
    deleteHistoryRecord,
    historyRecordLabelFromDom,
    formatHistoryDateShort,
    refreshHistoryClick,
    bindUserHistoryTableEvents,
  };
})(window);
