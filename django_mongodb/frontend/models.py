# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import *
# Create your models here.
import random
from mongoengine.django.auth import User
import mongoengine
from librerias import tokens
from mongoengine import *


class Persona(Document):
    id = StringField(default=tokens.get_identificador())
    nombre = StringField()
    apellido = StringField()
    hobbies = ListField(StringField())
