from django.urls import path
from . import views  # Importez vos vues depuis gestion/views.py

urlpatterns = [
    path('clients/', views.liste_clients, name='liste_clients'),  
    path('clients/nouveau/', views.ajouter_client, name='ajouter_client'),
    path('clients/<int:client_id>/modifier/',views.modifier_client,name='modifier_client'),
    path('clients/<int:client_id>/supprimer/',views.supprimer_client,name='supprimer_client'),
]

# les routes pour la gestion des ascenseurs
urlpatterns = [
    path('ascenseur/', views.liste_ascenseurs, name='liste_ascenseurs'),  
    path('ascenseur/ajouter/', views.ajouter_ascenseur, name='ajouter_ascenseur'),
    path('ascenseur/<int:id>/modifier/',views.modifier_ascenseur,name='modifier_ascenseur'),
    path('ascenseur/<int:id>/supprimer/',views.supprimer_ascenseur,name='modifier_ascenseur'),
]