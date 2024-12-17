# Register your models here.
from django.contrib import admin
from .models import Client, Ascenseur, Intervention, Facture

admin.site.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'adresse')
admin.site.register(Ascenseur)
admin.site.register(Intervention)
admin.site.register(Facture)
