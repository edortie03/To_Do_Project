from django.urls import path, include
from . import views

pathpatterns = [
    path('', views.base, name='base'),
    path('/login', views.login, name='login'),
    path('/register', views.register, name='register'),
    path('/logout', views.logout, name='logout'),
    path('/dashboard', views.dashboard, name='dashboard'),
]