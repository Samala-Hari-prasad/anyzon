from django.shortcuts import render

def index(request):
    return render(request, 'mail_client/index.html')
