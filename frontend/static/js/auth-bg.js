/**
 * 登录/注册页：Canvas 流体背景（品牌青绿色，持续动画）
 */
(function initAuthGateCanvas() {
  const gate = document.getElementById("authGate");
  const canvas = document.getElementById("authGateCanvas");
  if (!gate || !canvas) return;

  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const blobs = [
    { ax: 0.18, ay: 0.22, rx: 0.42, ry: 0.38, speed: 0.55, phase: 0, color: "rgba(45, 212, 191, 0.55)" },
    { ax: 0.82, ay: 0.18, rx: 0.38, ry: 0.34, speed: 0.48, phase: 1.2, color: "rgba(13, 148, 136, 0.5)" },
    { ax: 0.55, ay: 0.78, rx: 0.45, ry: 0.4, speed: 0.42, phase: 2.4, color: "rgba(94, 234, 212, 0.42)" },
    { ax: 0.28, ay: 0.62, rx: 0.32, ry: 0.28, speed: 0.62, phase: 3.6, color: "rgba(15, 118, 110, 0.38)" },
    { ax: 0.72, ay: 0.55, rx: 0.28, ry: 0.32, speed: 0.5, phase: 4.8, color: "rgba(20, 184, 166, 0.35)" },
  ];

  let raf = 0;
  let t = 0;
  let running = false;

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const w = window.innerWidth;
    const h = window.innerHeight;
    canvas.width = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    canvas.style.width = `${w}px`;
    canvas.style.height = `${h}px`;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function draw() {
    const w = window.innerWidth;
    const h = window.innerHeight;
    t += 0.012;

    const g = ctx.createLinearGradient(0, 0, w, h);
    g.addColorStop(0, "#f0fdfa");
    g.addColorStop(0.45, "#ecfeff");
    g.addColorStop(1, "#f8fafc");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);

    ctx.globalCompositeOperation = "screen";
    for (const b of blobs) {
      const cx = w * (b.ax + Math.sin(t * b.speed + b.phase) * 0.12);
      const cy = h * (b.ay + Math.cos(t * b.speed * 0.85 + b.phase) * 0.1);
      const rx = w * (b.rx + Math.sin(t * 0.35 + b.phase) * 0.06);
      const ry = h * (b.ry + Math.cos(t * 0.4 + b.phase) * 0.05);
      const rad = ctx.createRadialGradient(cx, cy, 0, cx, cy, Math.max(rx, ry));
      rad.addColorStop(0, b.color);
      rad.addColorStop(1, "rgba(255, 255, 255, 0)");
      ctx.fillStyle = rad;
      ctx.beginPath();
      ctx.ellipse(cx, cy, rx, ry, t * 0.15 + b.phase, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalCompositeOperation = "source-over";

    raf = requestAnimationFrame(draw);
  }

  function start() {
    if (running) return;
    running = true;
    resize();
    draw();
    window.addEventListener("resize", resize);
  }

  function stop() {
    running = false;
    cancelAnimationFrame(raf);
    window.removeEventListener("resize", resize);
  }

  function sync() {
    const visible = !gate.classList.contains("hidden");
    if (visible) start();
    else stop();
  }

  const obs = new MutationObserver(sync);
  obs.observe(gate, { attributes: true, attributeFilter: ["class", "aria-hidden"] });
  sync();
})();
