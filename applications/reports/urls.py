from django.conf.urls import url
import views

urlpatterns = [
    url('por_movimiento/(?P<patient_id>\d+)/', views.by_movement, name='por_movimiento'),
    url('por_minijuego/(?P<patient_id>\d+)/', views.by_minigame, name='por_minijuego'),
]