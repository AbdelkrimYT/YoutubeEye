from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Channel
from services import youtube

class ChannelList(ListView):
    model = Channel
    context_object_name = 'channels'

def youtubeChannelsIndex(request):
    return render(request, 'index.html', context={})

def index(request):
    try:
        api_request = youtube.channels().list(part='id,snippet,statistics,status', id='UCfiwzLy-8yKzIbsmZTzxDgw')
        content = api_request.execute()
        #return HttpResponse(content)
        return render(request, 'index.html', {'content': content, 'type': type(content)})
    except Exception as e:
        return HttpResponse(e)
