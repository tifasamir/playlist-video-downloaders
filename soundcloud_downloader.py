import yt_dlp
import os

# Make sure you have yt-dlp installed
# pip install yt-dlp

# Playlist URL

playlist_url = "https://soundcloud.com/  playlist-url-path"

# Output folder
output_folder = "downloads4"
os.makedirs(output_folder, exist_ok=True)

# yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(playlist_index)02d - %(title)s.%(ext)s'),
    # 'playliststart': 215,   # 👈 THIS is the key
    'playlistend': 162,  # last index to download
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': r"C:\\Program Files\\ffmpeg\\bin",  # <-- set your ffmpeg folder here

    'quiet': False,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
