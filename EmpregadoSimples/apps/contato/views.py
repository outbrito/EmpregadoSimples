# Create your views here.
from django.core.mail import EmailMessage
from django.http.response import HttpResponse

def contato(request):
    if  request.method == 'POST':
        email= request.POST.get('email', '')
        nome= request.POST.get('nome','')
        msg = request.POST.get('msg','')
        email = EmailMessage('Contato Empregado Simples',
                            'Nome: ' + nome +'\nEmail: ' + email + '\n Mensagem:\n ' + msg,
                            to=['tpborion@gmail.com', 'ionaysilva@gmail.com'])
        if email.send() == 1:
            return HttpResponse("Mensagem Enviada com Sucesso!")