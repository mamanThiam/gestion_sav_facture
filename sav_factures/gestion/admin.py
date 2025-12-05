#  gestion/admin.py
# Importent les modules nécessaires et enregistrent les modèles dans l'interface d'administration de Django.
# Cela permet aux administrateurs de gérer les données des modèles via une interface utilisateur conviviale.
# Register your models here.
from django.contrib import admin
from .models import Client, Ascenseur, Intervention

admin.site.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'adresse')
admin.site.register(Ascenseur)
admin.site.register(Intervention)
