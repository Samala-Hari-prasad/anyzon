from django.urls import path
from . import views

app_name = 'help_desk'

urlpatterns = [
    path('', views.index, name='index'),
]
