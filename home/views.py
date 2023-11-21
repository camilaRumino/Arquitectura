from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def formulario(request):
    return render(request, 'formulario.html')

