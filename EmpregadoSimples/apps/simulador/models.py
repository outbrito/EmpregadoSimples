# -*- coding: UTF-8 -*-

'''
Created on 25/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.db import models
# Project Imports


class Aliquotas(models.Model):
    
    vigencia = models.DateField()
    faixa_inicio = models.FloatField()
    faixa_fim = models.FloatField()
    inss_empregado = models.CharField(max_length=200)
    inss_empregador = models.CharField(max_length=200)
    fgts_empregado = models.FloatField()
    fgts_empregador = models.FloatField()
    
    
    def __unicode__(self):
        return "%.2f ate %.2f" %(self.faixa_inicio, self.faixa_fim) 
    
    class Meta:
        verbose_name_plural = "Aliquotas"
    

def getAliquotas(salario):
    return Aliquotas.objects.get(faixa_inicio__lte=salario, faixa_fim__gte=salario)

def getInssEmpregado (salario):
    aliquotas = Aliquotas.objects.get(faixa_inicio__lte=salario, faixa_fim__gte=salario)
    return eval(aliquotas.inss_enpregado)

    
def getInssEmpregador (salario):
    aliquotas = Aliquotas.objects.get(faixa_inicio__lte=salario, faixa_fim__gte=salario)
    return eval(aliquotas.inss_enpregador)

    