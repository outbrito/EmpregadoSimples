# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

from django.conf.urls import patterns, url


urlpatterns = patterns('EmpregadoSimples.apps.home.views',
                       url(r'^$', 'index'),
                       url(r'^home/?$', 'home'),
                       )