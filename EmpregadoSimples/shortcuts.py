# -*- coding: UTF-8 -*-

'''
Created on 09/05/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.shortcuts import render_to_response as django_render_to_response
from django.shortcuts import RequestContext
# Project Imports



def render_to_response(template, dict, request):
    return django_render_to_response(template, dict, context_instance=RequestContext(request))