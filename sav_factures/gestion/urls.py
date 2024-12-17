from django.urls import path
from . import views  # Importez vos vues depuis gestion/views.py

urlpatterns = [
    path('clients/', views.liste_clients, name='liste_clients'),  
    path('clients/nouveau/', views.formulaire_client, name='nouveau_client'),
    path('clients/<int:id>/modifier/', views.formulaire_client, name='modifier_client')# Exemple de route
]
