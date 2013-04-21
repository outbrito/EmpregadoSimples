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
            user = User.objects.create_user(username=username, password=password, email=email, first_name=nome, last_name=sobrenome)
            
            login(request, user)
    
            ret =  home(request) 
        
    return ret
    
    
@login_required
def home(request):
    if request.method == 'GET':
        ret = render_to_response("contas/home.html", context_instance=RequestContext(request))
    
    elif request.method == 'POST':
        email= request.POST.get('email', '')
        nome= request.POST.get('nome','')
        sobrenome= request.POST.get('sobrenome','')
        
        user = request.user
        
        user.email = email
        user.first_name = nome
        user.last_name = sobrenome
        user.save()
        
        ret = render_to_response("contas/home.html",
                                 {
                                  'message': ["success", "Dados salvos com sucesso."],
                                  },
                                 context_instance=RequestContext(request)
                                 )
        
    return ret
    

def pagamento(request):
    pass


def paypal_return(request):
    pass