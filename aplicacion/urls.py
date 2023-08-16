from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name="home" ),
    path('clientes/', clientes, name="clientes" ),
    path('vehiculos/', vehiculos, name="vehiculos" ),
    path('mecanicos/', mecanicos, name="mecanicos" ),

    path('cliente_form2/', clienteForm2, name="cliente_form2")
]
