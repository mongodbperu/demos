#! /usr/bin/python
# -*- coding: UTF-8-*-

__author__ = 'calujord'

from django import forms
from frontend.models import *

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=20, label=("Nombre"))
    apellido = forms.CharField(max_length=220, min_length=3, label=("Apellido"))
    direccion = forms.CharField(max_length=220, min_length=3, label=("Dirección"))
    telefono = forms.CharField(max_length=220, min_length=3, label=("Teléfono"))
    ciudad = forms.CharField(max_length=220, min_length=3, label=("Ciudad"))
    pais = forms.ModelChoiceField(queryset=Pais.objects.all())

    def __init__(self,*args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = "form-control"
        self.fields['apellido'].widget.attrs['class'] = "form-control"
        self.fields['direccion'].widget.attrs['class'] = "form-control"
        self.fields['telefono'].widget.attrs['class'] = "form-control"
        self.fields['ciudad'].widget.attrs['class'] = "form-control"
        self.fields['pais'].widget.attrs['class'] = "form-control"

    def get_nombre(self):
        return self.data["nombre"]
    def get_apellido(self):
        return self.data["apellido"]
    def get_direccion(self):
        return self.data["apellido"]
    def get_telefono(self):
        return self.data["apellido"]
    def get_ciudad(self):
        return self.data["apellido"]
    def get_pais(self):
        return Pais.objects.get(id=self.data["pais"])