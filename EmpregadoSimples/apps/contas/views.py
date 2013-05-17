# -*- coding: utf-8 -*-

'''
Created on 18/04/2013

@author: ThiagoP
'''

# Python Imports
from datetime import date, timedelta
from time import strftime
# Django Imports
from shortcuts import render_to_response
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Project Imports
from forms import FormPerfil, FormUsuario, FormRegistrar, FormLicencas
from models import PerfilUsuario, Cidade, Estado
from apps.empregados.models import Empregado
import settings
from paypal.standard.forms import PayPalPaymentsForm


def registrar(request):
    if request.method == 'GET':
        form = FormRegistrar()
        ret = render_to_response("contas/registrar.html", {'form': form}, request)
        
    elif request.method == 'POST':
        form = FormRegistrar(request.POST)
        
        if form.is_valid():
            user_form = form.save(commit=False)
            user = User.objects.create_user(username=user_form.username, password=user_form.password, email=user_form.email, first_name=user_form.first_name, last_name=user_form.last_name)
            perfil, true = PerfilUsuario.objects.get_or_create(usuario=user)
            
            user = authenticate(username=user_form.username, password=user_form.password)
            login(request, user)
    
            ret =  home(request)
        else:
            ret = render_to_response("contas/registrar.html", {'form': form}, request)
        
    return ret
    
    
@login_required
def home(request):
    if request.method == 'POST':
        form_usuario = FormUsuario(request.POST)
        form_perfil = FormPerfil(request.POST)
        
        if form_usuario.is_valid() and form_perfil.is_valid():
            user = form_usuario.save(commit=False)
            perfil = form_perfil.save(commit=False)
            
            request.user.first_name = user.first_name
            request.user.last_name = user.last_name
            request.user.email = user.email
            request.user.save()
            
            try:
                perfil_usuario = request.user.perfil
            except PerfilUsuario.DoesNotExist:
                perfil_usuario = PerfilUsuario()
                perfil_usuario.usuario = request.user
                perfil_usuario.expiracao = date.today()
            
            perfil_usuario.endereco = perfil.endereco
            perfil_usuario.numero = perfil.numero
            perfil_usuario.cpf_cnpj = perfil.cpf_cnpj
            perfil_usuario.complemento = perfil.complemento
            perfil_usuario.cidade = perfil.cidade
            perfil_usuario.estado = perfil.estado
            perfil_usuario.estabelecimento = perfil.estabelecimento
            
            perfil_usuario.save()
             
            form_usuario = FormUsuario(instance=request.user)
            form_perfil = FormPerfil(instance=request.user.perfil)
            
            ret = {'form_usuario': form_usuario, 'form_perfil': form_perfil, 'success': "Dados salvos com sucesso."}
            
        else:
            ret = {'form_usuario': form_usuario, 'form_perfil': form_perfil, 'error': "Verifique os erros abaixo...\n"}
            
    else:
        form_usuario = FormUsuario(instance=request.user)
        try:
            form_perfil = FormPerfil(instance=request.user.perfil)
        except PerfilUsuario.DoesNotExist:
            form_perfil = FormPerfil()
            
        ret = {'form_usuario': form_usuario, 'form_perfil': form_perfil}
            
    return render_to_response("contas/home.html", ret, request)
    

@login_required
def licencas(request):
    form = FormLicencas(initial={"licencas":request.user.perfil.licencas})
    
    return render_to_response("contas/licencas.html", {'form': form}, request)


@login_required
def pagamento(request):
    
    if request.method == "POST":
        licencas = request.POST.get('licencas')
        
        invoice_id = "empregadosimples.com-date=%s-uid=%d" %(strftime("%Y%m%d%H%M%S"), request.user.id)
        # What you want the button to do.
        paypal_dict = {
            "cmd": "_xclick-subscriptions",
            "lc": "pt",
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "a3": 5,                      # monthly price 
            "p3": 30,                           # duration of each unit (depends on unit)
            "t3": "D",                         # duration unit ("M for Month")
            "src": "1",                        # make payments recur
            "sra": "1",                        # reattempt payment on payment error
#            "no_note": "1",                    # remove extra notes (optional)
            "quantity": licencas,
            "currency_code": "BRL",
            "item_name": "Cadastro de Empregados",
            "invoice": invoice_id,
            "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
            "return_url": reverse('apps.contas.views.pagamento'),
            "cancel_return": reverse('apps.contas.views.pagamento'),
            'custom' : str({"user": request.user.id}),
        }
    
        # Create the instance.
        form_pay = PayPalPaymentsForm(button_type='subscribe', initial=paypal_dict)
    
        return render_to_response("contas/pagamento.html", 
                                  {
                                   "form_pay": form_pay.sandbox()
                                   },
                                  request
                                  )
        
        
@login_required
def cancelar(request, op='N'):
    if op and op.upper() == 'S':
        user = User.objects.get(pk=request.user.id)
        logout(request)
        
        for e in user.empregados.all():
            e.delete()
        user.perfil.delete()
        user.delete()
        
        
        return HttpResponseRedirect(reverse('apps.home.views.index'))
    else:
        return render_to_response('contas/cancelar.html', {}, request)