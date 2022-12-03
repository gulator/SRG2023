from django.shortcuts import render
from Configuracion.models import *
from Configuracion.forms import *


def inicio(request):
    cig = CIG.objects.all()
    return render(request, 'index.html', {'cig': cig})
# Create your views here.


def config_main(request):
    return render(request, 'config_main.html')


def config_cig(request):
    cig = CIG.objects.all()
    return render(request, 'config_cig.html', {'cig': cig})


def del_item_cig(request, id):
    item = CIG.objects.get(id=id)
    item.delete()
    cig = CIG.objects.all()
    return render(request, 'config_cig.html', {'cig': cig})


def edit_item_cig(request, id):
    cig = CIG.objects.all()
    item = CIG.objects.get(id=id)
    if request.method == "POST":
        formulario = EditarCIG(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item.codigo = datos['codigo']
            item.save()
        return render(request, 'config_cig.html', {'cig': cig})

    return render(request, 'config_cig_edit.html', {'item': item})


def add_item_cig(request):

    if request.method == "POST":
        formulario = EditarCIG(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item = CIG(codigo=datos['codigo'])
            item.save()
        cig = CIG.objects.all()
        return render(request, 'config_cig.html', {'cig': cig})

    return render(request, 'config_cig_add.html')

# ------ AUDIO PRODUCTO ------

def config_audio_producto(request):
    productos = ProductoAudio.objects.all().order_by('productoAudio')
    return render(request, 'config_audio_producto.html', {'audio_producto': productos})


def del_item_audio_producto(request, id):
    item = ProductoAudio.objects.get(id=id)
    item.delete()
    productos = ProductoAudio.objects.all().order_by('productoAudio')
    return render(request, 'config_audio_producto.html', {'audio_producto': productos})


def edit_item_audio_producto(request, id):
    productos = ProductoAudio.objects.all().order_by('productoAudio')
    item = ProductoAudio.objects.get(id=id)
    if request.method == "POST":
        formulario = AudioProductos(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item.productoAudio = datos['productoAudio']
            item.save()
        return render(request, 'config_audio_producto.html', {'audio_producto': productos})
    return render(request, 'config_audio_producto_edit.html', {'item': item})


def add_item_audio_producto(request):

    if request.method == "POST":
        formulario = AudioProductos(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item = ProductoAudio(productoAudio=datos['productoAudio'])
            item.save()
            productos = ProductoAudio.objects.all().order_by('productoAudio')
            return render(request, 'config_audio_producto.html', {'audio_producto': productos})

    return render(request, 'config_audio_producto_add.html')

# ------ AUDIO MOTIVO ------

def config_audio_motivo(request):
    productos = MotivoAudio.objects.all().order_by('motivoAudio')
    return render(request, 'config_audio_motivo.html', {'audio_motivo': productos})


def del_item_audio_motivo(request, id):
    item = MotivoAudio.objects.get(id=id)
    item.delete()
    productos = MotivoAudio.objects.all().order_by('motivoAudio')
    return render(request, 'config_audio_motivo.html', {'audio_motivo': productos})


def edit_item_audio_motivo(request, id):
    productos = MotivoAudio.objects.all().order_by('motivoAudio')
    item = MotivoAudio.objects.get(id=id)
    if request.method == "POST":
        formulario = AudioMotivo(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item.motivoAudio = datos['motivoAudio']
            item.save()
        return render(request, 'config_audio_motivo.html', {'audio_motivo': productos})
    return render(request, 'config_audio_motivo_edit.html', {'item': item})


def add_item_audio_motivo(request):

    if request.method == "POST":
        formulario = AudioMotivo(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item = MotivoAudio(motivoAudio=datos['motivoAudio'])
            item.save()
            productos = MotivoAudio.objects.all().order_by('motivoAudio')
            return render(request, 'config_audio_motivo.html', {'audio_motivo': productos})

    return render(request, 'config_audio_motivo_add.html')


# ------ AUDIO ESTADO ------

def config_audio_estado(request):
    productos = EstadoAudio.objects.all().order_by('estadoAudio')
    return render(request, 'config_audio_estado.html', {'audio_estado': productos})


def del_item_audio_estado(request, id):
    item = EstadoAudio.objects.get(id=id)
    item.delete()
    productos = EstadoAudio.objects.all().order_by('estadoAudio')
    return render(request, 'config_audio_estado.html', {'audio_estado': productos})


def edit_item_audio_estado(request, id):
    productos = EstadoAudio.objects.all().order_by('estadoAudio')
    item = EstadoAudio.objects.get(id=id)
    if request.method == "POST":
        formulario = AudioEstado(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item.estadoAudio = datos['estadoAudio']
            item.save()
        return render(request, 'config_audio_estado.html', {'audio_estado': productos})
    return render(request, 'config_audio_estado_edit.html', {'item': item})


def add_item_audio_estado(request):

    if request.method == "POST":
        formulario = AudioEstado(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item = EstadoAudio(estadoAudio=datos['estadoAudio'])
            item.save()
            productos = EstadoAudio.objects.all().order_by('estadoAudio')
            return render(request, 'config_audio_estado.html', {'audio_estado': productos})

    return render(request, 'config_audio_estado_add.html')

# ------ ALARMA PRODUCTO ------

def config_alarma_producto(request):
    productos = ProductoAlarmas.objects.all().order_by('productoAlarmas')
    return render(request, 'config_alarma_producto.html', {'alarma_producto': productos})


def del_item_alarma_producto(request, id):
    item = ProductoAlarmas.objects.get(id=id)
    item.delete()
    productos = ProductoAlarmas.objects.all().order_by('productoAlarmas')
    return render(request, 'config_alarma_producto.html', {'alarma_producto': productos})


def edit_item_alarma_producto(request, id):
    productos = ProductoAlarmas.objects.all().order_by('productoAlarmas')
    item = ProductoAlarmas.objects.get(id=id)
    if request.method == "POST":
        formulario = AlarmasProductos(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item.productoAlarmas = datos['productoAlarmas']
            item.save()
        return render(request, 'config_alarma_producto.html', {'alarma_producto': productos})
    return render(request, 'config_alarma_producto_edit.html', {'item': item})


def add_item_alarma_producto(request):

    if request.method == "POST":
        formulario = AlarmasProductos(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            item = ProductoAlarmas(productoAlarmas=datos['productoAlarmas'])
            item.save()
            productos = ProductoAlarmas.objects.all().order_by('productoAlarmas')
            return render(request, 'config_alarma_producto.html', {'alarma_producto': productos})

    return render(request, 'config_alarma_producto_add.html')
