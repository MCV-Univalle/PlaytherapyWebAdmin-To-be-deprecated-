from django.conf.urls import url
import views

urlpatterns = [
    url(r'^crear_terapeuta/$', views.create_therapist, name='crear_terapeuta'),
    url(r'^modificar_terapeuta/(?P<therapist_id>.*$)', views.modify_therapist, name='modificar_terapeuta'),
    url(r'^lista_terapeutas/$', views.list_therapist, name='lista_terapeutas'),
    url(r'^cambiar_password/(?P<therapist_id>.*$)', views.setpassword_therapist, name='cambiar_password'),
    url(r'^cambiar_estado/(?P<therapist_id>.*$)', views.change_state, name='cambiar_estado_terapeuta'),
    
]