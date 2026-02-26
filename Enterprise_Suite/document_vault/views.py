from django.shortcuts import render
from .models import Document

def index(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'document_vault/index.html', {'documents': documents})
