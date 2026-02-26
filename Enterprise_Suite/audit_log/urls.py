from django.urls import path
from . import views

app_name = 'audit_log'

urlpatterns = [
    path('', views.index, name='index'),
]
