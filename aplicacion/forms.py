from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    mail = forms.EmailField(required=True)

class MecanicoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    mail = forms.EmailField(required=True)
    especilidad = forms.CharField(max_length=50, required=True)

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    ano = forms.IntegerField(required=True)
    propietario = forms.CharField(max_length=50, required=True)
    problema = forms.CharField(max_length=50, required=True)