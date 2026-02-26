from django.shortcuts import render, redirect
from .models import NewsArticle

def index(request):
    featured = NewsArticle.objects.filter(is_featured=True).first()
    articles = NewsArticle.objects.all().order_by('-published_at')
    category = request.GET.get('cat', '')
    if category:
        articles = articles.filter(category=category)
    return render(request, 'news_feed/index.html', {
        'featured': featured, 'articles': articles, 'category': category
    })
