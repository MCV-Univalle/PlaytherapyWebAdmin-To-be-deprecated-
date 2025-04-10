from django.urls import path

from applications.reports import views

urlpatterns = [
    path('por-movimiento/<int:patient_id>/', views.by_movement, name='por_movimiento'),
    path('por-minijuego/<int:patient_id>/', views.by_minigame, name='por_minijuego'),
    path('por-fim/<int:patient_id>/', views.by_fim, name='por_fim'),
    path('por-nivel/<int:patient_id>/', views.by_level, name='por_nivel'),
    path('reports/by_minigame/download/<int:patient_id>/', views.download_csv_by_minigame, name='download_csv_by_minigame'),
]