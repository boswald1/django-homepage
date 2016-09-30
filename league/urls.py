from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^champions/$', views.champions),
    url(r'^champions/(?P<champ_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^summoner/(?P<summoner_name>[a-zA-Z0-9]+)/$', views.summoner_detail, name='summoner_detail'),
]


# REST API
from rest_framework.urlpatterns import format_suffix_patterns
from league import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/champions/$', views.ChampionList.as_view()),
    url(r'^api/champions/(?P<pk>[0-9]+)/$', views.ChampionDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)