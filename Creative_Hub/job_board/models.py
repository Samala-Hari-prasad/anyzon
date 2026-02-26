from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='jobs/logos/', blank=True)
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    def __str__(self): return self.name

class Job(models.Model):
    TYPES = [('full', 'Full-time'), ('remote', 'Remote'), ('contract', 'Contract')]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=10, choices=TYPES, default='full')
    salary_range = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title
