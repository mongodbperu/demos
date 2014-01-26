# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import *
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
                              direccion = formulario.get_direccion(),
                              telefono = formulario.get_telefono(),
                              ciudad = formulario.get_ciudad(),
                              pais = formulario.get_pais(),
                              apellido=formulario.get_apellido())
            persona.save()
            messages.success(request,
                             "Su requerimiento fue realizado con exito")
            return HttpResponseRedirect(reverse("ingreso"))
    return render_to_response("ingresar.html", {"formulario": formulario},
                              context_instance=RequestContext(request))


# python manage.py syncdb
@csrf_exempt
def editar_persona(request, id):
    persona = Persona.objects.get(id=id)
    formulario = forms.PersonaForm(initial={
        "nombre": persona.nombre,
        "apellido": persona.apellido,
        "direccion": persona.direccion,
        "telefono": persona.telefono,
        "ciudad": persona.ciudad,
        "pais": persona.pais_origen,

    })
    if request.method == "POST":
        formulario = forms.PersonaForm(request.POST)
        if formulario.is_valid():
            persona.nombre = formulario.get_nombre()
            persona.direccion = formulario.get_direccion()
            persona.telefono = formulario.get_telefono()
            persona.ciudad = formulario.get_ciudad()
            persona.apellido = formulario.get_apellido()
            persona.pais_origen = formulario.get_pais()
            persona.save()

            messages.success(request, "Se modifico exitosamente")
            return HttpResponseRedirect(reverse("editar_persona", kwargs={"id": persona.id}))

    return render_to_response("editar_persona.html", {"persona": persona,
                                  "formulario": formulario},
                              context_instance=RequestContext(request))
