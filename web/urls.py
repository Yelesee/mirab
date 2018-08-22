from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^check/$', views.check, name='index'),
    url(r'^calculate/$', views.calculate, name='index'),
    # url(r'^login/$', views.log_in, name='login'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^json/$', views.json, name='json'),
    url(r'^form/$', views.form, name="form"),
    url(r'^response/$', views.response, name="response"),
]