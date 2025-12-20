from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def base(request):
    return render(request, 'base.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('base')



###################################################################################
"""
Projects logic which includes creating, updating, deleting, viewing tasks
"""

#This is a listing dashboard which shows all details about tasks
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'list'
    template_name = 'dashboard.html'

# This is a description logic which handles details of a particular task
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_detail.html'

#This is a creation logic which handles creating a new task
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

#This is an updating logic which handles updating an existing task
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

#This is a deletion logic which handles deleting an existing task
class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
