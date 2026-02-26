from django.urls import path
from . import views

app_name = 'document_vault'

urlpatterns = [
    path('', views.index, name='index'),
]
