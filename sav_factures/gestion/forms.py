from django import forms
from .models import Client, Ascenseur, Intervention, User

#form pour client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'adresse','email', 'telephone']

#forms pour client
class AscenseurForm(forms.ModelForm):
    class Meta:
        model = Ascenseur
        fields = [  "id","client", "nom", "emplacement", "modele", "marque",
                "numero_serie", "charge", "capacite", "nombre_etages",
                "date_installation", "statut", "dernier_maintenance",
                "prochain_maintenance", "notes"]

#form pour intervention
class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields ="__all__"

#form pour user
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'email', 'role', 'statut'] 

