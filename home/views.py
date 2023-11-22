from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')
def talleres(request):
    return render(request, 'talleres.html')

