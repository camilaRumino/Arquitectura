from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django import views
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name= 'index'),
    path('registro/', registro, name= 'registro'),
    path('login/', login_view, name='login'),
    path('talleres/', talleres , name='talleres'),
    path('inscripcion/<int:taller_id>/', inscripcion, name='inscripcion'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('index-funcionarios/', FuncionarioIndexView.as_view(), name='index_funcionario'),
    path('index-instructor/', InstructorIndexView.as_view(), name='index_instructor'),
    path('registro-funcionarios/', registrar_funcionarios, name='registrar_funcionarios'), 
    path('index-instructor/', FuncionarioRegistroView.as_view(), name='index_instructor'),
    path('listar_am/', listar_am , name='listar_am'),
    path('modificar_am/<id>/', modificar_am, name="modificar_am"),
    path('eliminar_am/<id>/', eliminar_am, name="eliminar_am"),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)