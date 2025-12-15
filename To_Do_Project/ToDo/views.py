from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

# Create your views here.
#User authentication
def base(request):
    return render(request, 'base.html')

def login(request):
    return HttpResponse('This is a login page')

def register(request):
    return HttpResponse('This is a register page') 

def logout(request):
    return HttpResponse('Successfully logged out')



###################################################################################
"""
Projects logic which includes creating, updating, deleting, viewing tasks
"""

#This is a listing dashboard which shows all details about tasks
class TaskList(ListView):
    model = Task
    context_object_name = 'list'
    template_name = 'dashboard.html'

# This is a description logic which handles details of a particular task
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_detail.html'

#This is a creation logic which handles creating a new task
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

#This is an updating logic which handles updating an existing task
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')

#This is a deletion logic which handles deleting an existing task
class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'dashboard.hmtl'