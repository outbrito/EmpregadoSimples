# -*- coding: UTF-8 -*-

'''
Created on 26/04/2013

@author: ThiagoP
'''

# Python Imports
from datetime import date, timedelta
import logging
# Django Imports
from django.db import models
from django.contrib.auth.models import User
# Project Imports
from paypal.standard.ipn.signals import subscription_signup, subscription_payment


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
    endereco = models.CharField("Endereco", null=True, blank=True, max_length=100)
    numero = models.IntegerField("Numero", null=True, blank=True)
    complemento = models.CharField("Complemento", null=True, blank=True, max_length=100)
    cidade = models.ForeignKey("Cidade", null=True, blank=True)
    estado = models.ForeignKey("Estado", null=True, blank=True)
    estabelecimento = models.ForeignKey("Estabelecimento", null=True, blank=True)
    
    licencas = models.IntegerField("Licenças", default=1)
    expiracao = models.DateField("Data de Expiração", default=date.today()+timedelta(days=30))
    
    def expired(self):
        return date.today() > self.expiracao
    
    def licencas_livres(self):
        return self.licencas - self.usuario.empregados.count()    
    
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
    
    
############################### SIGNALS #####################################################
logger = logging.getLogger('payments')
def registered(sender, **kwargs):
    ipn_obj = sender
    logger.info("subscription_signup: " + ipn_obj.custom)
    # Undertake some action depending upon `ipn_obj`.
    d = eval(ipn_obj.custom)
    
    user = User.objects.get(id=d["user"])
    user.perfil.licencas = ipn_obj.quantity
    user.perfil.save()
    
def paid(sender, **kwargs):
    ipn_obj = sender
    logger.info("payment_was_successful: " + ipn_obj.custom)
    # Undertake some action depending upon `ipn_obj`.
    d = eval(ipn_obj.custom)
    
    user = User.objects.get(id=d["user"])
    user.perfil.expiracao = date.today()+timedelta(days=30)
    user.perfil.save()
    
def cancel(sender, **kwargs):
    ipn_obj = sender
    # Undertake some action depending upon `ipn_obj`.
    d = eval(ipn_obj.custom)
    
    user = User.objects.get(id=d["user"])
    user.licencas = 0
    user.save()
            

subscription_signup.connect(registered)
subscription_payment.connect(paid)
#subscription_cancel.connect(cancel)
#subscription_eot.connect(cancel)