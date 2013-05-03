# -*- coding: UTF-8 -*-

'''
Created on 01/05/2013

@author: ThiagoP
'''

# Python Imports
import cStringIO as StringIO
# Django Imports
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
# Project Imports
import ho.pisa as pisa
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))