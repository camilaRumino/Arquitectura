from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name= "index"),
    path('formulario/', formulario, name="formulario" ),
    path('login/', login, name= "login"),
    path('talleres/', talleres , name="talleres" ),
    path('inscripcion/<int:taller_id>/', inscripcion, name='inscripcion')

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)