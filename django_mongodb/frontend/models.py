# -*- coding: utf-8 -*-
from django.contrib.auth.models import *
from librerias import tokens
from mongoengine import *


class Pais(Document):
    id = StringField(default=tokens.get_identificador())
    nombre = StringField()

    def __unicode__(self):
        return self.nombre


class Persona(Document):
    id = StringField(default=tokens.get_identificador())
    nombre = StringField()
    apellido = StringField()
    direccion = StringField()
    telefono = StringField()
    ciudad = StringField()
    pais_origen = ReferenceField("Pais")
    hobbies = ListField(StringField())
