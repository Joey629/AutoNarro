#!/usr/bin/env python3
"""生成绘本学习原创插画 SVG（与 MAIN 图卡无关）。运行：python scripts/generate_picturebook_svgs.py"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "frontend" / "static" / "picturebooks"

def _wrap(body: str, bg: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">{bg}</linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  {body}
</svg>'''


def _sky_night(stars: int, highlight: str | None) -> str:
    bg = '<stop offset="0%" stop-color="#1e3a5f"/><stop offset="100%" stop-color="#0f172a"/>'
    parts = [
        '<circle cx="620" cy="90" r="55" fill="#fef9c3" opacity="0.95"/>',
        '<circle cx="600" cy="78" r="48" fill="#1e3a5f"/>',
    ]
    import random

    rng = random.Random(42 + stars)
    for i in range(stars):
        x, y = rng.randint(40, 760), rng.randint(40, 320)
        r = rng.choice([2, 2.5, 3])
        parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fde68a" opacity="0.9"/>')
    if highlight == "moon":
        parts.append(
            '<path d="M120 420 Q200 360 280 420 T440 420" stroke="#94a3b8" stroke-width="3" fill="none" opacity="0.6"/>'
        )
        parts.append('<text x="400" y="200" text-anchor="middle" font-size="28" fill="#e2e8f0" font-family="sans-serif">← 银河</text>')
    if highlight == "roofs":
        parts.append('<rect x="80" y="380" width="120" height="70" rx="6" fill="#334155"/>')
        parts.append('<polygon points="80,380 140,320 200,380" fill="#475569"/>')
        parts.append('<rect x="280" y="400" width="100" height="50" rx="4" fill="#334155"/>')
    if highlight in ("home", "family"):
        for i in range(6 if highlight == "family" else 4):
            cx = 320 + i * 45
            parts.append(f'<circle cx="{cx}" cy="180" r="8" fill="#fbbf24"/>')
        parts.append('<ellipse cx="400" cy="250" rx="120" ry="40" fill="#38bdf8" opacity="0.25"/>')
    hero = '<circle cx="400" cy="300" r="28" fill="#fde047" stroke="#f59e0b" stroke-width="3"/>'
    hero += '<circle cx="392" cy="294" r="4" fill="#1e293b"/><circle cx="408" cy="294" r="4" fill="#1e293b"/>'
    parts.append(hero)
    return _wrap("\n  ".join(parts), bg)


def _rain_scene(kind: str) -> str:
    bg = '<stop offset="0%" stop-color="#cbd5e1"/><stop offset="100%" stop-color="#94a3b8"/>'
    parts = ['<rect x="0" y="420" width="800" height="180" fill="#86efac" opacity="0.5"/>']
    if kind in ("cloud", "umbrella", "rainbow"):
        parts.append('<ellipse cx="400" cy="120" rx="180" ry="60" fill="#64748b"/>')
        parts.append('<ellipse cx="300" cy="100" rx="100" ry="45" fill="#64748b"/>')
        parts.append('<ellipse cx="500" cy="105" rx="110" ry="50" fill="#64748b"/>')
    if kind in ("cloud", "umbrella"):
        for x in range(60, 760, 35):
            parts.append(f'<line x1="{x}" y1="180" x2="{x-8}" y2="400" stroke="#60a5fa" stroke-width="2" opacity="0.5"/>')
    if kind == "umbrella":
        parts.append('<path d="M350 280 Q400 220 450 280 L450 380 L350 380Z" fill="#ef4444"/>')
        parts.append('<line x1="400" y1="280" x2="400" y2="420" stroke="#78350f" stroke-width="4"/>')
        parts.append('<ellipse cx="480" cy="400" rx="25" ry="15" fill="#a3e635"/>')
    if kind == "rainbow":
        for i, c in enumerate(["#ef4444", "#f97316", "#eab308", "#22c55e", "#3b82f6", "#8b5cf6"]):
            parts.append(
                f'<path d="M200 380 Q400 {280-i*12} 600 380" fill="none" stroke="{c}" stroke-width="8" opacity="0.7"/>'
            )
        parts.append('<ellipse cx="520" cy="430" rx="30" ry="18" fill="#84cc16" opacity="0.8"/>')
    if kind == "sun":
        bg = '<stop offset="0%" stop-color="#7dd3fc"/><stop offset="100%" stop-color="#bae6fd"/>'
        parts.append('<circle cx="650" cy="100" r="50" fill="#fde047"/>')
        parts.append('<path d="M350 300 Q400 250 450 300 L450 400 L350 400Z" fill="#ef4444" opacity="0.9"/>')
    if kind == "bench":
        bg = '<stop offset="0%" stop-color="#bae6fd"/><stop offset="100%" stop-color="#fef3c7"/>'
        parts.append('<rect x="280" y="360" width="240" height="20" rx="4" fill="#92400e"/>')
        parts.append('<rect x="300" y="380" width="16" height="60" fill="#78350f"/>')
        parts.append('<rect x="484" y="380" width="16" height="60" fill="#78350f"/>')
        parts.append('<path d="M300 200 Q400 120 500 200" fill="none" stroke="#a855f7" stroke-width="10" opacity="0.35"/>')
    return _wrap("\n  ".join(parts), bg)


def _garden_scene(kind: str) -> str:
    bg = '<stop offset="0%" stop-color="#ecfccb"/><stop offset="100%" stop-color="#bbf7d0"/>'
    parts = [
        '<rect x="0" y="450" width="800" height="150" fill="#a3e635" opacity="0.4"/>',
        '<rect x="300" y="320" width="200" height="130" rx="12" fill="#b45309"/>',
        '<rect x="310" y="300" width="180" height="30" rx="8" fill="#92400e"/>',
    ]
    if kind == "pot":
        parts.append('<ellipse cx="400" cy="380" rx="70" ry="25" fill="#78350f"/>')
        parts.append('<circle cx="400" cy="365" r="12" fill="#854d0e"/>')
    if kind == "water":
        parts.append('<path d="M520 260 Q540 220 560 260" stroke="#0ea5e9" stroke-width="4" fill="none"/>')
        parts.append('<ellipse cx="400" cy="375" rx="60" ry="18" fill="#57534e" opacity="0.5"/>')
    if kind in ("sprout", "grow", "wave"):
        h = 40 if kind == "sprout" else 90 if kind == "grow" else 110
        parts.append(f'<line x1="400" y1="380" x2="400" y2="{380-h}" stroke="#16a34a" stroke-width="6"/>')
        parts.append(f'<ellipse cx="385" cy="{380-h+15}" rx="18" ry="10" fill="#4ade80" transform="rotate(-30 385 {380-h+15})"/>')
        parts.append(f'<ellipse cx="415" cy="{380-h+15}" rx="18" ry="10" fill="#4ade80" transform="rotate(30 415 {380-h+15})"/>')
    if kind == "grow":
        parts.append('<ellipse cx="400" cy="250" rx="22" ry="14" fill="#22c55e"/>')
    if kind == "wave":
        parts.append('<circle cx="320" cy="200" r="35" fill="#fdba74" opacity="0.9"/>')
        parts.append('<path d="M300 195 Q320 175 340 195" stroke="#1e293b" stroke-width="2" fill="none"/>')
    return _wrap("\n  ".join(parts), bg)


def _lake_scene(kind: str) -> str:
    bg = '<stop offset="0%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#312e81"/>'
    parts = ['<ellipse cx="400" cy="420" rx="360" ry="80" fill="#1d4ed8" opacity="0.5"/>']
    if kind == "mirror":
        parts.append('<circle cx="400" cy="200" r="70" fill="#fef08a" opacity="0.95"/>')
        parts.append('<circle cx="400" cy="420" r="50" fill="#fef9c3" opacity="0.7"/>')
    if kind in ("boat", "firefly", "lily"):
        parts.append('<path d="M280 400 Q400 340 520 400 L500 430 L300 430Z" fill="#e2e8f0" opacity="0.9"/>')
        parts.append('<circle cx="400" cy="360" r="35" fill="#fef08a"/>')
    if kind == "firefly":
        for x, y in [(200, 280), (600, 300), (350, 250)]:
            parts.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#a3e635"/>')
            parts.append(f'<circle cx="{x}" cy="{y}" r="14" fill="#a3e635" opacity="0.25"/>')
    if kind == "lily":
        parts.append('<ellipse cx="250" cy="410" rx="40" ry="20" fill="#4ade80"/>')
        parts.append('<ellipse cx="550" cy="405" rx="35" ry="18" fill="#4ade80"/>')
        parts.append('<circle cx="270" cy="395" r="8" fill="#86efac"/>')
    if kind == "gift":
        bg = '<stop offset="0%" stop-color="#fef9c3"/><stop offset="100%" stop-color="#fde68a"/>'
        parts = ['<rect x="320" y="200" width="160" height="120" rx="8" fill="#fff" stroke="#cbd5e1"/>']
        parts.append('<path d="M360 280 Q400 220 440 280" fill="none" stroke="#94a3b8" stroke-width="2"/>')
        parts.append('<ellipse cx="400" cy="360" rx="50" ry="28" fill="#fef08a" opacity="0.8"/>')
    return _wrap("\n  ".join(parts), bg)


def _all_scenes() -> dict[str, list[str]]:
    return {
        "star-path": [
            _sky_night(stars=3, highlight=None),
            _sky_night(stars=5, highlight="moon"),
            _sky_night(stars=4, highlight="roofs"),
            _sky_night(stars=8, highlight="home"),
            _sky_night(stars=12, highlight="family"),
        ],
        "rain-umbrella": [
            _rain_scene("cloud"),
            _rain_scene("umbrella"),
            _rain_scene("rainbow"),
            _rain_scene("sun"),
            _rain_scene("bench"),
        ],
        "seed-sprout": [
            _garden_scene("pot"),
            _garden_scene("water"),
            _garden_scene("sprout"),
            _garden_scene("grow"),
            _garden_scene("wave"),
        ],
        "moon-boat": [
            _lake_scene("mirror"),
            _lake_scene("boat"),
            _lake_scene("firefly"),
            _lake_scene("lily"),
            _lake_scene("gift"),
        ],
    }


def main() -> None:
    for book_id, pages in _all_scenes().items():
        book_dir = OUT / book_id
        book_dir.mkdir(parents=True, exist_ok=True)
        for i, svg in enumerate(pages, start=1):
            path = book_dir / f"{i:02d}.svg"
            path.write_text(svg.strip() + "\n", encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
