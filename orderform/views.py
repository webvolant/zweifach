# ~*~ coding: utf-8 ~*~
from django.shortcuts import render

from models import OrderForm

from django.core.mail import send_mail

from datetime import date
from datetime import datetime

#from django.http import HttpResponse
#from django.template import RequestContext, loader

def order(request):
    message=""
    br = "</br>"
    name = request.POST.get('name','')
    contact = request.POST.get('contact','')
    sourcelang = request.POST.get('sourcelang','')
    resultlang = request.POST.get('resultlang','')
    doc_file = request.POST.get('doc_file','')
    comments = request.POST.get('comments','')
    html = "Name:"+name+br+"Kontakt:"+contact+br+sourcelang+">"+resultlang+br+doc_file+br+"Comments:"+comments+br
    d = date.today()
    # datetime.combine(d, datetime.min.time())name = request.POST.get('name', '')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail('ZweiFach-email', html, 'volant247@gmail.com',['barkalov_anton@mail.ru'], fail_silently=False)
			#email_subject = "I need test it"
    		#email_body = render_to_string("email/invite.html", {})
    		#from_email = "noreply@mail.ru"
    		#to = "barkalov_anton@mail.ru"
    		#msg = EmailMultiAlternatives(subject,message,from_email, [to])
            #msg.content_subtype = "html"
            #msg.send()
            message = "Gut!"
            form = OrderForm()
    else:
        form = OrderForm()
    return render(request, 'order.html', {
        'form': form,
        'message': message,
        'time': d,
    })


