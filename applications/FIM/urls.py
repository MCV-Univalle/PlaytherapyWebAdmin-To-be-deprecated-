from django.urls import path
from applications.FIM import views

urlpatterns = [
    path('list_fim/<str:patient_id>/', views.list_fim, name='listar_FIM'),
    path('list_fim_data/<str:patient_id>/', views.list_fim_data, name='datos_lista_FIM'),
    path('save_fim_data/', views.save_fim_data, name='save_list_FIM'),
    path('delete_fim_data/', views.delete_fim_data, name='delete_list_FIM'),
]