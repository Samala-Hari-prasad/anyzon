from django.urls import path
from . import views

app_name = 'settings_panel'

urlpatterns = [
    path('', views.index, name='index'),
]
