from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    elif request.user.groups.filter(name='Funcionario').exists():
        return redirect('index_funcionario')
    elif request.user.groups.filter(name='Instructor').exists():
        return redirect('index')
    else:
        return render(request, 'index.html')
    
def index_funcionarios(request):
    return render(request, 'index-funcionarios.html')

class FuncionarioIndexView(UserPassesTestMixin, TemplateView):
    template_name = 'index-funcionarios.html'
    def test_func(self):
        return self.request.user.groups.filter(name='Funcionario').exists()
    def get_login_url(self):
        # specify the URL to redirect to if the user fails the test
        return '/index/'
    
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige al usuario a la página de inicio después del registro
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def talleres(request):
    return render(request, 'talleres.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

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
