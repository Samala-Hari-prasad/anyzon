from django.urls import path
from . import views

app_name = 'backup_service'

urlpatterns = [
    path('', views.index, name='index'),
]
