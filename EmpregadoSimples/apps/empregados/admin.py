# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.contrib import admin
# Project Imports
from models import *


class EmpregadoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'id', 'nome')
    list_display_links = ('id', 'nome')


admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Funcao)

