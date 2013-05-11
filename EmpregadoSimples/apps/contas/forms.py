# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django import forms
from django.contrib.auth.models import User
# Project Imports
from models import PerfilUsuario, Cidade, Estado
from html5forms.fields import Html5CharField, Html5EmailField, Html5IntegerField
from html5forms.widgets import Html5PasswordInput


class FormPerfil(forms.ModelForm):
    cpf_cnpj = Html5CharField(placeholder="CPF/CNPJ...", label="CPF/CNPJ")
    endereco = Html5CharField(placeholder="Rua...", label="Endereço")
    numero = Html5IntegerField(placeholder="Numero...", label="Número")
    complemento = Html5CharField(placeholder="Casa, condomínio, apt...", label="Complemento", required=False)
    cidade = Html5CharField(placeholder="Nome da sua cidade (seta pra baixo para sugestões)", label="Cidade (aperte ↓)", datalist=[(c.nome,) for c in Cidade.objects.all()])
    estado = Html5CharField(placeholder="Nome do seu estado (seta pra baixo para sugestões)", label="Estado (aperte ↓)", datalist=[(e.nome,) for e in Estado.objects.all()])
    
    def __init__(self, *args, **kwargs):
        super(FormPerfil, self).__init__(*args, **kwargs)
        if self.initial:
            if self.instance.cidade:
                self.initial['cidade'] = self.instance.cidade.nome
            if self.instance.estado:
                self.initial['estado'] = self.instance.estado.nome
    
    class Meta:
        model = PerfilUsuario
        exclude = ('usuario', 'expiracao', 'licencas')
        
    def clean(self):
        cidade, estado = self.cleaned_data.get('cidade'), self.cleaned_data.get('estado')
        cidade, estado = cidade.strip(), estado.strip()
        cidade, estado = cidade.upper(), estado.upper()
        if not cidade:
            # not specified so raise an error to user
            raise forms.ValidationError('Você precisa digitar o nome da Cidade')
        else:
            # get/create `Cidade`
            cidade, created = Cidade.objects.get_or_create(nome=cidade)
            self.cleaned_data['cidade'] = cidade
            
        if not estado:
            # not specified so raise an error to user
            raise forms.ValidationError('Você precisa digitar o nome do Estado')
        else:
            # get/create `Estado`
            estado, created = Estado.objects.get_or_create(nome=estado)
            self.cleaned_data['estado'] = estado

        return super(FormPerfil, self).clean()
        

class FormUsuario(forms.ModelForm):
    first_name = Html5CharField(placeholder="Nome...", label="Nome")
    last_name = Html5CharField(placeholder="Sobrenome...", label="Sobrenome", required=False)
    email = Html5EmailField(placeholder="E-mail...")
    
    class Meta:
        model = User
        exclude = (
                   'username', 
                   'password', 
                   'last_login', 
                   'date_joined', 
                   'is_superuser', 
                   'is_active',
                   'is_staff',
                   'groups',
                   'user_permissions',
                   )


class FormRegistrar(forms.ModelForm):
    username = Html5CharField(placeholder="Login...", label="Login")
    password = Html5CharField(placeholder="Senha...", label="Senha", widget=Html5PasswordInput(attrs={'onchange':"form.password2.pattern = this.value;"}))
    password2 = Html5CharField(placeholder="Senha novamente...", label="Confirme a Senha", widget=Html5PasswordInput())
    first_name = Html5CharField(placeholder="Nome...", label="Nome Completo")
    last_name = Html5CharField(placeholder="Sobrenome...", label="Sobrenome", required=False)
    email = Html5EmailField(placeholder="E-mail...")
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'first_name', 'last_name', 'email')
        exclude = (
                   'last_login', 
                   'date_joined', 
                   'is_superuser', 
                   'is_active',
                   'is_staff',
                   'groups',
                   'user_permissions',
                   )
    def clean(self):
        password, password2 = self.cleaned_data.get('password'), self.cleaned_data.get('password2')
        if password <> password2:
            # not specified so raise an error to user
            raise forms.ValidationError('As senhas devem ser iguais.')

        return super(FormRegistrar, self).clean()
    

class FormCidade(forms.ModelForm):
    class Meta:
        model = Cidade
        
        
class FormEstado(forms.ModelForm):
    class Meta:
        model = Estado
        
        
class FormLicencas(forms.Form):
    licencas = Html5IntegerField(placeholder="Numero...", label="Total de Licenças a Pagar")