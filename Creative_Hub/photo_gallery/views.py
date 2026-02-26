from django.shortcuts import render
from .models import Photo, Album

def index(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    albums = Album.objects.all()
    return render(request, 'photo_gallery/index.html', {'photos': photos, 'albums': albums})
