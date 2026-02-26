from django.urls import path
from . import views

app_name = 'task_scheduler'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:pk>/<str:status>/', views.update_status, name='update_status'),
]
