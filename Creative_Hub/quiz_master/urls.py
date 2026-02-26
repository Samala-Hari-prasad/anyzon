from django.urls import path
from . import views
app_name = 'quiz_master'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.take_quiz, name='take'),
]
