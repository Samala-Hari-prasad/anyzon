from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Emoji icon")
    def __str__(self): return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True)
    tags = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title
