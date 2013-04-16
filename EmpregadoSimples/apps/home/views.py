# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
# Project Imports


def home(request):
    return render_to_response("home/index.html",
                              {},
                              context_instance=RequestContext(request))