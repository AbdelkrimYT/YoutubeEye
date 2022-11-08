from django.db import models
from services import youtube


class Channel(models.Model):
    channel_id = models.CharField(max_length=255, primary_key=True)

    def __init__(self, *args, **kwargs):
        super(Channel, self).__init__(*args, **kwargs)
        youtube_api = youtube.channels().list(part='id,snippet,statistics,status', id=self.channel_id)
        self.collection = youtube_api.execute()

    def __str__(self):
        return self.channel_title

    @property
    def channel_url(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    @property
    def channel_title(self):
        return str(self.collection['items'][0]['snippet']['title'])

    @property
    def subscriber_count(self):
        return str(self.collection['items'][0]['statistics']['subscriberCount'])

    @property
    def view_count(self):
        return str(self.collection['items'][0]['statistics']['viewCount'])


class Video(models.Model):
    video_id = models.CharField(max_length=255, primary_key=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    # disk_path = models.CharField()
    # is_downloaded = models.BooleanField()

    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)
        api_request = youtube.videos().list(part='id,snippet,statistics,status', id=self.video_id)
        self.collection = api_request.execute()

    def __str__(self):
        return self.video_title

    @property
    def video_url(self):
        return f'https://www.youtube.com/watch?v={self.video_id}'

    @property
    def video_title(self):
        return str(self.collection['items'][0]['snippet']['title'])

    @property
    def view_count(self):
        return str(self.collection['items'][0]['statistics']['viewCount'])

    @property
    def like_count(self):
        return str(self.collection['items'][0]['statistics']['likeCount'])

    @property
    def comment_count(self):
        return str(self.collection['items'][0]['statistics']['commentCount'])
