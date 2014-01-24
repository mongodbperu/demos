#! /usr/bin/python
# -*- coding: UTF-8-*-

# +-----------------------------------------------------------------------------+
# |                                                                             |
# |     Nombre archivo:         registrar_hoteles.py                                        |
# |     Autor:                  Carlos Jordán Murillo                           |
# |                                                                             |
# |     Descripción:                                                            |
# |     Sirve para poder validar y verificar cuando un usuario intenta ingresar |
# |     en los templates.                                                       |
# |                                                                             |
# +-----------------------------------------------------------------------------+

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import *
import datetime
from django.contrib.auth import login, logout
from django.contrib import messages
from frontend.models import *

def inicio(request):
    personas = Persona.objects.all()
    return render_to_response("listado.html",{"listado": personas},
                              context_instance=RequestContext(request))