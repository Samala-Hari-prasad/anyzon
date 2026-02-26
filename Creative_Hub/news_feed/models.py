from django.db import models

class NewsArticle(models.Model):
    CATS = [('tech','Technology'),('art','Art & Culture'),('music','Music'),('film','Film'),('sports','Sports')]
    title = models.CharField(max_length=500)
    summary = models.TextField()
    source = models.CharField(max_length=255, default='The Hindu')
    source_url = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATS, default='tech')
    image = models.ImageField(upload_to='news/', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    def __str__(self): return self.title
