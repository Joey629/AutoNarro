#!/usr/bin/env bash
# Pre-matte PN agent idle video: green screen -> VP9 WebM with alpha.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${SRC:-$ROOT/frontend/static/videos/pn-agent/xiaole-idle.mp4}"
OUT="${OUT:-$ROOT/frontend/static/videos/pn-agent/xiaole-idle.webm}"

# Sampled from source corners/edges; studio green is not pure #00FF00.
KEY_COLOR="${KEY_COLOR:-0x1FF61A}"
SIMILARITY="${SIMILARITY:-0.30}"
BLEND="${BLEND:-0.12}"
CRF="${CRF:-28}"
CPU_USED="${CPU_USED:-2}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found. Install with: brew install ffmpeg" >&2
  exit 1
fi

if [[ ! -f "$SRC" ]]; then
  echo "Source video not found: $SRC" >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT")"

FILTER="colorkey=${KEY_COLOR}:${SIMILARITY}:${BLEND},format=rgba,despill=green,split[a][b];[a]alphaextract,erosion,format=gray[alpha];[b][alpha]alphamerge,format=yuva420p"

echo "Input : $SRC"
echo "Output: $OUT"
echo "Key   : color=${KEY_COLOR} similarity=${SIMILARITY} blend=${BLEND}"

ffmpeg -hide_banner -y -i "$SRC" \
  -filter_complex "$FILTER" \
  -an \
  -c:v libvpx-vp9 \
  -pix_fmt yuva420p \
  -auto-alt-ref 0 \
  -b:v 0 \
  -crf "$CRF" \
  -cpu-used "$CPU_USED" \
  -row-mt 1 \
  "$OUT"

ffprobe -hide_banner -v error -select_streams v:0 \
  -show_entries stream=codec_name,pix_fmt,width,height \
  -of default=noprint_wrappers=1 "$OUT"

echo "Done."
