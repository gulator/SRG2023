from django.contrib import admin
from Configuracion.models import *
from Ordenes.models import *

# Register your models here.

admin.site.register (CIG)
admin.site.register (ProductoAudio)
admin.site.register (MotivoAudio)
admin.site.register (EstadoAudio)
admin.site.register (ProductoAlarmas)
admin.site.register (MotivoAlarma)