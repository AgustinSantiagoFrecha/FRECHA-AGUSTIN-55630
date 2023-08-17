from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name="home" ),
    path('clientes/', clientes, name="clientes" ),
    path('vehiculos/', vehiculos, name="vehiculos" ),
    path('mecanicos/', mecanicos, name="mecanicos" ),

    path('cliente_form2/', clienteForm2, name="cliente_form2"),
    path('mecanico_form3/', mecanicoForm3, name="mecanico_form3"),
    path('vehiculo_form4/', vehiculoForm4, name="vehiculo_form4"),
    
    path('buscar_vehiculo/', buscarVehiculos, name="buscar_vehiculo"),
    path('buscar2/', buscar2, name="buscar2")
]
