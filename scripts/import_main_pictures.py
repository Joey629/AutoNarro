#!/usr/bin/env python3
"""从 MAIN_pictures_Standard.pdf 切分四则故事图卡并写入 frontend/static/stories/。"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "frontend" / "static" / "stories"
CONFIG = ROOT / "configs" / "story_stimuli.json"
STORIES = ("cat", "dog", "bird", "goat")


def split_page(img_path: Path, out_dir: Path, prefix: str) -> int:
    from PIL import Image
    import numpy as np

    im = Image.open(img_path).convert("RGB")
    gray = np.array(im).mean(axis=2)

    def find_segments(proj, min_len=100):
        segments = []
        in_content = False
        start = 0
        for i, v in enumerate(proj):
            is_gap = v > 0.92
            if not is_gap and not in_content:
                start = i
                in_content = True
            elif is_gap and in_content:
                if i - start >= min_len:
                    segments.append((start, i))
                in_content = False
        if in_content and len(proj) - start >= min_len:
            segments.append((start, len(proj)))
        return segments

    rows = find_segments((gray > 245).mean(axis=1))
    cols = find_segments((gray > 245).mean(axis=0))
    out_dir.mkdir(parents=True, exist_ok=True)
    idx = 1
    for r0, r1 in rows:
        for c0, c1 in cols:
            crop = im.crop((c0, r0, c1, r1))
            if crop.width < 150 or crop.height < 150:
                continue
            crop.save(out_dir / f"panel-{idx:02d}.jpg", quality=92)
            idx += 1
    return idx - 1


def main() -> int:
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Downloads" / "MAIN_pictures_Standard.pdf"
    if not pdf.is_file():
        print(f"找不到 PDF: {pdf}", file=sys.stderr)
        return 1

    try:
        import subprocess
        tmp = Path("/tmp/narro_main_pages")
        tmp.mkdir(exist_ok=True)
        subprocess.run(
            ["pdftoppm", "-png", "-r", "200", str(pdf), str(tmp / "page")],
            check=True,
        )
    except Exception as e:
        print(f"需要 pdftoppm: {e}", file=sys.stderr)
        return 1

    pages = sorted(tmp.glob("page-*.png"), key=lambda p: int(re.search(r"(\d+)", p.name).group(1)))
    if len(pages) < 4:
        print("PDF 页数不足 4", file=sys.stderr)
        return 1

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    for story, page in zip(STORIES, pages[:4]):
        n = split_page(page, OUT / story, story)
        panels = cfg["stories"][story]["panels"]
        for i in range(min(n, len(panels))):
            panels[i]["image"] = f"/static/stories/{story}/panel-{i + 1:02d}.jpg"
        print(f"{story}: {n} panels -> {OUT / story}")

    CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    static_cfg = ROOT / "frontend" / "static" / "story_stimuli.json"
    static_cfg.write_text(CONFIG.read_text(encoding="utf-8"), encoding="utf-8")
    print("已更新", CONFIG, "与", static_cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
