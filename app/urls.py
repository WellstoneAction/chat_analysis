
from django.conf.urls import include, url
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
    url(r'^trainings/$', views.trainings, name='trainings'),
    url(r'^lessons/$', views.lessons, name='lessons'),
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^messages/$', views.messages, name='messages'),
]
