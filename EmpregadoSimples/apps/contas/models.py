# -*- coding: UTF-8 -*-

'''
Created on 26/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.db import models
from django.contrib.auth.models import User
# Project Imports


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, related_name="perfil")
    expiracao = models.DateField("Data de Expiração")
    endereco = models.CharField("Endereco", max_length=100)
    numero = models.IntegerField("Numero")
    complemento = models.CharField("Complemento", max_length=100)
    cidade = models.ForeignKey("Cidade")
    estado = models.ForeignKey("Estado")
    cpf_cnpj = models.CharField("CPF/CNPJ", max_length=20)
    estabelecimento = models.ForeignKey("Estabelecimento")
    
        
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