from django.urls import path
from applications.patient import views

urlpatterns = [
    path('crear_paciente/', views.create_patient, name='crear_paciente'),
    path('modificar_paciente/<int:patient_id>/', views.modify_patient, name='modificar_paciente'),
    path('lista_pacientes/', views.view_patients, name='lista_pacientes'),
    path('cambiar_estado/<int:patient_id>/', views.change_state, name='cambiar_estado_paciente'),
]