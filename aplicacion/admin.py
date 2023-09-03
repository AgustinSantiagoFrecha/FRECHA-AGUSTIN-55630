from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Mecanico)
admin.site.register(Producto)
admin.site.register(AutosVenta)
admin.site.register(Turno)