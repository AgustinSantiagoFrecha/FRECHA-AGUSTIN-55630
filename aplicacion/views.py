from django.shortcuts import render, redirect
from.models import *
from django.http import HttpResponse
from .forms import *
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import UpdateView


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *

def home(request):
    return render(request, "aplicacion/home.html")

def acercaDeMi(request):
    return render(request, 'aplicacion/acercaDeMi.html')

@login_required
def clientes(request):
    contexto = {'clientes': Cliente.objects.all(), 'titulo' : 'Listado de Clientes'}
    return render(request, "aplicacion/clientes.html", contexto)

@login_required
def vehiculos(request):
    contexto = {'vehiculos': Vehiculo.objects.all(), 'titulo' : 'Listado de Vehículos'}
    return render(request, "aplicacion/vehiculos.html", contexto)

@login_required
def mecanicos(request):
    contexto = {'mecanicos': Mecanico.objects.all(), 'titulo' : 'Listado de Mecánicos'}
    return render(request, "aplicacion/mecanicos.html", contexto)


def productos(request):
    contexto = {'productos': Producto.objects.all(), 'titulo' : 'Listado de Productos'}
    return render(request, "aplicacion/productos.html", contexto)

def autosVenta(request):
    contexto = {'autosVenta': AutosVenta.objects.all(), 'titulo' : 'Listado de Vehículos en venta'}
    return render(request, "aplicacion/autosVenta.html", contexto)

@login_required
def clientesForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'],
                          telefono=request.POST['telefono'],
                          mail=request.POST['mail'])
        cliente.save()
        return HttpResponse("Se grabo con exito el vehiculo")
    return render(request, "aplicacion/clienteForm.html")

@login_required
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

@login_required
def mecanicoForm3(request):
    if request.method == "POST":
        miForm = MecanicoForm(request.POST)
        if miForm.is_valid():
            mecanico_nombre = miForm.cleaned_data.get('nombre')
            mecanico_telefono = miForm.cleaned_data.get('telefono')
            mecanico_mail = miForm.cleaned_data.get('mail')
            mecanico_especialidad = miForm.cleaned_data.get('especialidad')
            mecanico = Mecanico(nombre=mecanico_nombre,
                              telefono=mecanico_telefono,
                              mail=mecanico_mail,
                              especialidad=mecanico_especialidad)
            mecanico.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = MecanicoForm()

    return render(request, "aplicacion/mecanicoForm3.html", {"form":miForm})

@login_required
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

@login_required
def autosVenta_form(request):
    if request.method == "POST":
        miForm = AutosVentaForm(request.POST)
        if miForm.is_valid():
            autosVenta_marca = miForm.cleaned_data.get('marca')
            autosVenta_modelo = miForm.cleaned_data.get('modelo')
            autosVenta_anio = miForm.cleaned_data.get('anio') 
            autosVenta_kilometraje = miForm.cleaned_data.get('kilometraje')
            autosVenta_precio = miForm.cleaned_data.get('precio')
            
            autosVenta = AutosVenta(marca=autosVenta_marca,
                                    modelo=autosVenta_modelo,
                                    anio=autosVenta_anio, 
                                    kilometraje=autosVenta_kilometraje,
                                    precio=autosVenta_precio)
            autosVenta.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = AutosVentaForm()

    return render(request, "aplicacion/autosVentaForm.html", {"form": miForm})

@login_required
def producto_form(request):
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_tipo_producto = miForm.cleaned_data.get('tipo_producto')
            producto_marca = miForm.cleaned_data.get('marca')
            producto_precio = miForm.cleaned_data.get('precio')  
            
            producto = Producto(tipo_producto=producto_tipo_producto,
                                    marca=producto_marca,
                                    precio=producto_precio)
            producto.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = ProductoForm()

    return render(request, "aplicacion/Producto_form.html", {"form": miForm})


@login_required
def buscarVehiculos(request):
    return render(request, "aplicacion/buscarVehiculos.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        vehiculos = Vehiculo.objects.filter(modelo__icontains=patron)
        contexto = {"vehiculos": vehiculos, 'titulo': f'Modelos de Vehículos que tienen el patron= "{patron}"'}
        return render(request,"aplicacion/vehiculos.html", contexto)
    return HttpResponse("No se ingreso nada.")

@login_required
def modifMecanico(request, id_mecanico):
    mecanico = Mecanico.objects.get(id=id_mecanico)
    if request.method == "POST":
        miForm = MecanicoForm(request.POST)
        if miForm.is_valid():
            mecanico.nombre = miForm.cleaned_data.get('nombre')
            mecanico.telefono = miForm.cleaned_data.get('telefono')
            mecanico.mail = miForm.cleaned_data.get('mail')
            mecanico.especialidad = miForm.cleaned_data.get('especialidad')
            mecanico.save()
            return redirect(reverse_lazy('mecanicos'))

    else:
        miForm = MecanicoForm(initial={
            'nombre': mecanico.nombre,
            'telefono': mecanico.telefono,
            'email': mecanico.mail,
            'especialidad': mecanico.especialidad,
        })
    return render(request, "aplicacion/mecanicoForm3.html", {"form":miForm})

@login_required
def deleteMecanico(request, id_mecanico):
    mecanico = Mecanico.objects.get(id=id_mecanico)
    mecanico.delete()
    return redirect(reverse_lazy('mecanicos'))

@login_required
def modifCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get('nombre')
            cliente.telefono = miForm.cleaned_data.get('telefono')
            cliente.mail = miForm.cleaned_data.get('mail')
            cliente.save()
            return redirect(reverse_lazy('clientes'))

    else:
        miForm = ClienteForm(initial={
            'nombre': cliente.nombre,
            'telefono': cliente.telefono,
            'email': cliente.mail,
        })
    return render(request, "aplicacion/clienteForm2.html", {"form":miForm})

@login_required
def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))

@login_required
def modifVehiculo(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id=id_vehiculo)
    if request.method == "POST":
        miForm = VehiculoForm(request.POST)
        if miForm.is_valid():
            vehiculo.marca = miForm.cleaned_data.get('marca')
            vehiculo.modelo = miForm.cleaned_data.get('modelo')
            vehiculo.ano = miForm.cleaned_data.get('ano')
            vehiculo.propietario = miForm.cleaned_data.get('propietario')
            vehiculo.problema = miForm.cleaned_data.get('problema')

            vehiculo.save()
            return redirect(reverse_lazy('vehiculos'))

    else:
        miForm = VehiculoForm(initial={
            'marca': vehiculo.marca,
            'modelo': vehiculo.modelo,
            'ano': vehiculo.ano,
            'propietario': vehiculo.propietario,
            'problema': vehiculo.problema,
        })
    return render(request, "aplicacion/vehiculoForm4.html", {"form":miForm})

@login_required
def deleteVehiculo(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id=id_vehiculo)
    vehiculo.delete()
    return redirect(reverse_lazy('vehiculos'))

@login_required
def modifAutoVenta(request, id_autosVenta):
    autosVenta = AutosVenta.objects.get(id=id_autosVenta)
    if request.method == "POST":
        miForm = AutosVentaForm(request.POST)
        if miForm.is_valid():
            autosVenta.marca = miForm.cleaned_data.get('marca')
            autosVenta.modelo = miForm.cleaned_data.get('modelo')
            autosVenta.anio = miForm.cleaned_data.get('anio')
            autosVenta.kilometraje = miForm.cleaned_data.get('kilometraje')
            autosVenta.precio = miForm.cleaned_data.get('precio')
            
            autosVenta.save()
            return redirect(reverse_lazy('autosVenta'))

    else:
        miForm = AutosVentaForm(initial={
            'marca': autosVenta.marca,
            'modelo': autosVenta.modelo,
            'anio': autosVenta.anio,
            'kilometraje': autosVenta.kilometraje,
            'precio': autosVenta.precio,
        })
    return render(request, "aplicacion/autosVentaForm_form.html", {"form": miForm})

@login_required
def deleteAutoVenta(request, id_autosVenta):
    autosVenta = AutosVenta.objects.get(id=id_autosVenta)
    autosVenta.delete()
    return redirect(reverse_lazy('autosVenta'))

@login_required
def modifProducto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto.tipo_producto = miForm.cleaned_data.get('tipo_producto')
            producto.marca = miForm.cleaned_data.get('marca')
            producto.precio = miForm.cleaned_data.get('precio')
            
            producto.save()
            return redirect(reverse_lazy('productos'))

    else:
        miForm = ProductoForm(initial={
            'tipo_producto': producto.tipo_producto,
            'marca': producto.marca,
            'precio': producto.precio,
        })
    return render(request, "aplicacion/Producto_form.html", {"form": miForm})

@login_required
def deleteProducto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect(reverse_lazy('productos'))

#__________________________Login____________________________#

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    Avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f"Bienvenido {usuario}!"})
            else:
                return render(request, "aplicacion/base.html", {'form': miForm, 'mensaje': "Los datos son inválidos"})
        else:
            return render(request, "aplicacion/base.html", {'form': miForm, 'mensaje': "Los datos son inválidos"})
    
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = RegistroUsuariosForm()

    return render(request, "aplicacion/registro.html", {"form": miForm})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html")
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar=Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})






