from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', custom_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
]