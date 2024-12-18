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

# les routes pour la gestion des clients

urlpatterns = [

    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('clients/', views.liste_clients, name='liste_clients'),  
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('clients/<int:client_id>/modifier/',views.modifier_client,name='modifier_client'),
    path('clients/<int:client_id>/supprimer/',views.supprimer_client,name='modifier_client'),
]

# les routes pour la gestion des ascenseurs
urlpatterns = [

    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('ascenseur/', views.liste_ascenseurs, name='liste_ascenseurs'),  
    path('ascenseur/ajouter/', views.ajouter_ascenseur, name='ajouter_ascenseur'),
    path('ascenseur/<int:id>/modifier/',views.modifier_ascenseur,name='modifier_ascenseur'),
    path('ascenseur/<int:id>/supprimer/',views.supprimer_ascenseur,name='modifier_ascenseur'),
]