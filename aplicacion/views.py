from django.shortcuts import render
from.models import Cliente, Mecanico, Vehiculo
from django.http import HttpResponse
from .forms import *
# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def clientes(request):
    contexto = {'clientes': Cliente.objects.all(), 'titulo' : 'Listado de Clientes'}
    return render(request, "aplicacion/clientes.html", contexto)

def vehiculos(request):
    contexto = {'vehiculos': Vehiculo.objects.all(), 'titulo' : 'Listado de Vehiculos'}
    return render(request, "aplicacion/vehiculos.html", contexto)

def mecanicos(request):
    contexto = {'mecanicos': Mecanico.objects.all(), 'titulo' : 'Listado de Mecanicos'}
    return render(request, "aplicacion/mecanicos.html", contexto)

def clientesForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'],
                          telefono=request.POST['telefono'],
                          mail=request.POST['mail'])
        cliente.save()
        return HttpResponse("Se grabo con exito el vehiculo")
    return render(request, "aplicacion/clienteForm.html")

def clienteForm2(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get('nombre')
            cliente_telefono = miForm.cleaned_data.get('telefono')
            cliente_email = miForm.cleaned_data.get('email')
            cliente = Cliente(nombre=cliente_nombre,
                              telefono=cliente_telefono,
                              email=cliente_email)
            cliente.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm.html", {"form":miForm})