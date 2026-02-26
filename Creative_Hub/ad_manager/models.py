from django.db import models

class AdCampaign(models.Model):
    TYPES = [('banner','Banner'),('featured','Featured Post'),('sidebar','Sidebar')]
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    ad_type = models.CharField(max_length=20, choices=TYPES, default='banner')
    image = models.ImageField(upload_to='ads/')
    target_url = models.URLField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    impressions = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    def __str__(self): return f"{self.client} – {self.title}"
    @property
    def ctr(self):
        return round((self.clicks / self.impressions * 100), 2) if self.impressions > 0 else 0
