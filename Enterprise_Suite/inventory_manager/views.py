from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.db import models

def index(request):
    products = Product.objects.all()
    return render(request, 'inventory_manager/index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            sku=request.POST.get('sku'),
            category=request.POST.get('category'),
            quantity=request.POST.get('quantity'),
            unit_price=request.POST.get('unit_price'),
            min_stock_level=request.POST.get('min_stock_level')
        )
        return redirect('inventory_manager:index')
    return render(request, 'inventory_manager/add.html')

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('inventory_manager:index')
