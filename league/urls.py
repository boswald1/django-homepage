from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^champions/', views.champions),
    url(r'^(?P<champ_id>[0-9]+)/$', views.detail, name='detail'),
]