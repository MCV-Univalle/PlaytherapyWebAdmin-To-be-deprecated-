from django.urls import path

from applications.start.forms import LoginForm
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('login/', custom_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]