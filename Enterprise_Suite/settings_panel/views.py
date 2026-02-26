from django.shortcuts import render

def index(request):
    return render(request, 'settings_panel/index.html')
