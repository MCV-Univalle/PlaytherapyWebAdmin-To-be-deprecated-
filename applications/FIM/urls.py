from django.conf.urls import url
import views

urlpatterns = [
    url('list_fim/(?P<patient_id>.*$)', views.list_fim, name='listar_FIM'),
    url(r'^list_fim_data/(?P<patient_id>.*$)', views.list_fim_data, name='datos_lista_FIM'),
    url(r'^save_fim_data', views.save_fim_data, name='guardar_list_FIM'),
]