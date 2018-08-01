from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check/$', views.check, name='index'),
    url(r'^calculate/$', views.calculate, name='index'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^json/$', views.json, name='json'),
    url(r'^recognize/$', views.recognize, name='recognize'),
    url(r'^define/$', views.define, name='recognize'),
]