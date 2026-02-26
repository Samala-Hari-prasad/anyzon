from django.shortcuts import render, redirect
from .models import Subscriber

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name', '')
        if email:
            Subscriber.objects.get_or_create(email=email, defaults={'name': name})
            return render(request, 'newsletter_sub/index.html', {'success': True})
    count = Subscriber.objects.filter(is_active=True).count()
    return render(request, 'newsletter_sub/index.html', {'count': count})
