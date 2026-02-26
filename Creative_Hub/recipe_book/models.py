from django.db import models

class Recipe(models.Model):
    CATS = [('veg','Vegetarian'),('nonveg','Non-Vegetarian'),('dessert','Dessert'),('snack','Snack')]
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField(help_text='One per line')
    instructions = models.TextField()
    category = models.CharField(max_length=20, choices=CATS, default='veg')
    image = models.ImageField(upload_to='recipes/', blank=True)
    prep_time = models.PositiveIntegerField(default=15, help_text='Minutes')
    cook_time = models.PositiveIntegerField(default=30, help_text='Minutes')
    servings = models.PositiveIntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
    @property
    def ingredient_list(self): return self.ingredients.splitlines()
