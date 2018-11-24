from django.conf.urls import url

from applications.reports import views

urlpatterns = [
    url('por-movimiento/(?P<patient_id>\d+)/', views.by_movement, name='por_movimiento'),
    url('por-minijuego/(?P<patient_id>\d+)/', views.by_minigame, name='por_minijuego'),
    url('por-fim/(?P<patient_id>\d+)/', views.by_fim, name='por_fim'),
    url('por-nivel/(?P<patient_id>\d+)/', views.by_level, name='por_nivel'),
]