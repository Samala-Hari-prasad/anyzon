from django.shortcuts import render, get_object_or_404
from .models import WikiPage

def index(request):
    q = request.GET.get('q', '')
    pages = WikiPage.objects.filter(title__icontains=q).order_by('-updated_at') if q else WikiPage.objects.all().order_by('-updated_at')
    return render(request, 'wiki_pages/index.html', {'pages': pages, 'q': q})

def detail(request, slug):
    page = get_object_or_404(WikiPage, slug=slug)
    return render(request, 'wiki_pages/detail.html', {'page': page})
