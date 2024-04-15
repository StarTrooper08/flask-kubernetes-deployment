from flask import Flask, render_template, request
from pytube import YouTube

from pathlib import Path

app = Flask(__name__)

def get_download_path():
    # Get user's download folder path based on the operating system
    return Path.home() / "Downloads"

def download_youtube_video(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download(output_path=get_download_path())

        return f" '{yt.title}' Youtube Video Download complete."

    except Exception as e:
        return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    download_message = None
    if request.method == 'POST':
        video_url = request.form['video_url']
        if video_url:
            download_message = download_youtube_video(video_url)
    return render_template('index.html', download_message=download_message)

if __name__ == '__main__':
    app.run(debug=True)
