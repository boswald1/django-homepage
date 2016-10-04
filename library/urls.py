from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_book/', views.add_book, name='add_book'),

]