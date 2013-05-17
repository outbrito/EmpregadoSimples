# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('apps.contas.views',
                       url(r'^$', 'home'),
                       url(r'^pagamento/?$', 'pagamento'),
                       url(r'^licencas/?$', 'licencas'),
                       url(r'^cancelar/(\w)?$', 'cancelar'),
                       )