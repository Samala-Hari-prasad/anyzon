from django.shortcuts import render

def index(request):
    return render(request, 'billing_module/index.html')
