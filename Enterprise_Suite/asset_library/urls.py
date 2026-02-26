from django.urls import path
from . import views

app_name = 'asset_library'

urlpatterns = [
    path('', views.index, name='index'),
]
