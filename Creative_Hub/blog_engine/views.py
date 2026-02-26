from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_engine/index.html', {'posts': posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_engine/detail.html', {'post': post})
