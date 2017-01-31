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
    status = None
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            try:
                form.send_mail()
            except:
                status = 'failed'
            form = ContactForm()
            status = 'success'
    return render(request, 'beutifulhome/contact.html', {
        'form': form, 'status': status})
