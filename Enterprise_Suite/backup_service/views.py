from django.shortcuts import render

def index(request):
    return render(request, 'backup_service/index.html')
