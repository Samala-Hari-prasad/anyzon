from django.shortcuts import render
from .models import Product, Category

def index(request):
    products = Product.objects.filter(is_sold=False).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'marketplace/index.html', {
        'products': products,
        'categories': categories
    })

def detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'marketplace/detail.html', {'product': product})
