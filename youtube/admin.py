from django.contrib import admin
from django import forms
from .models import Channel, Video

class ChannelForm(forms.Form):

    class Meta:
        model = Channel

    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(args, kwargs)

class ChannelAdmin(admin.ModelAdmin):
    forms = ChannelForm
    list_display = ('channel_title', 'channel_url', 'subscriber_count', 'view_count')

class VideoForm(forms.Form):

    class Meta:
        model = Video

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(args, kwargs)

class VideoAdmin(admin.ModelAdmin):
    forms = ChannelForm
    list_display = ('video_title', 'channel', 'view_count', 'like_count', 'comment_count')

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Video, VideoAdmin)
