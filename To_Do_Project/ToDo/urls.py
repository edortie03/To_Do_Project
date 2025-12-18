from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('task_list/', TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task-create/', TaskCreate.as_view(), name='task_create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task_delete'),
]
