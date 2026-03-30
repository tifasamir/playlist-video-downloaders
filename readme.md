🎬 Video playlist Downloader Toolkit
for youtube and soundcloud

A simple Python-based toolkit to download and cache:

📺 YouTube videos & playlists
🎧 SoundCloud playlists
🎞 Convert media to MP4 / MP3 using FFmpeg
🚀 Features
Download single videos or full playlists
Select specific resolution (YouTube)
Convert to MP4 (video) or MP3 (audio)
Resume downloads (avoid duplicates)
Partial playlist download support
📦 Installation
1. Install Python dependencies
pip install yt-dlp
2. Install FFmpeg (REQUIRED)

FFmpeg is used for:

merging audio + video → MP4
converting audio → MP3
macOS
brew install ffmpeg
Linux
sudo apt install ffmpeg
Windows
Download FFmpeg from official website
Extract and add to PATH:
C:\Program Files\ffmpeg\bin
📺 Usage — YouTube Downloader

Run from terminal:

python yt_app.py

You will be prompted to enter:

YouTube video or playlist URL
Desired resolution (e.g., 720, 1080)
✅ Supports:
Single video
Full playlist (auto organized into folders)
🎧 Usage — SoundCloud Downloader
Open:
soundcloud_downloader.py
Replace:
playlist_url = "YOUR_PLAYLIST_URL"
Run the script:
python soundcloud_downloader.py
⚙️ Advanced Configuration

You can control which part of a playlist to download:

'playliststart': 162,  # start index
'playlistend': 215,    # end index
💡 Use cases:
Resume long playlist downloads
Download only specific segments
Skip already processed items
📁 Output Structure
YouTube playlists:
videos/
 └── Playlist Name/
     ├── 1 - Video Title.mp4
     ├── 2 - Video Title.mp4
SoundCloud:
downloads/
 ├── Track1.mp3
 ├── Track2.mp3

