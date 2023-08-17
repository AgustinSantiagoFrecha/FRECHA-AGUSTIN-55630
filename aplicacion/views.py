from django.shortcuts import render
from.models import *
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
            cliente_mail = miForm.cleaned_data.get('mail')
            cliente = Cliente(nombre=cliente_nombre,
                              telefono=cliente_telefono,
                              mail=cliente_mail)
            cliente.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm2.html", {"form":miForm})


def mecanicoForm3(request):
    if request.method == "POST":
        miForm = MecanicoForm(request.POST)
        if miForm.is_valid():
            mecanico_nombre = miForm.cleaned_data.get('nombre')
            mecanico_telefono = miForm.cleaned_data.get('telefono')
            mecanico_mail = miForm.cleaned_data.get('mail')
            mecanico_especialidad = miForm.cleaned_data.get('especilidad')
            mecanico = Mecanico(nombre=mecanico_nombre,
                              telefono=mecanico_telefono,
                              mail=mecanico_mail,
                              especilidad=mecanico_especialidad)
            mecanico.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = MecanicoForm()

    return render(request, "aplicacion/mecanicoForm3.html", {"form":miForm})

def vehiculoForm4(request):
    if request.method == "POST":
        miForm = VehiculoForm(request.POST)
        if miForm.is_valid():
            vehiculo_marca = miForm.cleaned_data.get('marca')
            vehiculo_modelo = miForm.cleaned_data.get('modelo')
            vehiculo_ano = miForm.cleaned_data.get('ano')
            vehiculo_propietario = miForm.cleaned_data.get('propietario')
            vehiculo_problema = miForm.cleaned_data.get('problema')
            vehiculo = Vehiculo(marca=vehiculo_marca,
                              modelo=vehiculo_modelo,
                              ano=vehiculo_ano,
                              propietario=vehiculo_propietario,
                              problema=vehiculo_problema)
            vehiculo.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = VehiculoForm()

    return render(request, "aplicacion/vehiculoForm4.html", {"form":miForm})

def buscarVehiculos(request):
    return render(request, "aplicacion/buscarVehiculos.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        vehiculos = Vehiculo.objects.filter(modelo__icontains=patron)
        contexto = {"vehiculos": vehiculos, 'titulo': f'Modelos de Vehiculos que tienen el patron= "{patron}"'}
        return render(request,"aplicacion/vehiculos.html", contexto)
    return HttpResponse("No se ingreso nada.")

