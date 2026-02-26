from django.shortcuts import render
from .models import Job

def index(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'job_board/index.html', {'jobs': jobs})

def detail(request, pk):
    job = Job.objects.get(pk=pk)
    return render(request, 'job_board/detail.html', {'job': job})
