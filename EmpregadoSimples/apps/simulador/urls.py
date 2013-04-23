# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

from django.conf.urls import patterns, url


urlpatterns = patterns('EmpregadoSimples.apps.simulador.views',
                       url(r'^simular_contratacao/?$', 'simulate_contract'),
                       url(r'^contratacao_simulada/(?P<empregado>\d)?$', 'simulated_contract'),
                       )