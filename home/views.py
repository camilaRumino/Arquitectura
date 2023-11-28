from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    elif request.user.groups.filter(name='Funcionario').exists():
        return redirect('index_funcionario')
    elif request.user.groups.filter(name='Instructor').exists():
        return redirect('index_instructor')
    else:
        return render(request, 'index.html')
    
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            detalle_usuario = DetalleUsuario(user=user)
            detalle_usuario.run = form.cleaned_data['run']
            detalle_usuario.nombre = form.cleaned_data['nombre']
            detalle_usuario.apellido = form.cleaned_data['apellido']
            detalle_usuario.fecnac = form.cleaned_data['fecnac']
            detalle_usuario.save()
            return redirect('index')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

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

@login_required(login_url='/index/')
def talleres(request):
    talleres = Taller.objects.all()
    return render(request, 'talleres.html', {'talleres': talleres})

@user_passes_test(lambda u: u.groups.filter(name='AdultoMayor').exists(), login_url='/index/')
def inscripcion(request, taller_id):
    taller = Taller.objects.get(id=taller_id)
    Inscripcion.objects.create(user=request.user, taller=taller)
    messages.success(request, 'Inscrito en taller exitosamente')
    return redirect('talleres')


# ADULTO MAYOR

@user_passes_test(lambda u: u.groups.filter(name='Funcionario').exists(), login_url='/index-funcionarios/')
def listar_am(request):
    registroAll = User.objects.select_related('detalleusuario').filter(groups__name='AdultoMayor').all()
    datos = {
        'listarAm' : registroAll
    }
    return render(request, 'listar_am.html', datos)

@user_passes_test(lambda u: u.groups.filter(name='Funcionario').exists(), login_url='/index-funcionarios/')
def modificar_am(request, id):
    user = User.objects.get(id=id)
    usuario = DetalleUsuario.objects.get(user=user)
    datos = {
        'form' : DetalleUsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = DetalleUsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente'
            datos['form'] = formulario
        else :
            datos['mensaje'] = formulario.errors
    return render(request, 'modificar_am.html', datos)

@user_passes_test(lambda u: u.groups.filter(name='Funcionario').exists(), login_url='/index-funcionarios/')
def eliminar_am(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('listar_am')

# FUNCIONARIO

@user_passes_test(lambda u: u.groups.filter(name='Funcionario').exists(), login_url='/index/')
def index_funcionarios(request):
    return render(request, 'index-funcionarios.html')

class FuncionarioIndexView(UserPassesTestMixin, TemplateView):
    template_name = 'index-funcionarios.html'
    def test_func(self):
        return self.request.user.groups.filter(name='Funcionario').exists()
    def get_login_url(self):
        return '/index/'

class FuncionarioRegistroView(UserPassesTestMixin, TemplateView):
    template_name = 'registro-funcionarios.html'
    def test_func(self):
        return self.request.user.groups.filter(name='Funcionario').exists()
    def get_login_url(self):
        return '/index/'

@user_passes_test(lambda u: u.groups.filter(name='Funcionario').exists(), login_url='/index-funcionarios/')    
def registrar_funcionarios(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            detalle_usuario = DetalleUsuario(user=user)
            detalle_usuario.run = form.cleaned_data['run']
            detalle_usuario.nombre = form.cleaned_data['nombre']
            detalle_usuario.apellido = form.cleaned_data['apellido']
            detalle_usuario.fecnac = form.cleaned_data['fecnac']
            detalle_usuario.save()
            return redirect('index')
    else:
        form = RegistroForm()
    
        return render(request, 'registro-funcionarios.html', {'form': form})
    
# INSTRUCTOR

@user_passes_test(lambda u: u.groups.filter(name='Instructor').exists(), login_url='/index/')
def index_instructor(request):
    return render(request, 'index-instructor.html')

class InstructorIndexView(UserPassesTestMixin, TemplateView):
    template_name = 'index-instructor.html'
    def test_func(self):
        return self.request.user.groups.filter(name='Instructor').exists()
    def get_login_url(self):
        return '/index/'