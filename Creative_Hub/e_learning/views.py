from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

def index(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'e_learning/index.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'e_learning/detail.html', {'course': course})
