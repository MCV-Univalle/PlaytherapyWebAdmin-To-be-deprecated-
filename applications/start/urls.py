from django.conf.urls import url
from applications.start.forms import LoginForm
import django.contrib.auth.views
import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'login$', views.user_login),
    url(r'^login$', django.contrib.auth.views.login, {'template_name':'init/login.html',
                                                         'authentication_form':LoginForm,}, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': views.index}, name='logout'),
    url(r'signup$', views.signup),
    url(r'dashboard$', views.dashboard),
]