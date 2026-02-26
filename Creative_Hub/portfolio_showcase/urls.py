from django.urls import path
from . import views

app_name = 'portfolio_showcase'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.project_detail, name='detail'),
]
