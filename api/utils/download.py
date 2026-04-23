from __future__ import annotations

from pathlib import Path

from yt_dlp import YoutubeDL


def download_video(
    url: str,
    output_dir: str | Path = "downloads/videos",
    output_template: str = "%(title)s.%(ext)s",
    format_selector: str = "bv*+ba/b",
    container: str = "mp4",
    cookies: str | None = None,
) -> Path:
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts: dict[str, object] = {
        "format": format_selector,
        "outtmpl": str(target_dir / output_template),
        "noplaylist": True,
        "merge_output_format": container,
        "restrictfilenames": True,
        "quiet": False,
    }
    if cookies:
        ydl_opts["cookiefile"] = cookies

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded_path = Path(ydl.prepare_filename(info))

    merged_path = downloaded_path.with_suffix(f".{container}")
    if merged_path.exists():
        return merged_path.resolve()

    return downloaded_path.resolve()
