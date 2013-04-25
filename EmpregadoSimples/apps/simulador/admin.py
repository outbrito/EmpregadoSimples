# -*- coding: UTF-8 -*-

'''
Created on 25/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.contrib import admin
# Project Imports
from models import *


class AliquotasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Aliquotas, AliquotasAdmin)