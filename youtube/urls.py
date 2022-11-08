from django.urls import include, path
from .views import index
from .views import ChannelList

urlpatterns = [
    path('', index, name='index'),
    path('channels/', ChannelList.as_view(template_name="YoutubeChannel/index.html"), name='channels.index')
]