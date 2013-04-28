# -*- coding: utf-8 -*-

'''
Created on 18/04/2013

@author: ThiagoP
'''

# Python Imports
from datetime import date
# Django Imports
from django.shortcuts import render_to_response, RequestContext
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Project Imports
from forms import FormPerfil, FormUsuario
from models import PerfilUsuario, Cidade, Estado


def registrar(request):
    if request.method == 'GET':
        ret = render_to_response("contas/registrar.html", context_instance=RequestContext(request))
        
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email= request.POST.get('email', '')
        nome= request.POST.get('nome','')
        sobrenome= request.POST.get('sobrenome','')
        
        if username and password and (password == password2) and email and nome:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=nome, last_name=sobrenome)
            
            login(request, user)
    
            ret =  home(request) 
        
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
                print "CHUPA\n\n\n"
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
            
            ret = render_to_response("contas/home.html",
                                 {
                                  'form_usuario': form_usuario,
                                  'form_perfil': form_perfil,
                                  'success': "Dados salvos com sucesso."
                                  },
                                 context_instance=RequestContext(request)
                                 )
        else:
           
            ret = render_to_response("contas/home.html",
                                 {
                                  'form_usuario': form_usuario,
                                  'form_perfil': form_perfil,
                                  'error': "Verifique os erros abaixo...\n"
                                  },
                                 context_instance=RequestContext(request)
                                 )
    else:
        form_usuario = FormUsuario(instance=request.user)
        try:
            form_perfil = FormPerfil(instance=request.user.perfil)
        except PerfilUsuario.DoesNotExist:
            form_perfil = FormPerfil()
        
        ret = render_to_response("contas/home.html",
                                 {
                                  'form_usuario': form_usuario,
                                  'form_perfil': form_perfil
                                  }, 
                                 context_instance=RequestContext(request)
                                 )
            
    return ret
    

def pagamento(request):
    pass


def paypal_return(request):
    pass