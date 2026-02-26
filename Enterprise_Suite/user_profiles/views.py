from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def index(request):
    return render(request, 'user_profiles/index.html', {'profile': request.user.profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.bio = request.POST.get('bio')
        profile.location = request.POST.get('location')
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()
        return redirect('user_profiles:index')
    return render(request, 'user_profiles/edit.html', {'profile': request.user.profile})
