from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
