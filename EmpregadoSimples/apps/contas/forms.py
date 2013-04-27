# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.forms import ModelForm
# Project Imports
from models import PerfilUsuario
from EmpregadoSimples.libs.html5forms.fields import Html5CharField, Html5EmailField, Html5DateField,\
    Html5RangeField, Html5NumberField, Html5IntegerField

class FormPerfil(ModelForm):
    endereco = Html5CharField(placeholder="Endereço...")
    numero = Html5IntegerField(placeholder="Numero...")
    complemento = Html5CharField(placeholder="Complemento...")
    cpf_cnpj = Html5CharField(placeholder="CPF/CNPJ...")
    
    class Meta:
        model = PerfilUsuario
        exclude = ('usuario', 'expiracao')
        

class FormUsuario(ModelForm):
    first_name = Html5CharField(placeholder="Nome...")
    last_name = Html5CharField(placeholder="Sobrenome...", required=False)
    cpf_cnpj = Html5CharField(placeholder="CPF/CNPJ...")
    
    class Meta:
        model = PerfilUsuario
        exclude = ('usuario', 'expiracao')