/**
 * Unified evaluation report rendering (history + manager surfaces).
 */
(function initNarroReport(global) {
  const $ = (id) => document.getElementById(id);
  const escapeHtml =
    global.NarroUI?.escapeHtml ||
    ((s) =>
      String(s ?? "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;"));

  const STORY_SHORT = {
    cat: "小猫",
    dog: "小狗",
    bird: "小鸟",
    goat: "小羊",
    "pn-agent": "个人叙事Agent",
  };

  function storyLabel(storyType) {
    return STORY_SHORT[storyType] || storyType || "—";
  }

  function rowToRenderPayload(row) {
    const ling = row.linguistics || {};
    const nq = row.narrative_quality || ling.narrative_quality || null;
    return {
      evaluation_id: row.evaluation_id ?? row.id,
      status: row.status || "completed",
      status_message: row.status_message || "",
      regression: row.regression || {},
      microstructure: row.microstructure || {},
      linguistics: ling,
      narrative_quality: nq,
      elapsed_ms: row.elapsed_ms ?? 0,
      parent_summary: row.parent_summary || "",
      report_text: row.report_text || "",
      story_type: row.story_type,
      text: row.text || row.narrative_text || "",
      parent_survey: row.parent_survey || null,
      coach_mode: row.coach_mode || "free",
      dialogue_log: row.dialogue_log || [],
      has_narrative_audio: !!row.has_narrative_audio,
    };
  }

  function getNarrativeQuality(data) {
    const stored = data?.narrative_quality || data?.linguistics?.narrative_quality;
    if (stored) return stored;
    const text = data?.text || "";
    const core = data?.linguistics?.core || {};
    return inferLegacyNarrativeQuality(text, core);
  }

  function inferLegacyNarrativeQuality(text, core) {
    const raw = String(text || "").trim();
    const chars = raw.replace(/\s+/g, "").length;
    const tnw = Number(core.TNW) || 0;
    const tnu = Number(core.TNU) || 0;
    const tdw = Number(core.TDW) || 0;
    if (/^(你好|嗨|hello|测试)[。.!！?？\s]*$/i.test(raw) || chars < 10 || tnw < 5) {
      return {
        status: "insufficient",
        message: "无法评估：讲述过短或未形成完整叙事，请结合图卡完整讲述后再试。",
      };
    }
    if (chars < 20 || tnu < 2 || tnw < 8 || tdw < 4) {
      return { status: "low_quality", message: "讲述偏短，分数仅供参考。" };
    }
    return { status: "sufficient", score: null, message: "" };
  }

  function paintQualityBanner(q, bannerId) {
    const el = typeof bannerId === "string" ? $(bannerId) : bannerId;
    if (!el) return;
    if (!q || q.status === "sufficient") {
      el.classList.add("hidden");
      el.innerHTML = "";
      return;
    }
    el.classList.remove("hidden");
    const insufficient = q.status === "insufficient";
    el.className = `narro-quality-banner ${insufficient ? "narro-quality-insufficient" : "narro-quality-warn"}`;
    const title = insufficient ? "无法评估" : "质量提示";
    el.innerHTML = `<p class="narro-quality-title">${title}</p><p class="narro-quality-msg">${escapeHtml(q.message || "")}</p>`;
  }

  function scoresSuppressed(q) {
    return q && q.status === "insufficient";
  }

  function dedupeParentSummary(summary, q) {
    if (!summary || !q || q.status === "sufficient") return summary || "";
    const msg = (q.message || "").trim();
    const lines = String(summary)
      .split("\n")
      .filter((line) => {
        const t = line.trim();
        if (!t) return false;
        if (msg && t.includes(msg)) return false;
        if (q.status === "insufficient" && /无法评估|讲述过短|未形成完整叙事/.test(t)) return false;
        if (q.status === "low_quality" && /讲述偏短|仅供参考/.test(t)) return false;
        return true;
      });
    return lines.join("\n").trim() || summary;
  }

  function sanitizeReportForDisplay(report, q) {
    if (!report || !q || q.status === "sufficient") return report || "";
    const msg = (q.message || "").replace(/[【】]/g, "").trim();
    return String(report)
      .split("\n")
      .filter((line) => {
        const t = line.trim();
        if (!t) return true;
        if (msg && t.includes(msg)) return false;
        if (/^【.*(无法评估|讲述偏短|质量提示).+】$/.test(t)) return false;
        if (/^【质量提示】/.test(t)) return false;
        return true;
      })
      .join("\n")
      .trim();
  }

  function formatScEpisode(v) {
    if (v == null) return null;
    const n = Number(v);
    return Number.isInteger(n) || Math.abs(n - Math.round(n)) < 1e-6
      ? String(Math.round(n))
      : n.toFixed(2);
  }

  function fillScDetail(el, reg) {
    if (!el) return;
    el.innerHTML = "";
    ["pred_SC_E1", "pred_SC_E2", "pred_SC_E3"].forEach((k, i) => {
      const v = reg[k];
      if (v == null) return;
      const li = document.createElement("li");
      li.textContent = `情节 ${i + 1}: ${formatScEpisode(v)}`;
      el.appendChild(li);
    });
  }

  function fillScDualTrack(el, reg) {
    if (!el) return;
    const main = reg?.sc_main;
    const direct = reg?.sc_direct;
    const agr = reg?.sc_agreement || {};
    if (!main && !direct) {
      el.innerHTML =
        '<p class="text-xs text-muted-foreground">双轨对照暂无（需训练 models/macro_sc_main 与 models/macro_sc_direct，或沿用 legacy 回归）</p>';
      return;
    }
    const lines = [];
    if (main) {
      lines.push(
        `<p><strong>轨 A · MAIN</strong> 合计 ${main.sum}（情节 ${main.SC_E1} / ${main.SC_E2} / ${main.SC_E3}）</p>`
      );
    }
    if (direct) {
      lines.push(
        `<p><strong>轨 B · 直接 SC</strong> 合计 ${direct.sum}（情节 ${direct.SC_E1} / ${direct.SC_E2} / ${direct.SC_E3}）</p>`
      );
    }
    if (main && direct && agr.delta_sum != null) {
      lines.push(`<p class="text-xs">Δ总和 = ${agr.delta_sum}</p>`);
    }
    if (agr.flag_review) {
      lines.push(
        `<p class="text-amber-600 text-xs font-medium">⚠ ${escapeHtml(agr.message || "建议人工复核")}</p>`
      );
    } else if (agr.message) {
      lines.push(`<p class="text-xs text-muted-foreground">${escapeHtml(agr.message)}</p>`);
    }
    el.innerHTML = lines.join("");
  }

  function fillLingMetrics(el, core, peer) {
    if (!el) return;
    const lingKeys = [
      ["TNW", "总词数"],
      ["TDW", "不同词数"],
      ["TNU", "句子数"],
      ["MLU", "平均句长"],
      ["TTR", "词型率"],
    ];
    el.innerHTML =
      lingKeys
        .map(([k, zh]) => {
          const v = core[k];
          if (v == null) return "";
          const disp = k === "MLU" || k === "TTR" ? Number(v).toFixed(k === "TTR" ? 3 : 2) : v;
          const norm =
            peer[k] != null ? ` <span class="text-xs text-muted-foreground">常模 ${peer[k]}</span>` : "";
          return `<li><strong>${zh}</strong> ${disp}${norm}</li>`;
        })
        .join("") || "<li class='text-muted-foreground'>—</li>";
  }

  function formatScBreakdown(reg) {
    const parts = [];
    ["pred_SC_E1", "pred_SC_E2", "pred_SC_E3"].forEach((k, i) => {
      const v = reg[k];
      const s = formatScEpisode(v);
      if (s != null) parts.push(`情节${i + 1} ${s}`);
    });
    return parts.join(" · ");
  }

  function fillTaskGrid(el, tasks) {
    if (!el) return;
    el.innerHTML = "";
    (tasks || []).forEach((t) => {
      const cell = document.createElement("div");
      cell.className = `badge text-center py-2 ${t.value ? "badge-default" : "badge-outline"}`;
      cell.innerHTML = `<strong class="block">${t.id}</strong><span class="text-[10px] opacity-80">${t.value ? "达标" : "—"} ${(t.probability * 100).toFixed(0)}%</span>`;
      el.appendChild(cell);
    });
  }

  function fillTaskGridCompact(el, tasks) {
    if (!el) return;
    const list = tasks || [];
    if (!list.length) {
      el.innerHTML = '<span class="text-sm text-muted-foreground">—</span>';
      return;
    }
    el.innerHTML = list
      .map((t) => {
        const pct = (t.probability * 100).toFixed(0);
        const cls = t.value ? "pass" : "fail";
        const mark = t.value ? "✓" : "—";
        const label = global.NarroUI?.ssTaskLabel(t.id) || t.id;
        return `<span class="record-task-chip ${cls}" title="${escapeHtml(label)} ${pct}%">${escapeHtml(label)} ${mark}</span>`;
      })
      .join("");
  }

  const REPORT_UI = {
    history: {
      title: "historyTitle",
      evalId: "historyEvalId",
      storyLabel: "historyStoryLabel",
      elapsed: "historyElapsed",
      qualityBanner: "historyQualityBanner",
      microHero: "historyMicroHero",
      scHero: "historyScHero",
      scPillWrap: "historyScPillWrap",
      qualityHint: "historyQualityScoreHint",
      scBreakdown: "historyScBreakdown",
      parentSummary: "historyParentSummary",
      microSum: "historyMicroSum",
      scSum: "historyScSum",
      scDetail: "historyScDetail",
      scDualTrack: "historyScDualTrack",
      scCardWrap: "historyScCardWrap",
      lingList: "historyLingMetricsList",
      taskGrid: "historyTaskGrid",
      reportText: "historyReportText",
      narrativeText: "historyNarrativeText",
      taskGridStyle: "compact",
    },
    manager: {
      qualityBanner: "qualityBannerManager",
      microChip: "microSumChip",
      scChip: "scSumChip",
      elapsed: "elapsedManager",
      parentSummary: "parentSummaryManager",
      microSum: "microSumManager",
      scSum: "scSumManager",
      scDetail: "scDetailManager",
      scDualTrack: "scDualTrackManager",
      scCardWrap: "scCardWrapManager",
      lingList: "lingMetricsManager",
      taskGrid: "taskGridManager",
      reportText: "reportTextManager",
      taskGridStyle: "badge",
    },
  };

  function paintReportSurface(data, row, ui, { titleText, afterPaint } = {}) {
    const reg = data.regression || {};
    const q = getNarrativeQuality(data);
    const suppressed = scoresSuppressed(q);
    const sc = !suppressed && reg.pred_SC_Sum != null ? reg.pred_SC_Sum.toFixed(2) : "—";
    const microVal = data.microstructure?.sum;
    const micro = suppressed || microVal == null ? "—" : String(microVal);
    const core = data.linguistics?.core || {};
    const peer = data.linguistics?.peer_norms?.averages || {};
    const tasks = suppressed ? [] : data.microstructure?.tasks || [];
    const summary = dedupeParentSummary(data.parent_summary || "（暂无摘要）", q);
    const report = sanitizeReportForDisplay(data.report_text || "", q);
    const elapsed = `${data.elapsed_ms}ms`;
    const story = storyLabel(row?.story_type || data.story_type || data.story_label);
    const qualityHint =
      q && q.status === "sufficient" && q.score != null
        ? `叙事质量指数 ${(q.score * 100).toFixed(0)}%（供参考）`
        : "";

    paintQualityBanner(q, ui.qualityBanner);
    if (ui.title && $(ui.title)) $(ui.title).textContent = titleText || `${story}故事`;
    if (ui.evalId && $(ui.evalId)) $(ui.evalId).textContent = String(data.evaluation_id ?? "—");
    if (ui.storyLabel && $(ui.storyLabel)) $(ui.storyLabel).textContent = story;
    if (ui.elapsed && $(ui.elapsed)) $(ui.elapsed).textContent = elapsed;
    if (ui.microHero && $(ui.microHero)) $(ui.microHero).textContent = micro;
    if (ui.scHero && $(ui.scHero)) $(ui.scHero).textContent = sc;
    if (ui.scPillWrap && $(ui.scPillWrap)) $(ui.scPillWrap).classList.toggle("hidden", suppressed);
    if (ui.qualityHint && $(ui.qualityHint)) $(ui.qualityHint).textContent = qualityHint;
    if (ui.microSum && $(ui.microSum)) $(ui.microSum).textContent = micro;
    if (ui.scSum && $(ui.scSum)) $(ui.scSum).textContent = sc;
    if (ui.microChip && $(ui.microChip)) {
      $(ui.microChip).textContent = suppressed ? "SS —/15" : `SS ${micro}/15`;
    }
    if (ui.scChip && $(ui.scChip)) {
      $(ui.scChip).textContent = suppressed ? "宏观 SC —" : `宏观 SC ${sc}`;
    }
    fillScDetail(ui.scDetail ? $(ui.scDetail) : null, reg);
    if (ui.scDualTrack) fillScDualTrack($(ui.scDualTrack), reg);
    if (ui.scCardWrap && $(ui.scCardWrap)) $(ui.scCardWrap).classList.toggle("opacity-50", suppressed);
    const br = ui.scBreakdown ? $(ui.scBreakdown) : null;
    if (br) {
      const bd = formatScBreakdown(reg);
      br.textContent = bd;
      br.classList.toggle("hidden", !bd || suppressed);
    }
    if (ui.parentSummary && $(ui.parentSummary)) $(ui.parentSummary).textContent = summary;
    fillLingMetrics(ui.lingList ? $(ui.lingList) : null, core, peer);
    const gridEl = ui.taskGrid ? $(ui.taskGrid) : null;
    if (gridEl) {
      if (ui.taskGridStyle === "badge") fillTaskGrid(gridEl, tasks);
      else fillTaskGridCompact(gridEl, tasks);
    }
    if (ui.reportText && $(ui.reportText)) $(ui.reportText).textContent = report;
    const narr = row?.text || data.text || "";
    if (ui.narrativeText && $(ui.narrativeText)) $(ui.narrativeText).textContent = narr;
    if (typeof afterPaint === "function") afterPaint(row);
  }

  global.NarroReport = {
    REPORT_UI,
    storyLabel,
    rowToRenderPayload,
    getNarrativeQuality,
    scoresSuppressed,
    paintQualityBanner,
    paintReportSurface,
    fillScDetail,
    fillTaskGrid,
    fillTaskGridCompact,
  };
})(window);
