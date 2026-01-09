from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegisterForm
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def base(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

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

    def get_queryset(self):
        search_input = self.request.GET.get('search') or ''
        if search_input:
            return Task.objects.filter(user=self.request.user, title__icontains=search_input)
        return Task.objects.filter(user=self.request.user)

# This is a description logic which handles details of a particular task
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_detail.html'

#This is a creation logic which handles creating a new task
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

#This is an updating logic which handles updating an existing task
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

#This is a deletion logic which handles deleting an existing task
class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
