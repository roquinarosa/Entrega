from django import forms
from .models import Menu

class MenuFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()

class BuscaMenuForm(forms.Form):
    nombre = forms.CharField()