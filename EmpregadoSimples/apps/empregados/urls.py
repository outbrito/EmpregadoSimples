# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''
# Python Imports
# Django Imports
from django.conf.urls import patterns, url, include
# Project Imports


urlpatterns = patterns('apps.empregados.views',
                       # Cadastro
                       url(r'^novo/?$', 'novo'),
                       url(r'^(\d*)/?$', 'empregado'),
                       # Processo de contrato
                       url(r'^(\d*)/c/?$', 'contratacao'),
#                       url(r'^(\d*)/c/contrato/?$', 'contrato'),
                       url(r'^(\d*)/c/ctps/?$', 'ctps'),
                       url(r'^(\d*)/c/ctps_pdf/?$', 'ctps_pdf'),
                       
                       url(r'^(\d*)/c/contrato/?$', 'contrato'),
                       url(r'^(\d*)/c/contrato_pdf/?$', 'contrato_pdf'),
                       # Processo mensal
                       url(r'^(\d*)/m/?$', 'mensal'),
                       url(r'^(\d*)/m/ponto/(\d{0,2})/(\d{4})/?$', 'ponto'),
                       url(r'^(\d*)/m/ponto_pdf/(\d{0,2})/(\d{4})/?$', 'ponto_pdf'),
#                       url(r'^(\d*)/m/contracheque/?$', ''),
#                       url(r'^(\d*)/m/inss/?$', ''),
#                       url(r'^(\d*)/m/fgts/?$', ''),
                       )