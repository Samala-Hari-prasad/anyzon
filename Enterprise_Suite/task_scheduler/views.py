from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    todo_tasks = Task.objects.filter(status='todo')
    doing_tasks = Task.objects.filter(status='doing')
    done_tasks = Task.objects.filter(status='done')
    return render(request, 'task_scheduler/index.html', {
        'todo': todo_tasks,
        'doing': doing_tasks,
        'done': done_tasks
    })

def add_task(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            priority=request.POST.get('priority'),
            due_date=request.POST.get('due_date') if request.POST.get('due_date') else None
        )
        return redirect('task_scheduler:index')
    return render(request, 'task_scheduler/add.html')

def update_status(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    task.status = status
    task.save()
    return redirect('task_scheduler:index')
