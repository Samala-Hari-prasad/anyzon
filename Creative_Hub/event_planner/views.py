from django.shortcuts import render, get_object_or_404, redirect
from .models import Event

def index(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event_planner/index.html', {'events': events})

def detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_planner/detail.html', {'event': event})
