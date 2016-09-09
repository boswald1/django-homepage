from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^champions/', views.champions),
    url(r'^(?P<champ_id>[0-9]+)/$', views.detail, name='detail'),
]


# REST API
from rest_framework import routers
from league import views

router = routers.DefaultRouter()
router.register(r'api/champions', views.ChampionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]