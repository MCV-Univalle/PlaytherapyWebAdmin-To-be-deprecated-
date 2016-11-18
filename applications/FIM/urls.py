from django.conf.urls import url
import views

urlpatterns = [
    url('list_fim/$', views.list_fim, name='listar_FIM'),
    url(r'^list_fim_data/$', views.list_fim_data, name='datos_lista_FIM'),
]