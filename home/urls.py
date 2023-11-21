from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name= "home"),
    path('formulario/', formulario, name="formulario" ),
    path('login/', login, name= "login"),
    
]