from django.urls import path
from . import views
app_name = 'poll_maker'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/vote/<int:choice_id>/', views.vote, name='vote'),
]
