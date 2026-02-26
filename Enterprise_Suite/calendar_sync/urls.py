from django.urls import path
from . import views

app_name = 'calendar_sync'

urlpatterns = [
    path('', views.index, name='index'),
]
