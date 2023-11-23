from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic.edit import CreateView

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')
def talleres(request):
    return render(request, 'talleres.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('talleres')
    return render(request, 'login.html')

@login_required
def talleres(request):
    talleres = Taller.objects.all()
    return render(request, 'talleres.html', {'talleres': talleres})

@login_required
def inscripcion(request, taller_id):
    taller = Taller.objects.get(id=taller_id)
    Inscripcion.objects.create(usuario=request.user, taller=taller)
    return redirect('talleres')

def listar_talleres(request):
    tallerAll = Taller.objects.all()
    datos = {
        'listaTalleres' : tallerAll
    }
    return render(request, 'talleres.html', datos)