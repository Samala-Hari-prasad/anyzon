from django.urls import path
from . import views
app_name = 'music_player'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/play/', views.play, name='play'),
]
