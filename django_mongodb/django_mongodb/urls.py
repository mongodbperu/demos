# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.inicio', name='inicio'),
    url(r'^ingresar/$', 'frontend.views.agregar_nueva_persona', name='ingreso'),
    # url(r'^django_mongodb/', include('django_mongodb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static',
    (r'^static/(?P<path>.*)$', 'serve',
     {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)