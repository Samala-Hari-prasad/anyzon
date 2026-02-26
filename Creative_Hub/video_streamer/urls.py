from django.urls import path
from . import views

app_name = 'video_streamer'

urlpatterns = [
    path('', views.index, name='index'),
    path('watch/<int:pk>/', views.watch, name='watch'),
]
