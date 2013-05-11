# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'contas/login.html'}),
     url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
     
     url(r'^registrar/?', 'apps.contas.views.registrar'),
    
     url(r'^simulador/', include('apps.simulador.urls')),
     url(r'^contato/', include('apps.contato.urls')),
     url(r'^conta/', include('apps.contas.urls')),
     url(r'^empregado/', include('apps.empregados.urls')),
     
     url(r'^_14py4p0nr0t3r/', include('paypal.standard.ipn.urls')),
     
     url(r'^/?', include('apps.home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
