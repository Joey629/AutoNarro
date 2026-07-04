"""火山引擎豆包语音合成（TTS）。"""
from __future__ import annotations

import base64
import json
import os
import re
import uuid
import urllib.error
import urllib.request
from typing import Optional

from logging_config import setup_logging

logger = setup_logging()

VOLC_TTS_V1_URL = "https://openspeech.bytedance.com/api/v1/tts"
VOLC_TTS_V3_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
_API_KEY_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.IGNORECASE,
)

# BV051（灿灿童声）在新版 API Key 鉴权下走大模型音色
VOICE_ALIASES = {
    "BV051_streaming": "zh_female_cancan_mars_bigtts",
    "BV051": "zh_female_cancan_mars_bigtts",
}


def _app_id() -> str:
    return os.environ.get("VOLC_TTS_APP_ID", "").strip()


def _access_token() -> str:
    return os.environ.get("VOLC_TTS_ACCESS_TOKEN", "").strip()


def _api_key() -> str:
    explicit = os.environ.get("VOLC_TTS_API_KEY", "").strip()
    if explicit:
        return explicit
    token = _access_token()
    return token if _API_KEY_RE.match(token) else ""


def _voice_type() -> str:
    return os.environ.get("VOLC_TTS_VOICE", "BV051_streaming").strip() or "BV051_streaming"


def _cluster() -> str:
    return os.environ.get("VOLC_TTS_CLUSTER", "volcano_tts").strip() or "volcano_tts"


def _resource_id() -> str:
    return os.environ.get("VOLC_TTS_RESOURCE_ID", "seed-tts-1.0").strip() or "seed-tts-1.0"


def _resolve_voice(voice_type: Optional[str] = None) -> str:
    voice = (voice_type or _voice_type()).strip()
    return VOICE_ALIASES.get(voice, voice)


def _uses_api_key() -> bool:
    return bool(_api_key())


def is_volc_tts_available() -> bool:
    if _uses_api_key():
        return True
    return bool(_app_id() and _access_token())


def volc_tts_config() -> dict:
    return {
        "available": is_volc_tts_available(),
        "voice": _voice_type(),
        "provider": "volcengine",
        "auth": "api_key" if _uses_api_key() else "app_token",
    }


def _normalize_text(text: str) -> str:
    msg = (text or "").strip()
    if not msg:
        raise ValueError("合成文本为空")
    if len(msg.encode("utf-8")) > 900:
        msg = msg[:300]
    return msg


def _speed_to_speech_rate(speed_ratio: float) -> int:
    ratio = max(0.5, min(2.0, float(speed_ratio)))
    return int(round((ratio - 1.0) * 100))


def _synthesize_v3(
    msg: str,
    *,
    voice_type: Optional[str],
    speed_ratio: float,
    encoding: str,
) -> tuple[bytes, str]:
    api_key = _api_key()
    if not api_key:
        raise RuntimeError("未配置 VOLC_TTS_API_KEY")

    body = {
        "user": {"uid": "narro_pn_agent"},
        "req_params": {
            "text": msg,
            "speaker": _resolve_voice(voice_type),
            "audio_params": {
                "format": encoding,
                "sample_rate": 24000,
                "speech_rate": _speed_to_speech_rate(speed_ratio),
                "loudness_rate": 0,
            },
        },
    }
    req = urllib.request.Request(
        VOLC_TTS_V3_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-Api-Key": api_key,
            "X-Api-Resource-Id": _resource_id(),
            "X-Api-Request-Id": str(uuid.uuid4()),
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:500]
        logger.warning("volc tts v3 http error: %s %s", e.code, detail)
        raise RuntimeError(f"豆包语音请求失败 ({e.code})") from e
    except urllib.error.URLError as e:
        raise RuntimeError("豆包语音网络不可达") from e

    audio = bytearray()
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        code = payload.get("code")
        if code in (20000000, "20000000"):
            continue
        if code not in (0, "0", 3000, "3000"):
            message = payload.get("message") or payload.get("msg") or "合成失败"
            raise RuntimeError(f"豆包语音：{message}")
        chunk = payload.get("data")
        if isinstance(chunk, str) and chunk:
            audio.extend(base64.b64decode(chunk))

    if not audio:
        raise RuntimeError("豆包语音音频为空")

    mime = "audio/mpeg" if encoding == "mp3" else f"audio/{encoding}"
    return bytes(audio), mime


def _synthesize_v1(
    msg: str,
    *,
    voice_type: Optional[str],
    speed_ratio: float,
    pitch_ratio: float,
    encoding: str,
) -> tuple[bytes, str]:
    app_id = _app_id()
    token = _access_token()
    if not app_id or not token:
        raise RuntimeError("未配置 VOLC_TTS_APP_ID / VOLC_TTS_ACCESS_TOKEN")

    body = {
        "app": {
            "appid": app_id,
            "token": token,
            "cluster": _cluster(),
        },
        "user": {"uid": "narro_pn_agent"},
        "audio": {
            "voice_type": _resolve_voice(voice_type),
            "encoding": encoding,
            "speed_ratio": max(0.5, min(2.0, float(speed_ratio))),
            "volume_ratio": 1.0,
            "pitch_ratio": max(0.5, min(2.0, float(pitch_ratio))),
        },
        "request": {
            "reqid": str(uuid.uuid4()),
            "text": msg,
            "text_type": "plain",
            "operation": "query",
        },
    }
    req = urllib.request.Request(
        VOLC_TTS_V1_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer;{token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:500]
        logger.warning("volc tts v1 http error: %s %s", e.code, detail)
        raise RuntimeError(f"豆包语音请求失败 ({e.code})") from e
    except urllib.error.URLError as e:
        raise RuntimeError("豆包语音网络不可达") from e

    code = payload.get("code")
    if code not in (3000, "3000", 0, "0"):
        message = payload.get("message") or payload.get("msg") or "合成失败"
        raise RuntimeError(f"豆包语音：{message}")

    data = payload.get("data")
    if not data:
        raise RuntimeError("豆包语音未返回音频数据")

    if isinstance(data, str):
        audio = base64.b64decode(data)
    elif isinstance(data, dict):
        b64 = data.get("audio") or data.get("data") or ""
        audio = base64.b64decode(b64) if b64 else b""
    else:
        audio = b""

    if not audio:
        raise RuntimeError("豆包语音音频为空")

    mime = "audio/mpeg" if encoding == "mp3" else f"audio/{encoding}"
    return audio, mime


def synthesize_speech(
    text: str,
    *,
    voice_type: Optional[str] = None,
    speed_ratio: float = 1.0,
    pitch_ratio: float = 1.0,
    encoding: str = "mp3",
) -> tuple[bytes, str]:
    """合成语音，返回 (音频字节, mime_type)。"""
    msg = _normalize_text(text)
    if _uses_api_key():
        return _synthesize_v3(
            msg,
            voice_type=voice_type,
            speed_ratio=speed_ratio,
            encoding=encoding,
        )
    return _synthesize_v1(
        msg,
        voice_type=voice_type,
        speed_ratio=speed_ratio,
        pitch_ratio=pitch_ratio,
        encoding=encoding,
    )
