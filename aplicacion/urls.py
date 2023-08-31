from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', home, name="home" ),
    path('acercaDeMi/', acercaDeMi, name="acercaDeMi"),
    path('clientes/', clientes, name="clientes" ),
    path('vehiculos/', vehiculos, name="vehiculos" ),
    path('mecanicos/', mecanicos, name="mecanicos" ),
    path('productos/', productos, name="productos" ),
    path('autosVenta/', autosVenta, name="autosVenta" ),

    path('cliente_form2/', clienteForm2, name="cliente_form2"),
    path('mecanico_form3/', mecanicoForm3, name="mecanico_form3"),
    path('vehiculo_form4/', vehiculoForm4, name="vehiculo_form4"),
    path('autosVenta_form/', autosVenta_form, name="autosVenta_form"),
    path('producto_form/', producto_form, name="producto_form"),
    
    path('buscar_vehiculo/', buscarVehiculos, name="buscar_vehiculo"),
    path('buscar2/', buscar2, name="buscar2"),
    
    path('modifMecanico/<id_mecanico>/', modifMecanico, name="modifMecanico"),
    path('deleteMecanico/<id_mecanico>/', deleteMecanico, name="deleteMecanico"),

    path('modifCliente/<id_cliente>/', modifCliente, name="modifCliente"),
    path('deleteCliente/<id_cliente>/', deleteCliente, name="deleteCliente"),

    path('modifVehiculo/<id_vehiculo>/', modifVehiculo, name="modifVehiculo"),
    path('deleteVehiculo/<id_vehiculo>/', deleteVehiculo, name="deleteVehiculo"),

    path('modifAutoVenta/<id_autosVenta>/', modifAutoVenta, name="modifAutoVenta"),
    path('deleteAutoVenta/<id_autosVenta>/', deleteAutoVenta, name="deleteAutoVenta"),

    path('modifProducto/<id_producto>/', modifProducto, name="modifProducto"),
    path('deleteProducto/<id_producto>/', deleteProducto, name="deleteProducto"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]
