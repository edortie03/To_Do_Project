from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base(request):
    return HttpResponse('This is a base page')

def login(request):
    return HttpResponse('This is a login page')

def register(request):
    return HttpResponse('This is a register page') 

def logout(request):
    return HttpResponse('Successfully logged out')

def dashboard(request):
    return HttpResponse('This is the dashboard page')