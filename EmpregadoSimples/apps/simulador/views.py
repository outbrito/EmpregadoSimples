# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
# Project Imports
from EmpregadoSimples.libs.Calc import Calc
from EmpregadoSimples.apps.empregados.models import Empregado 


def simulate_contract(request):
    return render_to_response("simulador/simular_contratacao.html",
                              {},
                              context_instance=RequestContext(request)
                              )
    

def simulated_contract(request, empregado=None):
    calc = Calc()
    
    if empregado:
        calc.initFromFuncionario(Empregado.objects.get(id=empregado))
    if request.method == 'POST':
        salary = request.POST.get('salario', 0) or 0
        semanal_journey = request.POST.get('jornada_semanal', 0) or 0
        transport_cost = request.POST.get('custo_transporte', 0) or 0
        transport_xtimes_day = request.POST.get('transporte_por_dia', 0) or 0
        week_days = request.POST.get('dias_semana', 0) or 0

        calc.init(salary, semanal_journey, transport_cost, transport_xtimes_day)
        
    return render_to_response("simulador/contratacao_simulada.html",
                              {
                               'calc': calc
                              },
                              context_instance=RequestContext(request)
                              )