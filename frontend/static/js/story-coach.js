/**
 * 讲故事页 · Naro 语音引导
 * 严格轮流：Naro 说完 → 等用户说 → 再回应一句
 */
(function () {
  const API = window.NARRO_API_BASE || "";
  const VOICE_STORAGE_KEY = "narro_coach_voice";
  const VOICE_NAME_KEY = "narro_coach_voice_name";
  const MIN_PANEL_CHARS = 14;
  const SILENCE_MS = 1100;
  const MIN_USER_CHARS = 3;
  const FOLLOWUP_COOLDOWN_MS = 1200;
  const LISTEN_NUDGE_MS = 6500;
  const NUDGE_COOLDOWN_MS = 12000;
  const WARMUP_AUTO_MS = 28000;
  const POST_TTS_GATE_MS = 500;

  const state = {
    interactionMode: "free",
    guidedActive: false,
    naroSpeaking: false,
    awaitingUserTurn: false,
    voiceOn: true,
    introDone: false,
    coachHistory: [],
    lastPanelKey: "",
    busy: false,
    panelChildChars: 0,
    voicesReady: false,
    idleTimer: null,
    followupTimer: null,
    listenWatchTimer: null,
    turnCommitted: "",
    liveInterim: "",
    pendingFollowup: "",
    lastFollowupAt: 0,
    speakGeneration: 0,
    fetchAbort: null,
    warmupComplete: true,
    warmupAwaitingChild: false,
    warmupFallbackTimer: null,
    lastChildSpeechAt: 0,
    lastNaroSpokeAt: 0,
    lastNudgeAt: 0,
    transcriptAtNaroEnd: 0,
  };

  function $(id) {
    return document.getElementById(id);
  }

  function apiHeaders() {
    return window.NarroUI?.apiHeadersFromStorage?.() || { "Content-Type": "application/json" };
  }

  function panelInfo() {
    const def = window.__narroCurrentStoryDef?.() || null;
    const panels = def?.panels || [];
    const idx = window.__narroStoryPanelIndex?.() ?? 0;
    return {
      index: idx,
      total: panels.length || 6,
      label: def?.label || def?.title || "",
      storyType: window.__narroSelectedStory?.() || "cat",
    };
  }

  function infoKey() {
    const info = panelInfo();
    return `${info.storyType}:${info.index}`;
  }

  function transcriptCharCount() {
    return (window.__narroGetRecentTranscriptTail?.(10000) || "").replace(/\s+/g, "").length;
  }

  function userSpokeSinceLastNaro() {
    if (state.lastChildSpeechAt <= state.lastNaroSpokeAt) return false;
    const growth = transcriptCharCount() - state.transcriptAtNaroEnd;
    return growth >= MIN_USER_CHARS || state.turnCommitted.replace(/\s+/g, "").length >= MIN_USER_CHARS;
  }

  function setMascotState(mode) {
    const mascot = $("naroMascot");
    if (!mascot) return;
    const allowed = ["idle", "listening", "thinking", "speaking"];
    mascot.dataset.state = allowed.includes(mode) ? mode : "idle";
  }

  function setMascotVisible(visible) {
    const stage = $("naroMascotStage");
    stage?.classList.toggle("hidden", !visible);
    stage?.setAttribute("aria-hidden", visible ? "false" : "true");
    $("sessionPage")?.classList.toggle("story-naro-guided-active", !!visible);
    if (!visible) setMascotState("idle");
  }

  function setCoachStatus(text) {
    const call = $("storyCallStatus");
    const dock = $("speechStatus");
    const msg = text || "";
    if (call) call.textContent = msg;
    else if (dock && msg && state.guidedActive) dock.textContent = msg;
    if (!state.guidedActive) return;
    if (/在想/.test(msg)) setMascotState("thinking");
    else if (/说话|准备/.test(msg)) setMascotState("speaking");
    else if (state.awaitingUserTurn) setMascotState("listening");
  }

  function setNaroSpeaking(on) {
    state.naroSpeaking = !!on;
    window.__narroSetSpeechGate?.(!!on);
    $("storyComposer")?.classList.toggle("is-naro-speaking", !!on);
    if (state.guidedActive) setMascotState(on ? "speaking" : state.awaitingUserTurn ? "listening" : "idle");
  }

  function stopSpeech() {
    state.speakGeneration += 1;
    window.speechSynthesis?.cancel?.();
    setNaroSpeaking(false);
  }

  function interruptNaro() {
    stopSpeech();
    if (state.fetchAbort) {
      try {
        state.fetchAbort.abort();
      } catch {
        /* ignore */
      }
      state.fetchAbort = null;
    }
  }

  function clearFollowupTimer() {
    if (state.followupTimer) {
      clearTimeout(state.followupTimer);
      state.followupTimer = null;
    }
  }

  function clearListenWatchdog() {
    if (state.listenWatchTimer) {
      clearTimeout(state.listenWatchTimer);
      state.listenWatchTimer = null;
    }
  }

  function beginAwaitUserTurn() {
    state.awaitingUserTurn = true;
    state.turnCommitted = "";
    state.liveInterim = "";
    state.transcriptAtNaroEnd = transcriptCharCount();
    state.lastNaroSpokeAt = Date.now();
    clearFollowupTimer();
    scheduleListenWatchdog();
    setCoachStatus(state.warmupAwaitingChild ? "跟 Naro 说句话吧" : "轮到你了，看着图讲");
    setMascotState("listening");
  }

  function scheduleListenWatchdog() {
    clearListenWatchdog();
    if (!state.guidedActive || state.busy || state.naroSpeaking) return;
    state.listenWatchTimer = setTimeout(() => {
      state.listenWatchTimer = null;
      void triggerListenNudge();
    }, LISTEN_NUDGE_MS);
  }

  async function triggerListenNudge() {
    if (!state.guidedActive || state.busy || state.naroSpeaking || !state.awaitingUserTurn) return;
    if (userSpokeSinceLastNaro()) return;
    const now = Date.now();
    if (now - state.lastNudgeAt < NUDGE_COOLDOWN_MS) {
      scheduleListenWatchdog();
      return;
    }
    if (now - state.lastNaroSpokeAt < LISTEN_NUDGE_MS - 200) return;
    state.lastNudgeAt = now;
    state.awaitingUserTurn = false;
    const phase = state.warmupAwaitingChild && !state.warmupComplete ? "warmup_nudge" : "listen_nudge";
    await runSpeakCoach(phase, "");
  }

  function onSpeechHeardFromUser() {
    if (state.naroSpeaking || state.busy) return;
    state.lastChildSpeechAt = Date.now();
    clearListenWatchdog();
  }

  function currentTurnText() {
    return [state.turnCommitted, state.liveInterim].filter(Boolean).join(" ").replace(/\s+/g, " ").trim();
  }

  function scoreVoice(v) {
    const n = (v.name || "").toLowerCase();
    const lang = (v.lang || "").toLowerCase();
    let s = 0;
    if (!lang.startsWith("zh")) return -100;
    if (lang.includes("zh-cn") || lang.includes("zh_cn")) s += 25;
    if (/xiaoxiao|晓晓|xiaoyi|xiaoyu|yunxi|云希|tingting|婷婷|sin-ji|sinji/i.test(n)) s += 50;
    if (/online|natural|neural|premium|enhanced|云端|普通话/i.test(n)) s += 35;
    if (/google|microsoft|apple/i.test(n)) s += 20;
    if (/compact|espeak|samantha|alex|fred|junior|cellos|bad/i.test(n)) s -= 90;
    if (/male|男|kangkang|康康|yunjian/i.test(n)) s -= 30;
    return s;
  }

  function pickChineseVoice() {
    const voices = window.speechSynthesis?.getVoices?.() || [];
    const zh = voices.filter((v) => (v.lang || "").toLowerCase().startsWith("zh"));
    if (!zh.length) return null;
    const saved = localStorage.getItem(VOICE_NAME_KEY);
    if (saved) {
      const hit = zh.find((v) => v.name === saved);
      if (hit && scoreVoice(hit) > 0) return hit;
    }
    return zh.sort((a, b) => scoreVoice(b) - scoreVoice(a))[0];
  }

  function ensureVoices() {
    return new Promise((resolve) => {
      if (state.voicesReady || !window.speechSynthesis) {
        resolve();
        return;
      }
      const done = () => {
        state.voicesReady = true;
        resolve();
      };
      if (window.speechSynthesis.getVoices().length) {
        done();
        return;
      }
      const onChange = () => {
        window.speechSynthesis.removeEventListener("voiceschanged", onChange);
        done();
      };
      window.speechSynthesis.addEventListener("voiceschanged", onChange);
      setTimeout(done, 800);
    });
  }

  function speakOneChunk(chunk, gen) {
    return new Promise((resolve) => {
      const part = String(chunk || "").trim();
      if (!part || !window.speechSynthesis) {
        resolve();
        return;
      }
      const utter = new SpeechSynthesisUtterance(part);
      utter.lang = "zh-CN";
      utter.rate = 0.86;
      utter.pitch = 1.12;
      utter.volume = 1;
      const voice = pickChineseVoice();
      if (voice) {
        utter.voice = voice;
        try {
          localStorage.setItem(VOICE_NAME_KEY, voice.name);
        } catch {
          /* ignore */
        }
      }
      utter.onstart = () => {
        if (gen !== state.speakGeneration) return;
        setNaroSpeaking(true);
        setCoachStatus("Naro 说话中…");
      };
      utter.onend = () => resolve();
      utter.onerror = () => resolve();
      window.speechSynthesis.speak(utter);
    });
  }

  async function speakAloud(text) {
    const msg = String(text || "").trim();
    if (!state.voiceOn || !msg || !window.speechSynthesis) return;
    stopSpeech();
    const gen = state.speakGeneration;
    setNaroSpeaking(true);
    const parts = msg.split(/(?<=[。！？；.!?])\s*/).map((s) => s.trim()).filter(Boolean);
    const chunks = parts.length ? parts : [msg];
    for (const chunk of chunks) {
      if (gen !== state.speakGeneration) break;
      await speakOneChunk(chunk, gen);
    }
    if (gen === state.speakGeneration) {
      await new Promise((r) => setTimeout(r, POST_TTS_GATE_MS));
      if (gen !== state.speakGeneration) return;
      setNaroSpeaking(false);
      window.__narroCommitPendingInterim?.();
      beginAwaitUserTurn();
    }
  }

  function resetIdleTimer() {
    if (state.idleTimer) clearTimeout(state.idleTimer);
    if (!state.guidedActive) return;
    state.idleTimer = setTimeout(() => {
      if (state.awaitingUserTurn) setCoachStatus("轮到你了，看着图讲");
    }, 25000);
  }

  async function setPetMessage(text, { thinking = false, speak = true } = {}) {
    if (thinking) setCoachStatus("Naro 在想…");
    if (!thinking && speak && text) return speakAloud(text);
    return Promise.resolve();
  }

  async function fetchGuide(phase, childUtterance = "") {
    const info = panelInfo();
    state.fetchAbort = new AbortController();
    const signal = state.fetchAbort.signal;
    try {
      const res = await fetch(`${API}/api/story-coach/guide`, {
        method: "POST",
        headers: apiHeaders(),
        signal,
        body: JSON.stringify({
          phase,
          story_type: info.storyType,
          story_label: info.label,
          panel_index: info.index,
          panel_total: info.total,
          caption: "",
          child_utterance: childUtterance,
          history: state.coachHistory.slice(-8),
          use_llm: true,
        }),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.detail || `HTTP ${res.status}`);
      return data;
    } finally {
      if (state.fetchAbort?.signal === signal) state.fetchAbort = null;
    }
  }

  function scheduleFollowupAfterSilence() {
    if (!state.awaitingUserTurn || state.naroSpeaking || state.busy) return;
    clearFollowupTimer();
    state.followupTimer = setTimeout(() => {
      state.followupTimer = null;
      triggerFollowupFromSilence();
    }, SILENCE_MS);
  }

  function triggerFollowupFromSilence() {
    if (!state.guidedActive || !state.awaitingUserTurn || state.busy || state.naroSpeaking) return;
    if (!userSpokeSinceLastNaro()) return;
    const text = currentTurnText();
    if (text.replace(/\s+/g, "").length < MIN_USER_CHARS) return;
    const now = Date.now();
    if (now - state.lastFollowupAt < FOLLOWUP_COOLDOWN_MS) return;

    state.awaitingUserTurn = false;
    state.turnCommitted = "";
    state.liveInterim = "";
    state.lastFollowupAt = now;
    state.panelChildChars += text.replace(/\s+/g, "").length;
    state.coachHistory.push({ role: "user", content: text });

    const phase =
      state.warmupAwaitingChild && !state.warmupComplete ? "warmup_reply" : "followup";
    void runSpeakCoach(phase, text);
  }

  async function runSpeakCoach(phase, childUtterance = "") {
    if (!state.guidedActive) return;
    state.busy = true;
    state.awaitingUserTurn = false;
    clearListenWatchdog();
    const genAtStart = state.speakGeneration;
    await setPetMessage("", { thinking: true, speak: false });
    try {
      const data = await fetchGuide(phase, childUtterance);
      if (genAtStart !== state.speakGeneration) return;
      const msg = (data.message || "").trim();
      if (msg) state.coachHistory.push({ role: "assistant", content: msg });
      await setPetMessage(msg, { thinking: false, speak: true });
    } catch (err) {
      if (err?.name === "AbortError") return;
      if (genAtStart !== state.speakGeneration) return;
      await setPetMessage("嗯，我在听，你讲。", { speak: true });
    } finally {
      state.busy = false;
      resetIdleTimer();
      if (phase === "warmup_reply" && state.warmupAwaitingChild) {
        void finishWarmupAfterChild();
      } else {
        maybeAdvanceAfterPanel();
      }
    }
  }

  function setWarmupBanner(visible) {
    $("storyWarmupBanner")?.classList.toggle("hidden", !visible);
    $("sessionPage")?.classList.toggle("story-warmup-active", !!visible);
  }

  function clearWarmupFallback() {
    if (state.warmupFallbackTimer) {
      clearTimeout(state.warmupFallbackTimer);
      state.warmupFallbackTimer = null;
    }
  }

  async function finishWarmupAfterChild() {
    if (state.warmupComplete || !state.guidedActive) return;
    clearWarmupFallback();
    state.warmupAwaitingChild = false;
    setWarmupBanner(false);
    state.warmupComplete = true;
    state.lastPanelKey = "";
    state.introDone = false;
    await onPanelRendered();
  }

  async function finishWarmupSilent() {
    if (state.warmupComplete || !state.guidedActive) return;
    clearWarmupFallback();
    state.warmupAwaitingChild = false;
    setWarmupBanner(false);
    state.warmupComplete = true;
    state.lastPanelKey = "";
    await onPanelRendered();
  }

  async function runWarmup() {
    state.warmupComplete = false;
    state.warmupAwaitingChild = true;
    setWarmupBanner(true);
    clearWarmupFallback();
    state.warmupFallbackTimer = setTimeout(() => {
      if (state.warmupAwaitingChild && state.guidedActive) void finishWarmupSilent();
    }, WARMUP_AUTO_MS);
    await runSpeakCoach("warmup_greet");
  }

  function maybeAdvanceAfterPanel() {
    if (!state.warmupComplete) return;
    if (state.panelChildChars < MIN_PANEL_CHARS) return;
    const info = panelInfo();
    if (info.index >= info.total - 1) return;
    state.panelChildChars = 0;
    window.__narroAdvanceStoryPanel?.();
  }

  async function onPanelRendered() {
    if (!state.guidedActive || !state.warmupComplete) return;
    const key = infoKey();
    if (key === state.lastPanelKey) return;
    state.lastPanelKey = key;
    state.panelChildChars = 0;
    state.turnCommitted = "";
    state.liveInterim = "";
    state.pendingFollowup = "";
    clearFollowupTimer();
    clearListenWatchdog();
    interruptNaro();

    if (!state.introDone && panelInfo().index === 0) state.introDone = true;
    await runSpeakCoach("panel_greet");
  }

  function onChildSpeechActivity({ interim = "", final = "" } = {}) {
    if (!state.guidedActive || state.naroSpeaking || state.busy) return;
    if (!state.awaitingUserTurn && !state.warmupAwaitingChild) return;

    const fin = String(final || "").trim();
    const interimText = String(interim || "").trim();

    if (fin) {
      if (state.naroSpeaking) return;
      interruptNaro();
      state.turnCommitted = state.turnCommitted ? `${state.turnCommitted} ${fin}`.trim() : fin;
      state.liveInterim = "";
      onSpeechHeardFromUser();
      scheduleFollowupAfterSilence();
    } else if (interimText.length >= 2) {
      state.liveInterim = interimText;
      onSpeechHeardFromUser();
      scheduleFollowupAfterSilence();
    }
  }

  function onChildSpeechEnd(text) {
    onChildSpeechActivity({ final: text });
  }

  async function startGuidedSession() {
    state.guidedActive = true;
    setMascotVisible(true);
    state.introDone = false;
    state.lastPanelKey = "";
    state.coachHistory = [];
    state.panelChildChars = 0;
    state.turnCommitted = "";
    state.liveInterim = "";
    state.awaitingUserTurn = false;
    state.lastChildSpeechAt = 0;
    state.lastNaroSpokeAt = 0;
    state.lastNudgeAt = 0;
    clearFollowupTimer();
    clearListenWatchdog();
    clearWarmupFallback();
    setCoachStatus("Naro 准备中…");
    void ensureVoices();
    $("storyViewerStage")?.scrollIntoView({ block: "nearest", behavior: "smooth" });
    await runWarmup();
  }

  function endGuidedSession() {
    state.guidedActive = false;
    state.awaitingUserTurn = false;
    setMascotVisible(false);
    setWarmupBanner(false);
    state.warmupComplete = true;
    state.warmupAwaitingChild = false;
    if (state.idleTimer) clearTimeout(state.idleTimer);
    clearFollowupTimer();
    clearListenWatchdog();
    clearWarmupFallback();
    interruptNaro();
    setNaroSpeaking(false);
  }

  function setNaroEnabled(enabled) {
    state.interactionMode = enabled ? "guided" : "free";
    if (!enabled) endGuidedSession();
  }

  function setInteractionMode(mode) {
    setNaroEnabled(mode === "guided");
  }

  function reset() {
    interruptNaro();
    endGuidedSession();
    state.coachHistory = [];
    state.lastPanelKey = "";
  }

  function shouldHandlePanelRender() {
    if (!state.guidedActive) return true;
    return state.warmupComplete;
  }

  function isWarmupComplete() {
    return state.warmupComplete;
  }

  function getCoachMode() {
    return state.guidedActive ? "guided" : "free";
  }

  function isNaroSpeaking() {
    return state.naroSpeaking;
  }

  function init() {
    state.voiceOn = localStorage.getItem(VOICE_STORAGE_KEY) !== "0";
    void ensureVoices();
    setNaroEnabled(false);
    reset();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.NarroStoryCoach = {
    setNaroEnabled,
    setInteractionMode,
    startGuidedSession,
    endGuidedSession,
    reset,
    onPanelRendered,
    onChildSpeechEnd,
    onChildSpeechActivity,
    isNaroSpeaking,
    getCoachMode,
    shouldHandlePanelRender,
    isWarmupComplete,
    stopSpeech: stopSpeech,
    interruptNaro,
  };
})();
