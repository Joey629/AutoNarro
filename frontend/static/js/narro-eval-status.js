/**
 * Async evaluation polling — uses lightweight GET /api/evaluate/{id}/status.
 */
(function initNarroEvalStatus(global) {
  const NarroAPI = global.NarroAPI;
  if (!NarroAPI?.fetchJson) return;

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

  /**
   * @param {number|string} eid
   * @param {object} hooks
   * @param {(status: object) => void} [hooks.onStatus]
   * @param {(row: object) => void} [hooks.onUpdate]
   * @param {(row: object) => void} [hooks.onDone]
   * @param {(msg: string) => void} [hooks.onFail]
   * @param {() => Promise<object>} [hooks.fetchFullRow] — called when status is terminal
   */
  function beginEvaluationPolling(eid, hooks = {}) {
    stopEvaluationPolling();
    activeEvalPollId = eid;
    const maxMs = 30 * 60 * 1000;
    const start = Date.now();

    const fetchFull =
      hooks.fetchFullRow ||
      (async (id) => NarroAPI.fetchJson(`/api/history/${id}`));

    const tick = async () => {
      if (activeEvalPollId !== eid) return;
      if (Date.now() - start > maxMs) {
        stopEvaluationPolling();
        hooks.onFail?.("评估耗时较长，请稍后在「我的记录」中刷新查看");
        return;
      }
      try {
        const status = await NarroAPI.fetchJson(`/api/evaluate/${eid}/status`);
        hooks.onStatus?.(status);
        if (isEvaluationInProgress(status.status)) {
          hooks.onUpdate?.(status);
          return;
        }
        stopEvaluationPolling();
        const row = await fetchFull(eid);
        hooks.onUpdate?.(row);
        if (status.status === "completed") {
          hooks.onDone?.(row);
          return;
        }
        if (status.status === "failed") {
          hooks.onFail?.(status.status_message || row.status_message || "评估失败", row);
        }
      } catch {
        /* 网络抖动时继续轮询 */
      }
    };

    tick();
    activeEvalPollTimer = setInterval(tick, 1500);
  }

  global.NarroEvalStatus = {
    beginEvaluationPolling,
    stopEvaluationPolling,
    isEvaluationInProgress,
  };
})(window);
