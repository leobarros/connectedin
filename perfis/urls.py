from django.conf.urls import patterns, include, url
from perfis import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar')
)