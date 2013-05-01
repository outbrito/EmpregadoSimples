# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('EmpregadoSimples.apps.contas.views',
                       url(r'^$', 'home'),
#                       url(r'^pagamento/?$', 'pagamento'),
#                       url(r'^pagamento/_14py4p0nr0t3r/$', 'paypal_return'),
                       )