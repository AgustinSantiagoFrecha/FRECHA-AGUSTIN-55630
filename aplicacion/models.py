from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    mail = models.EmailField()



    def __str__(self):
        return f"{self.nombre}"

class Mecanico(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    mail = models.EmailField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    propietario = models.CharField(max_length=50)
    problema = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.modelo}, {self.propietario}"
    
class AutosVenta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    kilometraje = models.PositiveBigIntegerField()
    precio = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.modelo}, {self.marca}"
    
class Producto(models.Model):
    tipo_producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.marca} - {self.tipo_producto}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
class imagenes(models.Model):
    imagen = models.ImageField(upload_to="Autos")
    accion = models.ForeignKey(AutosVenta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.accion} {self.imagen}"