from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name= "index"),
    path('formulario/', formulario, name="formulario" ),
    path('login/', login, name= "login"),
    
]