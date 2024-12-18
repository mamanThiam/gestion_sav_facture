from django import forms
from .models import Client, Ascenseur

#form pour client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'adresse','email', 'telephone']

#forms pour client
class AscenseurForm(forms.ModelForm):
    class Meta:
        model = Ascenseur
        fields = ['client', 'marque', 'charge','modele','numero_serie','date_installation']