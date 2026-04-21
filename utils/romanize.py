from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Callable

from pykakasi import kakasi
from pypinyin import Style, lazy_pinyin

_JP_KAKASI = kakasi()


def _normalize_spacing(text: str) -> str:
    collapsed = re.sub(r"\s+", " ", text).strip()
    collapsed = re.sub(r"\s+([.,!?;:)\]})])", r"\1", collapsed)
    collapsed = re.sub(r"([([\{])\s+", r"\1", collapsed)
    return collapsed


def _romanize_japanese_text(text: str) -> str:
    converted = _JP_KAKASI.convert(text)
    parts: list[str] = []
    for item in converted:
        hepburn = item.get("hepburn", "")
        parts.append(hepburn if hepburn else item.get("orig", ""))
    return _normalize_spacing(" ".join(parts))


def _romanize_chinese_text(text: str) -> str:
    tokens = lazy_pinyin(text, style=Style.NORMAL, errors=lambda item: [item])
    return _normalize_spacing(" ".join(tokens))


def _romanize_segment(
    segment: dict[str, Any], romanize_text: Callable[[str], str]
) -> dict[str, Any]:
    updated = dict(segment)

    text_value = updated.get("text")
    if isinstance(text_value, str):
        updated["text_romanized"] = romanize_text(text_value)

    word_value = updated.get("word")
    if isinstance(word_value, str):
        updated["romanized"] = romanize_text(word_value)

    char_value = updated.get("char")
    if isinstance(char_value, str):
        updated["romanized"] = romanize_text(char_value)

    for nested_key in ("words", "chars"):
        nested = updated.get(nested_key)
        if isinstance(nested, list):
            new_nested: list[Any] = []
            for item in nested:
                if isinstance(item, dict):
                    new_nested.append(_romanize_segment(item, romanize_text))
                else:
                    new_nested.append(item)
            updated[nested_key] = new_nested

    return updated


def _romanize_json(
    lyrics_json_path: str | Path,
    language_tag: str,
    romanize_text: Callable[[str], str],
) -> Path:
    source = Path(lyrics_json_path)
    if not source.exists():
        raise FileNotFoundError(f"Lyrics json not found: {source}")

    payload = json.loads(source.read_text(encoding="utf-8"))
    segments = payload.get("segments", [])
    if not isinstance(segments, list):
        raise ValueError("Invalid lyrics json format: 'segments' must be a list")

    romanized_payload = dict(payload)
    romanized_payload["segments"] = [
        _romanize_segment(segment, romanize_text)
        if isinstance(segment, dict)
        else segment
        for segment in segments
    ]
    romanized_payload["romanized_from"] = str(source.resolve())
    romanized_payload["romanization"] = language_tag

    source.write_text(
        json.dumps(romanized_payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return source.resolve()


def romanize_japanese_lyrics_json(lyrics_json_path: str | Path) -> Path:
    return _romanize_json(
        lyrics_json_path=lyrics_json_path,
        language_tag="jp",
        romanize_text=_romanize_japanese_text,
    )


def romanize_chinese_lyrics_json(lyrics_json_path: str | Path) -> Path:
    return _romanize_json(
        lyrics_json_path=lyrics_json_path,
        language_tag="zh",
        romanize_text=_romanize_chinese_text,
    )


def romanize_lyrics_for_supported_language(lyrics_json_path: str | Path) -> Path | None:
    source = Path(lyrics_json_path)
    payload = json.loads(source.read_text(encoding="utf-8"))
    language = str(payload.get("language", "")).lower()

    if language.startswith("ja"):
        return romanize_japanese_lyrics_json(source)
    if language.startswith("zh"):
        return romanize_chinese_lyrics_json(source)
    return None
