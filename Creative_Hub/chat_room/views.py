from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message

@login_required
def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat_room/index.html', {'rooms': rooms})

@login_required
def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = room.messages.all()
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=room, user=request.user, content=content)
            return redirect('chat_room:room_detail', slug=slug)
            
    return render(request, 'chat_room/room.html', {
        'room': room,
        'messages': messages,
        'rooms': Room.objects.all()
    })
