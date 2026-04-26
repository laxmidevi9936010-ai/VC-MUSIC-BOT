"""
YouTube search & download helper
"""
import os
import asyncio
import yt_dlp
from youtubesearchpython.__future__ import VideosSearch

DOWNLOADS = "downloads"
os.makedirs(DOWNLOADS, exist_ok=True)


async def search_youtube(query: str):
    """Search YouTube and return first result info"""
    search = VideosSearch(query, limit=1)
    result = (await search.next())["result"]
    if not result:
        return None
    v = result[0]
    return {
        "title": v["title"],
        "duration": v.get("duration", "0:00"),
        "thumbnail": v["thumbnails"][0]["url"].split("?")[0],
        "link": v["link"],
        "channel": v["channel"]["name"],
        "views": v.get("viewCount", {}).get("text", "N/A"),
        "id": v["id"],
    }


async def download_audio(video_url: str) -> str:
    """Download audio from YouTube and return file path"""
    loop = asyncio.get_event_loop()

    def _dl():
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{DOWNLOADS}/%(id)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            return f"{DOWNLOADS}/{info['id']}.mp3"

    return await loop.run_in_executor(None, _dl)


def duration_to_seconds(duration: str) -> int:
    """Convert '3:45' or '1:23:45' -> seconds"""
    try:
        parts = list(map(int, duration.split(":")))
        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        elif len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
    except Exception:
        return 0
    return 0
