from django.conf.urls import url
import views

urlpatterns = [
    url(r'^crear_terapeuta/$', views.create_therapist),
    url(r'^modificar_terapeuta/(?P<therapist_id>.*$)', views.modify_therapist),
    url(r'^lista_terapeutas/$', views.list_therapist),
    url(r'^setpassword_therapist/(?P<therapist_id>\d+)/', views.setpassword_therapist, name='setpassword_therapist'),
    url(r'^cambiar_estado/(?P<therapist_id>\d+)', views.change_state, name='cambiar_estado'),
    
]