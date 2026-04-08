# gestion/serializers.py
#les serializers sont utilisés pour convertir les instances de modèles en formats JSON ou autres formats de données.
#Pour chaque modèle (Client, Ascenseur, Intervention), un serializer est défini pour gérer la sérialisation et la désérialisation des données.
#Ces serializers facilitent la communication entre l'application backend et les clients frontend ou d'autres services.
#iLSmportent les modules nécessaires et définissent des serializers pour chaque modèle.
# Chaque serializer hérite de serializers.ModelSerializer et spécifie les champs à inclure.
# Ils gèrent également les relations entre les modèles en utilisant des champs liés.
# Voici le code complet pour les serializers dans gestion/serializers.py : 

from urllib import response

from rest_framework import serializers
from .models import Client, Ascenseur, Intervention, User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "nom", "adresse", "email", "telephone", "personne_de_contact", "ville", "code_postal", "statut", "notes"]

class AscenseurSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
   
    class Meta:
        model = Ascenseur
        fields = [
                "id","client", "nom", "emplacement", "modele", "marque",
                "numero_serie", "charge", "capacite", "nombre_etages",
                "annee_installation", "statut", "dernier_maintenance",
                "prochain_maintenance", "notes"
            ]

    def create(self, request, *args, **kwargs):
            print(f"REQUEST DATA: {request.data}")
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                print(f"SERIALIZER ERRORS: {serializer.errors}")
                return response(serializer.errors, status=400)
            return super().create(request, *args, **kwargs)


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = [
                "id","title", "ascenseur", "client",
                "date_intervention", "duration","location",
                "type_intervention", "priority", "technicien",
                "statut", "description","notes", 
            ]

        def create(self, request, *args, **kwargs):
            print(f"REQUEST DATA: {request.data}")
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                print(f"SERIALIZER ERRORS: {serializer.errors}")
                return response(serializer.errors, status=400)
            return super().create(request, *args, **kwargs)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "nom", "email", "role", "statut"]