from __future__ import annotations

import subprocess
from pathlib import Path


def extract_audio(
    video_path: str | Path,
    output_path: str | Path | None = None,
    codec: str = "pcm_s16le",
    sample_rate: int = 44100,
    channels: int = 2,
) -> Path:
    source = Path(video_path)
    if not source.exists():
        raise FileNotFoundError(f"Input video not found: {source}")

    if output_path is None:
        target = Path("downloads/audio") / f"{source.stem}.wav"
    else:
        target = Path(output_path)

    target.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(source),
        "-vn",
        "-acodec",
        codec,
        "-ar",
        str(sample_rate),
        "-ac",
        str(channels),
        str(target),
    ]

    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        raise RuntimeError("ffmpeg failed while extracting audio")

    return target.resolve()
