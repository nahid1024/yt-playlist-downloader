import yt_dlp
import os

# ==== CONFIGURATION ====
VIDEO_URL = "https://www.youtube.com/playlist?list=PLNEimsLEIzwBrPc5mrUWAyjZ_f_pP8Nd9"  # replace with your URL
COOKIES_FILE = "cookies.txt"  # make sure this file exists and is in Netscape format
OUTPUT_TEMPLATE = "%(playlist_index)02d - %(title)s.%(ext)s"
MAX_HEIGHT = 720
# =======================

ydl_opts = {
    "cookies": COOKIES_FILE,
    "format": f"bestvideo[height<={MAX_HEIGHT}][vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[height<={MAX_HEIGHT}][vcodec^=avc1]",
    "playlist_items": "13-",
    "merge_output_format": "mp4",
    "outtmpl": OUTPUT_TEMPLATE,
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "http_headers": {
        "Accept-Language": "en-US,en;q=0.5",
    },
    "noplaylist": False,  # Set to True if downloading a single video
    "concurrent_fragment_downloads": 5,
    "retries": 10,
    "quiet": False,
    "no_warnings": False,
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Download failed: {e}")

if __name__ == "__main__":
    if not os.path.exists(COOKIES_FILE):
        print(f"❌ Cookies file '{COOKIES_FILE}' not found. Please export it in Netscape format.")
    else:
        download_video(VIDEO_URL)
