from django.urls import path
from . import views

app_name = 'chat_room'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.room_detail, name='room_detail'),
]
