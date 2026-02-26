from django.shortcuts import render
from .models import Video

def index(request):
    videos = Video.objects.all().order_by('-created_at')
    # If no videos, create some sample ones (In a real app this wouldn't be in a view, but for demo it's fine)
    if not videos.exists():
        return render(request, 'video_streamer/index.html', {'videos': []})
    return render(request, 'video_streamer/index.html', {'videos': videos})

def watch(request, pk):
    from .models import Video
    video = Video.objects.get(pk=pk)
    video.views += 1
    video.save()
    next_videos = Video.objects.exclude(pk=pk)[:5]
    return render(request, 'video_streamer/watch.html', {'video': video, 'next_videos': next_videos})
