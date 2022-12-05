import csv
import codecs
from Configuracion.models import *
from Configuracion.forms import *
from django.http import HttpResponse
from django.shortcuts import render

def cargar (request):
    return render (request,'loader.html')

def funcion_loader (request):

    with codecs.open("C:\\Users\\gulad\\OneDrive\\Documentos\\Python\\instaladores\\usuarios_sitio_depurado.csv", "r", encoding="ANSI") as f1:
    
                csv_reader = csv.reader(f1,delimiter=";")                
                for n in csv_reader:
                    print(n)
                    nuevo_usuario = RegisterUserForm({'username':n[0],'email':n[1],'password1':'XD05ttoo01pp','password2':'XD05ttoo01pp'})
                    print(nuevo_usuario)
                    user = nuevo_usuario.save()
                    perfil = Profile(
                            user_id=user.id,
                            usuario=user.username,
                            comercio=n[2],
                            cuit=n[3],
                            telefono=n[6],
                            localidad=n[4],
                            provincia=n[5],
                            pais=n[7],
                        )
                    perfil.save()
                    user.save()
                f1.close()  
                        
                return HttpResponse('Usuarios cargados')

