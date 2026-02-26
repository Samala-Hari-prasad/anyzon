from django.shortcuts import render

def index(request):
    return render(request, 'help_desk/index.html')
