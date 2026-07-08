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
const $ = (id) => document.getElementById(id);

const PERSONA_KEY = "narro_persona";
const LAST_EVAL_KEY = "narro_last_evaluation_id";

const STORY_SHORT = { cat: "小猫", dog: "小狗", bird: "小鸟", goat: "小羊", "pn-agent": "个人叙事Agent" };

let currentEvaluationId = null;
let lastBatchSummaryCsv = null;
let currentPersona = "user";
let llmAvailable = false;
let activeTabName = null;
let historyNavExpanded = true;
const SIDEBAR_COLLAPSED_KEY = "narro_sidebar_collapsed";
const LEGACY_STORAGE_KEYS = [
  ["autonarro_persona", "narro_persona"],
  ["autonarro_last_evaluation_id", "narro_last_evaluation_id"],
  ["autonarro_sidebar_collapsed", "narro_sidebar_collapsed"],
  ["autonarro_api_key", "narro_api_key"],
];

function migrateLegacyStorage() {
  for (const [oldKey, newKey] of LEGACY_STORAGE_KEYS) {
    const v = localStorage.getItem(oldKey);
    if (v != null && localStorage.getItem(newKey) == null) {
      localStorage.setItem(newKey, v);
    }
  }
}

migrateLegacyStorage();
let sidebarCollapsed = localStorage.getItem(SIDEBAR_COLLAPSED_KEY) === "1";

function isSidebarCollapsed() {
  return $("appSidebar")?.classList.contains("narro-sidebar-collapsed");
}

function applySidebarCollapsed(collapsed) {
  sidebarCollapsed = collapsed;
  $("appSidebar")?.classList.toggle("narro-sidebar-collapsed", collapsed);
  const closeBtn = $("sidebarCollapseBtn");
  const expandBtn = $("sidebarExpandBtn");
  if (closeBtn) {
    closeBtn.setAttribute("aria-expanded", String(!collapsed));
    closeBtn.hidden = collapsed;
  }
  if (expandBtn) {
    expandBtn.setAttribute("aria-expanded", String(!collapsed));
  }
  localStorage.setItem(SIDEBAR_COLLAPSED_KEY, collapsed ? "1" : "0");
}

function toggleSidebarCollapsed() {
  applySidebarCollapsed(!sidebarCollapsed);
}
let selectedHistoryEvalId = null;

const SAMPLE = {
  text: "小猫想抓蝴蝶。它跳了起来，但是没有抓到。蝴蝶飞走了。小猫很难过，坐在草地上。后来男孩来拿球，小猫又去拿鱼。",
  age: 5,
  left_behind: 0,
};

const TAB_TITLES = {
  session: ["MAIN评估Agent", "先看完全部图卡，录下孩子的讲述，完成后到「我的记录」查看报告"],
  "pn-agent": ["个人叙事Agent", ""],
  history: ["我的记录", "查看并回溯历次评估结果"],
  insights: ["洞察", "长期进步追踪 · 关注薄弱项与告警"],
  profile: ["个人信息", "管理看护人与儿童基本信息"],
};

const PROFILE_CACHE_KEY = "narro_family_profile";
const SESSION_KEY = "narro_session_token";
const AVATAR_IDS = ["default", "child-boy", "child-girl", "caregiver"];
let familyProfile = null;
let currentUser = null;

const DEFAULT_TAB = "session";

function applyPersonaChrome() {
  currentPersona = "user";
  document.body.classList.remove("persona-manager");
  document.body.classList.add("persona-user");
  $("navUser")?.classList.remove("hidden");
  $("navManager")?.classList.add("hidden");
  $("managerBatchBlock")?.classList.add("hidden");
  refreshLlmStatus();
}

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

function hasSessionToken() {
  return !!localStorage.getItem(SESSION_KEY);
}

function hasApiKeyAccess() {
  return !!localStorage.getItem("narro_api_key");
}

function avatarImageUrl(avatarId) {
  const id = AVATAR_IDS.includes(avatarId) ? avatarId : "default";
  return `/static/images/avatars/${id}.svg`;
}

function showAuthGate(show) {
  const gate = $("authGate");
  const shell = $("appShell");
  if (gate) {
    gate.classList.toggle("hidden", !show);
    gate.setAttribute("aria-hidden", show ? "false" : "true");
  }
  shell?.classList.toggle("app-shell--auth-locked", !!show);
  if (show) {
    setAuthGateError("");
    void verifyAuthApiAvailable().then((ok) => {
      if (!ok) {
        setAuthGateError(
          "认证服务未就绪：请在项目根目录执行 python run_web.py，并访问 http://127.0.0.1:8000/platform（若刚更新代码，请先停止旧进程再启动）。"
        );
      } else {
        setAuthGateError("");
      }
    });
  }
}

function setAuthGateError(msg) {
  const el = $("authGateError");
  if (!el) return;
  if (msg) {
    el.textContent = msg;
    el.classList.remove("hidden");
  } else {
    el.textContent = "";
    el.classList.add("hidden");
  }
}

function switchAuthTab(tab) {
  const login = tab === "login";
  $("authLoginForm")?.classList.toggle("hidden", !login);
  $("authRegisterForm")?.classList.toggle("hidden", login);
  document.querySelectorAll(".auth-tab").forEach((btn) => {
    const on = btn.dataset.authTab === tab;
    btn.classList.toggle("active", on);
    btn.setAttribute("aria-selected", on ? "true" : "false");
  });
  setAuthGateError("");
}

async function onAuthSuccess(data) {
  if (data?.token) localStorage.setItem(SESSION_KEY, data.token);
  currentUser = data?.user || null;
  familyProfile = data?.profile || familyProfile || defaultFamilyProfile();
  if (familyProfile) localStorage.setItem(PROFILE_CACHE_KEY, JSON.stringify(familyProfile));
  showAuthGate(false);
  setAuthGateError("");
  paintSidebarProfile();
  fillProfileForm(familyProfile);
  switchTab(DEFAULT_TAB);
  await refreshUserHistoryNav();
  syncCoachEvaluationContext();
  await refreshLlmStatus();
}

async function restoreSession() {
  if (hasSessionToken()) {
    try {
      const data = await fetchJson("/api/auth/me");
      currentUser = data.user || null;
      familyProfile = data.profile || defaultFamilyProfile();
      localStorage.setItem(PROFILE_CACHE_KEY, JSON.stringify(familyProfile));
      showAuthGate(false);
      return true;
    } catch {
      localStorage.removeItem(SESSION_KEY);
      currentUser = null;
    }
  }
  if (hasApiKeyAccess()) {
    showAuthGate(false);
    await loadFamilyProfile();
    return true;
  }
  showAuthGate(true);
  return false;
}

async function logoutUser() {
  try {
    await fetchJson("/api/auth/logout", { method: "POST" });
  } catch {
    /* ignore */
  }
  localStorage.removeItem(SESSION_KEY);
  currentUser = null;
  familyProfile = defaultFamilyProfile();
  showAuthGate(true);
  switchAuthTab("login");
  paintSidebarProfile();
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

function getNarrativeText() {
  if (currentPersona === "user") {
    return ($("storyTranscript")?.value || "").trim();
  }
  return ($("narrativeText")?.value || "").trim();
}

function setNarrativeText(text) {
  if ($("storyTranscript")) $("storyTranscript").value = text;
  if ($("narrativeText")) $("narrativeText").value = text;
  updateCharCount();
}

function evalPayload() {
  if (currentPersona === "user") {
    const p = familyProfile || defaultFamilyProfile();
    const coach = window.NarroStoryCoach;
    return {
      text: getNarrativeText(),
      age: parseInt(String(p.age ?? 5), 10) || 5,
      left_behind: parseInt(String(p.left_behind ?? 0), 10) ? 1 : 0,
      child_id: p.child_id || "",
      child_name: p.child_name || "",
      class_name: p.class_name || "",
      story_type: selectedStory,
      coach_mode: coach?.getCoachMode?.() || "free",
      dialogue_log: coach?.getDialogueLog?.() || [],
    };
  }
  return {
    text: getNarrativeText(),
    age: parseInt($("age").value, 10),
    left_behind: parseInt($("leftBehind").value, 10),
    child_id: ($("childId")?.value || "").trim(),
    child_name: ($("childName")?.value || "").trim(),
    class_name: ($("className")?.value || "").trim(),
  };
}

/** 叙事评估页仅保留讲述区（结果统一在「我的记录」查看） */
function resetSessionAssessmentView() {
  $("sessionPage")?.classList.remove("session-has-results");
  refreshLlmStatus();
}

function scrollHistoryDetailIntoView() {
  $("historyDetailWrap")?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function clearSidebarActive() {
  document
    .querySelectorAll("#navUser .sidebar-nav-item, #navManager .sidebar-nav-item")
    .forEach((t) => t.classList.remove("active"));
  $("sidebarProfileBtn")?.classList.remove("active");
  document
    .querySelectorAll("#historyNavItems .sidebar-nav-record-row")
    .forEach((r) => r.classList.remove("active"));
}

function setSidebarActive(name, evalId = null) {
  clearSidebarActive();
  if (evalId != null && currentPersona !== "user") {
    const row = document.querySelector(
      `#historyNavItems .sidebar-nav-record-row[data-eval-id="${evalId}"]`
    );
    row?.classList.add("active");
    return;
  }
  if (name === "profile") {
    $("sidebarProfileBtn")?.classList.add("active");
    return;
  }
  const navRoot = currentPersona === "user" ? "#navUser" : "#navManager";
  const nav = document.querySelector(`${navRoot} .sidebar-nav-item[data-tab="${name}"]`);
  nav?.classList.add("active");
}

function defaultFamilyProfile() {
  return {
    caregiver_name: "",
    child_name: "",
    child_id: "",
    age: 5,
    gender: "",
    left_behind: 0,
    class_name: "",
    notes: "",
    updated_at: null,
  };
}

function profileInitials(profile) {
  const p = profile || defaultFamilyProfile();
  const src = (p.caregiver_name || p.child_name || "").trim();
  if (!src) return "?";
  const parts = src.replace(/\s+/g, "").split("");
  if (parts.length >= 2 && /[\u4e00-\u9fff]/.test(src)) {
    return parts.slice(0, 2).join("");
  }
  return parts.slice(0, 2).join("").toUpperCase() || "?";
}

function profileDisplayName(profile) {
  const userName = (currentUser?.display_name || "").trim();
  if (userName) return userName;
  const p = profile || defaultFamilyProfile();
  return (p.caregiver_name || "").trim() || (p.child_name || "").trim() || "未设置";
}

function profileDisplaySub(profile) {
  const p = profile || defaultFamilyProfile();
  const bits = ["家庭版"];
  const child = (p.child_name || "").trim();
  if (child) bits.push(child);
  if (p.age) bits.push(`${p.age} 岁`);
  if (p.gender) bits.push(p.gender);
  if (!child) bits.push("请完善儿童信息");
  return bits.join(" · ");
}

function paintSidebarProfile() {
  const p = familyProfile || defaultFamilyProfile();
  const img = $("sidebarProfileAvatarImg");
  const fallback = $("sidebarProfileAvatar");
  const nameEl = $("sidebarProfileName");
  const subEl = $("sidebarProfileSub");
  const display = profileDisplayName(p);
  const useAvatar = currentUser && currentUser.id > 0;
  if (useAvatar && img) {
    img.src = avatarImageUrl(currentUser.avatar_id || "default");
    img.alt = display;
    img.classList.remove("hidden");
    if (fallback) fallback.classList.add("hidden");
  } else if (img) {
    img.classList.add("hidden");
    if (fallback) {
      fallback.classList.remove("hidden");
      fallback.textContent = profileInitials(p);
    }
  }
  if (nameEl) nameEl.textContent = display;
  if (subEl) subEl.textContent = profileDisplaySub(p);
  const tip = $("sidebarProfileBtn")?.querySelector(".sidebar-nav-tooltip");
  if (tip) tip.textContent = display;
}

function syncProfileAvatarUi(avatarId) {
  const id = AVATAR_IDS.includes(avatarId) ? avatarId : "default";
  const url = avatarImageUrl(id);
  const preview = $("profileAvatarPreview");
  if (preview) preview.src = url;
  document.querySelectorAll(".profile-avatar-option").forEach((btn) => {
    btn.classList.toggle("selected", btn.dataset.avatarId === id);
  });
}

function fillAccountForm(user) {
  const u = user || currentUser;
  const emailEl = $("profileAccountEmail");
  if (emailEl) {
    emailEl.textContent = u?.email ? `登录邮箱：${u.email}` : "访客模式（API Key）";
  }
  if ($("profileDisplayName")) $("profileDisplayName").value = u?.display_name || "";
  if ($("profilePhone")) $("profilePhone").value = u?.phone || "";
  syncProfileAvatarUi(u?.avatar_id || "default");
  const guest = !u || u.id <= 0;
  $("profileAccountCard")?.classList.toggle("hidden", guest);
  $("profilePasswordForm")?.classList.toggle("hidden", guest);
  $("profileLogoutBtn")?.classList.toggle("hidden", guest);
}

function fillProfileForm(profile) {
  const p = profile || defaultFamilyProfile();
  if ($("profileCaregiverName")) $("profileCaregiverName").value = p.caregiver_name || "";
  if ($("profileChildName")) $("profileChildName").value = p.child_name || "";
  if ($("profileChildId")) $("profileChildId").value = p.child_id || "";
  if ($("profileAge")) $("profileAge").value = String(p.age ?? 5);
  if ($("profileGender")) $("profileGender").value = p.gender || "";
  if ($("profileLeftBehind")) $("profileLeftBehind").value = String(p.left_behind ?? 0);
  if ($("profileClassName")) $("profileClassName").value = p.class_name || "";
  if ($("profileNotes")) $("profileNotes").value = p.notes || "";
  const at = $("profileUpdatedAt");
  if (at) {
    at.textContent = p.updated_at
      ? `上次保存：${String(p.updated_at).slice(0, 19).replace("T", " ")}`
      : "";
  }
  fillAccountForm(currentUser);
}

function readProfileForm() {
  return {
    caregiver_name: ($("profileCaregiverName")?.value || "").trim(),
    child_name: ($("profileChildName")?.value || "").trim(),
    child_id: ($("profileChildId")?.value || "").trim(),
    age: parseInt($("profileAge")?.value || "5", 10) || 5,
    gender: ($("profileGender")?.value || "").trim(),
    left_behind: parseInt($("profileLeftBehind")?.value || "0", 10) ? 1 : 0,
    class_name: ($("profileClassName")?.value || "").trim(),
    notes: ($("profileNotes")?.value || "").trim(),
  };
}

async function loadFamilyProfile() {
  try {
    const path = hasSessionToken() ? "/api/auth/me" : "/api/profile";
    const data = await fetchJson(path);
    if (data.user) currentUser = data.user;
    familyProfile = data.profile || defaultFamilyProfile();
    localStorage.setItem(PROFILE_CACHE_KEY, JSON.stringify(familyProfile));
  } catch {
    try {
      const raw = localStorage.getItem(PROFILE_CACHE_KEY);
      familyProfile = raw ? JSON.parse(raw) : defaultFamilyProfile();
    } catch {
      familyProfile = defaultFamilyProfile();
    }
  }
  paintSidebarProfile();
  if ($("panel-profile")?.classList.contains("active")) fillProfileForm(familyProfile);
}

async function saveFamilyProfile() {
  const payload = readProfileForm();
  if (!payload.child_name) {
    const hint = $("profileSaveHint");
    if (hint) {
      hint.textContent = "请填写儿童姓名或昵称";
      hint.classList.remove("hidden");
      hint.classList.add("text-destructive");
    }
    $("profileChildName")?.focus();
    return false;
  }
  const btn = $("profileSaveBtn");
  if (btn) btn.disabled = true;
  try {
    const data = await fetchJson("/api/profile", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    if (data.user) currentUser = data.user;
    familyProfile = data.profile || payload;
    localStorage.setItem(PROFILE_CACHE_KEY, JSON.stringify(familyProfile));
    paintSidebarProfile();
    fillProfileForm(familyProfile);
    const hint = $("profileSaveHint");
    if (hint) {
      hint.textContent = "已保存";
      hint.classList.remove("hidden", "text-destructive");
      hint.classList.add("text-primary");
      setTimeout(() => hint.classList.add("hidden"), 2500);
    }
    return true;
  } catch (e) {
    const hint = $("profileSaveHint");
    if (hint) {
      hint.textContent = e.message || "保存失败";
      hint.classList.remove("hidden");
      hint.classList.add("text-destructive");
    }
    return false;
  } finally {
    if (btn) btn.disabled = false;
  }
}

async function saveAccountProfile() {
  if (!currentUser || currentUser.id <= 0) return false;
  const selected = document.querySelector(".profile-avatar-option.selected");
  const payload = {
    display_name: ($("profileDisplayName")?.value || "").trim(),
    phone: ($("profilePhone")?.value || "").trim(),
    avatar_id: selected?.dataset.avatarId || currentUser.avatar_id || "default",
  };
  const btn = $("profileAccountSaveBtn");
  if (btn) btn.disabled = true;
  const hint = $("profileAccountHint");
  try {
    const data = await fetchJson("/api/auth/account", {
      method: "PATCH",
      body: JSON.stringify(payload),
    });
    currentUser = data.user || currentUser;
    paintSidebarProfile();
    fillAccountForm(currentUser);
    if (hint) {
      hint.textContent = "账户信息已保存";
      hint.classList.remove("hidden", "text-destructive");
      hint.classList.add("text-primary");
      setTimeout(() => hint.classList.add("hidden"), 2500);
    }
    return true;
  } catch (e) {
    if (hint) {
      hint.textContent = e.message || "保存失败";
      hint.classList.remove("hidden");
      hint.classList.add("text-destructive");
    }
    return false;
  } finally {
    if (btn) btn.disabled = false;
  }
}

function applyHistoryNavExpanded(expanded) {
  historyNavExpanded = expanded;
  $("historyNavGroup")?.classList.toggle("history-expanded", expanded);
  $("historyNavToggle")?.setAttribute("aria-expanded", String(expanded));
  $("historyNavItems")?.classList.toggle("sidebar-nav-children-collapsed", !expanded);
  $("historyNavChevron")?.classList.toggle("sidebar-nav-chevron-open", expanded);
}

function toggleHistoryNavExpanded() {
  applyHistoryNavExpanded(!historyNavExpanded);
}

/** 侧栏收起时点击「我的记录」：展开侧栏并打开记录列表 */
async function openHistoryFromCollapsedSidebar() {
  applySidebarCollapsed(false);
  switchTab("history");
}

function switchTab(name, { evalId = null } = {}) {
  const prev = activeTabName;
  if (evalId != null) selectedHistoryEvalId = evalId;
  else if (name !== "history") selectedHistoryEvalId = null;

  setSidebarActive(name, evalId);

  document.querySelectorAll(".tab-panel").forEach((p) => {
    p.classList.toggle("active", p.id === `panel-${name}`);
  });

  const [title, sub] = TAB_TITLES[name] || ["Narro", ""];
  if ($("mainTitle")) $("mainTitle").textContent = title;
  if ($("mainSub")) {
    if (name === "history" && evalId != null) {
      const label = historyRecordLabelFromDom(evalId);
      $("mainSub").textContent = label !== "该记录" ? label : sub;
    } else {
      $("mainSub").textContent = sub;
    }
  }

  if (name === "session" && currentPersona === "user") {
    resetSessionAssessmentView();
  }

  if (name !== "history") closeNarroChatDrawer();
  updateHistoryAskNarroBtn();

  if (name === "history") {
    if (currentPersona === "user") loadHistory({ evalId });
    else loadHistory();
  }
  if (name === "insights") loadInsights();
  if (name === "pn-agent") window.NarroPnAgent?.onTabShown?.();
  if (prev === "pn-agent" && name !== "pn-agent") window.NarroPnAgent?.onTabHidden?.();
  document.body.classList.toggle("pn-agent-view-active", name === "pn-agent");
  $("storyCards")?.classList.toggle("hidden", name !== "session");
  if (name === "profile") {
    switchProfileSubTab("account");
    fillProfileForm(familyProfile);
  }

  activeTabName = name;
}

window.NarroPnAgent = {
  ...(window.NarroPnAgent || {}),
  afterSessionSaved: async (evaluationId) => {
    await refreshUserHistoryNav({ highlightEvalId: evaluationId || null });
    window.NarroUI?.showNarroBanner?.("通话记录已保存", { variant: "success", timeoutMs: 2800 });
    if (evaluationId && $("panel-history")?.classList.contains("active")) {
      try {
        await openEvaluation(evaluationId, { silent: true });
      } catch {
        /* 侧边栏已刷新即可 */
      }
    }
  },
};

let openHistoryKebabId = null;

function closeHistoryKebabMenus() {
  document.querySelectorAll(".sidebar-nav-menu").forEach((m) => m.classList.add("hidden"));
  openHistoryKebabId = null;
}

$("navUser")?.addEventListener("click", (e) => {
  const menuBtn = e.target.closest("[data-history-menu-action]");
  if (menuBtn) {
    e.stopPropagation();
    const row = menuBtn.closest(".narro-nav-record");
    const evalId = row?.dataset.evalId;
    const action = menuBtn.dataset.historyMenuAction;
    closeHistoryKebabMenus();
    if (evalId && action === "rename") {
      queueMicrotask(() => void renameHistoryRecord(evalId));
    }
    if (evalId && action === "delete") {
      queueMicrotask(() => void deleteHistoryRecord(evalId));
    }
    return;
  }

  const kebabBtn = e.target.closest(".sidebar-nav-kebab");
  if (kebabBtn) {
    e.stopPropagation();
    const row = kebabBtn.closest(".narro-nav-record");
    const evalId = row?.dataset.evalId;
    const menu = row?.querySelector(".sidebar-nav-menu");
    if (!menu || !evalId) return;
    const willOpen = openHistoryKebabId !== String(evalId);
    closeHistoryKebabMenus();
    if (willOpen) {
      menu.classList.remove("hidden");
      openHistoryKebabId = String(evalId);
    }
    return;
  }

  if (!e.target.closest(".narro-nav-record")) {
    closeHistoryKebabMenus();
  }

  const recordBtn = e.target.closest("#historyNavItems .sidebar-nav-item-record[data-eval-id]");
  if (recordBtn?.dataset.evalId) {
    applyHistoryNavExpanded(true);
    switchTab("history", { evalId: recordBtn.dataset.evalId });
    if (window.matchMedia("(max-width: 767px)").matches) closeMobileSidebar();
    return;
  }
  const tabBtn = e.target.closest(
    "#navUser .sidebar-nav-item[data-tab], #navManager .sidebar-nav-item[data-tab]"
  );
  if (tabBtn && !tabBtn.closest("#historyNavItems")) {
    switchTab(tabBtn.dataset.tab);
    if (window.matchMedia("(max-width: 767px)").matches) closeMobileSidebar();
  }
});

$("sidebarProfileBtn")?.addEventListener("click", () => {
  switchTab("profile");
  if (window.matchMedia("(max-width: 767px)").matches) closeMobileSidebar();
});

function switchProfileSubTab(name) {
  document.querySelectorAll(".profile-tab-btn[data-profile-tab]").forEach((btn) => {
    const on = btn.dataset.profileTab === name;
    btn.classList.toggle("active", on);
    btn.setAttribute("aria-selected", on ? "true" : "false");
  });
  document.querySelectorAll(".profile-tab-panel[data-profile-panel]").forEach((panel) => {
    const on = panel.dataset.profilePanel === name;
    panel.classList.toggle("hidden", !on);
    if (on) panel.removeAttribute("hidden");
    else panel.setAttribute("hidden", "");
  });
}

$("profileTabs")?.addEventListener("click", (e) => {
  const btn = e.target.closest(".profile-tab-btn[data-profile-tab]");
  if (btn?.dataset.profileTab) switchProfileSubTab(btn.dataset.profileTab);
});

$("profileForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  await saveFamilyProfile();
});

$("profileAccountSaveBtn")?.addEventListener("click", () => saveAccountProfile());

$("profileAvatarGrid")?.addEventListener("click", (e) => {
  const btn = e.target.closest(".profile-avatar-option");
  if (!btn) return;
  document.querySelectorAll(".profile-avatar-option").forEach((el) => el.classList.remove("selected"));
  btn.classList.add("selected");
  syncProfileAvatarUi(btn.dataset.avatarId);
});

$("profilePasswordForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const hint = $("profilePasswordHint");
  const cur = $("profileCurrentPassword")?.value || "";
  const neu = $("profileNewPassword")?.value || "";
  if (!cur || neu.length < 8) {
    if (hint) {
      hint.textContent = "请填写当前密码，新密码至少 8 位";
      hint.classList.remove("hidden");
      hint.classList.add("text-destructive");
    }
    return;
  }
  try {
    await fetchJson("/api/auth/change-password", {
      method: "POST",
      body: JSON.stringify({ current_password: cur, new_password: neu }),
    });
    $("profileCurrentPassword").value = "";
    $("profileNewPassword").value = "";
    if (hint) {
      hint.textContent = "密码已更新";
      hint.classList.remove("hidden", "text-destructive");
      hint.classList.add("text-primary");
      setTimeout(() => hint.classList.add("hidden"), 2500);
    }
  } catch (err) {
    if (hint) {
      hint.textContent = err.message || "修改失败";
      hint.classList.remove("hidden");
      hint.classList.add("text-destructive");
    }
  }
});

$("profileLogoutBtn")?.addEventListener("click", () => logoutUser());

document.querySelectorAll("[data-parent-survey-dismiss]").forEach((el) => {
  el.addEventListener("click", closeParentSurveyModal);
});
$("parentSurveySubmit")?.addEventListener("click", () => submitParentSurvey());

document.querySelectorAll(".auth-tab").forEach((btn) => {
  btn.addEventListener("click", () => switchAuthTab(btn.dataset.authTab || "login"));
});

$("authLoginForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  setAuthGateError("");
  const email = ($("authLoginEmail")?.value || "").trim();
  const password = $("authLoginPassword")?.value || "";
  const btn = $("authLoginBtn");
  if (btn) btn.disabled = true;
  try {
    const data = await fetchJson("/api/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    await onAuthSuccess(data);
  } catch (err) {
    setAuthGateError(err.message || "登录失败");
  } finally {
    if (btn) btn.disabled = false;
  }
});

$("authRegisterForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  setAuthGateError("");
  const password = $("authRegisterPassword")?.value || "";
  const password2 = $("authRegisterPassword2")?.value || "";
  if (password !== password2) {
    setAuthGateError("两次输入的密码不一致");
    return;
  }
  const btn = $("authRegisterBtn");
  if (btn) btn.disabled = true;
  try {
    const data = await fetchJson("/api/auth/register", {
      method: "POST",
      body: JSON.stringify({
        email: ($("authRegisterEmail")?.value || "").trim(),
        password,
        display_name: ($("authRegisterName")?.value || "").trim(),
      }),
    });
    await onAuthSuccess(data);
  } catch (err) {
    setAuthGateError(err.message || "注册失败");
  } finally {
    if (btn) btn.disabled = false;
  }
});

document.addEventListener("click", () => closeHistoryKebabMenus());

$("historyNavToggle")?.addEventListener("click", async (e) => {
  e.stopPropagation();
  if (isSidebarCollapsed()) {
    await openHistoryFromCollapsedSidebar();
    return;
  }
  switchTab("history");
});

$("sidebarCollapseBtn")?.addEventListener("click", () => applySidebarCollapsed(true));
$("sidebarExpandBtn")?.addEventListener("click", () => applySidebarCollapsed(false));

function closeMobileSidebar() {
  $("appSidebar")?.classList.remove("narro-sidebar-mobile-open");
  $("mobileSidebarBtn")?.setAttribute("aria-expanded", "false");
  $("sidebarBackdrop")?.classList.add("hidden");
}

$("mobileSidebarBtn")?.addEventListener("click", () => {
  const sb = $("appSidebar");
  const open = !sb?.classList.contains("narro-sidebar-mobile-open");
  sb?.classList.toggle("narro-sidebar-mobile-open", open);
  $("mobileSidebarBtn")?.setAttribute("aria-expanded", String(open));
  $("sidebarBackdrop")?.classList.toggle("hidden", !open);
});

document.getElementById("sidebarBackdrop")?.addEventListener("click", closeMobileSidebar);

document.querySelectorAll("#navManager .sidebar-nav-item[data-tab]").forEach((btn) => {
  btn.addEventListener("click", () => switchTab(btn.dataset.tab));
});

async function loadMeta() {
  const meta = await fetchJson("/api/meta");
}

function drawInsightsLineChart(canvas, points, series, { title, maxY } = {}) {
  if (!canvas || !points.length) return;
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  const w = Math.max(rect.width || 320, 280);
  const h = Number(canvas.getAttribute("height")) || 160;
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  const ctx = canvas.getContext("2d");
  ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, w, h);
  const pad = { l: 36, r: 12, t: 22, b: 28 };
  const plotW = w - pad.l - pad.r;
  const plotH = h - pad.t - pad.b;
  let yMax = maxY;
  if (yMax == null) {
    const vals = [];
    series.forEach((s) => points.forEach((p) => { if (p[s.key] != null) vals.push(p[s.key]); }));
    yMax = Math.max(...vals, 1);
  }
  const n = points.length;
  const xAt = (i) => pad.l + (n === 1 ? plotW / 2 : (i / (n - 1)) * plotW);
  const yAt = (v) => pad.t + plotH - (v / yMax) * plotH;

  ctx.strokeStyle = "hsl(240 5.9% 90%)";
  ctx.lineWidth = 1;
  for (let g = 0; g <= 4; g++) {
    const y = pad.t + (g / 4) * plotH;
    ctx.beginPath();
    ctx.moveTo(pad.l, y);
    ctx.lineTo(w - pad.r, y);
    ctx.stroke();
  }

  series.forEach((s) => {
    const pts = points
      .map((p, i) => (p[s.key] != null ? { x: xAt(i), y: yAt(p[s.key]) } : null))
      .filter(Boolean);
    if (pts.length >= 2) {
      ctx.strokeStyle = s.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(pts[0].x, pts[0].y);
      for (let i = 1; i < pts.length; i++) ctx.lineTo(pts[i].x, pts[i].y);
      ctx.stroke();
    }
    points.forEach((p, i) => {
      if (p[s.key] == null) return;
      ctx.fillStyle = s.color;
      ctx.beginPath();
      ctx.arc(xAt(i), yAt(p[s.key]), 4, 0, Math.PI * 2);
      ctx.fill();
    });
  });

  ctx.fillStyle = "#64748b";
  ctx.font = "11px sans-serif";
  ctx.fillText(title || "", pad.l, 14);
}

function drawInsightsChart(points) {
  drawInsightsLineChart($("insightsChart"), points, [
    { key: "pred_SC_Sum", color: "#16a34a" },
    { key: "micro_sum", color: "#3b82f6" },
  ], { title: "宏观 SC（绿）· SS/15（蓝）", maxY: 15 });
  const langPts = points.filter((p) => p.TNW != null || p.MLU != null);
  if (langPts.length) {
    const maxT = Math.max(...langPts.map((p) => p.TNW || 0), 1);
    drawInsightsLineChart(
      $("insightsChartLang"),
      langPts,
      [{ key: "TNW", color: "#8b5cf6" }],
      { title: `总词数 TNW（最高约 ${Math.round(maxT)}）`, maxY: maxT * 1.1 }
    );
  }
}

async function loadInsights() {
  const empty = $("insightsEmpty");
  const content = $("insightsContent");
  try {
    const data = await fetchJson("/api/insights");
    if (!data.evaluation_count) {
      empty?.classList.remove("hidden");
      content?.classList.add("hidden");
      return;
    }
    empty?.classList.add("hidden");
    content?.classList.remove("hidden");

    const growth = data.growth || {};
    const trendLabel = growth.trend_label || "—";
    const delta =
      data.sc_delta != null ? `${data.sc_delta > 0 ? "+" : ""}${data.sc_delta}` : "—";

    const microDelta =
      data.micro_delta != null
        ? `${data.micro_delta > 0 ? "+" : ""}${data.micro_delta}`
        : "—";
    const interval =
      data.avg_interval_days != null ? `平均间隔 ${data.avg_interval_days} 天` : "—";
    const parentMean =
      data.parent_composite_mean != null ? `${data.parent_composite_mean}/5` : "—";

    $("insightsSummary").innerHTML = `
      <div class="rounded-xl border bg-card p-3">
        <p class="text-xs text-muted-foreground">累计评估</p>
        <p class="text-xl font-bold mt-0.5 tabular-nums">${data.evaluation_count}</p>
        <p class="text-[11px] text-muted-foreground mt-0.5">次 · ${interval}</p>
      </div>
      <div class="rounded-xl border bg-card p-3">
        <p class="text-xs text-muted-foreground">宏观 SC / SS</p>
        <p class="text-xl font-bold mt-0.5 tabular-nums">${data.sc_last != null ? Number(data.sc_last).toFixed(1) : "—"} / ${data.micro_last ?? "—"}</p>
        <p class="text-[11px] text-muted-foreground mt-0.5">SC ${delta} · SS ${microDelta} · ${trendLabel}</p>
      </div>
      <div class="rounded-xl border bg-card p-3">
        <p class="text-xs text-muted-foreground">家长观察均分</p>
        <p class="text-xl font-bold mt-0.5 tabular-nums">${parentMean}</p>
        <p class="text-[11px] text-muted-foreground mt-0.5">已填 ${data.parent_survey_count ?? 0} 次</p>
      </div>
      <div class="rounded-xl border bg-card p-3">
        <p class="text-xs text-muted-foreground">AI 引导 / 告警</p>
        <p class="text-xl font-bold mt-0.5 tabular-nums">${data.guided_session_count ?? 0} / ${data.alerts_count}</p>
        <p class="text-[11px] text-muted-foreground mt-0.5">引导次数 · 需关注条数</p>
      </div>`;

    const pts = growth.points || [];
    $("insightsTrendText").textContent = pts.length
      ? `共 ${pts.length} 次评估 · 趋势 ${trendLabel} · 左：SC/SS，右：总词数 TNW`
      : "完成至少 2 次评估后可看进步曲线";
    drawInsightsChart(pts);

    const byStory = data.by_story || [];
    const storyCard = $("insightsStoryCard");
    const storyEl = $("insightsByStory");
    if (byStory.length && storyCard && storyEl) {
      storyCard.classList.remove("hidden");
      storyEl.innerHTML = `<table class="insights-story-table"><thead><tr><th>故事</th><th>次数</th><th>SS 均</th><th>SC 均</th></tr></thead><tbody>${byStory
        .map(
          (s) =>
            `<tr><td>${escapeHtml(s.label)}</td><td>${s.count}</td><td>${s.ss_mean ?? "—"}</td><td>${s.sc_mean ?? "—"}</td></tr>`
        )
        .join("")}</tbody></table>`;
    } else {
      storyCard?.classList.add("hidden");
    }

    const alerts = data.alerts || [];
    $("insightsAlerts").innerHTML = alerts.length
      ? alerts
          .map(
            (a) => `<div class="flex flex-wrap items-center gap-2 rounded-lg border px-3 py-2">
              <span class="badge ${a.severity === "high" ? "badge-destructive" : "badge-outline"}">${escapeHtml(a.label || a.alert_id)}</span>
              <button type="button" class="text-primary underline text-xs insights-goto-eval" data-eval-id="${a.evaluation_id}">查看 #${a.evaluation_id}</button>
            </div>`
          )
          .join("")
      : '<p class="text-sm text-muted-foreground">暂无告警，请继续保持练习与观察。</p>';

    document.querySelectorAll(".insights-goto-eval").forEach((btn) => {
      btn.addEventListener("click", () => {
        applyHistoryNavExpanded(true);
        switchTab("history", { evalId: btn.dataset.evalId });
      });
    });

    const weakEntries = Object.entries(data.weak_ss_tasks || data.weak_micro_tasks || {});
    $("insightsWeakTasks").innerHTML = weakEntries.length
      ? `<ul class="text-sm space-y-1">${weakEntries
          .map(([k, v]) => `<li><span class="font-mono">${escapeHtml(k)}</span> · 未达标 ${v} 次</li>`)
          .join("")}</ul>`
      : '<p class="text-sm text-muted-foreground">历次评估中 SS 要素表现稳定。</p>';
  } catch (e) {
    empty?.classList.remove("hidden");
    content?.classList.add("hidden");
    if (empty) empty.textContent = e.message || "加载失败";
  }
}

function updateCharCount() {
  const n = getNarrativeText().length;
  if ($("charCount")) $("charCount").textContent = n;
}

function showLoading(show, msg) {
  $("loadingOverlay")?.classList.toggle("hidden", !show);
  if (msg) $("loadingMsg").textContent = msg;
  if ($("submitBtn")) $("submitBtn").disabled = show;
  if ($("submitBtnUser")) $("submitBtnUser").disabled = show;
  if ($("storySubmitEvalBtn")) $("storySubmitEvalBtn").disabled = show;
}

function appendThreadBubble(role, html) {
  const thread = $("chatThread");
  if (!thread) return;
  const el = document.createElement("div");
  el.className = role === "user" ? "coach-bubble-user max-w-[90%]" : "coach-bubble-bot max-w-[90%]";
  el.innerHTML = role === "user" && typeof html === "string" && !html.startsWith("<") ? escapeHtml(html) : html;
  thread.appendChild(el);
  thread.scrollTop = thread.scrollHeight;
}

function setExportEnabled(on) {
  [
    "exportTxtBtnManager",
    "exportCsvBtnManager",
    "historyExportTxtBtn",
    "historyExportCsvBtn",
  ].forEach((id) => {
    if ($(id)) $(id).disabled = !on;
  });
}

function escapeHtml(s) {
  return window.NarroUI?.escapeHtml(s) ?? String(s ?? "");
}

async function refreshLlmStatus() {
  try {
    const llm = await fetchJson("/api/llm/status");
    llmAvailable = !!llm.available;
  } catch {
    llmAvailable = false;
  }
}

function resetEvaluateView() {
  currentEvaluationId = null;
  $("resultsContentManager")?.classList.add("hidden");
  setExportEnabled(false);
  refreshLlmStatus();
  const thread = $("chatThread");
  if (thread) thread.innerHTML = `<div class="coach-bubble-bot max-w-[90%]"><p class="font-medium">单条叙事评估</p><p class="mt-1 text-muted-foreground text-sm">粘贴已采集的叙事文本，或先完成上方批量导入。</p></div>`;
}

function resetForNewStory() {
  localStorage.removeItem(LAST_EVAL_KEY);
  stopSpeechRecognition();
  clearStoryDock();
  resetSessionAssessmentView();
  currentEvaluationId = null;
  setExportEnabled(false);
  if (currentPersona === "manager") resetEvaluateView();
  switchTab("session");
  $("storySection")?.scrollIntoView({ behavior: "smooth", block: "start" });
}

let speechRec = null;
let speechRecHandlers = null;
let speechHealthTimer = null;
let lastSpeechHeardAt = 0;
let speechGateNaro = false;
let speechPrefix = "";
let speechFinalized = "";
let speechInterim = "";
let speechLastInterim = "";
let transcriptUserEdited = false;
/** @type {"immersive-free"|"immersive-guided"|null} */
let speechMode = null;
let speechKeepAlive = false;
let speechSessionBuffer = "";
let immersiveSessionActive = false;
let xiaoleCompanionEnabled = false;
let storyMicStream = null;
let storyAudioRecorder = null;
let storyAudioChunks = [];
let storySessionAudioBlob = null;
let historyNarrativeAudioUrl = null;
let selectedStory = "cat";
let storyPanelIndex = 0;
let storyStimuliData = null;

async function loadStoryStimuli() {
  const sources = ["/api/story-stimuli", "/static/story_stimuli.json"];
  let lastErr = null;
  for (const path of sources) {
    try {
      const res = await fetch(`${API}${path}`, { headers: apiHeaders() });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) {
        const detail = typeof data.detail === "string" ? data.detail : `HTTP ${res.status}`;
        throw new Error(detail);
      }
      storyStimuliData = data;
      lastErr = null;
      break;
    } catch (e) {
      lastErr = e;
    }
  }
  if (!storyStimuliData?.stories) {
    window.NarroUI?.showNarroBanner?.(
      `图卡配置加载失败：${lastErr?.message || "未知错误"}`,
      { variant: "info", timeoutMs: 8000 }
    );
    return;
  }
  const stories = storyStimuliData.stories;
  document.querySelectorAll(".story-toggle-btn").forEach((btn) => {
    const st = stories[btn.dataset.story];
    if (st?.task_label) btn.title = st.task_label;
  });
  renderStoryPanel();
}

function currentStoryDef() {
  return storyStimuliData?.stories?.[selectedStory] || null;
}

function renderStoryPanel() {
  const def = currentStoryDef();
  const panels = def?.panels || [];
  if (!panels.length) return;
  if (storyPanelIndex >= panels.length) storyPanelIndex = 0;
  if (storyPanelIndex < 0) storyPanelIndex = panels.length - 1;
  const p = panels[storyPanelIndex];
  if ($("storyPanelImg")) {
    $("storyPanelImg").onerror = () => {
      $("storyPanelImg").alt = "图卡加载失败";
    };
    $("storyPanelImg").src = p.image;
    const cap = (p.caption || "").trim();
    $("storyPanelImg").alt = cap || `故事图卡 ${storyPanelIndex + 1}`;
  }
  if ($("storyPanelIndicator")) $("storyPanelIndicator").textContent = `${storyPanelIndex + 1} / ${panels.length}`;
  if ($("storyPrompt")) {
    $("storyPrompt").textContent = def.task_label || def.title || "";
  }
  if ($("storyPrevBtn")) $("storyPrevBtn").disabled = storyPanelIndex <= 0;
  if ($("storyNextBtn")) $("storyNextBtn").disabled = storyPanelIndex >= panels.length - 1;
  if (window.NarroStoryCoach?.shouldHandlePanelRender?.() !== false) {
    window.NarroStoryCoach?.onPanelRendered?.();
  }
}

window.__narroCurrentStoryDef = () => currentStoryDef();
window.__narroStoryPanelIndex = () => storyPanelIndex;
window.__narroSelectedStory = () => selectedStory;

window.__narroGetFamilyProfile = () => familyProfile || defaultFamilyProfile();

window.__narroGoToStorySession = (storyKey) => {
  if (storyKey && storyStimuliData?.stories?.[storyKey]) selectStory(storyKey);
  switchTab("session");
};

window.__narroSwitchTab = (name, opts) => switchTab(name, opts || {});

function selectStory(storyKey) {
  stopSpeechRecognition();
  selectedStory = storyKey;
  storyPanelIndex = 0;
  document.querySelectorAll(".story-toggle-btn").forEach((b) => {
    const on = b.dataset.story === storyKey;
    b.classList.toggle("active", on);
    b.setAttribute("aria-selected", on ? "true" : "false");
  });
  renderStoryPanel();
}

function commitSpeechInterim() {
  const t = speechInterim.trim();
  if (!t) return;
  const fin = speechFinalized.trim();
  if (!fin) {
    speechFinalized = t;
  } else if (!fin.endsWith(t) && !t.startsWith(fin)) {
    speechFinalized = fin + t;
  }
  speechInterim = "";
  speechLastInterim = "";
}

function commitTranscriptFromEditor() {
  const ta = $("storyTranscript");
  if (!ta) return;
  speechPrefix = (ta.value || "").trim();
  speechFinalized = "";
  speechInterim = "";
  speechLastInterim = "";
  transcriptUserEdited = false;
}

function appendChildNarration(text) {
  const t = String(text || "").trim();
  if (t) {
    commitSpeechInterim();
    const fin = speechFinalized.trim();
    if (!fin) speechFinalized = t;
    else if (!fin.includes(t)) speechFinalized = fin + t;
  }
  syncStoryTranscriptDisplay();
}

window.__narroAppendChildNarration = appendChildNarration;
window.__narroCommitPendingInterim = commitSpeechInterim;

function markSpeechHeard() {
  lastSpeechHeardAt = Date.now();
}

window.__narroSetSpeechGate = (on) => {
  speechGateNaro = !!on;
};

function shouldIgnoreSttResult() {
  return speechGateNaro || window.NarroStoryCoach?.isNaroSpeaking?.();
}

window.__narroGetRecentTranscriptTail = (maxLen = 400) => {
  const ta = $("storyTranscript");
  if (!ta) return "";
  const v = (ta.value || "").trim();
  if (!v) return "";
  return v.length > maxLen ? v.slice(-maxLen) : v;
};

async function warmupMicrophone() {
  await startStoryAudioCapture();
}

function releaseStoryMicStream() {
  storyMicStream?.getTracks?.().forEach((t) => t.stop());
  storyMicStream = null;
  storyAudioRecorder = null;
}

async function startStoryAudioCapture() {
  if (!navigator.mediaDevices?.getUserMedia) return false;
  if (storyMicStream) return true;
  try {
    storyMicStream = await navigator.mediaDevices.getUserMedia({
      audio: { echoCancellation: true, noiseSuppression: true },
    });
    storyAudioChunks = [];
    const mime = MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
      ? "audio/webm;codecs=opus"
      : MediaRecorder.isTypeSupported("audio/webm")
        ? "audio/webm"
        : "";
    storyAudioRecorder = new MediaRecorder(
      storyMicStream,
      mime ? { mimeType: mime } : undefined
    );
    storyAudioRecorder.ondataavailable = (ev) => {
      if (ev.data?.size) storyAudioChunks.push(ev.data);
    };
    storyAudioRecorder.start(1000);
    return true;
  } catch {
    releaseStoryMicStream();
    return false;
  }
}

async function stopStoryAudioCapture() {
  if (!storyAudioRecorder || storyAudioRecorder.state === "inactive") {
    releaseStoryMicStream();
    return storySessionAudioBlob;
  }
  return new Promise((resolve) => {
    storyAudioRecorder.onstop = () => {
      if (storyAudioChunks.length) {
        storySessionAudioBlob = new Blob(storyAudioChunks, {
          type: storyAudioRecorder?.mimeType || "audio/webm",
        });
      }
      storyAudioChunks = [];
      releaseStoryMicStream();
      resolve(storySessionAudioBlob);
    };
    try {
      storyAudioRecorder.stop();
    } catch {
      releaseStoryMicStream();
      resolve(storySessionAudioBlob);
    }
  });
}

async function uploadNarrativeAudio(evaluationId, blob) {
  const fd = new FormData();
  const ext = (blob.type || "").includes("wav") ? "wav" : "webm";
  fd.append("audio", blob, `narrative_${evaluationId}.${ext}`);
  const res = await fetch(`${API}/api/evaluate/${evaluationId}/narrative-audio`, {
    method: "POST",
    body: fd,
    headers: apiAuthHeaders(),
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.detail || "录音保存失败");
  return data;
}

async function paintHistoryNarrativeAudio(row, data) {
  const audioEl = $("historyNarrativeAudio");
  if (!audioEl) return;
  if (historyNarrativeAudioUrl) {
    URL.revokeObjectURL(historyNarrativeAudioUrl);
    historyNarrativeAudioUrl = null;
  }
  const eid = row?.id || row?.evaluation_id || data?.evaluation_id;
  if (!row?.has_narrative_audio || !eid) {
    audioEl.pause?.();
    audioEl.removeAttribute("src");
    audioEl.classList.add("hidden");
    return;
  }
  try {
    const res = await fetch(`${API}/api/history/${eid}/narrative-audio`, {
      headers: apiAuthHeaders(),
    });
    if (!res.ok) throw new Error("no audio");
    const blob = await res.blob();
    historyNarrativeAudioUrl = URL.createObjectURL(blob);
    audioEl.src = historyNarrativeAudioUrl;
    audioEl.classList.remove("hidden");
  } catch {
    audioEl.pause?.();
    audioEl.removeAttribute("src");
    audioEl.classList.add("hidden");
  }
}

function stopSpeechHealthMonitor() {
  if (speechHealthTimer) {
    clearInterval(speechHealthTimer);
    speechHealthTimer = null;
  }
}

function speechHealthTick() {
  if (!immersiveSessionActive || !speechKeepAlive) return;
  const silentMs = Date.now() - (lastSpeechHeardAt || 0);
  if (silentMs > 10000 && speechRec) {
    try {
      speechRec.stop();
    } catch {
      speechRec = null;
      void bootSpeechRecognition();
    }
  }
}

function startSpeechHealthMonitor() {
  stopSpeechHealthMonitor();
  lastSpeechHeardAt = Date.now();
  speechHealthTimer = setInterval(speechHealthTick, 2000);
}

function attachSpeechRecognitionHandlers(rec) {
  if (!rec || !speechRecHandlers) return;
  rec.lang = "zh-CN";
  rec.continuous = true;
  rec.interimResults = true;
  rec.maxAlternatives = 1;
  rec.onresult = speechRecHandlers.onResult;
  rec.onerror = speechRecHandlers.onError;
  rec.onend = speechRecHandlers.onEnd;
  rec.onaudiostart = speechRecHandlers.onAudioStart;
  rec.onspeechstart = speechRecHandlers.onSpeechStart;
}

async function bootSpeechRecognition() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR || !speechRecHandlers || !speechKeepAlive || !immersiveSessionActive) return;
  if (speechRec) return;
  try {
    speechRec = new SR();
    attachSpeechRecognitionHandlers(speechRec);
    speechRec.start();
    setSpeechStatus("");
  } catch (e) {
    setSpeechStatus(e.message || "无法启动语音识别", true);
  }
}

window.__narroAdvanceStoryPanel = () => {
  const n = currentStoryDef()?.panels?.length || 0;
  if (n && storyPanelIndex < n - 1) {
    storyPanelIndex += 1;
    renderStoryPanel();
  }
};

function setXiaoleCompanionVisual(mode) {
  const mascot = $("naroMascot");
  if (!mascot) return;
  const sleep = mode !== "active";
  mascot.dataset.companion = sleep ? "sleep" : "active";
  mascot.querySelector(".xiaole-mode-sleep")?.classList.toggle("hidden", !sleep);
  mascot.querySelector(".xiaole-mode-listen")?.classList.toggle("hidden", sleep);
  mascot.setAttribute(
    "aria-label",
    sleep ? "叫醒小乐，开始 AI 陪伴" : "小乐正在陪伴倾听，点击让小乐休息"
  );
  const label = $("naroMascotLabel");
  if (label) {
    label.textContent = sleep ? "小乐睡着了，点击叫醒" : "小乐正在倾听，点击让小乐休息";
  }
}

function activateXiaoleCompanion() {
  xiaoleCompanionEnabled = true;
  setXiaoleCompanionVisual("active");
  window.NarroStoryCoach?.setNaroEnabled?.(true);
  syncStoryComposerHint();
}

function deactivateXiaoleCompanion() {
  xiaoleCompanionEnabled = false;
  window.NarroStoryCoach?.endGuidedSession?.();
  window.NarroStoryCoach?.setNaroEnabled?.(false);
  setXiaoleCompanionVisual("sleep");
  syncStoryComposerHint();
}

function onXiaoleMascotClick() {
  if (immersiveSessionActive) return;
  if (xiaoleCompanionEnabled) deactivateXiaoleCompanion();
  else activateXiaoleCompanion();
}

window.__narroSetXiaoleCompanionVisual = setXiaoleCompanionVisual;
window.__narroIsXiaoleCompanionEnabled = () => xiaoleCompanionEnabled;

function syncStoryComposerHint() {
  const hint = $("storyComposerHint");
  if (hint && !immersiveSessionActive) {
    hint.textContent = xiaoleCompanionEnabled
      ? "点击麦克风，小乐会陪你讲故事"
      : "点击小乐或麦克风开始讲述";
  }
}

function syncStoryTranscriptDisplay(interim = null) {
  const ta = $("storyTranscript");
  if (!ta) return;
  if (transcriptUserEdited && document.activeElement === ta) return;

  if (interim !== null) {
    const next = String(interim).trim();
    const prev = speechLastInterim.trim();
    if (prev && next && prev.length >= 2) {
      const p = prev.replace(/\s+/g, "");
      const n = next.replace(/\s+/g, "");
      if (!n.startsWith(p) && !p.startsWith(n)) commitSpeechInterim();
    }
    speechInterim = next;
    speechLastInterim = next;
  }

  const base = speechPrefix.trim();
  const session = (speechFinalized + speechInterim).trim();
  ta.value = [base, session].filter(Boolean).join(base && session ? "\n" : "");
  autoResizeStoryInput();
}

function handleSpeechInterim(interim) {
  if (!interim?.trim()) return;
  if (shouldIgnoreSttResult()) return;
  markSpeechHeard();
  syncStoryTranscriptDisplay(interim.trim());
  if (speechMode === "immersive-guided") {
    window.NarroStoryCoach?.onChildSpeechActivity?.({ interim: interim.trim() });
  }
}

function updateMicUiIdle() {
  if (immersiveSessionActive) return;
  $("storyMicBtn")?.classList.remove("hidden");
  $("storyMicStopBtn")?.classList.add("hidden");
}

function setSpeechUiRecording(recording) {
  $("storyMicBtn")?.classList.toggle("hidden", recording);
  $("storyMicStopBtn")?.classList.toggle("hidden", !recording);
  $("storyComposer")?.classList.toggle("is-recording", recording);
  $("storyComposerIdle")?.classList.toggle("hidden", recording);
  $("storyComposerRecording")?.classList.toggle("hidden", !recording);
  $("storyDock")?.classList.toggle("is-immersive", recording || immersiveSessionActive);
}

function setSpeechStatus(msg, isError = false) {
  const el = $("speechStatus");
  if (!el) return;
  el.textContent = msg || "";
  el.classList.toggle("story-speech-status-error", isError);
}

function handleSpeechFinalSegment(piece) {
  if (!piece?.trim()) return;
  const seg = piece.trim();
  if (shouldIgnoreSttResult()) return;
  markSpeechHeard();
  commitSpeechInterim();
  const ta = $("storyTranscript");
  if (transcriptUserEdited && ta) {
    const cur = (ta.value || "").trim();
    ta.value = cur ? `${cur}${seg}` : seg;
    commitTranscriptFromEditor();
  } else {
    const fin = speechFinalized.trim();
    if (!fin) speechFinalized = seg;
    else if (!fin.endsWith(seg)) speechFinalized = fin + seg;
    speechInterim = "";
    speechLastInterim = "";
  }
  syncStoryTranscriptDisplay();
  if (speechMode === "immersive-guided") {
    window.NarroStoryCoach?.onChildSpeechActivity?.({ final: seg });
  }
}

function showCallOverlay() {
  immersiveSessionActive = true;
  syncStoryComposerHint();
  setSpeechUiRecording(true);
  const status = $("storyCallStatus");
  if (status) {
    status.textContent = xiaoleCompanionEnabled ? "小乐在听…" : "正在听…";
  }
  syncStoryTranscriptDisplay();
}

function hideCallOverlay() {
  immersiveSessionActive = false;
  setSpeechUiRecording(false);
  updateMicUiIdle();
}

function finalizeImmersiveTranscript() {
  commitSpeechInterim();
  speechPrefix = ($("storyTranscript")?.value || "").trim();
  speechFinalized = "";
  speechInterim = "";
  speechLastInterim = "";
  speechSessionBuffer = "";
  transcriptUserEdited = false;
  syncStoryTranscriptDisplay();
}

async function endImmersiveSession() {
  speechKeepAlive = false;
  immersiveSessionActive = false;
  stopSpeechHealthMonitor();
  stopSpeechRecognition();
  hideCallOverlay();
  syncStoryComposerHint();
  await stopStoryAudioCapture();
  finalizeImmersiveTranscript();
  setSpeechStatus("");
  updateMicUiIdle();
}

function stopSpeechRecognition({ userStop = true } = {}) {
  if (userStop) speechKeepAlive = false;
  if (!speechRec) {
    setSpeechUiRecording(false);
    speechMode = null;
    return;
  }
  if (userStop) {
    try {
      speechRec.stop();
    } catch {
      speechRec = null;
      setSpeechUiRecording(false);
      speechMode = null;
    }
    return;
  }
  try {
    speechRec.stop();
  } catch {
    speechRec = null;
    setSpeechUiRecording(false);
    speechMode = null;
  }
}

async function startImmersiveSession() {
  if (speechRec) {
    endImmersiveSession();
    return;
  }
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) {
    void openNarroAlert("当前浏览器不支持语音转文字，请改用 Chrome 或 Edge 桌面版。", {
      title: "无法使用录音",
    });
    return;
  }

  speechMode = xiaoleCompanionEnabled ? "immersive-guided" : "immersive-free";
  speechKeepAlive = true;
  speechSessionBuffer = "";
  speechFinalized = "";
  speechInterim = "";
  speechLastInterim = "";
  const ta = $("storyTranscript");
  if (transcriptUserEdited && ta) {
    commitTranscriptFromEditor();
  } else {
    speechPrefix = ta?.value || "";
    speechFinalized = "";
  }

  await warmupMicrophone();

  showCallOverlay();
  startSpeechHealthMonitor();

  speechRecHandlers = {
    onResult(ev) {
      if (shouldIgnoreSttResult()) return;
      let interim = "";
      for (let i = ev.resultIndex; i < ev.results.length; i++) {
        const piece = ev.results[i][0].transcript;
        if (ev.results[i].isFinal) {
          handleSpeechFinalSegment(piece);
        } else {
          interim += piece;
        }
      }
      if (interim.trim()) handleSpeechInterim(interim);
      else syncStoryTranscriptDisplay("");
    },
    onError(ev) {
      if (ev.error === "no-speech" && speechKeepAlive) return;
      if (ev.error === "aborted" && speechKeepAlive) return;
      const err = ev.error === "not-allowed" ? "请允许麦克风权限" : ev.error || "识别出错";
      if (ev.error === "not-allowed" || ev.error === "service-not-allowed") {
        void openNarroAlert(err, { title: "录音" });
        endImmersiveSession();
        return;
      }
      setSpeechStatus("正在重新连接麦克风…", true);
      speechRec = null;
      setTimeout(() => void bootSpeechRecognition(), 400);
    },
    onEnd() {
      speechRec = null;
      if (speechKeepAlive && immersiveSessionActive) {
        setTimeout(() => void bootSpeechRecognition(), 120);
      } else if (!immersiveSessionActive) {
        setSpeechUiRecording(false);
        speechMode = null;
      }
    },
    onAudioStart() {},
    onSpeechStart() {},
  };

  await bootSpeechRecognition();

  if (speechMode === "immersive-guided") {
    window.NarroStoryCoach?.stopSpeech?.();
    await window.NarroStoryCoach?.startGuidedSession?.();
  }
}

function getNarrativeQuality(data) {
  const stored = data?.narrative_quality || data?.linguistics?.narrative_quality;
  if (stored) return stored;
  const text = data?.text || "";
  const core = data?.linguistics?.core || {};
  return inferLegacyNarrativeQuality(text, core);
}

/** 旧记录无 narrative_quality 时，与后端规则近似的前端推断 */
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
    return {
      status: "low_quality",
      message: "讲述偏短，分数仅供参考。",
    };
  }
  return { status: "sufficient", score: null, message: "" };
}

function paintQualityBanner(q, bannerId) {
  const el = $(bannerId || "qualityBanner");
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

async function clearStoryDock() {
  await endImmersiveSession();
  deactivateXiaoleCompanion();
  if ($("storyTranscript")) $("storyTranscript").value = "";
  speechPrefix = "";
  speechFinalized = "";
  speechInterim = "";
  speechLastInterim = "";
  transcriptUserEdited = false;
  speechSessionBuffer = "";
  speechMode = null;
  storySessionAudioBlob = null;
  storyAudioChunks = [];
  autoResizeStoryInput();
  window.NarroStoryCoach?.reset?.();
  syncStoryComposerHint();
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
  el.innerHTML = lingKeys
    .map(([k, zh]) => {
      const v = core[k];
      if (v == null) return "";
      const disp = k === "MLU" || k === "TTR" ? Number(v).toFixed(k === "TTR" ? 3 : 2) : v;
      const norm = peer[k] != null ? ` <span class="text-xs text-muted-foreground">常模 ${peer[k]}</span>` : "";
      return `<li><strong>${zh}</strong> ${disp}${norm}</li>`;
    })
    .join("") || "<li class='text-muted-foreground'>—</li>";
}

function fillLingMetricsDl(el, core, peer) {
  if (!el) return;
  const lingKeys = [
    ["TNW", "总词数"],
    ["TDW", "不同词数"],
    ["TNU", "句子数"],
    ["MLU", "平均句长"],
    ["TTR", "词型率"],
  ];
  const items = lingKeys
    .map(([k, zh]) => {
      const v = core[k];
      if (v == null) return "";
      const disp = k === "MLU" || k === "TTR" ? Number(v).toFixed(k === "TTR" ? 3 : 2) : v;
      const norm = peer[k] != null ? `<span class="norm">常模 ${peer[k]}</span>` : "";
      return `<div><dt>${zh}</dt><dd>${disp}${norm}</dd></div>`;
    })
    .join("");
  el.innerHTML = items || '<div><dt>—</dt><dd>无数据</dd></div>';
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
      const label = window.NarroUI?.ssTaskLabel(t.id) || t.id;
      return `<span class="record-task-chip ${cls}" title="${escapeHtml(label)} ${pct}%">${escapeHtml(label)} ${mark}</span>`;
    })
    .join("");
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

let activeEvalPollId = null;
let activeEvalPollTimer = null;

function stopEvaluationPolling() {
  if (activeEvalPollTimer) {
    clearInterval(activeEvalPollTimer);
    activeEvalPollTimer = null;
  }
  activeEvalPollId = null;
}

function isEvaluationInProgress(status) {
  return status && status !== "completed" && status !== "failed";
}

function beginEvaluationPolling(eid, hooks = {}) {
  stopEvaluationPolling();
  activeEvalPollId = eid;
  const maxMs = 30 * 60 * 1000;
  const start = Date.now();

  const tick = async () => {
    if (activeEvalPollId !== eid) return;
    if (Date.now() - start > maxMs) {
      stopEvaluationPolling();
      hooks.onFail?.("评估耗时较长，请稍后在「我的记录」中刷新查看");
      return;
    }
    try {
      const row = await fetchJson(`/api/history/${eid}`);
      const st = row.status || "completed";
      hooks.onUpdate?.(row);
      if (
        currentPersona === "user" &&
        String(selectedHistoryEvalId) === String(eid) &&
        isEvaluationInProgress(st)
      ) {
        if ($("historyEvalProgressMsg")) {
          $("historyEvalProgressMsg").textContent = row.status_message || "正在分析…";
        }
      }
      if (st === "completed") {
        stopEvaluationPolling();
        if (
          currentPersona === "user" &&
          String(selectedHistoryEvalId) === String(eid)
        ) {
          renderHistoryDetail(rowToRenderPayload(row), row);
          maybePromptParentSurvey(row);
        }
        hooks.onDone?.(row);
        if (currentPersona === "user") {
          await refreshUserHistoryNav({ highlightEvalId: eid });
        }
        return;
      }
      if (st === "failed") {
        stopEvaluationPolling();
        if (
          currentPersona === "user" &&
          String(selectedHistoryEvalId) === String(eid)
        ) {
          renderHistoryDetail(rowToRenderPayload(row), row);
        }
        hooks.onFail?.(row.status_message || "评估失败");
        if (currentPersona === "user") {
          await refreshUserHistoryNav({ highlightEvalId: eid });
        }
      }
    } catch {
      /* 网络抖动时继续轮询 */
    }
  };

  tick();
  activeEvalPollTimer = setInterval(tick, 1500);
}

function paintHistoryEvalState(row, data) {
  const status = row?.status || data?.status || "completed";
  const pending = isEvaluationInProgress(status);
  const failed = status === "failed";
  const block = $("historyDetailBlock");
  block?.classList.remove("record-report--pending", "record-report--failed");
  if (pending) block?.classList.add("record-report--pending");
  if (failed) block?.classList.add("record-report--failed");
  const prog = $("historyEvalProgress");
  if (prog) {
    prog.classList.toggle("hidden", !pending);
    if ($("historyEvalProgressMsg")) {
      $("historyEvalProgressMsg").textContent =
        row?.status_message || data?.status_message || "正在分析…";
    }
  }
  return pending || failed;
}

function persistLastEvaluation(id) {
  if (id != null) localStorage.setItem(LAST_EVAL_KEY, String(id));
}

function storyLabel(storyType) {
  return STORY_SHORT[storyType] || storyType || "—";
}

function historyStoryPhrase(storyType) {
  if (storyType === "pn-agent") return "个人叙事Agent";
  return `${storyLabel(storyType)}故事`;
}

function isPnAgentRecord(row) {
  return row?.story_type === "pn-agent" || row?.coach_mode === "pn-agent";
}

function formatPnDialogueLog(dialogueLog) {
  const skip = new Set(["__CALL_START__", "__USER_SILENT__"]);
  const lines = [];
  for (const turn of dialogueLog || []) {
    const content = String(turn?.content || "").trim();
    if (!content || skip.has(content)) continue;
    const speaker = turn?.role === "assistant" ? "小乐" : turn?.role === "user" ? "孩子" : "";
    if (!speaker) continue;
    lines.push(`${speaker}：${content}`);
  }
  return lines.join("\n");
}

function setHistoryAssessmentSectionsVisible(visible) {
  $("historyEvalResults")
    ?.querySelector(".record-scores")
    ?.classList.toggle("hidden", !visible);
  $("historyQualityScoreHint")?.classList.toggle("hidden", !visible);
  $("historyScBreakdown")?.classList.toggle("hidden", !visible);
  $("historyParentSummary")
    ?.closest(".record-section")
    ?.classList.toggle("hidden", !visible);
  $("historyEvalResults")
    ?.querySelector(".grid.gap-3")
    ?.classList.toggle("hidden", !visible);
  $("historyEvalResults")
    ?.querySelector(".record-pro-details")
    ?.classList.toggle("hidden", !visible);
  if (!visible) $("historyParentSurveySection")?.classList.add("hidden");
}

function paintPnAgentHistoryUI(row, data) {
  $("historyDetailBlock")?.classList.add("record-report--pn-agent");
  setHistoryAssessmentSectionsVisible(false);
  const label = (row?.record_label || "").trim();
  const titleText = label || `个人叙事Agent · ${formatHistoryDateShort(row?.created_at)}`;
  if ($(REPORT_UI.history.title)) $(REPORT_UI.history.title).textContent = titleText;
  if ($(REPORT_UI.history.evalId)) {
    $(REPORT_UI.history.evalId).textContent = String(data.evaluation_id ?? "—");
  }
  if ($(REPORT_UI.history.storyLabel)) $(REPORT_UI.history.storyLabel).textContent = "个人叙事Agent";
  const elapsed = row?.elapsed_ms ?? data?.elapsed_ms ?? 0;
  if ($(REPORT_UI.history.elapsed)) {
    $(REPORT_UI.history.elapsed).textContent = elapsed ? `${elapsed}ms` : "语音陪伴";
  }
  const dialogue =
    formatPnDialogueLog(row?.dialogue_log) || row?.text || data?.text || "（无对话内容）";
  const narrEl = $(REPORT_UI.history.narrativeText);
  if (narrEl) {
    narrEl.textContent = dialogue;
    narrEl.classList.add("record-dialogue-transcript");
  }
  const narrTitle = narrEl?.closest(".record-section")?.querySelector(".record-section-title");
  if (narrTitle) narrTitle.textContent = "通话实录";
  $("historyQualityBanner")?.classList.add("hidden");
  $("historyEvalProgress")?.classList.add("hidden");
  void paintHistoryNarrativeAudio(row, data);
}

function resetPnAgentHistoryUI() {
  $("historyDetailBlock")?.classList.remove("record-report--pn-agent");
  setHistoryAssessmentSectionsVisible(true);
  const narrEl = $(REPORT_UI.history.narrativeText);
  narrEl?.classList.remove("record-dialogue-transcript");
  const narrTitle = narrEl?.closest(".record-section")?.querySelector(".record-section-title");
  if (narrTitle) narrTitle.textContent = "讲述原文";
}

function formatHistoryTableLabel(r, index, total) {
  const custom = (r.record_label || "").trim();
  if (custom) return custom;
  return `第${total - index}次 · ${historyStoryPhrase(r.story_type)} · ${formatHistoryDateShort(r.created_at)}`;
}

function historyRecordLabelFromDom(evalId) {
  const tableCell = document.querySelector(
    `#historyUserBody tr[data-eval-id="${evalId}"] [data-history-label]`
  );
  if (tableCell?.textContent?.trim()) return tableCell.textContent.trim();
  const row = document.querySelector(`.narro-nav-record[data-eval-id="${evalId}"]`);
  return row?.querySelector(".sidebar-nav-record-title")?.textContent?.trim() || "该记录";
}

function formatHistoryDateShort(createdAt) {
  if (!createdAt) return "未知日期";
  const d = new Date(createdAt.replace("Z", ""));
  if (Number.isNaN(d.getTime())) return createdAt.slice(0, 10);
  return `${d.getMonth() + 1}月${d.getDate()}日`;
}

function formatHistoryItemMeta(r) {
  return (r.created_at || "").slice(0, 16).replace("T", " ");
}

function updateHistoryAskNarroBtn() {
  const btn = $("historyAskNarroBtn");
  if (!btn) return;
  const show =
    currentPersona === "user" &&
    $("panel-history")?.classList.contains("active") &&
    !$("historyDetailWrap")?.classList.contains("hidden") &&
    !!currentEvaluationId &&
    !$("historyDetailBlock")?.classList.contains("record-report--pn-agent");
  btn.classList.toggle("hidden", !show);
  if (!show) closeNarroChatDrawer();
}

function updateHistoryNarroCoachChips() {
  const chips = $("historyNarroChatChips");
  if (!chips) return;
  const userCount =
    $("historyCoachMessages")?.querySelectorAll(".narro-chat-msg.user").length || 0;
  chips.classList.toggle("is-hidden", userCount > 0);
}

const NARRO_RAIL_WIDTH_KEY = "narro_rail_width_px";
const NARRO_RAIL_MIN = 280;
const NARRO_RAIL_DEFAULT = 352;
const NARRO_RAIL_MAX_RATIO = 0.55;

function readNarroRailWidthPx() {
  const saved = parseInt(localStorage.getItem(NARRO_RAIL_WIDTH_KEY) || "", 10);
  return Number.isFinite(saved) && saved >= NARRO_RAIL_MIN ? saved : NARRO_RAIL_DEFAULT;
}

function syncHistoryRailHeight() {
  const head = document.querySelector(".app-page-head");
  const main = document.querySelector(".app-main");
  const top = head ? Math.round(head.getBoundingClientRect().bottom) : 0;
  const rightInset = main
    ? Math.max(0, Math.round(window.innerWidth - main.getBoundingClientRect().right))
    : 0;
  document.documentElement.style.setProperty("--history-rail-top", `${top}px`);
  document.documentElement.style.setProperty("--history-rail-height", `calc(100dvh - ${top}px)`);
  document.documentElement.style.setProperty("--history-rail-right", `${rightInset}px`);
}

function applyNarroRailWidth(px) {
  const split = $("historyDetailWrap");
  const rail = $("narroChatDrawer");
  if (!split || !rail) return;
  const maxW = Math.max(NARRO_RAIL_MIN, Math.floor(split.getBoundingClientRect().width * NARRO_RAIL_MAX_RATIO));
  const w = Math.min(Math.max(Math.round(px), NARRO_RAIL_MIN), maxW);
  const val = `${w}px`;
  rail.style.setProperty("--narro-rail-width", val);
  split.style.setProperty("--narro-rail-width", val);
  return w;
}

function initNarroRailResize() {
  const handle = $("narroChatResizeHandle");
  const split = $("historyDetailWrap");
  if (!handle || !split) return;

  applyNarroRailWidth(readNarroRailWidthPx());

  let dragging = false;

  const finishDrag = () => {
    if (!dragging) return;
    dragging = false;
    document.body.classList.remove("narro-rail-resizing");
    const w = parseInt(
      getComputedStyle($("narroChatDrawer") || document.documentElement).getPropertyValue("--narro-rail-width"),
      10
    );
    if (Number.isFinite(w)) localStorage.setItem(NARRO_RAIL_WIDTH_KEY, String(w));
  };

  const onPointerMove = (e) => {
    if (!dragging) return;
    const rect = split.getBoundingClientRect();
    applyNarroRailWidth(rect.right - e.clientX);
    syncHistoryRailHeight();
  };

  handle.addEventListener("pointerdown", (e) => {
    if (!$("narroChatDrawer")?.classList.contains("is-open")) return;
    dragging = true;
    handle.setPointerCapture?.(e.pointerId);
    document.body.classList.add("narro-rail-resizing");
    e.preventDefault();
  });
  handle.addEventListener("pointermove", onPointerMove);
  handle.addEventListener("pointerup", finishDrag);
  handle.addEventListener("pointercancel", finishDrag);
  window.addEventListener("pointerup", finishDrag);
}

function openNarroChatDrawer() {
  if (!currentEvaluationId) return;
  const rail = $("narroChatDrawer");
  const split = $("historyDetailWrap");
  if (!rail || !split || rail.classList.contains("is-open")) return;
  syncHistoryRailHeight();
  applyNarroRailWidth(readNarroRailWidthPx());
  syncHistoryRailHeight();
  rail.classList.remove("hidden");
  rail.setAttribute("aria-hidden", "false");
  split.classList.add("history-rail-open");
  $("panel-history")?.classList.add("history-rail-open");
  requestAnimationFrame(() => {
    rail.classList.add("is-open");
    syncHistoryRailHeight();
  });
  $("historyAskNarroBtn")?.setAttribute("aria-expanded", "true");
  const ctx = $("historyTitle")?.textContent?.trim();
  if ($("narroChatDrawerContext") && ctx) $("narroChatDrawerContext").textContent = ctx;
  requestAnimationFrame(() => $("historyCoachInput")?.focus());
}

function closeNarroChatDrawer() {
  const rail = $("narroChatDrawer");
  const split = $("historyDetailWrap");
  if (!rail) return;
  rail.classList.remove("is-open");
  split?.classList.remove("history-rail-open");
  $("panel-history")?.classList.remove("history-rail-open");
  $("historyAskNarroBtn")?.setAttribute("aria-expanded", "false");
  window.setTimeout(() => {
    if (!rail.classList.contains("is-open")) {
      rail.classList.add("hidden");
      rail.setAttribute("aria-hidden", "true");
    }
  }, 240);
}

function hideHistoryDetail() {
  closeNarroChatDrawer();
  $("historyDetailWrap")?.classList.add("hidden");
  selectedHistoryEvalId = null;
  updateHistoryAskNarroBtn();
  document.querySelectorAll("#historyNavItems .sidebar-nav-record-row").forEach((el) =>
    el.classList.remove("active")
  );
  document.querySelectorAll(".history-row-clickable, .history-row-manager-clickable").forEach((tr) =>
    tr.classList.remove("history-row-selected")
  );
  if (currentPersona === "user") {
    const hasRows = !!$("historyUserBody")?.querySelector("tr[data-eval-id]");
    $("historyUserListWrap")?.classList.toggle("hidden", !hasRows);
    $("historyEmpty")?.classList.toggle("hidden", hasRows);
  } else {
    $("historyEmpty")?.classList.remove("hidden");
  }
}

function resetHistoryCoachThread() {
  const box = $("historyCoachMessages");
  if (!box) return;
  box.innerHTML =
    '<p class="narro-chat-msg bot text-muted-foreground">你好，我是 Narro。已读取本次评估，可在下方提问。</p>';
  if ($("historyCoachInput")) $("historyCoachInput").value = "";
  $("historyCoachHint")?.classList.add("hidden");
  $("historyNarroChatQuick")?.classList.add("hidden");
  updateHistoryNarroCoachChips();
}

function renderHistoryDetail(data, row) {
  currentEvaluationId = data.evaluation_id;
  selectedHistoryEvalId = data.evaluation_id;
  persistLastEvaluation(data.evaluation_id);
  paintEvaluationUI(data, row, "history");
  void paintHistoryNarrativeAudio(row, data);
  const st = row?.status || data?.status || "completed";
  setExportEnabled(st === "completed" && !isPnAgentRecord(row));
  if (st === "completed") refreshLlmStatus();
  resetHistoryCoachThread();

  $("historyDetailWrap")?.classList.remove("hidden");
  $("historyEmpty")?.classList.add("hidden");
  if (currentPersona === "user") $("historyUserListWrap")?.classList.add("hidden");
  setSidebarActive("history", data.evaluation_id);
  document.querySelectorAll(".history-row-clickable, .history-row-manager-clickable").forEach((tr) => {
    tr.classList.toggle("history-row-selected", String(tr.dataset.evalId) === String(data.evaluation_id));
  });
  updateHistoryAskNarroBtn();
  closeNarroChatDrawer();
  if (currentPersona === "user") {
    const title = $(REPORT_UI.history.title)?.textContent?.trim();
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
      const type = historyStoryPhrase(r.story_type);
      const date = formatHistoryDateShort(r.created_at);
      const score =
        r.story_type === "pn-agent"
          ? r.elapsed_ms
            ? `${Math.round(Number(r.elapsed_ms) / 1000)}秒`
            : "通话"
          : r.micro_sum != null
            ? `${r.micro_sum}/15`
            : "—";
      const status = isEvaluationInProgress(r.status)
        ? '<span class="history-status-pending">分析中</span>'
        : '<span class="history-status-done">完成</span>';
      return `<tr class="history-row-clickable${selected ? " history-row-selected" : ""}" data-eval-id="${r.id}">
        <td class="font-mono text-xs text-muted-foreground">#${r.id}</td>
        <td class="font-medium" data-history-label>${escapeHtml(label)}</td>
        <td>${escapeHtml(type)}</td>
        <td class="whitespace-nowrap">${escapeHtml(date)}</td>
        <td class="tabular-nums">${score}</td>
        <td>${status}</td>
        <td class="whitespace-nowrap">
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
  if (currentPersona === "user") {
    container.innerHTML = "";
    return;
  }
  applyHistoryNavExpanded(historyNavExpanded);
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
        `第${total - index}次 · ${historyStoryPhrase(r.story_type)} · ${formatHistoryDateShort(r.created_at)}`;
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

let narroDialogResolve = null;
let narroDialogKeyHandler = null;
let narroDialogFocusTrapHandler = null;
let narroDialogBackdropDismiss = false;
let narroDialogPreviousFocus = null;

function closeNarroDialog(result = null) {
  const root = $("narroDialogRoot");
  if (!root) return;
  root.classList.add("hidden");
  root.setAttribute("aria-hidden", "true");
  document.body.classList.remove("narro-dialog-open");
  narroDialogBackdropDismiss = false;
  if (narroDialogKeyHandler) {
    document.removeEventListener("keydown", narroDialogKeyHandler);
    narroDialogKeyHandler = null;
  }
  if (narroDialogFocusTrapHandler) {
    document.removeEventListener("keydown", narroDialogFocusTrapHandler);
    narroDialogFocusTrapHandler = null;
  }
  const resolve = narroDialogResolve;
  narroDialogResolve = null;
  if (resolve) resolve(result);
  if (narroDialogPreviousFocus?.focus) {
    try {
      narroDialogPreviousFocus.focus();
    } catch {
      /* ignore */
    }
  }
  narroDialogPreviousFocus = null;
}

function openNarroDialog({
  title,
  message = "",
  confirmLabel = "确定",
  cancelLabel = "取消",
  destructive = false,
  hideCancel = false,
  input = false,
  inputValue = "",
  validate = null,
  onSubmit = null,
} = {}) {
  return new Promise((resolve) => {
    const root = $("narroDialogRoot");
    const titleEl = $("narroDialogTitle");
    const descEl = $("narroDialogDesc");
    const bodyEl = $("narroDialogBody");
    const errEl = $("narroDialogError");
    const confirmBtn = $("narroDialogConfirm");
    const cancelBtn = $("narroDialogCancel");
    const panelEl = root?.querySelector(".narro-dialog");
    const backdropEl = root?.querySelector(".narro-dialog-backdrop");
    if (!root || !titleEl || !confirmBtn || !cancelBtn || !bodyEl || !errEl) {
      resolve(null);
      return;
    }

    narroDialogResolve = resolve;
    narroDialogBackdropDismiss = false;
    titleEl.textContent = title || "";
    if (message && descEl) {
      descEl.textContent = message;
      descEl.classList.remove("hidden");
    } else if (descEl) {
      descEl.textContent = "";
      descEl.classList.add("hidden");
    }

    bodyEl.innerHTML = "";
    errEl.textContent = "";
    errEl.classList.add("hidden");

    let inputEl = null;
    if (input) {
      inputEl = document.createElement("input");
      inputEl.type = "text";
      inputEl.className = "input w-full";
      inputEl.value = inputValue;
      inputEl.maxLength = 120;
      inputEl.setAttribute("aria-label", title || "输入");
      bodyEl.appendChild(inputEl);
    }

    confirmBtn.type = "button";
    cancelBtn.type = "button";
    confirmBtn.disabled = false;
    cancelBtn.disabled = false;
    confirmBtn.textContent = confirmLabel;
    cancelBtn.textContent = cancelLabel;
    cancelBtn.classList.toggle("hidden", hideCancel);
    confirmBtn.className = destructive
      ? "btn btn-sm narro-dialog-btn-danger"
      : "btn-primary btn-sm";

    const onConfirm = async () => {
      const raw = input ? inputEl.value : true;
      const value = input ? String(raw).trim() : raw;
      if (validate) {
        const err = validate(value);
        if (err) {
          errEl.textContent = err;
          errEl.classList.remove("hidden");
          (inputEl || confirmBtn).focus();
          return;
        }
      }

      if (onSubmit) {
        confirmBtn.disabled = true;
        cancelBtn.disabled = true;
        if (inputEl) inputEl.disabled = true;
        const idleLabel = confirmLabel;
        confirmBtn.textContent = destructive ? "删除中…" : "保存中…";
        errEl.classList.add("hidden");
        try {
          await onSubmit(value);
          closeNarroDialog(input ? value : true);
        } catch (e) {
          errEl.textContent = e.message || "操作失败";
          errEl.classList.remove("hidden");
        } finally {
          confirmBtn.disabled = false;
          cancelBtn.disabled = false;
          if (inputEl) inputEl.disabled = false;
          confirmBtn.textContent = idleLabel;
        }
        return;
      }

      closeNarroDialog(input ? value : true);
    };

    confirmBtn.onclick = () => void onConfirm();
    cancelBtn.onclick = () => closeNarroDialog(null);
    if (backdropEl) {
      backdropEl.onclick = (e) => {
        if (!narroDialogBackdropDismiss || e.target !== backdropEl) return;
        closeNarroDialog(null);
      };
    }
    if (panelEl) {
      panelEl.onclick = (e) => e.stopPropagation();
    }

    if (inputEl) {
      inputEl.onkeydown = (e) => {
        if (e.key === "Enter") {
          e.preventDefault();
          void onConfirm();
        }
      };
    }

    narroDialogKeyHandler = (e) => {
      if (e.key === "Escape") closeNarroDialog(null);
    };
    document.addEventListener("keydown", narroDialogKeyHandler);

    narroDialogPreviousFocus = document.activeElement;
    const focusables = () =>
      Array.from(
        panelEl?.querySelectorAll(
          'button:not([disabled]), input:not([disabled]), [href], textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
        ) || []
      );
    narroDialogFocusTrapHandler = (e) => {
      if (e.key !== "Tab" || root.classList.contains("hidden")) return;
      const nodes = focusables();
      if (!nodes.length) return;
      const first = nodes[0];
      const last = nodes[nodes.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("keydown", narroDialogFocusTrapHandler);

    root.classList.remove("hidden");
    root.setAttribute("aria-hidden", "false");
    document.body.classList.add("narro-dialog-open");
    setTimeout(() => {
      narroDialogBackdropDismiss = true;
    }, 180);
    requestAnimationFrame(() => {
      if (inputEl) {
        inputEl.focus();
        inputEl.select();
      } else {
        confirmBtn.focus();
      }
    });
  });
}

function openNarroAlert(message, { title = "提示", confirmLabel = "知道了" } = {}) {
  return openNarroDialog({
    title,
    message,
    confirmLabel,
    hideCancel: true,
  });
}

function historyRecordLabel(evalId) {
  return historyRecordLabelFromDom(evalId);
}

async function applyHistoryRecordRenamed(evalId, label) {
  await refreshUserHistoryNav({ highlightEvalId: evalId });
  const labelCell = document.querySelector(
    `#historyUserBody tr[data-eval-id="${evalId}"] [data-history-label]`
  );
  if (labelCell) labelCell.textContent = label;
  setSidebarActive(null, evalId);
  if (
    String(selectedHistoryEvalId) === String(evalId) ||
    String(currentEvaluationId) === String(evalId)
  ) {
    if ($("mainSub")) $("mainSub").textContent = label;
    if ($("historyTitle")) $("historyTitle").textContent = label;
  }
}

async function applyHistoryRecordDeleted(evalId) {
  const wasViewing =
    String(selectedHistoryEvalId) === String(evalId) ||
    String(currentEvaluationId) === String(evalId);

  if (String(currentEvaluationId) === String(evalId)) {
    currentEvaluationId = null;
    setExportEnabled(false);
  }
  if (localStorage.getItem(LAST_EVAL_KEY) === String(evalId)) {
    localStorage.removeItem(LAST_EVAL_KEY);
  }

  const items = await refreshUserHistoryNav();
  if (wasViewing && $("panel-history")?.classList.contains("active")) {
    const nextId = items?.[0]?.id;
    if (nextId) {
      await openEvaluation(nextId, { silent: true });
    } else {
      hideHistoryDetail();
    }
  } else if (String(selectedHistoryEvalId) === String(evalId)) {
    hideHistoryDetail();
  }

  if ($("panel-insights")?.classList.contains("active")) loadInsights();
}

async function renameHistoryRecord(evalId) {
  const eid = parseInt(String(evalId), 10);
  if (!eid) return;
  const current = historyRecordLabel(evalId);

  await openNarroDialog({
    title: "重命名记录",
    message: "为这条记录设置名称",
    confirmLabel: "保存",
    input: true,
    inputValue: current,
    validate: (v) => (v ? null : "名称不能为空"),
    onSubmit: async (label) => {
      await fetchJson(`/api/history/${eid}/rename`, {
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

  await openNarroDialog({
    title: "删除记录",
    message: `确定删除「${name}」？此操作不可恢复。`,
    confirmLabel: "删除",
    destructive: true,
    onSubmit: async () => {
      await fetchJson(`/api/history/${eid}/delete`, { method: "POST" });
      await applyHistoryRecordDeleted(eid);
    },
  });
}

/** 与「我的记录」详情一致的报告 UI（session / history 共用） */
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
  },
};

function paintReportSurface(data, row, ui, { titleText } = {}) {
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
  if ($(ui.title)) $(ui.title).textContent = titleText || `${story}故事`;
  if ($(ui.evalId)) $(ui.evalId).textContent = String(data.evaluation_id ?? "—");
  if ($(ui.storyLabel)) $(ui.storyLabel).textContent = story;
  if ($(ui.elapsed)) $(ui.elapsed).textContent = elapsed;
  if ($(ui.microHero)) $(ui.microHero).textContent = micro;
  if ($(ui.scHero)) $(ui.scHero).textContent = sc;
  if ($(ui.scPillWrap)) $(ui.scPillWrap).classList.toggle("hidden", suppressed);
  if ($(ui.qualityHint)) $(ui.qualityHint).textContent = qualityHint;
  if ($(ui.microSum)) $(ui.microSum).textContent = micro;
  if ($(ui.scSum)) $(ui.scSum).textContent = sc;
  fillScDetail($(ui.scDetail), reg);
  fillScDualTrack($(ui.scDualTrack), reg);
  if ($(ui.scCardWrap)) $(ui.scCardWrap).classList.toggle("opacity-50", suppressed);
  const br = $(ui.scBreakdown);
  if (br) {
    const bd = formatScBreakdown(reg);
    br.textContent = bd;
    br.classList.toggle("hidden", !bd || suppressed);
  }
  if ($(ui.parentSummary)) $(ui.parentSummary).textContent = summary;
  fillLingMetrics($(ui.lingList), core, peer);
  fillTaskGridCompact($(ui.taskGrid), tasks);
  if ($(ui.reportText)) $(ui.reportText).textContent = report;
  const narr = row?.text || data.text || "";
  if ($(ui.narrativeText)) $(ui.narrativeText).textContent = narr;
  paintParentSurveyBlock(row);
}

let parentSurveyConfigCache = null;
let parentSurveyTargetEvalId = null;

async function loadParentSurveyConfig() {
  if (parentSurveyConfigCache) return parentSurveyConfigCache;
  parentSurveyConfigCache = await fetchJson("/api/parent-survey/config");
  return parentSurveyConfigCache;
}

function closeParentSurveyModal() {
  const root = $("parentSurveyRoot");
  if (!root) return;
  root.classList.add("hidden");
  root.setAttribute("aria-hidden", "true");
  document.body.classList.remove("narro-dialog-open");
  parentSurveyTargetEvalId = null;
}

function renderParentSurveyForm(cfg) {
  const host = $("parentSurveyQuestions");
  if (!host) return;
  const labels = cfg.scale_labels || ["1", "2", "3", "4", "5"];
  host.innerHTML = (cfg.questions || [])
    .map(
      (q) => `<div class="parent-survey-q" data-qid="${escapeHtml(q.id)}">
        <label>${escapeHtml(q.text)}</label>
        <div class="parent-survey-scale" role="group" aria-label="${escapeHtml(q.text)}">
          ${[1, 2, 3, 4, 5]
            .map(
              (n) =>
                `<button type="button" data-value="${n}" title="${escapeHtml(labels[n - 1] || String(n))}">${n}</button>`
            )
            .join("")}
        </div>
      </div>`
    )
    .join("");
  host.querySelectorAll(".parent-survey-scale").forEach((scale) => {
    scale.addEventListener("click", (e) => {
      const btn = e.target.closest("button[data-value]");
      if (!btn) return;
      scale.querySelectorAll("button").forEach((b) => b.classList.remove("selected"));
      btn.classList.add("selected");
    });
  });
}

async function openParentSurveyModal(evaluationId) {
  if (currentPersona !== "user") return;
  const root = $("parentSurveyRoot");
  if (!root) return;
  try {
    const cfg = await loadParentSurveyConfig();
    parentSurveyTargetEvalId = evaluationId;
    if ($("parentSurveyTitle")) $("parentSurveyTitle").textContent = cfg.title || "家长观察";
    if ($("parentSurveyIntro")) $("parentSurveyIntro").textContent = cfg.intro || "";
    if ($("parentSurveyError")) $("parentSurveyError").classList.add("hidden");
    renderParentSurveyForm(cfg);
    root.classList.remove("hidden");
    root.setAttribute("aria-hidden", "false");
    document.body.classList.add("narro-dialog-open");
  } catch (e) {
    window.NarroUI?.showNarroBanner?.(e.message || "无法加载问卷", { variant: "info" });
  }
}

async function submitParentSurvey() {
  const eid = parentSurveyTargetEvalId;
  if (!eid) return;
  const answers = {};
  let missing = false;
  document.querySelectorAll(".parent-survey-q").forEach((block) => {
    const qid = block.dataset.qid;
    const sel = block.querySelector(".parent-survey-scale button.selected");
    if (!sel) missing = true;
    else answers[qid] = parseInt(sel.dataset.value, 10);
  });
  const errEl = $("parentSurveyError");
  if (missing) {
    if (errEl) {
      errEl.textContent = "请完成全部题目";
      errEl.classList.remove("hidden");
    }
    return;
  }
  try {
    const data = await fetchJson(`/api/evaluate/${eid}/parent-survey`, {
      method: "POST",
      body: JSON.stringify({ answers }),
    });
    closeParentSurveyModal();
    window.NarroUI?.showNarroBanner?.("家长观察已保存", { variant: "success" });
    if (String(selectedHistoryEvalId) === String(eid)) {
      const row = await fetchJson(`/api/history/${eid}`);
      paintParentSurveyBlock(row);
    }
    if ($("panel-insights")?.classList.contains("active")) loadInsights();
  } catch (e) {
    if (errEl) {
      errEl.textContent = e.message || "提交失败";
      errEl.classList.remove("hidden");
    }
  }
}

function paintParentSurveyBlock(row) {
  const sec = $("historyParentSurveySection");
  const textEl = $("historyParentSurveyText");
  const btn = $("historyParentSurveyBtn");
  if (!sec || !textEl) return;
  const ps = row?.parent_survey;
  const st = row?.status || "completed";
  if (st !== "completed") {
    sec.classList.add("hidden");
    return;
  }
  sec.classList.remove("hidden");
  if (ps?.composite != null) {
    textEl.textContent = ps.triangulation || `家长综合观察 ${ps.composite}/5。`;
    btn?.classList.add("hidden");
  } else {
    textEl.textContent = "填写 3–5 题快速问卷，与自动评估对照，提升可信度。";
    btn?.classList.remove("hidden");
    if (btn) {
      btn.onclick = () => openParentSurveyModal(row.id || row.evaluation_id);
    }
  }
}

function maybePromptParentSurvey(row) {
  if (currentPersona !== "user") return;
  if (!row || row.status !== "completed") return;
  if (row.parent_survey?.composite != null) return;
  const eid = row.id || row.evaluation_id;
  if (!eid) return;
  setTimeout(() => openParentSurveyModal(eid), 400);
}

function paintEvaluationUI(data, row, surface) {
  if (surface === "history") {
    resetPnAgentHistoryUI();
    if (isPnAgentRecord(row)) {
      paintPnAgentHistoryUI(row, data);
      setExportEnabled(false);
      return;
    }
    const blocked = paintHistoryEvalState(row, data);
    const label = (row?.record_label || "").trim();
    const story = storyLabel(row?.story_type || data.story_type);
    const titleText = label || `${story}故事 · ${formatHistoryDateShort(row?.created_at)}`;
    if ($(REPORT_UI.history.title)) $(REPORT_UI.history.title).textContent = titleText;
    if ($(REPORT_UI.history.evalId)) {
      $(REPORT_UI.history.evalId).textContent = String(data.evaluation_id ?? "—");
    }
    if ($(REPORT_UI.history.storyLabel)) $(REPORT_UI.history.storyLabel).textContent = story;
  const narr = row?.text || data.text || "";
  if ($(REPORT_UI.history.narrativeText)) $(REPORT_UI.history.narrativeText).textContent = narr;
  void paintHistoryNarrativeAudio(row, data);
  if (blocked) {
      setExportEnabled(false);
      if ((row?.status || data?.status) === "failed") {
        paintQualityBanner(
          { status: "insufficient", message: row?.status_message || data?.status_message || "评估失败" },
          REPORT_UI.history.qualityBanner
        );
      }
      return;
    }
    paintReportSurface(data, row, REPORT_UI.history, { titleText });
    return;
  }

  if (surface === "manager") {
    const reg = data.regression || {};
    const q = getNarrativeQuality(data);
    const suppressed = scoresSuppressed(q);
    const sc = !suppressed && reg.pred_SC_Sum != null ? reg.pred_SC_Sum.toFixed(2) : "—";
    const microVal = data.microstructure?.sum;
    const micro = suppressed || microVal == null ? "—" : String(microVal);
    const core = data.linguistics?.core || {};
    const peer = data.linguistics?.peer_norms?.averages || {};
    const summary = data.parent_summary || "（暂无摘要）";
    const report = data.report_text || "";
    const elapsed = `${data.elapsed_ms}ms`;
    const tasks = suppressed ? [] : data.microstructure?.tasks || [];
    paintQualityBanner(q, "qualityBannerManager");
    if ($("scSumChip")) $("scSumChip").textContent = suppressed ? "宏观 SC —" : `宏观 SC ${sc}`;
    if ($("microSumChip")) $("microSumChip").textContent = `SS ${micro}/15`;
    if ($("elapsedManager")) $("elapsedManager").textContent = elapsed;
    if ($("parentSummaryManager")) $("parentSummaryManager").textContent = summary;
    if ($("scSumManager")) $("scSumManager").textContent = sc;
    fillScDetail($("scDetailManager"), reg);
    if ($("scCardWrapManager")) $("scCardWrapManager").classList.toggle("opacity-50", suppressed);
    if ($("microSumManager")) $("microSumManager").textContent = micro;
    fillLingMetrics($("lingMetricsManager"), core, peer);
    if ($("reportTextManager")) $("reportTextManager").textContent = report;
    fillTaskGrid($("taskGridManager"), tasks);
  }
}

async function openEvaluation(id, { silent = false } = {}) {
  const eid = parseInt(String(id), 10);
  if (!eid) return;
  try {
    const row = await fetchJson(`/api/history/${eid}`);
    const payload = rowToRenderPayload(row);

    if (currentPersona === "user") {
      renderHistoryDetail(payload, row);
      $("historyEmpty")?.classList.add("hidden");
      if (isEvaluationInProgress(row.status)) {
        beginEvaluationPolling(eid);
      }
      requestAnimationFrame(() => scrollHistoryDetailIntoView());
      return;
    }

    if (row.story_type && storyStimuliData?.stories?.[row.story_type]) {
      selectStory(row.story_type);
    }
    renderResults(payload);
    persistLastEvaluation(eid);
    if (!$("panel-evaluate")?.classList.contains("active")) {
      switchTab("evaluate");
    }
  } catch (e) {
    if (!silent) void openNarroAlert(e.message || "无法加载该条记录", { title: "记录" });
    throw e;
  }
}

/** 恢复最近一次评估 ID（供「我的记录」中 Narro 对话使用） */
function syncCoachEvaluationContext() {
  if (currentPersona !== "user") return;
  const raw = localStorage.getItem(LAST_EVAL_KEY);
  if (!raw) return;
  const eid = parseInt(raw, 10);
  if (eid) currentEvaluationId = eid;
}

function renderResults(data) {
  currentEvaluationId = data.evaluation_id;
  persistLastEvaluation(data.evaluation_id);
  setExportEnabled(true);
  $("resultsContentManager")?.classList.remove("hidden");
  paintEvaluationUI(data, null, "manager");
  refreshLlmStatus();
}

async function ensureProfileBeforeEval() {
  const name = (familyProfile?.child_name || "").trim();
  if (name) return true;
  const goProfile = await openNarroDialog({
    title: "建议完善儿童信息",
    message: "尚未填写儿童姓名时，将使用默认年龄参与常模对比。是否现在填写？",
    confirmLabel: "去填写",
    cancelLabel: "继续评估",
  });
  if (goProfile === true) {
    switchTab("profile");
    return false;
  }
  return true;
}

async function runEvaluation() {
  const text = getNarrativeText();
  if (!text) {
    void openNarroAlert(
      currentPersona === "user" ? "请先完成讲述（录音或打字）" : "请输入叙事正文"
    );
    return;
  }
  if (currentPersona === "user") {
    const ok = await ensureProfileBeforeEval();
    if (!ok) return;
  }
  const payload = evalPayload();
  if (currentPersona === "manager") {
    const snippet = escapeHtml(text.slice(0, 400)) + (text.length > 400 ? "…" : "");
    appendThreadBubble("user", `<p>${snippet}</p>`);
    showLoading(true, "正在创建评估记录…");
  }
  try {
    const data = await fetchJson("/api/evaluate", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    const eid = data.evaluation_id;
    if (!eid) {
      throw new Error("未返回评估记录 ID");
    }

    if (currentPersona === "user") {
      const audioBlob = storySessionAudioBlob;
      await clearStoryDock();
      resetSessionAssessmentView();
      currentEvaluationId = eid;
      persistLastEvaluation(eid);
      if (audioBlob) {
        try {
          await uploadNarrativeAudio(eid, audioBlob);
        } catch (err) {
          console.warn("narrative audio upload failed", err);
        }
      }
      applyHistoryNavExpanded(true);
      await refreshUserHistoryNav({ highlightEvalId: eid });
      switchTab("history", { evalId: eid });
      await openEvaluation(eid, { silent: true });
      const row = await fetchJson(`/api/history/${eid}`);
      void paintHistoryNarrativeAudio(row, rowToRenderPayload(row));
      beginEvaluationPolling(eid);
      if ($("panel-insights")?.classList.contains("active")) loadInsights();
      return;
    }

    showLoading(true, data.status_message || "分析中…");
    beginEvaluationPolling(eid, {
      onUpdate(row) {
        if ($("loadingMsg")) {
          $("loadingMsg").textContent = row.status_message || "正在分析…";
        }
      },
      onDone(row) {
        showLoading(false);
        const payload = rowToRenderPayload(row);
        renderResults(payload);
        appendThreadBubble(
          "bot",
          `<p>评估完成 · #${row.id}<br>宏观 SS <strong>${row.microstructure?.sum ?? "—"}/15</strong>${
            scoresSuppressed(getNarrativeQuality(payload))
              ? `<br><span class="text-amber-700">${escapeHtml(getNarrativeQuality(payload)?.message || "无法评估")}</span>`
              : ` · 宏观 SC <strong>${row.regression?.pred_SC_Sum?.toFixed(2) ?? "—"}</strong>`
          }</p>`
        );
        refreshLlmStatus();
        window.NarroUI?.showNarroBanner?.("评估完成", { variant: "success" });
      },
      onFail(msg) {
        showLoading(false);
        void openNarroAlert(msg || "评估失败", { title: "评估" });
      },
    });
  } catch (err) {
    if (currentPersona === "manager") showLoading(false);
    void openNarroAlert(err.message || "评估失败", { title: "评估" });
  }
}

function bindExport(id, fmt) {
  $(id)?.addEventListener("click", async () => {
    if (!currentEvaluationId) return;
    try {
      await window.NarroUI.downloadWithAuth(
        API,
        `/api/history/${currentEvaluationId}/export?format=${fmt}`
      );
    } catch (e) {
      void openNarroAlert(e.message || "导出失败", { title: "导出" });
    }
  });
}
bindExport("exportTxtBtnManager", "txt");
bindExport("exportCsvBtnManager", "csv");
bindExport("historyExportTxtBtn", "txt");
bindExport("historyExportCsvBtn", "csv");

$("historyAskNarroBtn")?.addEventListener("click", () => {
  const drawer = $("narroChatDrawer");
  if (drawer?.classList.contains("is-open")) closeNarroChatDrawer();
  else openNarroChatDrawer();
});
$("narroChatDrawerCloseBtn")?.addEventListener("click", closeNarroChatDrawer);
$("historyNarroChatChips")?.addEventListener("click", (e) => {
  const item = e.target.closest(".narro-chat-quick-item");
  if (item?.dataset.prompt) sendHistoryCoachMessage(item.dataset.prompt);
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && $("narroChatDrawer")?.classList.contains("is-open")) {
    closeNarroChatDrawer();
  }
});

function appendHistoryCoachMessage(role, text) {
  const box = $("historyCoachMessages");
  if (!box) return;
  const el = document.createElement("p");
  el.className = `narro-chat-msg ${role === "user" ? "user" : "bot"}`;
  el.innerHTML = role === "user" ? escapeHtml(text) : escapeHtml(text).replace(/\n/g, "<br>");
  box.appendChild(el);
  box.scrollTop = box.scrollHeight;
  updateHistoryNarroCoachChips();
}

async function sendHistoryCoachMessage(presetMsg) {
  const input = $("historyCoachInput");
  const msg = (presetMsg || input?.value || "").trim();
  if (!msg) return;
  if (!currentEvaluationId) return;

  const hint = $("historyCoachHint");
  if (!llmAvailable) {
    await refreshLlmStatus();
    if (!llmAvailable) {
      hint?.classList.remove("hidden");
      if (hint) hint.textContent = "AI 未配置或不可用，请在 .env 配置 DEEPSEEK_API_KEY 后重启服务。";
      return;
    }
  }
  hint?.classList.add("hidden");
  if (input && !presetMsg) input.value = "";
  appendHistoryCoachMessage("user", msg);

  const sendBtn = $("historyCoachSendBtn");
  if (sendBtn) sendBtn.disabled = true;
  const pending = document.createElement("p");
  pending.className = "narro-chat-msg bot text-muted-foreground";
  pending.textContent = "Narro 正在思考…";
  $("historyCoachMessages")?.appendChild(pending);

  try {
    const data = await fetchJson(`/api/evaluate/${currentEvaluationId}/coach`, {
      method: "POST",
      body: JSON.stringify({ question: msg }),
    });
    pending.remove();
    appendHistoryCoachMessage("bot", data.reply || "（无回复）");
  } catch (e) {
    pending.remove();
    appendHistoryCoachMessage("bot", e.message || "请求失败");
  } finally {
    if (sendBtn && llmAvailable) sendBtn.disabled = false;
  }
}

$("historyNarroChatForm")?.addEventListener("submit", (e) => {
  e.preventDefault();
  sendHistoryCoachMessage();
});
$("historyNarroChatAttachBtn")?.addEventListener("click", (e) => {
  e.stopPropagation();
  $("historyNarroChatQuick")?.classList.toggle("hidden");
});
$("historyNarroChatQuick")?.addEventListener("click", (e) => {
  const item = e.target.closest(".narro-chat-quick-item");
  if (item?.dataset.prompt) {
    $("historyNarroChatQuick")?.classList.add("hidden");
    sendHistoryCoachMessage(item.dataset.prompt);
  }
});
document.addEventListener("click", (e) => {
  if (!e.target.closest("#narroChatDrawer") && !e.target.closest("#historyAskNarroBtn")) {
    $("historyNarroChatQuick")?.classList.add("hidden");
  }
});

$("evalForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  await runEvaluation();
});

function autoResizeStoryInput() {
  const ta = $("storyTranscript");
  if (!ta) return;
  ta.scrollTop = ta.scrollHeight;
}

function closeStoryDockMenu() {
  $("storyDockMenu")?.classList.add("hidden");
  $("storyDockMenuBtn")?.setAttribute("aria-expanded", "false");
}

function toggleStoryDockMenu() {
  const menu = $("storyDockMenu");
  if (!menu) return;
  const open = menu.classList.toggle("hidden");
  $("storyDockMenuBtn")?.setAttribute("aria-expanded", String(!open));
}

$("storyDockForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  closeStoryDockMenu();
  if (immersiveSessionActive || speechRec) {
    await endImmersiveSession();
  } else {
    stopSpeechRecognition();
  }
  const t = ($("storyTranscript")?.value || "").trim();
  if (!t) {
    void openNarroAlert("请先看完图卡，用「开始讲述」录下完整讲述");
    return;
  }
  setNarrativeText(t);
  await runEvaluation();
});

$("storyDockMenuBtn")?.addEventListener("click", (e) => {
  e.stopPropagation();
  toggleStoryDockMenu();
});

document.addEventListener("click", (e) => {
  if (!e.target.closest("#storyDockMenuBtn") && !e.target.closest("#storyDockMenu")) {
    closeStoryDockMenu();
  }
});

async function runStoryBatchImport(file) {
  const name = (file.name || "").toLowerCase();
  const isCsv = name.endsWith(".csv");
  const isAudio =
    (file.type && file.type.startsWith("audio/")) ||
    /\.(mp3|wav|m4a|webm|ogg|aac)$/i.test(name);
  if (isAudio) {
    void openNarroAlert(
      "当前批量导入仅支持 CSV（需含 text、age 列）。单条讲述请用麦克风录音。",
      { title: "批量导入" }
    );
    return;
  }
  if (!isCsv) {
    void openNarroAlert("请选择 CSV 文件，或使用麦克风录音。", { title: "批量导入" });
    return;
  }
  window.NarroUI?.showNarroBanner?.("正在提交批量评估…", { variant: "info", timeoutMs: 12000 });
  const fd = new FormData();
  fd.append("file", file);
  try {
    const res = await fetch(`${API}/api/batch`, { method: "POST", body: fd, headers: apiHeaders({}) });
    const queued = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(queued.detail || "批量提交失败");
    const job = await pollBatchJob(queued.job_id);
    const summary = job.summary || {};
    const total = summary.total_rows ?? job.total_rows;
    const done = summary.completed ?? job.completed_rows;
    window.NarroUI?.showNarroBanner?.(`批量完成：${done}/${total} 条`, {
      variant: "success",
      timeoutMs: 8000,
    });
    await refreshUserHistoryNav();
    switchTab("history");
  } catch (err) {
    window.NarroUI?.showNarroBanner?.(err.message || "批量导入失败", {
      variant: "info",
      timeoutMs: 8000,
    });
  }
}

$("storyImportBtn")?.addEventListener("click", () => {
  closeStoryDockMenu();
  $("storyImportFile")?.click();
});

$("storyImportFile")?.addEventListener("change", async (e) => {
  const input = e.target;
  const file = input.files?.[0];
  input.value = "";
  if (!file) return;
  await runStoryBatchImport(file);
});
$("historyNewStoryBtn")?.addEventListener("click", resetForNewStory);
$("sampleBtn")?.addEventListener("click", () => {
  setNarrativeText(SAMPLE.text);
  if ($("age")) $("age").value = String(SAMPLE.age);
  if ($("leftBehind")) $("leftBehind").value = String(SAMPLE.left_behind);
});

$("narrativeText")?.addEventListener("input", updateCharCount);
async function refreshUserHistoryNav({ highlightEvalId = null } = {}) {
  if (currentPersona !== "user") return;
  const tbody = $("historyUserBody");
  const detailOpen = !$("historyDetailWrap")?.classList.contains("hidden");
  if (tbody && !detailOpen) {
    tbody.innerHTML = `<tr><td colspan="7" class="text-muted-foreground">加载中…</td></tr>`;
  }
  try {
    const { items } = await fetchJson("/api/history?limit=50");
    const onHistoryTab = $("panel-history")?.classList.contains("active");
    const selectedId =
      highlightEvalId ??
      (onHistoryTab
        ? selectedHistoryEvalId ||
          (detailOpen ? currentEvaluationId : null)
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

async function loadHistory({ evalId = null } = {}) {
  const tbody = $("historyBody");
  const emptyEl = $("historyEmpty");
  const isUser = currentPersona === "user";
  const cols = 9;
  const reopenId =
    evalId ||
    selectedHistoryEvalId ||
    (!$("historyDetailWrap")?.classList.contains("hidden") && currentEvaluationId
      ? currentEvaluationId
      : null);
  if (!reopenId) hideHistoryDetail();

  if (isUser) {
    bindUserHistoryTableEvents();
    const tbody = $("historyUserBody");
    const detailOpen = !$("historyDetailWrap")?.classList.contains("hidden");
    if (tbody && !detailOpen) {
      tbody.innerHTML = `<tr><td colspan="7" class="text-muted-foreground">加载中…</td></tr>`;
    }
    try {
      const { items } = await fetchJson("/api/history?limit=50");
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
      if (tbody && !detailOpen) {
        tbody.innerHTML = `<tr><td colspan="7">${escapeHtml(e.message || "加载失败")}</td></tr>`;
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
    let { items } = await fetchJson(`/api/history${q}`);
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
      b.addEventListener("click", () => downloadUrl(`/api/history/${b.dataset.exportTxt}/export?format=txt`));
    });
    tbody.querySelectorAll("[data-export-csv]").forEach((b) => {
      b.addEventListener("click", () => downloadUrl(`/api/history/${b.dataset.exportCsv}/export?format=csv`));
    });
  } catch (e) {
    tbody.innerHTML = `<tr><td colspan="${cols}">${e.message}</td></tr>`;
  }
}

function refreshHistoryClick() {
  if (currentPersona === "user") {
    const reopenId =
      selectedHistoryEvalId ||
      (!$("historyDetailWrap")?.classList.contains("hidden") ? currentEvaluationId : null);
    loadHistory({ evalId: reopenId });
  } else {
    loadHistory();
  }
}
document.querySelectorAll(".refresh-history-btn").forEach((btn) => {
  btn.addEventListener("click", refreshHistoryClick);
});
$("historyBackToListBtn")?.addEventListener("click", () => {
  hideHistoryDetail();
  if ($("mainSub")) $("mainSub").textContent = TAB_TITLES.history?.[1] || "";
  loadHistory();
});
$("historyFilterBtn")?.addEventListener("click", () => loadHistory());
$("historyClearFilterBtn")?.addEventListener("click", () => {
  if ($("historyChildFilter")) $("historyChildFilter").value = "";
  if ($("historyClassFilter")) $("historyClassFilter").value = "";
  loadHistory();
});

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function pollBatchJob(jobId) {
  const maxWait = 30 * 60 * 1000;
  const t0 = Date.now();
  while (Date.now() - t0 < maxWait) {
    const job = await fetchJson(`/api/batch/${jobId}`);
    const done = job.completed_rows + (job.failed_rows || 0);
    const pct = job.total_rows ? Math.round((done / job.total_rows) * 100) : 0;
    $("batchResult").innerHTML = `<p>处理中… <strong>${job.status}</strong> ${done}/${job.total_rows}（${pct}%）</p>`;
    if (job.status === "completed" || job.status === "failed") return job;
    await sleep(1500);
  }
  throw new Error("批量任务超时，请稍后在历史记录中查看");
}

$("batchForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const file = $("batchFile").files[0];
  if (!file) return;
  const box = $("batchResult");
  box.classList.remove("hidden");
  box.innerHTML = "<p>已提交批量任务…</p>";
  $("batchSubmitBtn").disabled = true;
  const fd = new FormData();
  fd.append("file", file);
  try {
    const res = await fetch(`${API}/api/batch`, { method: "POST", body: fd, headers: apiHeaders({}) });
    const queued = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(queued.detail || "批量提交失败");
    const job = await pollBatchJob(queued.job_id);
    const summary = job.summary || {};
    lastBatchSummaryCsv = summary.summary_csv || "";
    let html = `<p><strong>完成 ${summary.completed ?? job.completed_rows}/${summary.total_rows ?? job.total_rows} 条</strong></p>`;
    const errs = job.errors || [];
    if (errs.length) {
      html += `<p class="text-sm text-destructive">失败 ${errs.length} 条</p>`;
    }
    if (lastBatchSummaryCsv) {
      html += `<button type="button" class="btn-primary btn-sm mt-2" id="downloadBatchCsv">下载汇总 CSV</button>`;
    }
    box.innerHTML = html;
    $("downloadBatchCsv")?.addEventListener("click", () => {
      const blob = new Blob([lastBatchSummaryCsv], { type: "text/csv;charset=utf-8" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "batch_summary.csv";
      a.click();
    });
    loadHistory();
  } catch (err) {
    box.innerHTML = `<p class="text-sm text-destructive">${err.message}</p>`;
  } finally {
    $("batchSubmitBtn").disabled = false;
  }
});

document.querySelectorAll(".story-toggle-btn").forEach((btn) => {
  btn.addEventListener("click", () => selectStory(btn.dataset.story));
});

$("storyPrevBtn")?.addEventListener("click", () => {
  if (storyPanelIndex > 0) {
    storyPanelIndex -= 1;
    renderStoryPanel();
  }
});
$("storyNextBtn")?.addEventListener("click", () => {
  const n = currentStoryDef()?.panels?.length || 0;
  if (n && storyPanelIndex < n - 1) {
    storyPanelIndex += 1;
    renderStoryPanel();
  }
});

$("storyMicBtn")?.addEventListener("click", () => void startImmersiveSession());
$("storyMicStopBtn")?.addEventListener("click", () => void endImmersiveSession());
$("naroMascot")?.addEventListener("click", onXiaoleMascotClick);
setXiaoleCompanionVisual("sleep");
syncStoryComposerHint();

async function loadAdmin() {
  const cls = ($("adminClassFilter")?.value || "").trim();
  const q = cls ? `?class_name=${encodeURIComponent(cls)}` : "";
  try {
    const ov = await fetchJson(`/api/admin/overview${q}`);
    $("adminStats").innerHTML = `
      <p>测评 <strong>${ov.total_evaluations}</strong> 次 · 幼儿 <strong>${ov.total_children}</strong> 人 ·
      预警 <strong class="${ov.alerts_count ? "text-destructive" : ""}">${ov.alerts_count}</strong> 条</p>
      <p class="text-muted-foreground">宏观 SC 均值 ${ov.sc_mean ?? "—"} · SS 均值 ${ov.micro_mean ?? "—"}/15</p>`;
    const alerts = ov.alerts || [];
    $("adminAlerts").innerHTML = alerts.length
      ? alerts
          .map(
            (a) =>
              `<div class="flex items-center gap-2"><span class="badge ${a.severity === "high" ? "badge-destructive" : "badge-outline"}">${a.label}</span><span>${a.child_name || a.child_id || "?"}</span></div>`
          )
          .join("")
      : "<p class='text-muted-foreground'>暂无预警</p>";
    const tbody = $("adminChildrenBody");
    tbody.innerHTML = (ov.children || [])
      .map(
        (c) => `<tr class="${c.flagged ? "bg-destructive/5" : ""}">
          <td>${c.child_name || c.child_id || "—"}</td>
          <td>${c.class_name || "—"}</td>
          <td>${c.n_evaluations}</td>
          <td>${c.last_SC_Sum != null ? Number(c.last_SC_Sum).toFixed(1) : "—"}</td>
          <td>${c.flagged ? '<span class="badge badge-destructive">关注</span>' : "—"}</td></tr>`
      )
      .join("");
    drawAdminChart(ov.distribution?.pred_SC_Sum || []);
  } catch (e) {
    $("adminStats").innerHTML = `<p class="text-sm text-destructive">${e.message}</p>`;
  }
}

function drawAdminChart(values) {
  const canvas = $("adminChart");
  if (!canvas || !values.length) return;
  const ctx = canvas.getContext("2d");
  const w = canvas.width;
  const h = canvas.height;
  ctx.clearRect(0, 0, w, h);
  const max = Math.max(...values, 1);
  const barW = w / values.length;
  values.forEach((v, i) => {
    const bh = (v / max) * (h - 20);
    ctx.fillStyle = v < 4 ? "#ef4444" : "#3b82f6";
    ctx.fillRect(i * barW + 2, h - bh, barW - 4, bh);
  });
  ctx.fillStyle = "#64748b";
  ctx.font = "12px sans-serif";
  ctx.fillText("宏观 SC 分布（最近测评）", 8, 14);
}

$("adminRefreshBtn")?.addEventListener("click", loadAdmin);

(async () => {
  applySidebarCollapsed(sidebarCollapsed);
  applyPersonaChrome();
  await loadStoryStimuli();
  selectStory("cat");
  try {
    await loadMeta();
  } catch {
    /* 元数据加载失败时仍可使用基础功能 */
  }

  const authed = await restoreSession();
  if (authed) {
    if (!familyProfile) await loadFamilyProfile();
    else paintSidebarProfile();
    switchTab(DEFAULT_TAB);
    await refreshUserHistoryNav();
  } else {
    switchAuthTab("login");
  }
  syncCoachEvaluationContext();
  await refreshLlmStatus();
  updateCharCount();
  initNarroRailResize();
  syncHistoryRailHeight();
  window.addEventListener("resize", syncHistoryRailHeight);
  autoResizeStoryInput();
  setSpeechUiRecording(false);
})();
