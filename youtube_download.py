import yt_dlp
import os

def download_youtube_playlist(url, output_path="videos", resolution="720"):
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        # Allow playlist
        'noplaylist': False,

        # Best video under resolution + audio
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',

        # Force MP4 merge
        'merge_output_format': 'mp4',

        # Organize by playlist folder
        'outtmpl': os.path.join(
            output_path,
            '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'
        ),

        # Skip already downloaded files
        'download_archive': os.path.join(output_path, 'downloaded.txt'),

        'quiet': False,
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"⬇ {d.get('_percent_str', '0%')} | {d.get('_speed_str', '')}")
    elif d['status'] == 'finished':
        print("✅ Downloaded, merging to MP4...")


if __name__ == "__main__":
    playlist_url = input("Enter YouTube Playlist URL: ")
    resolution = input("Enter resolution (e.g., 720, 1080): ")

    download_youtube_playlist(playlist_url, resolution=resolution)