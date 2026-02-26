from django.db import models
from django.contrib.auth.models import User

class ReviewItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/', blank=True)
    def __str__(self): return self.name

class Review(models.Model):
    item = models.ForeignKey(ReviewItem, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.user.username} → {self.item.name}"
