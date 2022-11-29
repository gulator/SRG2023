from django.db import models

# Create your models here.


#class headerOrden:
#    pass

#class bodyOrdenAlarma:
#    pass

#class bodyOrdenAudio:
#    pass

class agregaItem (models.Model):
    
    estado = models.CharField (max_length=60,blank=True, null=True)
    faltantes= models.CharField (max_length=250,blank=True, null=True)
    producto = models.CharField (max_length=250)
    serie = models.IntegerField (blank=True, null=True)
    cliente = models.CharField (max_length=100,blank=True, null=True)
    vendedor = models.CharField (max_length=60,blank=True, null=True)
    motivo = models.CharField (max_length=60,blank=True, null=True)
    cig = models.CharField (max_length=10,blank=True, null=True)
    observaciones = models.CharField (max_length=250,blank=True, null=True)
    saleSerie = models.IntegerField (blank=True, null=True)
    factura = models.CharField (max_length=20,blank=True, null=True)
