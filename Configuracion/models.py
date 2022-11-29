from django.db import models

# Create your models here.


class CIG(models.Model):
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f'Codigo: {self.codigo}'


class MotivoAudio(models.Model):
    tipo = models.CharField(max_length=60)


class MotivoAlarma(models.Model):
    tipo = models.CharField(max_length=60)


class Estado(models.Model):
    estado = models.CharField(max_length=60)


class ProductoAudio(models.Model):
    audio = models.CharField(max_length=80)


class ProductoAlarmas(models.Model):
    alarmas = models.CharField(max_length=60)
