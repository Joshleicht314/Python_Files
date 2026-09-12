import subprocess
import sys

url = "https://www.youtube.com/watch?v=FrNHQDydWmo"  # ← replace with your URL

cmd = [
    sys.executable, "-m", "yt_dlp",
    "-x",
    "--audio-format", "mp3",
    "--audio-quality", "0",
    "-o", "%(title)s.%(ext)s",
    url
]

subprocess.run(cmd, check=True)

