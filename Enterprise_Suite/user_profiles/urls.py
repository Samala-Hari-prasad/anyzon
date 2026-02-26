from django.urls import path
from . import views

app_name = 'user_profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit_profile, name='edit_profile'),
]
