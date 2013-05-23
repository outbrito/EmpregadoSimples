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
from django.template.loader import render_to_string
# Project Imports
import xhtml2pdf.pisa as pisa
from cgi import escape


def render_to_pdf(template_src, context_dict):
#    template = get_template(template_src)
#    context = Context(context_dict)
    html  = render_to_string(template_src, context_dict)
    print html
    result = StringIO.StringIO()
    pdf = pisa.CreatePDF(StringIO.StringIO(html.encode("UTF-8")),
                                            dest=result,
                                            encoding='UTF-8',
                                            link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def fetch_resources(uri, rel):
    import os.path
    import settings
    path = os.path.join(
            settings.STATICFILES_DIRS[0],
            uri.replace(settings.STATIC_URL, ""))
    print path
    return path