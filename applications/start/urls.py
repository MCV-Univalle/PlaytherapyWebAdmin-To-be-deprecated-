
from django.conf.urls import url

from applications.start.forms import LoginForm
from .views import *
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'login$', custom_login, name='login'),
    # url(r'^login$', django.contrib.auth.views.login, {'template_name':'init/login.html',
                                                        #  'authentication_form':LoginForm,}, name='login'),
    url(r'^logout/$', logout, {'next_page': index}, name='logout'),
    # url(r'signup$', views.signup),
    url(r'dashboard$', dashboard, name='dashboard'),
]