from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice

def index(request):
    polls = Poll.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'poll_maker/index.html', {'polls': polls})

def vote(request, poll_id, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id, poll_id=poll_id)
    choice.votes += 1
    choice.save()
    return redirect('poll_maker:index')
