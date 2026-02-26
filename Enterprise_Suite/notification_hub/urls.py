from django.urls import path
from . import views

app_name = 'notification_hub'

urlpatterns = [
    path('', views.index, name='index'),
]
