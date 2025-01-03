"""
URL configuration for sav_factures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestion import views
from django.conf import settings
from django.conf.urls.static import static




# les routes pour la gestion des clients

urlpatterns=[

    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('clients/', views.liste_clients, name='liste_clients'),  
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
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
