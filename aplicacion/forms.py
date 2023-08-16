from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    mail = forms.EmailField(required=True)