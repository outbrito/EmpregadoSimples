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


class CidadeAdmin(admin.ModelAdmin):
    pass

class EstadoAdmin(admin.ModelAdmin):
    pass


class EstabelecimentoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)