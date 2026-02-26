from django.urls import path
from . import views

app_name = 'feedback_collector'

urlpatterns = [
    path('', views.index, name='index'),
]
