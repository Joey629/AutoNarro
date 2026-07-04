/**
 * PN agent · 语音通话：单击电话开始/挂断
 */
(function () {
  const API = window.NARRO_API_BASE || "";
  const PROFILE_KEY = "narro_family_profile";
  const VOICE_NAME_KEY = "narro_pn_agent_child_voice_v1";

  const SILENCE_MS = 1000;
  const HINT_SILENCE_MS = 9000;
  const MIN_USER_CHARS = 2;
  const BARGE_IN_CHARS = 1;
  const POST_TTS_MS = 50;
  const REC_RESTART_MS = 20;
  const LISTEN_LEAD_MS = 650;
  const TTS_SPEED = 1.3;
  const CALL_START = "__CALL_START__";
  const USER_SILENT = "__USER_SILENT__";

  const state = {
    inCall: false,
    voiceOn: false,
    introPlayed: false,
    phase: "idle",
    pnSession: {},
    callStartedAt: 0,
    hintTimer: null,
    healthTimer: null,
    keepAlive: false,
    agentSpeaking: false,
    busy: false,
    speechRec: null,
    recStarting: false,
    micStream: null,
    audioCtx: null,
    mixDest: null,
    micGain: null,
    ttsGain: null,
    micSourceNode: null,
    audioRecorder: null,
    audioChunks: [],
    sessionAudioBlob: null,
    endingCall: false,
    lastSpeechAt: 0,
    history: [],
    turnCommitted: "",
    liveInterim: "",
    turnBuffer: "",
    silenceTimer: null,
    speakGen: 0,
    fetchAbort: null,
    llmOk: null,
    ttsOk: null,
    ttsAudio: null,
    ttsAudioUrl: null,
    bargeInListen: false,
    earlyListenTimer: null,
    voicesReady: false,
    canUseSpeech: !!(window.SpeechRecognition || window.webkitSpeechRecognition),
  };

  function $(id) {
    return document.getElementById(id);
  }

  function apiHeaders(extra = {}) {
    const h = { "Content-Type": "application/json", ...extra };
    try {
      const key = localStorage.getItem("narro_api_key");
      if (key) h["X-API-Key"] = key;
      const session = localStorage.getItem("narro_session_token");
      if (session) h.Authorization = `Bearer ${session}`;
    } catch {
      /* ignore */
    }
    return h;
  }

  function apiAuthHeaders(extra = {}) {
    const h = { ...extra };
    try {
      const key = localStorage.getItem("narro_api_key");
      if (key) h["X-API-Key"] = key;
      const session = localStorage.getItem("narro_session_token");
      if (session) h.Authorization = `Bearer ${session}`;
    } catch {
      /* ignore */
    }
    return h;
  }

  function readProfile() {
    try {
      const raw = localStorage.getItem(PROFILE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  }

  function setStatus(text) {
    state.phase = text;
    const el = $("pnAgentCallStatus");
    if (el) el.textContent = text || "";
  }

  function setLiveCaption(text, hearing = false) {
    const el = $("pnAgentLiveCaption");
    if (!el) return;
    const msg = String(text || "").trim();
    el.textContent = msg;
    el.classList.toggle("hidden", !msg);
    el.classList.toggle("is-hearing", !!hearing && !!msg);
  }

  function setWarn(text) {
    const el = $("pnAgentCallWarn");
    if (!el) return;
    el.textContent = text || "";
    el.classList.toggle("hidden", !text);
  }

  function syncToolbar() {
    const btn = $("pnAgentCallBtn");
    if (btn) {
      btn.disabled = !state.canUseSpeech || state.llmOk === false || state.endingCall;
      btn.classList.toggle("is-in-call", state.inCall && state.voiceOn);
      btn.setAttribute("aria-pressed", state.inCall ? "true" : "false");
      btn.setAttribute("aria-label", state.inCall ? "挂断通话" : "开始通话");
    }
    document.body.classList.toggle("pn-agent-in-call", state.inCall && state.voiceOn);
  }

  function clearHintTimer() {
    if (state.hintTimer) {
      clearTimeout(state.hintTimer);
      state.hintTimer = null;
    }
  }

  function stopHealthMonitor() {
    if (state.healthTimer) {
      clearInterval(state.healthTimer);
      state.healthTimer = null;
    }
  }

  function startHealthMonitor() {
    stopHealthMonitor();
    state.lastSpeechAt = Date.now();
    state.healthTimer = setInterval(() => {
      if (!state.inCall || !state.voiceOn || state.busy) return;
      if (state.agentSpeaking && !state.bargeInListen) return;
      const silentMs = Date.now() - state.lastSpeechAt;
      if (silentMs > 8000 && state.speechRec) {
        void restartRecognition();
      } else if (!state.speechRec && !state.recStarting) {
        void bootRecognition();
      }
    }, 1200);
  }

  function scheduleHintCheck() {
    clearHintTimer();
    /* 讲故事陪伴流程关闭自动提示，避免思考时被小乐插话 */
  }

  function clearEarlyListenTimer() {
    if (state.earlyListenTimer) {
      clearTimeout(state.earlyListenTimer);
      state.earlyListenTimer = null;
    }
  }

  function clearSilenceTimer() {
    if (state.silenceTimer) {
      clearTimeout(state.silenceTimer);
      state.silenceTimer = null;
    }
  }

  function scheduleSilenceCommit() {
    clearSilenceTimer();
    state.silenceTimer = setTimeout(() => {
      void commitUserTurn();
    }, SILENCE_MS);
  }

  function normalizedChars(s) {
    return String(s || "").replace(/\s+/g, "").trim();
  }

  function currentUserText() {
    return `${state.turnCommitted}${state.liveInterim}`.trim() || state.turnBuffer.trim();
  }

  function canAcceptSpeech() {
    if (!state.inCall || !state.voiceOn || state.busy) return false;
    if (state.agentSpeaking) return !!state.bargeInListen;
    return true;
  }

  function triggerBargeIn(liveText = "") {
    if (!state.agentSpeaking) return;
    stopTts();
    const piece = String(liveText || "").trim();
    if (piece && normalizedChars(piece).length >= BARGE_IN_CHARS) {
      state.turnCommitted = piece;
      state.turnBuffer = piece;
      setLiveCaption(piece, true);
    }
    state.agentSpeaking = false;
    state.bargeInListen = false;
    setStatus("正在听你说…");
    setLiveCaption(state.turnCommitted || "正在听你说…", true);
    void bootRecognition();
    scheduleSilenceCommit();
  }

  async function fetchJson(path, options = {}) {
    const res = await fetch(`${API}${path}`, {
      ...options,
      headers: { ...apiHeaders(), ...(options.headers || {}) },
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || data.message || `请求失败 (${res.status})`);
    return data;
  }

  async function refreshLlmStatus() {
    try {
      const [llm, tts] = await Promise.all([
        fetchJson("/api/llm/status"),
        fetchJson("/api/pn-agent/tts/status").catch(() => ({ available: false })),
      ]);
      state.llmOk = !!llm.available;
      state.ttsOk = !!tts.available;
    } catch {
      state.llmOk = false;
      state.ttsOk = false;
    }
    updateAvailability();
  }

  function updateAvailability() {
    if (!state.canUseSpeech) {
      setWarn("当前浏览器不支持语音，请使用 Chrome 或 Edge 桌面版。");
      setStatus("语音不可用");
    } else if (state.llmOk === false) {
      setWarn("AI 未配置：请在 .env 设置 DEEPSEEK_API_KEY 后重启服务。");
      setStatus("AI 未就绪");
    } else if (state.ttsOk === false) {
      setWarn("豆包语音未配置，小乐将使用浏览器音色。建议在 .env 设置 VOLC_TTS_APP_ID 与 VOLC_TTS_ACCESS_TOKEN。");
      if (!state.inCall) setStatus("点击电话开始通话");
    } else {
      setWarn("");
      if (!state.inCall) setStatus("点击电话开始通话");
    }
    syncToolbar();
  }

  /** 优先童声/幼声，让小乐听起来像同龄小朋友 */
  function scoreChildVoice(v) {
    const n = (v.name || "").toLowerCase();
    const lang = (v.lang || "").toLowerCase();
    let s = 0;
    if (!lang.startsWith("zh")) return -100;
    if (lang.includes("zh-cn") || lang.includes("zh_cn")) s += 20;
    if (/child|kid|children|童声|少儿|少兒|儿童|兒童|男孩|女孩|小姑娘|小朋友|男童|女童/i.test(n)) s += 130;
    if (/xiaoyi|晓伊|xiaobei|晓北|xiaoni|晓妮|yunye|云野|穗秋/i.test(n)) s += 95;
    if (/junior|young|youth|童年/i.test(n)) s += 70;
    if (/xiaoxiao|晓晓|xiaoyu|晓宇|yunxi|云希|tingting|婷婷|sin-ji|sinji|meijia|meiyi/i.test(n)) s += 42;
    if (/online|natural|neural|premium|enhanced|云端|普通话/i.test(n)) s += 22;
    if (/google|microsoft|apple/i.test(n)) s += 12;
    if (/compact|espeak|bad|cellos|fred|alex|samantha/i.test(n)) s -= 90;
    if (/male|男|kangkang|康康|yunjian|云健|yunyang|云扬|yunze|云泽|yunhao|云皓|yunfeng|云枫/i.test(n)) s -= 85;
    return s;
  }

  function pickChildCompanionVoice() {
    const voices = window.speechSynthesis?.getVoices?.() || [];
    const zh = voices.filter((v) => scoreChildVoice(v) > 0);
    if (!zh.length) return null;
    const saved = localStorage.getItem(VOICE_NAME_KEY);
    if (saved) {
      const hit = zh.find((v) => v.name === saved);
      if (hit && scoreChildVoice(hit) >= 40) return hit;
    }
    return zh.sort((a, b) => scoreChildVoice(b) - scoreChildVoice(a))[0];
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

  function stopTts() {
    state.speakGen += 1;
    clearEarlyListenTimer();
    if (state.ttsAudio) {
      try {
        state.ttsAudio.pause();
        state.ttsAudio.src = "";
      } catch {
        /* ignore */
      }
      state.ttsAudio = null;
    }
    if (state.ttsAudioUrl) {
      URL.revokeObjectURL(state.ttsAudioUrl);
      state.ttsAudioUrl = null;
    }
    window.speechSynthesis?.cancel?.();
    state.agentSpeaking = false;
    state.bargeInListen = false;
  }

  function splitSpeechChunks(text) {
    const parts = String(text || "")
      .split(/(?<=[。！？；.!?，,、])\s*/)
      .map((s) => s.trim())
      .filter(Boolean);
    return parts.length ? parts : [String(text || "").trim()].filter(Boolean);
  }

  async function fetchTtsBlob(text) {
    const res = await fetch(`${API}/api/pn-agent/tts`, {
      method: "POST",
      headers: apiHeaders(),
      body: JSON.stringify({ text, speed_ratio: TTS_SPEED, pitch_ratio: 1.0 }),
    });
    if (!res.ok) {
      const data = await res.json().catch(() => ({}));
      throw new Error(data.detail || "语音合成失败");
    }
    return res.blob();
  }

  function playTtsAudio(audio, gen, { bargeIn = true } = {}) {
    return new Promise((resolve) => {
      const done = () => {
        clearEarlyListenTimer();
        resolve();
      };
      audio.onloadedmetadata = () => {
        if (gen !== state.speakGen || !state.agentSpeaking || !bargeIn) return;
        const dur = (audio.duration || 0) * 1000;
        const lead = Math.max(280, dur * 0.52);
        clearEarlyListenTimer();
        state.earlyListenTimer = setTimeout(() => {
          if (gen !== state.speakGen || !state.agentSpeaking) return;
          state.bargeInListen = true;
          void bootRecognition();
        }, lead);
      };
      audio.onplay = () => {
        if (gen !== state.speakGen) return;
        setStatus("小乐说话中");
        setLiveCaption("");
      };
      audio.onended = done;
      audio.onerror = done;
      void audio.play().catch(done);
    });
  }

  async function playTtsBlob(blob, gen, { bargeIn = true } = {}) {
    if (state.ttsAudioUrl) {
      URL.revokeObjectURL(state.ttsAudioUrl);
      state.ttsAudioUrl = null;
    }
    state.ttsAudioUrl = URL.createObjectURL(blob);
    const audio = new Audio(state.ttsAudioUrl);
    state.ttsAudio = audio;
    routeTtsElement(audio);
    await playTtsAudio(audio, gen, { bargeIn });
  }

  async function speakCloudChunks(chunks, gen, firstPrefetch = null) {
    if (!chunks.length) return;
    let nextFetch = firstPrefetch || fetchTtsBlob(chunks[0]);
    for (let i = 0; i < chunks.length; i++) {
      if (gen !== state.speakGen || !state.voiceOn || !state.inCall) return;
      const blob = await nextFetch;
      if (i + 1 < chunks.length) nextFetch = fetchTtsBlob(chunks[i + 1]);
      await playTtsBlob(blob, gen, { bargeIn: true });
    }
  }

  function speakChunk(text, gen) {
    return new Promise((resolve) => {
      const part = String(text || "").trim();
      if (!part || !window.speechSynthesis) {
        resolve();
        return;
      }
      const utter = new SpeechSynthesisUtterance(part);
      utter.lang = "zh-CN";
      utter.rate = TTS_SPEED;
      utter.pitch = 1.34;
      utter.volume = 1;
      const voice = pickChildCompanionVoice();
      if (voice) {
        utter.voice = voice;
        try {
          localStorage.setItem(VOICE_NAME_KEY, voice.name);
        } catch {
          /* ignore */
        }
      }
      utter.onstart = () => {
        if (gen !== state.speakGen) return;
        state.agentSpeaking = true;
        setStatus("小乐说话中");
        setLiveCaption("");
        clearEarlyListenTimer();
        const est = Math.max(250, part.length * 90 - LISTEN_LEAD_MS);
        state.earlyListenTimer = setTimeout(() => {
          if (gen !== state.speakGen || !state.agentSpeaking) return;
          state.bargeInListen = true;
          void bootRecognition();
        }, est);
      };
      utter.onend = () => resolve();
      utter.onerror = () => resolve();
      window.speechSynthesis.speak(utter);
    });
  }

  async function speakAloud(text, { firstPrefetch = null } = {}) {
    if (!state.voiceOn || !state.inCall) return;
    const msg = String(text || "").trim();
    if (!msg) return;
    stopTts();
    const gen = state.speakGen;
    state.agentSpeaking = true;
    const chunks = splitSpeechChunks(msg);

    try {
      if (state.ttsOk) {
        await speakCloudChunks(chunks, gen, firstPrefetch);
      } else {
        for (const chunk of chunks) {
          if (gen !== state.speakGen || !state.voiceOn || !state.inCall) break;
          await speakChunk(chunk, gen);
        }
      }
    } catch (e) {
      console.warn("cloud tts failed, fallback", e);
      if (gen === state.speakGen && state.voiceOn && state.inCall) {
        for (const chunk of chunks) {
          if (gen !== state.speakGen) break;
          await speakChunk(chunk, gen);
        }
      }
    }

    if (gen === state.speakGen && state.voiceOn && state.inCall) {
      state.bargeInListen = false;
      state.agentSpeaking = false;
      void bootRecognition();
      await new Promise((r) => setTimeout(r, POST_TTS_MS));
      setStatus("正在听你说…");
      setLiveCaption("正在听你说…", true);
      await resumeListening({ freshTurn: true });
    }
  }

  async function warmupMicrophone() {
    if (!navigator.mediaDevices?.getUserMedia) {
      throw new Error("当前浏览器无法访问麦克风");
    }
    if (state.micStream) return;
    state.micStream = await navigator.mediaDevices.getUserMedia({
      audio: {
        echoCancellation: false,
        noiseSuppression: true,
        autoGainControl: true,
      },
    });
    connectMicToMix();
    startPnAudioCapture();
  }

  function ensureAudioMix() {
    if (state.audioCtx) return;
    const Ctx = window.AudioContext || window.webkitAudioContext;
    if (!Ctx) return;
    state.audioCtx = new Ctx();
    state.mixDest = state.audioCtx.createMediaStreamDestination();
    state.micGain = state.audioCtx.createGain();
    state.ttsGain = state.audioCtx.createGain();
    state.micGain.gain.value = 1.12;
    state.ttsGain.gain.value = 1;
    state.ttsGain.connect(state.mixDest);
    state.ttsGain.connect(state.audioCtx.destination);
  }

  async function resumeAudioMix() {
    ensureAudioMix();
    if (state.audioCtx?.state === "suspended") {
      try {
        await state.audioCtx.resume();
      } catch {
        /* ignore */
      }
    }
  }

  function connectMicToMix() {
    if (!state.micStream || state.micSourceNode) return;
    ensureAudioMix();
    if (!state.audioCtx || !state.mixDest) return;
    try {
      state.micSourceNode = state.audioCtx.createMediaStreamSource(state.micStream);
      state.micSourceNode.connect(state.micGain);
      state.micGain.connect(state.mixDest);
    } catch (e) {
      console.warn("mic mix route failed", e);
    }
  }

  function routeTtsElement(audio) {
    if (!audio || audio.__mixRouted) return;
    ensureAudioMix();
    if (!state.audioCtx || !state.ttsGain) return;
    try {
      const src = state.audioCtx.createMediaElementSource(audio);
      src.connect(state.ttsGain);
      audio.__mixRouted = true;
    } catch (e) {
      console.warn("tts mix route failed", e);
    }
  }

  function teardownMixBus() {
    try {
      state.micSourceNode?.disconnect();
    } catch {
      /* ignore */
    }
    state.micSourceNode = null;
    const ctx = state.audioCtx;
    state.audioCtx = null;
    state.mixDest = null;
    state.micGain = null;
    state.ttsGain = null;
    if (ctx) {
      void ctx.close().catch(() => {});
    }
  }

  function captureStreamForRecording() {
    connectMicToMix();
    return state.mixDest?.stream || state.micStream;
  }

  function startPnAudioCapture() {
    const stream = captureStreamForRecording();
    if (!stream || state.audioRecorder) return;
    void resumeAudioMix();
    state.audioChunks = [];
    const mime = MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
      ? "audio/webm;codecs=opus"
      : MediaRecorder.isTypeSupported("audio/webm")
        ? "audio/webm"
        : "";
    try {
      state.audioRecorder = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined);
      state.audioRecorder.ondataavailable = (ev) => {
        if (ev.data?.size) state.audioChunks.push(ev.data);
      };
      state.audioRecorder.start(500);
    } catch {
      state.audioRecorder = null;
    }
  }

  function stopPnAudioCapture() {
    const rec = state.audioRecorder;
    if (!rec || rec.state === "inactive") {
      state.audioRecorder = null;
      return Promise.resolve(state.sessionAudioBlob);
    }
    return new Promise((resolve) => {
      rec.onstop = () => {
        if (state.audioChunks.length) {
          state.sessionAudioBlob = new Blob(state.audioChunks, {
            type: rec.mimeType || "audio/webm",
          });
        }
        state.audioChunks = [];
        state.audioRecorder = null;
        resolve(state.sessionAudioBlob);
      };
      try {
        rec.stop();
      } catch {
        state.audioRecorder = null;
        resolve(state.sessionAudioBlob);
      }
    });
  }

  function releaseMic() {
    void stopPnAudioCapture();
    state.micStream?.getTracks?.().forEach((t) => t.stop());
    state.micStream = null;
    teardownMixBus();
  }

  function stopRecognitionInstance(rec) {
    if (!rec) return;
    try {
      rec.onresult = null;
      rec.onerror = null;
      rec.onend = null;
      rec.onaudiostart = null;
      rec.onspeechstart = null;
      rec.stop();
    } catch {
      /* ignore */
    }
  }

  async function pauseListening() {
    const rec = state.speechRec;
    state.speechRec = null;
    stopRecognitionInstance(rec);
    if (REC_RESTART_MS > 0) {
      await new Promise((r) => setTimeout(r, REC_RESTART_MS));
    }
  }

  function stopListeningNow() {
    const rec = state.speechRec;
    state.speechRec = null;
    stopRecognitionInstance(rec);
  }

  function speechErrorMessage(code) {
    if (code === "not-allowed" || code === "service-not-allowed") {
      return "请允许麦克风权限，并在浏览器地址栏检查是否被阻止。";
    }
    if (code === "network") {
      return "语音识别需要网络。若在国内，请确认 Chrome 能访问 Google 语音服务，或改用可联网环境。";
    }
    if (code === "audio-capture") return "未检测到麦克风，请检查系统输入设备。";
    return `语音识别异常：${code || "未知错误"}`;
  }

  function attachRecHandlers(rec) {
    rec.lang = "zh-CN";
    rec.continuous = true;
    rec.interimResults = true;
    rec.maxAlternatives = 1;

    rec.onaudiostart = () => {
      if (!state.voiceOn) return;
      setStatus("正在听你说…");
      setLiveCaption("正在听你说…", true);
    };

    rec.onspeechstart = () => {
      state.lastSpeechAt = Date.now();
      clearHintTimer();
    };

    rec.onresult = (ev) => {
      if (!state.inCall || !state.voiceOn) return;
      if (state.busy && !state.bargeInListen) return;
      if (state.agentSpeaking && !state.bargeInListen) return;

      state.lastSpeechAt = Date.now();
      clearHintTimer();
      let interim = "";
      for (let i = ev.resultIndex; i < ev.results.length; i++) {
        const piece = ev.results[i][0].transcript;
        if (ev.results[i].isFinal) {
          const seg = piece.trim();
          if (seg) {
            if (state.agentSpeaking && state.bargeInListen) {
              triggerBargeIn(`${state.turnCommitted}${seg}`);
              return;
            }
            state.turnCommitted += seg;
            state.turnBuffer = state.turnCommitted;
            setLiveCaption(state.turnCommitted, true);
            scheduleSilenceCommit();
          }
        } else {
          interim += piece;
        }
      }
      const live = `${state.turnCommitted}${interim}`.trim();
      state.liveInterim = interim.trim();
      if (state.agentSpeaking && state.bargeInListen) {
        if (normalizedChars(live).length >= BARGE_IN_CHARS) {
          triggerBargeIn(live);
        }
        return;
      }
      if (live) {
        setLiveCaption(live, true);
        scheduleSilenceCommit();
      }
    };

    rec.onerror = (ev) => {
      if (!state.inCall || !state.voiceOn) return;
      if (ev.error === "no-speech" || ev.error === "aborted") {
        state.speechRec = null;
        state.recStarting = false;
        if (
          state.keepAlive &&
          state.voiceOn &&
          !state.busy &&
          (!state.agentSpeaking || state.bargeInListen)
        ) {
          setTimeout(() => void bootRecognition(), REC_RESTART_MS);
        }
        return;
      }
      if (ev.error === "not-allowed" || ev.error === "service-not-allowed") {
        setWarn(speechErrorMessage(ev.error));
        void endCall();
        return;
      }
      if (ev.error === "network") {
        setWarn(speechErrorMessage("network"));
      }
      state.speechRec = null;
      if (
        state.keepAlive &&
        state.voiceOn &&
        !state.busy &&
        (!state.agentSpeaking || state.bargeInListen)
      ) {
        setTimeout(() => void bootRecognition(), 500);
      }
    };

    rec.onend = () => {
      state.speechRec = null;
      state.recStarting = false;
      if (
        state.keepAlive &&
        state.voiceOn &&
        !state.busy &&
        (!state.agentSpeaking || state.bargeInListen)
      ) {
        setTimeout(() => void bootRecognition(), REC_RESTART_MS);
      }
    };
  }

  async function bootRecognition() {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    const barge = state.bargeInListen;
    if (
      !SR ||
      !state.keepAlive ||
      !state.inCall ||
      !state.voiceOn ||
      state.busy ||
      (!barge && state.agentSpeaking)
    ) {
      return false;
    }
    if (state.speechRec || state.recStarting) return true;
    state.recStarting = true;
    try {
      const rec = new SR();
      attachRecHandlers(rec);
      rec.start();
      state.speechRec = rec;
      state.recStarting = false;
      setWarn("");
      return true;
    } catch (e) {
      state.speechRec = null;
      state.recStarting = false;
      setWarn(e?.message || "无法启动语音识别，请重试");
      return false;
    }
  }

  async function restartRecognition() {
    await pauseListening();
    if (state.voiceOn && state.inCall) await bootRecognition();
  }

  async function resumeListening({ freshTurn = false } = {}) {
    if (!state.inCall || !state.voiceOn || state.busy) return;
    if (state.agentSpeaking && !state.bargeInListen) return;
    state.bargeInListen = false;
    state.liveInterim = "";
    if (freshTurn) {
      state.turnCommitted = "";
      state.turnBuffer = "";
    }
    clearSilenceTimer();
    setStatus("正在听你说…");
    setLiveCaption(state.turnCommitted ? state.turnCommitted : "正在听你说…", true);
    const ok = await bootRecognition();
    if (!ok) {
      await new Promise((r) => setTimeout(r, 160));
      const retry = await bootRecognition();
      if (!retry) setWarn("麦克风未就绪，请挂断后重新拨打。");
    }
  }

  async function fetchReply(userText) {
    const profile = readProfile() || {};
    state.fetchAbort = new AbortController();
    const data = await fetchJson("/api/pn-agent/chat", {
      method: "POST",
      signal: state.fetchAbort.signal,
      body: JSON.stringify({
        message: userText,
        history: state.history,
        session: state.pnSession,
        child_name: profile.child_name || profile.childName || "",
        child_age: profile.age ?? profile.child_age ?? null,
      }),
    });
    if (data.session) state.pnSession = data.session;
    return String(data.reply || "").trim();
  }

  async function agentRespond(userText, { pushUser = true } = {}) {
    if (pushUser && userText && userText !== USER_SILENT && userText !== CALL_START) {
      state.history.push({ role: "user", content: userText });
    }
    setStatus("小乐在想");
    setLiveCaption("");
    let reply = "";
    try {
      reply = await fetchReply(userText);
    } catch (e) {
      if (e?.name === "AbortError") return;
      throw e;
    }
    if (reply) {
      state.history.push({ role: "assistant", content: reply });
      if (state.history.length > 30) state.history = state.history.slice(-30);
    } else if (state.inCall && state.voiceOn) {
      await resumeListening();
      return;
    }
    if (!reply || !state.inCall || !state.voiceOn) return;
    const chunks = splitSpeechChunks(reply);
    const firstPrefetch = state.ttsOk && chunks.length ? fetchTtsBlob(chunks[0]) : null;
    await speakAloud(reply, { firstPrefetch });
  }

  async function requestSilentHint() {
    if (!state.inCall || !state.voiceOn || state.busy || state.agentSpeaking) return;
    if (!state.pnSession?.awaiting_user_speech || state.pnSession?.hint_used) return;
    state.busy = true;
    clearSilenceTimer();
    await pauseListening();
    setStatus("小乐在想");
    try {
      await agentRespond(USER_SILENT, { pushUser: false });
    } catch (e) {
      if (e?.name !== "AbortError" && state.inCall && state.voiceOn) await resumeListening();
    } finally {
      state.busy = false;
      state.fetchAbort = null;
    }
  }

  async function commitUserTurn() {
    if (!state.inCall || !state.voiceOn || state.busy || state.agentSpeaking) return;
    const text = currentUserText();
    if (normalizedChars(text).length < MIN_USER_CHARS) return;
    const lastUser = [...state.history].reverse().find((h) => h.role === "user");
    if (lastUser?.content === text) return;

    state.busy = true;
    clearSilenceTimer();
    stopListeningNow();
    state.turnCommitted = "";
    state.liveInterim = "";
    state.turnBuffer = "";
    setLiveCaption("");
    state.history.push({ role: "user", content: text });

    try {
      await agentRespond(text, { pushUser: false });
    } catch (e) {
      if (e?.name === "AbortError") return;
      if (state.inCall && state.voiceOn) {
        setStatus(e?.message || "对话失败");
        await new Promise((r) => setTimeout(r, 900));
        if (state.voiceOn) await resumeListening();
      }
    } finally {
      state.busy = false;
      state.fetchAbort = null;
    }
  }

  function flushPendingUserSpeech() {
    const text = currentUserText();
    if (normalizedChars(text).length < MIN_USER_CHARS) return;
    const lastUser = [...state.history].reverse().find((h) => h.role === "user");
    if (lastUser?.content === text) return;
    state.history.push({ role: "user", content: text });
  }

  async function waitForSessionIdle(maxMs = 4000) {
    const start = Date.now();
    while (state.busy && Date.now() - start < maxMs) {
      await new Promise((r) => setTimeout(r, 80));
    }
  }

  function meaningfulDialogue(history) {
    return (history || []).filter((turn) => {
      const content = String(turn?.content || "").trim();
      if (!content || content === CALL_START || content === USER_SILENT) return false;
      return turn?.role === "user" || turn?.role === "assistant";
    });
  }

  async function uploadSessionAudio(evaluationId, blob) {
    const fd = new FormData();
    const ext = (blob.type || "").includes("wav") ? "wav" : "webm";
    fd.append("audio", blob, `pn_agent_${evaluationId}.${ext}`);
    const res = await fetch(`${API}/api/evaluate/${evaluationId}/narrative-audio`, {
      method: "POST",
      body: fd,
      headers: apiAuthHeaders(),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || "录音保存失败");
    return data;
  }

  async function saveSessionSnapshot({ history, pnSession, elapsedMs, audioBlob }) {
    const log = meaningfulDialogue(history);
    if (!log.length) {
      window.NarroUI?.showNarroBanner?.("本次通话太短，未生成记录", {
        variant: "info",
        timeoutMs: 3200,
      });
      return null;
    }
    const profile = readProfile() || {};
    try {
      const data = await fetchJson("/api/pn-agent/sessions", {
        method: "POST",
        body: JSON.stringify({
          dialogue_log: log,
          session: pnSession || {},
          child_name: profile.child_name || profile.childName || "",
          child_id: profile.child_id || profile.childId || "",
          child_age: profile.age ?? profile.child_age ?? null,
          class_name: profile.class_name || profile.className || "",
          elapsed_ms: Math.max(0, Number(elapsedMs) || 0),
        }),
      });
      if (audioBlob?.size && data?.evaluation_id) {
        try {
          await uploadSessionAudio(data.evaluation_id, audioBlob);
        } catch (e) {
          console.warn("PN session audio upload failed", e);
        }
      }
      await window.NarroPnAgent?.afterSessionSaved?.(data?.evaluation_id);
      return data;
    } catch (e) {
      console.warn("PN session save failed", e);
      window.NarroUI?.showNarroBanner?.(e?.message || "通话记录保存失败", {
        variant: "info",
        timeoutMs: 5000,
      });
      return null;
    }
  }

  async function ensureCallSession() {
    if (state.inCall) return true;
    await refreshLlmStatus();
    if (!state.llmOk) {
      setWarn("AI 未配置：请在 .env 设置 DEEPSEEK_API_KEY 后重启服务。");
      return false;
    }
    try {
      await warmupMicrophone();
      await ensureVoices();
      state.inCall = true;
      state.callStartedAt = Date.now();
      state.history = [];
      state.pnSession = {};
      state.introPlayed = false;
      setWarn("");
      setStatus("通话已连接");
      syncToolbar();
      return true;
    } catch (e) {
      setWarn(e?.message || "无法开始通话");
      return false;
    }
  }

  async function enableVoice() {
    const ok = await ensureCallSession();
    if (!ok) return;

    await resumeAudioMix();
    state.voiceOn = true;
    state.keepAlive = true;
    syncToolbar();
    startHealthMonitor();

    if (!state.introPlayed) {
      state.introPlayed = true;
      state.busy = true;
      try {
        await agentRespond(CALL_START, { pushUser: false });
      } finally {
        state.busy = false;
        state.fetchAbort = null;
      }
      return;
    }

    setStatus("正在听你说…");
    setLiveCaption("正在听你说…", true);
    await resumeListening();
  }

  async function disableVoice() {
    state.voiceOn = false;
    state.keepAlive = false;
    state.busy = false;
    clearSilenceTimer();
    clearHintTimer();
    stopHealthMonitor();
    stopTts();
    state.fetchAbort?.abort?.();
    state.fetchAbort = null;
    await pauseListening();
    state.turnCommitted = "";
    state.liveInterim = "";
    state.turnBuffer = "";
    setLiveCaption("");
    if (state.inCall) setStatus("通话进行中");
    syncToolbar();
  }

  async function toggleCall() {
    if (state.endingCall) return;
    if (state.inCall && state.voiceOn) {
      await endCall();
      return;
    }
    await enableVoice();
  }

  async function endCall() {
    if (state.endingCall) return;
    state.endingCall = true;
    try {
      stopTts();
      state.fetchAbort?.abort?.();
      state.fetchAbort = null;
      await waitForSessionIdle();
      flushPendingUserSpeech();

      const audioBlob = await stopPnAudioCapture();
      const snapshot = {
        history: state.history.slice(),
        pnSession: { ...state.pnSession },
        elapsedMs: state.callStartedAt ? Date.now() - state.callStartedAt : 0,
        audioBlob: audioBlob || state.sessionAudioBlob,
      };

      state.inCall = false;
      state.voiceOn = false;
      state.keepAlive = false;
      state.busy = false;
      state.introPlayed = false;
      state.callStartedAt = 0;
      clearSilenceTimer();
      clearHintTimer();
      stopHealthMonitor();
      stopRecognitionInstance(state.speechRec);
      state.speechRec = null;
      state.micStream?.getTracks?.().forEach((t) => t.stop());
      state.micStream = null;
      teardownMixBus();
      state.history = [];
      state.pnSession = {};
      state.sessionAudioBlob = null;
      state.turnCommitted = "";
      state.liveInterim = "";
      state.turnBuffer = "";
      setLiveCaption("");
      setStatus("通话已结束");
      syncToolbar();
      updateAvailability();

      if (meaningfulDialogue(snapshot.history).length) {
        await saveSessionSnapshot(snapshot);
      }
    } finally {
      state.endingCall = false;
    }
  }

  function onTabShown() {
    void refreshLlmStatus();
  }

  function onTabHidden() {
    void endCall();
  }

  $("pnAgentCallBtn")?.addEventListener("click", () => {
    void toggleCall();
  });

  window.NarroPnAgent = {
    ...(window.NarroPnAgent || {}),
    onTabShown,
    onTabHidden,
    endCall,
  };

  updateAvailability();
  void refreshLlmStatus();
})();
