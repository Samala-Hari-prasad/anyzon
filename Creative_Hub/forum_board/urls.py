from django.urls import path
from . import views

app_name = 'forum_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.thread_detail, name='thread_detail'),
    path('upvote/<int:pk>/', views.upvote, name='upvote'),
]
