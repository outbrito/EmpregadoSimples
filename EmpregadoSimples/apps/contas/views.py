# -*- coding: utf-8 -*-

'''
Created on 18/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.shortcuts import render_to_response, RequestContext
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Project Imports


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
            user, created = User.objects.get_or_create(username=username, password=password, defaults={'email': email, 'first_name': nome, 'last_name': sobrenome})
            
            if created:
                user = authenticate(username=username, password=password)
                
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        
                        ret = home(request, user.id)
                    else:
                        ret = render_to_response("contas/registrar.html", 
                                                 {
                                                  "message" : "Conta desativada. Contate o administrador pelo formulário de contato.",
                                                  "user": user
                                                  },
                                                 context_instance=RequestContext(request)
                                                 )
                        
                else:
                    ret = render_to_response("contas/registrar.html", 
                                                 {
                                                  "message" : "Login inválido. Contate o administrador pelo formulário de contato.",
                                                  "username": username,
                                                  "nome": nome,
                                                  "sobrenome": sobrenome
                                                  },
                                                 context_instance=RequestContext(request)
                                                 )
            else:
                ret = render_to_response("contas/registrar.html", 
                                                 {
                                                  "message" : "Este nome de usuário já existe.",
                                                  "username": username,
                                                  "nome": nome,
                                                  "sobrenome": sobrenome
                                                  },
                                                 context_instance=RequestContext(request)
                                                 )
        
    return ret
    
    
@login_required
def home(request, uid):
    return render_to_response("contas/home.html", context_instance=RequestContext(request))
    

def pagamento(request):
    pass


def paypal_return(request):
    pass