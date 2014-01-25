# -*- coding: utf-8 -*-
from django.contrib.auth.models import *
from librerias import tokens
from mongoengine import *


class Persona(Document):
    id = StringField(default=tokens.get_identificador())
    nombre = StringField()
    apellido = StringField()
    hobbies = ListField(StringField())
