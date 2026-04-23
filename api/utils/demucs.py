from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def separate_stems(
    audio_path: str | Path,
    output_dir: str | Path,
    model: str = "htdemucs",
    device: str = "cpu",
    two_stems: str = "vocals",
    mp3: bool = False,
) -> tuple[Path, Path, Path]:
    source = Path(audio_path)
    if not source.exists():
        raise FileNotFoundError(f"Input audio not found: {source}")

    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    command = [
        sys.executable,
        "-m",
        "demucs.separate",
        "-n",
        model,
        "--device",
        device,
        "--two-stems",
        two_stems,
        "-o",
        str(target_dir),
    ]
    if mp3:
        command.append("--mp3")
    command.append(str(source))

    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        raise RuntimeError("Demucs separation failed")

    track_dir = (target_dir / model / source.stem).resolve()
    ext = "mp3" if mp3 else "wav"
    vocals_path = track_dir / f"vocals.{ext}"
    no_vocals_path = track_dir / f"no_vocals.{ext}"
    return track_dir, vocals_path, no_vocals_path
