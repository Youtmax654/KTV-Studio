from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import torchaudio
import whisperx

if not hasattr(torchaudio, "list_audio_backends"):
    torchaudio.list_audio_backends = lambda: [""]  # type: ignore[attr-defined]

from config.safe_globals import setup_torch_safe_globals

setup_torch_safe_globals()


def transcribe_lyrics(
    audio_file: str | Path,
    output_dir: str | Path,
    model_name: str = "large-v2",
    device: str = "cpu",
    batch_size: int = 16,
    compute_type: str = "int8",
) -> Path:
    audio_path = Path(audio_file)
    if not audio_path.exists():
        raise FileNotFoundError(f"Input audio not found: {audio_path}")

    target_dir = Path(output_dir)
    song_dir = target_dir
    song_dir.mkdir(parents=True, exist_ok=True)
    output_path = song_dir / "lyrics.json"

    print("Loading audio...")
    audio = whisperx.load_audio(str(audio_path))

    print("Loading WhisperX model...")
    model = whisperx.load_model(
        model_name,
        device,
        compute_type=compute_type,
    )

    print("Transcribing...")
    result: dict[str, Any] = model.transcribe(audio, batch_size=batch_size)

    print(f"Detected language: {result['language']}")
    model_align, metadata = whisperx.load_align_model(
        language_code=result["language"],
        device=device,
    )

    aligned_result = whisperx.align(
        result["segments"],
        model_align,
        metadata,
        audio,
        device,
        return_char_alignments=True,
    )

    payload = {
        "audio_file": str(audio_path.resolve()),
        "language": result["language"],
        "segments": aligned_result["segments"],
    }

    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Lyrics exported: {output_path.resolve()}")
    return output_path.resolve()
