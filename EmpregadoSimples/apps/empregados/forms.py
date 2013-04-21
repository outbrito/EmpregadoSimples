# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.forms import ModelForm
# Project Imports
from models import Empregado
from EmpregadoSimples.libs.html5forms.fields import Html5CharField, Html5EmailField, Html5DateField

class FormEmpregado(ModelForm):
    nome = Html5CharField(placeholder="Nome do Empregado...", autofocus=True)
    sobrenome = Html5CharField(placeholder="Sobrenome do Empregado...")
    data_nascimento = Html5DateField()
    
    rg = Html5CharField(placeholder="Número do RG do Empregado...")
    cpf = Html5CharField(placeholder="Número do CPF do Empregado...")
    ctps = Html5CharField(placeholder="Número da Carteira Profissional do Empregado...")
    pis = Html5CharField(placeholder="Número do Cadastro no PIS do Empregado...")
    endereco = Html5CharField(placeholder="Endereço do Empregado")
    telefone = Html5CharField(placeholder="Telefone para Contato...")
    email = Html5EmailField(placeholder="E-mail do empregado, se houver...", required=False)

    data_admissao = Html5DateField()
    
    class Meta:
        model = Empregado
        exclude = ('data_cadastro', 'data_demissao', 'conta')