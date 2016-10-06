from django.conf.urls import url
import views

urlpatterns = [
    url(r'^crear_terapeuta/$', views.create_therapist),
    url(r'^modificar_terapeuta/(?P<therapist_id>.*$)', views.modify_therapist),
    url(r'^ver_terapeutas/$', views.view_therapist),
]