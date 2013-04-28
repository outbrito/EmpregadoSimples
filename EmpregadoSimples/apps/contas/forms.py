# -*- coding: UTF-8 -*-

'''
Created on 21/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.forms import ModelForm
from django.contrib.auth.models import User
# Project Imports
from models import PerfilUsuario, Cidade, Estado
from EmpregadoSimples.libs.html5forms.fields import Html5CharField, Html5EmailField, Html5IntegerField

class FormPerfil(ModelForm):
    cpf_cnpj = Html5CharField(placeholder="CPF/CNPJ...", label="CPF/CNPJ")
    endereco = Html5CharField(placeholder="Rua...", label="Endereço")
    numero = Html5IntegerField(placeholder="Numero...", label="Número")
    complemento = Html5CharField(placeholder="Casa, condomínio, apt...", label="Complemento", required=False)
    cidade = Html5CharField(placeholder="Digite o nome de sua cidade...", label="Cidade", datalist=Cidade.objects.values_list('id', 'nome'))
    estado = Html5CharField(placeholder="Digite o nome de seu estado...", label="Estado", datalist=Estado.objects.values_list('id', 'nome'))
    
    def save(self, *args, **kwargs):
        nome_estado = self.cleaned_data['estado'].upper()
        estado = Estado.objects.get_or_create(nome=nome_estado)[0]
        self.instance.estado = estado
        
        nome_cidade = self.cleaned_data['cidade'].upper()
        cidade = Cidade.objects.get_or_create(nome=nome_cidade)[0]
        self.instance.cidade = cidade
        
        return super(FormPerfil, self).save(*args, **kwargs)
    
    class Meta:
        model = PerfilUsuario
        exclude = ('usuario', 'expiracao')
        

class FormUsuario(ModelForm):
    first_name = Html5CharField(placeholder="Nome...", label="Nome Completo")
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


class FormCidade(ModelForm):
    class Meta:
        model = Cidade
        
        
class FormEstado(ModelForm):
    class Meta:
        model = Estado