from django.urls import path

from applications.therapist import views

urlpatterns = [
    path('crear_terapeuta/', views.create_therapist, name='crear_terapeuta'),
    path('modificar_terapeuta/<int:therapist_id>/', views.modify_therapist, name='modificar_terapeuta'),
    path('lista_terapeutas/', views.list_therapist, name='lista_terapeutas'),
    path('cambiar_password/<int:therapist_id>/', views.setpassword_therapist, name='cambiar_password'),
    path('cambiar_estado/<int:therapist_id>/', views.change_state, name='cambiar_estado_terapeuta'),
    
]