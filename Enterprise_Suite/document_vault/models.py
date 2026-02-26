from django.db import models

class Document(models.Model):
    FILE_TYPES = [
        ('pdf', 'PDF Document'),
        ('docx', 'Word Document'),
        ('xlsx', 'Excel Sheet'),
        ('img', 'Image File'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='vault/documents/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, default='pdf')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size_mb = models.DecimalField(max_digits=5, decimal_places=2, help_text="Size in MB")

    def __str__(self): return self.title
