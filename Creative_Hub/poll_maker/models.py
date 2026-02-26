from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.question
    @property
    def total_votes(self):
        return sum(c.votes for c in self.choices.all())

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    def __str__(self): return self.text
    @property
    def percentage(self):
        total = self.poll.total_votes
        return round((self.votes / total) * 100) if total > 0 else 0
