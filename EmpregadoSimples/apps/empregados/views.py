# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import render_to_response, RequestContext
# Project Imports
from forms import FormEmpregado
from models import Empregado


def novo(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FormEmpregado(request.POST)
        if form.is_valid(): # All validation rules pass
            e = form.save(commit=False)
            e.conta = request.user
            e.save()
            
            ret = empregado(request, e.id)
        else:
            ret = render_to_response('empregados/novo.html',
                              {'form': form},
                              context_instance=RequestContext(request)
                              )
    else:
        form = FormEmpregado() # An unbound form
        ret = render_to_response('empregados/novo.html',
                              {'form': form},
                              context_instance=RequestContext(request)
                              ) 
    
    return ret


def empregado(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        form = FormEmpregado(instance=e)
        ret = render_to_response('empregados/empregado.html',
                              {
                               'form': form,
                               'empregado': e
                               
                               },
                              context_instance=RequestContext(request)
                              )
    except Empregado.DoesNotExist:
        msg = "Empregado '%d' não existe ou não está associado a esta conta." %id
        ret = render_to_response('home/home.html',
                              {
                               'error': msg
                               },
                              context_instance=RequestContext(request)
                              )
    
    return ret