from django.urls import path
from . import views
app_name = 'ad_manager'
urlpatterns = [
    path('', views.index, name='index'),
]
