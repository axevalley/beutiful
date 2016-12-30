from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'beutifulhome/index.html')


def about(request):
    return render(request, 'beutifulhome/about.html')


def services(request):
    return render(request, 'beutifulhome/services.html')


def contact(request):
    return render(request, 'beutifulhome/contact.html')
