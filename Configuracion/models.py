from django.db import models

# Create your models here.


class CIG(models.Model):
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f'Codigo: {self.codigo}'


class MotivoAudio(models.Model):
    motivoAudio = models.CharField(max_length=60)

    def __str__(self):
       return f'Motivo_Audio: {self.motivoAudio}'


class MotivoAlarma(models.Model):
    motivoAlarma = models.CharField(max_length=60)


class EstadoAudio(models.Model):
    estadoAudio = models.CharField(max_length=60)

    def __str__(self):
       return f'Estado_Audio: {self.estadoAudio}'


class EstadoAlarma (models.Model):
    estadoAlarma = models.CharField(max_length=60)


class ProductoAudio(models.Model):
    productoAudio = models.CharField(max_length=80)

    def __str__(self):
       return f'Producto_Audio: {self.productoAudio}'


class ProductoAlarmas(models.Model):
    productoAlarmas = models.CharField(max_length=60)

    def __str__(self):
       return f'Producto_Alarma: {self.productoAlarmas}'
