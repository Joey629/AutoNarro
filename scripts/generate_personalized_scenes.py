#!/usr/bin/env python3
"""生成专属绘本场景 SVG（供 LLM 选择的 scene_key）。运行：python scripts/generate_personalized_scenes.py"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "frontend" / "static" / "picturebooks" / "scenes"

PALETTES = {
    "dawn_hill": ("#fecaca", "#fef3c7", "#86efac"),
    "sunny_park": ("#bae6fd", "#fef08a", "#86efac"),
    "rain_cloud": ("#94a3b8", "#cbd5e1", "#86efac"),
    "rainbow_path": ("#bae6fd", "#c4b5fd", "#86efac"),
    "garden_pot": ("#ecfccb", "#bbf7d0", "#a3e635"),
    "sprout_grow": ("#d9f99d", "#bbf7d0", "#4ade80"),
    "moon_lake": ("#312e81", "#1e3a8a", "#60a5fa"),
    "friends_play": ("#fde68a", "#fbcfe8", "#93c5fd"),
    "small_problem": ("#e2e8f0", "#fcd34d", "#94a3b8"),
    "kind_help": ("#fef3c7", "#fda4af", "#86efac"),
    "joyful_end": ("#fef08a", "#fde047", "#f9a8d4"),
    "cozy_home": ("#ffedd5", "#fed7aa", "#fdba74"),
}


def svg(name: str, body: str, c0: str, c1: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{c0}"/>
      <stop offset="100%" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  {body}
</svg>'''


def body_for(name: str) -> str:
    g = '<rect x="0" y="460" width="800" height="140" fill="#4ade80" opacity="0.35"/>'
    if name == "dawn_hill":
        return g + '<circle cx="120" cy="100" r="45" fill="#fb923c" opacity="0.9"/>' + _star_field(6)
    if name == "sunny_park":
        return (
            g
            + '<circle cx="680" cy="90" r="55" fill="#fde047"/>'
            + '<rect x="120" y="320" width="50" height="140" fill="#854d0e"/>'
            + '<circle cx="145" cy="280" r="55" fill="#22c55e"/>'
        )
    if name == "rain_cloud":
        return (
            '<ellipse cx="400" cy="110" rx="200" ry="55" fill="#64748b"/>'
            + _rain_lines()
            + g
        )
    if name == "rainbow_path":
        return _rainbow() + g + '<ellipse cx="400" cy="480" rx="120" ry="30" fill="#38bdf8" opacity="0.4"/>'
    if name == "garden_pot":
        return (
            g
            + '<rect x="320" y="300" width="160" height="100" rx="10" fill="#b45309"/>'
            + '<ellipse cx="400" cy="360" rx="70" ry="22" fill="#78350f"/>'
        )
    if name == "sprout_grow":
        return (
            g
            + '<rect x="330" y="310" width="140" height="90" rx="8" fill="#92400e"/>'
            + '<line x1="400" y1="310" x2="400" y2="200" stroke="#16a34a" stroke-width="8"/>'
            + '<ellipse cx="385" cy="215" rx="20" ry="11" fill="#4ade80"/>'
            + '<ellipse cx="415" cy="215" rx="20" ry="11" fill="#4ade80"/>'
        )
    if name == "moon_lake":
        return (
            '<circle cx="400" cy="160" r="65" fill="#fef08a"/>'
            + '<ellipse cx="400" cy="420" rx="300" ry="70" fill="#1d4ed8" opacity="0.45"/>'
            + '<circle cx="400" cy="420" r="45" fill="#fef9c3" opacity="0.6"/>'
        )
    if name == "friends_play":
        return (
            g
            + _blob(280, 380, "#fdba74")
            + _blob(400, 370, "#93c5fd")
            + _blob(520, 385, "#f9a8d4")
        )
    if name == "small_problem":
        return g + '<path d="M350 200 L450 200 L400 280 Z" fill="#fbbf24" stroke="#b45309" stroke-width="3"/>'
    if name == "kind_help":
        return g + _blob(320, 360, "#fda4af") + _blob(480, 360, "#86efac") + '<path d="M380 300 Q400 260 420 300" stroke="#e11d48" stroke-width="4" fill="none"/>'
    if name == "joyful_end":
        return g + _star_field(10) + '<circle cx="400" cy="320" r="50" fill="#fde047"/>'
    if name == "cozy_home":
        return (
            g
            + '<rect x="280" y="280" width="240" height="160" fill="#fdba74"/>'
            + '<polygon points="280,280 400,200 520,280" fill="#ef4444"/>'
            + '<rect x="360" y="360" width="80" height="80" fill="#fef3c7"/>'
        )
    return g + '<circle cx="400" cy="300" r="40" fill="#2ec492"/>'


def _star_field(n: int) -> str:
    import random

    rng = random.Random(7)
    parts = []
    for _ in range(n):
        x, y = rng.randint(50, 750), rng.randint(40, 250)
        parts.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#fde68a"/>')
    return "".join(parts)


def _rain_lines() -> str:
    return "".join(
        f'<line x1="{x}" y1="170" x2="{x-10}" y2="420" stroke="#60a5fa" stroke-width="2" opacity="0.55"/>'
        for x in range(100, 700, 40)
    )


def _rainbow() -> str:
    colors = ["#ef4444", "#f97316", "#eab308", "#22c55e", "#3b82f6", "#8b5cf6"]
    return "".join(
        f'<path d="M150 400 Q400 220 650 400" fill="none" stroke="{c}" stroke-width="10" opacity="0.75"/>'
        for c in colors
    )


def _blob(cx: int, cy: int, color: str) -> str:
    return f'<ellipse cx="{cx}" cy="{cy}" rx="45" ry="50" fill="{color}"/>'


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (c0, c1, _c2) in PALETTES.items():
        path = OUT / f"{name}.svg"
        path.write_text(svg(name, body_for(name), c0, c1).strip() + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
