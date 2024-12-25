from django.urls import path
from . import views  # Importez vos vues depuis gestion/views.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('clients/', views.liste_clients, name='liste_clients'),  
    path('clients/nouveau/', views.ajouter_client, name='ajouter_client'),
    path('clients/<int:client_id>/modifier/',views.modifier_client,name='modifier_client'),
    path('clients/<int:client_id>/supprimer/',views.supprimer_client,name='supprimer_client'),
# les routes pour la gestion des ascenseurs
    path('ascenseur/', views.liste_ascenseurs, name='liste_ascenseurs'),  
    path('ascenseur/ajouter/', views.ajouter_ascenseur, name='ajouter_ascenseur'),
    path('ascenseur/<int:id>/modifier/',views.modifier_ascenseur,name='modifier_ascenseur'),
    path('ascenseur/<int:id>/supprimer/',views.supprimer_ascenseur,name='supprimer_ascenseur'),
#les routes pour les rapports des clients et des ascenseurs
    path('rapport/clients/pdf/', views.rapport_clients_pdf, name='rapport_clients_pdf'),
    path('rapport/ascenseurs/excel/', views.rapport_ascenseurs_excel, name='rapport_ascenseurs_excel'),
 #les routes pour les interventions
    path('intervention/', views.liste_interventions, name='liste_interventions'),  
    path('intervention/ajouter/', views.ajouter_intervention, name='ajouter_intervention'),
]

# Ajouter cette ligne uniquement en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

