from django.conf.urls import url
import views

urlpatterns = [
    url('crear_paciente/$', views.create_patient),
    url('ver_pacientes/$', views.view_patients),
]