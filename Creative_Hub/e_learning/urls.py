from django.urls import path
from . import views

app_name = 'e_learning'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.course_detail, name='detail'),
]
