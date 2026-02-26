from django.urls import path
from . import views
app_name = 'event_planner'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]
