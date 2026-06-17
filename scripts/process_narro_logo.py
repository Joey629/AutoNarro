#!/usr/bin/env python3
"""Remove near-white background from Narro logo PNGs and crop to content."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
LOGO = ROOT / "frontend/static/images/narro-logo.png"
ICON = ROOT / "frontend/static/images/narro-icon.png"


def remove_white_background(im: Image.Image, threshold: int = 230, edge_softness: int = 20) -> Image.Image:
    im = im.convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
    dist = np.minimum(np.minimum(255 - r, 255 - g), 255 - b)
    bg_cut = 255 - threshold
    new_a = np.clip((dist - bg_cut) / edge_softness * 255.0, 0, 255)
    new_a = np.minimum(new_a, a)
    new_a = np.where(dist > bg_cut + edge_softness, 255, new_a)
    out = np.stack([r, g, b, new_a], axis=-1).astype(np.uint8)
    return Image.fromarray(out)


def crop_to_content(im: Image.Image, pad: int = 8) -> Image.Image:
    bbox = im.getbbox()
    if not bbox:
        return im
    l, t, r, b = bbox
    w, h = im.size
    return im.crop((max(0, l - pad), max(0, t - pad), min(w, r + pad), min(h, b + pad)))


def icon_from_logo(logo: Image.Image, size: int = 128) -> Image.Image:
    w, h = logo.size
    side = min(w, h)
    return logo.crop((0, 0, side, h)).resize((size, size), Image.Resampling.LANCZOS)


def main() -> None:
    raw = Image.open(LOGO)
    logo = crop_to_content(remove_white_background(raw))
    logo.save(LOGO, optimize=True)
    icon_from_logo(logo).save(ICON, optimize=True)
    print(f"logo: {raw.size} -> {logo.size}")
    print(f"icon: saved to {ICON} (128px square from logo left)")


if __name__ == "__main__":
    main()
