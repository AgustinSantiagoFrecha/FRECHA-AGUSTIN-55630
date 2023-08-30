from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    mail = forms.EmailField(required=True)

class MecanicoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)
    mail = forms.EmailField(label="Email", required=True)
    especialidad = forms.CharField(label="Especialidad", max_length=50, required=True)

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    ano = forms.IntegerField(required=True)
    propietario = forms.CharField(max_length=50, required=True)
    problema = forms.CharField(max_length=50, required=True)

class AutosVentaForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    anio = forms.IntegerField(required=True)
    kilometraje = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)

class ProductoForm(forms.Form):
    tipo_producto = forms.CharField(max_length=50, required=True)
    marca = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

