from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'auth_system'

from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('auth_system:login')),
    path('login/', auth_views.LoginView.as_view(template_name='auth_system/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dashboard'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
