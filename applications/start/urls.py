from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'login$', views.user_login),
    url(r'logout$', views.user_logout),
    url(r'signup$', views.signup),
    url(r'dashboard$', views.dashboard),
]