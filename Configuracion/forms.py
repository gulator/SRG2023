from .models import *
from django import forms

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