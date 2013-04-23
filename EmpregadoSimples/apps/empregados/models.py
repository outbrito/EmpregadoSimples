# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.db import models
from django.contrib.auth.models import User
# Project Imports

SEX_CHOICES = (
               ('M', 'Masc'),
               ('F', 'Fem')
               )


class Empregado(models.Model):
    # Dados Pessoais
    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    data_nascimento = models.DateField("Data de Nascimento")
    sexo = models.CharField("Sexo", max_length=1, choices=SEX_CHOICES)
    rg = models.CharField("RG", max_length=20)
    cpf = models.CharField("CPF", max_length=20)
    ctps = models.CharField("CTPS", max_length=20)
    pis = models.CharField("PIS", max_length=20)
    endereco = models.CharField("Endereco", max_length=100)
    telefone = models.CharField("Telefone", max_length=10)
    email = models.EmailField("E-mail", null=True, blank=True)
    data_admissao = models.DateField("Data de Admissão", max_length=20)
    data_demissao = models.DateField("Data de Demissão", max_length=20, null=True, blank=True)
    
    # Dados de trabalho
    funcao = models.ForeignKey("Funcao")
    salario = models.FloatField("Salário")
    horas_semana = models.IntegerField("Horas de Trabalho/Semana")
    custo_transporte = models.FloatField("Custo de Transporte", null=True, blank=True)
    transporte_dia = models.IntegerField("Transportes Utilizados/dia", null=True, blank=True)
    
    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    conta = models.ForeignKey(User, related_name="empregados")
    
    def __unicode__(self):
        return "%d: %s" %(self.id, self.nome) 
     
     
class Funcao(models.Model):
    nome = models.CharField("Nome", max_length=20)
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Funcoes"