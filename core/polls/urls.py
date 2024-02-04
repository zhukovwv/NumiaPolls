from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('polls', views.poll_list, name='poll_list'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
]
