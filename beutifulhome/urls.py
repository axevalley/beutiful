from django.conf.urls import url

from . import views

app_name = 'beutifulhome'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^products/$', views.products, name='products'),
    url(r'^services/$', views.services, name='services'),
    url(r'^contact/$', views.contact, name='contact'),
]
