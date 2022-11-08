from app.settings import DOWNLOADS_DIR
from pytube import YouTube
from os import path

def download(url):
    video = YouTube(url)
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() \
        .download(output_path=path.join(DOWNLOADS_DIR, video.channel_id), filename=f'{video.video_id}__{video.title}.mp4')

def watch():
    pass

if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=BpMh6Qu2uGY')
