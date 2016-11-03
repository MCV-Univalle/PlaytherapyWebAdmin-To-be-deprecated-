from django.conf.urls import url
import views

urlpatterns = [
    url('crear_paciente/$', views.create_patient, name='crear_paciente'),
    url('modificar_paciente/(?P<patient_id>.*$)', views.modify_patient, name='modificar_paciente'),
    url('lista_pacientes/$', views.view_patients, name='lista_pacientes'),
    url(r'^cambiar_estado/(?P<patient_id>.*$)', views.change_state, name='cambiar_estado_paciente'),
]