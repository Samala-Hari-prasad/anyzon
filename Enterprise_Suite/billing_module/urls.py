from django.urls import path
from . import views

app_name = 'billing_module'

urlpatterns = [
    path('', views.index, name='index'),
]
