# 🎬 Media Downloader Toolkit

A simple Python toolkit to download and convert media from YouTube and SoundCloud.

---

## 🚀 How to Use

### 📺 YouTube Videos

Run from terminal:

```bash
python yt_app.py
```

Enter:
- Video URL  
- Resolution (e.g., 720, 1080)

---

### 🎧 SoundCloud Downloader

1. Open the file:

```bash
soundcloud_downloader.py
```

2. Replace:

```python
playlist_url = "YOUR_PLAYLIST_URL"
```

3. Run:

```bash
python soundcloud_downloader.py
```

---

## ⚙️ Partial Playlist Download

```python
'playliststart': 162,
'playlistend': 215
```

---

## 📦 Install Dependencies

```bash
pip install yt-dlp
```

---

## 🎞 Install FFmpeg

### macOS
```bash
brew install ffmpeg
```

### Linux
```bash
sudo apt install ffmpeg
```

### Windows
Add to PATH:
```
C:\Program Files\ffmpeg\bin
```

---

## ⚠️ Notes

- FFmpeg is required for conversion  
- Some videos may not support selected resolution  
- Private videos will be skipped  
