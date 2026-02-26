from django.shortcuts import render

def index(request):
    return render(request, 'role_manager/index.html')
