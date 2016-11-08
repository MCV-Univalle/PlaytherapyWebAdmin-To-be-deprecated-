from django.conf.urls import url
import views

urlpatterns = [
    url('por_movimiento/', views.by_movement, name='por_movimiento'),
]