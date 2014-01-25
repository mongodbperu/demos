# -*- coding: utf-8 -*-

# +-----------------------------------------------------------------------------+
# |                                                                             |
# |     Autor:                  Carlos Jordán Murillo                           |
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
from django.core.urlresolvers import reverse
from frontend import forms


def inicio(request):
    personas = Persona.objects.all()
    return render_to_response("listado.html", {"listado": personas},
                              context_instance=RequestContext(request))


@csrf_exempt
def agregar_nueva_persona(request):
    formulario = forms.PersonaForm()
    if request.method == "POST":
        formulario = forms.PersonaForm(request.POST)
        if formulario.is_valid():
            persona = Persona(nombre=formulario.get_nombre(),
                              apellido=formulario.get_apellido())
            persona.save()
            messages.success(request,
                             "Su requerimiento fue realizado con exito")
            return HttpResponseRedirect(reverse("ingreso"))
    return render_to_response("ingresar.html", {"formulario": formulario},
                              context_instance=RequestContext(request))