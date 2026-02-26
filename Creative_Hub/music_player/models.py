from django.db import models

class Track(models.Model):
    GENRES = [('indian','Indian Classical'),('bollywood','Bollywood'),('indie','Indie'),('folk','Folk'),('electronic','Electronic')]
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, choices=GENRES, default='indie')
    audio_file = models.FileField(upload_to='music/', blank=True)
    cover_art = models.ImageField(upload_to='music/covers/', blank=True)
    duration = models.PositiveIntegerField(default=180, help_text='Seconds')
    plays = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.title} - {self.artist}"
    @property
    def duration_display(self):
        m, s = divmod(self.duration, 60)
        return f"{m}:{s:02d}"
