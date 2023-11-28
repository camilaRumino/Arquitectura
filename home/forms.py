from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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

class RegistroForm(UserCreationForm):
    username = forms.CharField(label="Correo electrónico", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'anasanchez@gmail.com'}))
    run = forms.CharField(label="RUT", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '11.111.111-K'}))
    nombre = forms.CharField(label="Nombre", max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ana'}))
    apellido = forms.CharField(label="Apellido", max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sánchez'}))
    fecnac = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'placeholder': '1980-12-31'}), validators=[MinValueValidator(date(1900, 1, 1)), MaxValueValidator(date(1980, 12, 31))])

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('run', 'nombre', 'apellido', 'fecnac')
    

class DetalleUsuarioForm(forms.ModelForm):
    class Meta:
        model = DetalleUsuario
        fields = ['run', 'nombre', 'apellido', 'fecnac']
