
from django.conf.urls import patterns, include, url
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
]
