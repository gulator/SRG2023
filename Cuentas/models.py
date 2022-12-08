from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
class Perfiles (models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=60)
    mail = models.EmailField()
    clave = models.CharField(max_length=20)