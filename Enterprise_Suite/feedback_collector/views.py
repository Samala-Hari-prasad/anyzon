from django.shortcuts import render

def index(request):
    return render(request, 'feedback_collector/index.html')
