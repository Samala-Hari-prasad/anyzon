from django.shortcuts import render, get_object_or_404
from .models import Recipe

def index(request):
    cat = request.GET.get('cat', '')
    recipes = Recipe.objects.filter(category=cat) if cat else Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipe_book/index.html', {'recipes': recipes, 'cat': cat})

def detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_book/detail.html', {'recipe': recipe})
