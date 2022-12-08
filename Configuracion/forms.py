from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class EditarCIG (forms.Form):
    codigo = forms.CharField(max_length=10)

class AudioProductos (forms.Form):
    productoAudio = forms.CharField(max_length=80)

class AudioMotivo (forms.Form):
    motivoAudio = forms.CharField(max_length=60)

class AudioEstado (forms.Form):
    estadoAudio = forms.CharField(max_length=60)

class AlarmasProductos (forms.Form):
    productoAlarmas = forms.CharField(max_length=80)

class AlarmaMotivo (forms.Form):
    motivoAlarma = forms.CharField(max_length=60)

class AlarmaEstado (forms.Form):
    estadoAlarma = forms.CharField(max_length=60)

class Login_formulario (AuthenticationForm):

    username = forms.CharField(label=('Usuario'), widget=forms.TextInput(attrs={'class':'form-control'}))   
    password = forms.CharField(label=('Contraseña'), widget=forms.PasswordInput(attrs={'class':'form-control'}))   
    class Meta:
        model = User
        fields = ['username', 'password']

    