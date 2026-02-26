from django.shortcuts import render

def index(request):
    return render(request, 'audit_log/index.html')
