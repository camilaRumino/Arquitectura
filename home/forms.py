from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Correo electrónico', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Correo electrónico'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))