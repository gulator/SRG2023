from django.shortcuts import render
from Configuracion.models import *


def inicio (request):
    cig = CIG.objects.all()
    return render (request,'testing_orden.html',{'cig':cig})
# Create your views here.
