from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Configuracion.models import *



# Create your views here.

'''def config_main (request):
    cig = CIG.objects.all ()
    return render (request,'config_main.html', {'cig':cig})'''