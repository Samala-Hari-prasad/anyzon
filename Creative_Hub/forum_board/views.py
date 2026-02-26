from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread

def index(request):
    threads = Thread.objects.all().order_by('-votes', '-created_at')
    return render(request, 'forum_board/index.html', {'threads': threads})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    return render(request, 'forum_board/detail.html', {'thread': thread})

def upvote(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.votes += 1
    thread.save()
    return redirect('forum_board:index')
