from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

#class LoginForm(AuthenticationForm):
#    username = forms.CharField(label='Correo electrónico', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Correo electrónico'}))
#    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Correo Electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': (
            "Correo electrónico o contraseña incorrectos. Intente nuevamente."
        ),
    }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['run', 'nombre', 'apellido', 'correo', 'contrasena', 'fecnac']
        widgets = {
            'run': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12.345.678-K'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ana'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sánchez'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'anasanchez@gmail.com'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'fecnac': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'placeholder': '1980-12-31'}),
        }
        validators = {
            'fecnac': [MinValueValidator(date(1900, 1, 1)), MaxValueValidator(date(1980, 12, 31))] # Esto validará el rango de fechas
        }
        labels = {
            'run': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo electrónico',
            'contrasena': 'Contraseña',
            'fecnac': 'Fecha de nacimiento',
        }