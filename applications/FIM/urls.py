from django.conf.urls import url
import views

urlpatterns = [
    url('list_fim/$', views.list_fim, name='listar_FIM'),
]