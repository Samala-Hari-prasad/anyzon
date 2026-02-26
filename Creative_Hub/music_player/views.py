from django.shortcuts import render, get_object_or_404
from .models import Track

def index(request):
    tracks = Track.objects.all().order_by('-plays')
    return render(request, 'music_player/index.html', {'tracks': tracks})

def play(request, pk):
    track = get_object_or_404(Track, pk=pk)
    track.plays += 1
    track.save()
    all_tracks = Track.objects.exclude(pk=pk)
    return render(request, 'music_player/player.html', {'track': track, 'tracks': all_tracks})
