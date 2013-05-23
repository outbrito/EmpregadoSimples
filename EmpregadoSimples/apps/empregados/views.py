# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
from time import strftime
from calendar import Calendar
# Django Imports
from django.http.response import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
# Project Imports
from forms import FormEmpregado
from models import Empregado
from tools import render_to_pdf
from settings import PAYPAL_RECEIVER_EMAIL
from paypal.standard.forms import PayPalPaymentsForm


@login_required
def novo(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FormEmpregado(request.POST)
        if form.is_valid(): # All validation rules pass
            e = form.save(commit=False)
            e.conta = request.user
            e.save()
            
            ret = HttpResponseRedirect(reverse('apps.empregados.views.empregado', args=(e.id,)))
        else:
            ret = {'form': form, 'error': "Verifique os erros abaixo"}
            
    else:
        if request.user.perfil.licencas_livres() > 0:
            form = FormEmpregado() # An unbound form
            
            ret = {'form': form}
        else:
            ret = {'alert': "Você não possui licenças livres para cadastrar um novo Empregado. Por favor, acesse o menu com seu nome acima e escolha 'Licenças' para adicionar mais licenças de cadastro à sua conta."}
    
    return render_to_response('empregados/novo.html',
                              ret,
                              context_instance=RequestContext(request)
                              )


@login_required
def contratacao(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        form = FormEmpregado(instance=e)
        
        # Create the instance.
        ret = render_to_response('empregados/contratacao.html',
                              {
                               'form': form,
                               'empregado': e,
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


@login_required
def empregado(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        form = FormEmpregado(instance=e)
        
        invoice_id = "empregadosimples.com-date=%s-uid=%d-eid=%d" %(strftime("%Y%m%d"), request.user.id, e.id)
        # What you want the button to do.
        paypal_dict = {
            "lc": "pt",
            "business": PAYPAL_RECEIVER_EMAIL,
            "amount": "5.00",
            "currency_code": "BRL",
            "item_name": "Cadastro de Empregado",
            "invoice": invoice_id,
            "notify_url": "https://empregadosimples.com/_14py4p0nr0t3r/",
            "return_url": reverse('apps.empregados.views.empregado', args=(e.id,)),
            "cancel_return": reverse('apps.empregados.views.empregado', args=(e.id,)),
    
        }
    
        # Create the instance.
        form_pay = PayPalPaymentsForm(button_type='subscribe', initial=paypal_dict)
        
        ret = render_to_response('empregados/empregado.html',
                              {
                               'form': form,
                               'empregado': e,
                               'form_pay': form_pay
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


@login_required
def ctps(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        
        ret = render_to_response('empregados/ctps_pdf.html',
                              {
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


@login_required
def ctps_pdf(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        
        ret = render_to_pdf('empregados/ctps_pdf.html',
                              {
                               'empregado': e,
                               'user': request.user
                               },
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


@login_required
def contrato(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        
        ret = render_to_response('empregados/contrato_pdf.html',
                              {
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


@login_required
def contrato_pdf(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        
        ret = render_to_pdf('empregados/contrato_pdf.html',
                              {
                               'empregado': e,
                               'user': request.user
                               }
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


@login_required
def mensal(request, id):
    id = int(id)
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        form = FormEmpregado(instance=e)
        
        # Create the instance.
        ret = render_to_response('empregados/mensal.html',
                              {
                               'form': form,
                               'empregado': e,
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


@login_required
def ponto(request, id, mes, ano):
    id = int(id)
    
    c = Calendar()
    gen_dates = c.itermonthdates(int(ano), int(mes))
    dates = []
    
    for d in gen_dates:
        if d.month == int(mes):
            dates.append(d)
    
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        
        ret = render_to_response('empregados/ponto.html',
                              {
                               'empregado': e,
                               'dates': dates,
                               'user': request.user
                               }
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


@login_required
def ponto_pdf(request, id, mes, ano):
    id = int(id)
    
    c = Calendar()
    gen_dates = c.itermonthdates(int(ano), int(mes))
    dates = []
    
    for d in gen_dates:
        if d.month == int(mes):
            dates.append(d)
    
    try:
        e = Empregado.objects.get(id=id, conta__id=request.user.id)
        
        ret = render_to_pdf('empregados/ponto.html',
                              {
                               'empregado': e,
                               'dates': dates,
                               'user': request.user
                               }
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