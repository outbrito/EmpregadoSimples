# -*- coding: UTF-8 -*-

'''
Created on 26/04/2013

@author: ThiagoP
'''

# Python Imports
from datetime import date, timedelta
# Django Imports
from django.db import models
from django.contrib.auth.models import User
# Project Imports


TIPO_INSCRICAO = (
                  (1, 'Free'),
                  (2, 'Subscricao Mensal'),
                  (3, 'Subscricao Permanente')
                  )

TIPO_PAGAMENTO = (
                  ("Pay Pal", "Pay Pal"),
                  )

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, related_name="perfil", primary_key=True)
    cpf_cnpj = models.CharField("CPF/CNPJ", max_length=20, null=True, blank=True)
#    tipo_inscricao = models.IntegerField("Tipo de Inscrição", choices=TIPO_INSCRICAO, default=1)
#    expiracao = models.DateField("Data de Expiração", default=date.today()+timedelta(days=30))
    endereco = models.CharField("Endereco", null=True, blank=True, max_length=100)
    numero = models.IntegerField("Numero", null=True, blank=True)
    complemento = models.CharField("Complemento", null=True, blank=True, max_length=100)
    cidade = models.ForeignKey("Cidade", null=True, blank=True)
    estado = models.ForeignKey("Estado", null=True, blank=True)
    estabelecimento = models.ForeignKey("Estabelecimento", null=True, blank=True)
    
    def expired(self):
        if self.tipo_inscricao == 3:
            ret = False
        else:
            ret = date.today() > self.expiracao
        return ret
    
    def __unicode__(self):
        return self.usuario.first_name
    
        
class Cidade(models.Model):
    nome = models.CharField("Nome", max_length=20)
    
    def __unicode__(self):
        return self.nome
    

class Estado(models.Model):
    nome = models.CharField("Nome", max_length=20)
    
    def __unicode__(self):
        return self.nome
    
    
class Estabelecimento(models.Model):
    nome = models.CharField("Nome", max_length=20)
    
    def __unicode__(self):
        return self.nome
    
    
class Subscricao(models.Model):
    usuario = models.ForeignKey(User, related_name="subscricoes")
    tipo_pagamento = models.IntegerField("Tipo", choices=TIPO_PAGAMENTO)
    chave = models.CharField("Chave", max_length=20)
    licencas = models.IntegerField("Licenças")
    ativa = models.BooleanField("Ativa")
    validade = models.DateField("Validade")