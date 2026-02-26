from django.shortcuts import render
from .models import Project, Skill

def index(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    return render(request, 'portfolio_showcase/index.html', {
        'projects': projects,
        'skills': skills
    })

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio_showcase/detail.html', {'project': project})
