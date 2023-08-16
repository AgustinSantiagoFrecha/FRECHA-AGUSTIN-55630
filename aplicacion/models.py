from django.db import models

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
    especilidad = models.CharField(max_length=50)

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