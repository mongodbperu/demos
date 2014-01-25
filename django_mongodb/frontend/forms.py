# -*- coding: utf-8 -*-
from django import forms


class PersonaForm(forms.Form):

    nombre = forms.CharField(max_length=20, label=("Cédula, Ruc o pasaporte"))
    apellido = forms.CharField(max_length=220, min_length=3,
                               label=("Razón Social"))

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = "form-control"
        self.fields['apellido'].widget.attrs['class'] = "form-control"

    def get_nombre(self):
        return self.data["nombre"]

    def get_apellido(self):
        return self.data["apellido"]