from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def index(request):
    notifications = request.user.notifications.all().order_by('-timestamp')
    return render(request, 'notification_hub/index.html', {'notifications': notifications})
