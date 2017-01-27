from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from beutiful import settings

from . forms import ContactForm


def index(request):
    return render(request, 'beutifulhome/index.html')


def about(request):
    return render(request, 'beutifulhome/about.html')


def products(request):
    return render(request, 'beutifulhome/products.html')


def services(request):
    return render(request, 'beutifulhome/services.html')


def friends(request):
    return render(request, 'beutifulhome/friends.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = EmailMessage(
                data['message_subject'],
                data['message_content'],
                settings.EMAIL_HOST_USER,
                ['axevalley@hotmail.co.uk'],
                reply_to=[data['return_email']])
            email.send(fail_silently=False)
            form = ContactForm()
    return render(request, 'beutifulhome/contact.html', {'form': form})
