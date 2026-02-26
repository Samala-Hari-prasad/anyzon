from django.urls import path
from . import views
app_name = 'wiki_pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
]
