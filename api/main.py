#!/usr/bin/env python3
"""Pipeline principal: téléchargement, extraction audio, séparation Demucs."""

from __future__ import annotations

import argparse
from pathlib import Path

from utils import (
    download_video,
    extract_audio,
    romanize_lyrics_for_supported_language,
    separate_stems,
    transcribe_lyrics,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Télécharge une vidéo YouTube, extrait l'audio, puis sépare voix/instru."
    )
    parser.add_argument("url", help="URL YouTube")
    parser.add_argument(
        "--downloads-dir",
        default="downloads",
        help="Dossier racine de sortie (default: downloads)",
    )
    parser.add_argument(
        "--model",
        default="htdemucs",
        help="Modèle Demucs (default: htdemucs)",
    )
    parser.add_argument(
        "--device",
        choices=("cpu", "cuda"),
        default="cpu",
        help="Device Demucs (default: cpu)",
    )
    parser.add_argument(
        "--mp3",
        action="store_true",
        help="Exporter les stems en mp3 au lieu de wav",
    )
    parser.add_argument(
        "--cookies",
        help="Chemin optionnel vers cookies.txt pour yt-dlp",
    )
    parser.add_argument(
        "--lyrics-model",
        default="large-v2",
        help="Modèle WhisperX pour la transcription (default: large-v2)",
    )
    parser.add_argument(
        "--lyrics-batch-size",
        type=int,
        default=16,
        help="Batch size WhisperX (default: 16)",
    )
    parser.add_argument(
        "--lyrics-compute-type",
        default="int8",
        help="compute_type WhisperX (default: int8)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    downloads_dir = Path(args.downloads_dir)

    print("[1/4] Téléchargement de la vidéo...")
    video_path = download_video(
        url=args.url,
        output_dir=downloads_dir,
        output_template="%(title)s/video.%(ext)s",
        cookies=args.cookies,
    )
    song_dir = video_path.parent
    print(f"Vidéo: {video_path}")
    print(f"Dossier morceau: {song_dir}")

    print("[2/4] Extraction de l'audio...")
    audio_path = extract_audio(
        video_path=video_path,
        output_path=song_dir / "song.wav",
    )
    print(f"Audio: {audio_path}")

    print("[3/4] Séparation Demucs...")
    track_dir, vocals_path, instrumental_path = separate_stems(
        audio_path=audio_path,
        output_dir=song_dir / "separated",
        model=args.model,
        device=args.device,
        two_stems="vocals",
        mp3=args.mp3,
    )

    print("[4/4] Transcription des paroles...")
    # lyrics_source = audio_path
    lyrics_source = vocals_path if vocals_path.exists() else audio_path
    lyrics_path = transcribe_lyrics(
        audio_file=lyrics_source,
        output_dir=song_dir,
        model_name=args.lyrics_model,
        device=args.device,
        batch_size=args.lyrics_batch_size,
        compute_type=args.lyrics_compute_type,
    )

    romanized_path = romanize_lyrics_for_supported_language(lyrics_path)

    print(f"Sortie Demucs: {track_dir}")
    print(f"Voix: {vocals_path}")
    print(f"Instru: {instrumental_path}")
    print(f"Paroles JSON: {lyrics_path}")
    if romanized_path is not None:
        print(f"Paroles romanisees JSON: {romanized_path}")
    else:
        print("Paroles romanisees JSON: non generees (langue non supportee)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
