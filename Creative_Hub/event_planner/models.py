from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100, default='Bengaluru')
    venue = models.CharField(max_length=255)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='events/', blank=True)
    TYPES = [('workshop','Workshop'),('meetup','Meetup'),('conference','Conference'),('online','Online')]
    event_type = models.CharField(max_length=20, choices=TYPES, default='meetup')
    seats_total = models.PositiveIntegerField(default=100)
    seats_booked = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def seats_left(self): return self.seats_total - self.seats_booked

    def __str__(self): return self.title
