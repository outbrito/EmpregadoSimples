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


class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_inscricao', 'expiracao')
    

admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Estabelecimento)
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)