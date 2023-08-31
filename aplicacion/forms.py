from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email de usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", required=True)
    last_name = forms.CharField(label="Apellido", required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

class autosFormulario(forms.Form):
    imagen = forms.ImageField(required=True)