from django.db import models

class WikiPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title

class WikiRevision(models.Model):
    page = models.ForeignKey(WikiPage, related_name='revisions', on_delete=models.CASCADE)
    content = models.TextField()
    summary = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
