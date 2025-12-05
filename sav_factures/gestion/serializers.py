# gestion/serializers.py
#les serializers sont utilisés pour convertir les instances de modèles en formats JSON ou autres formats de données.
#Pour chaque modèle (Client, Ascenseur, Intervention), un serializer est défini pour gérer la sérialisation et la désérialisation des données.
#Ces serializers facilitent la communication entre l'application backend et les clients frontend ou d'autres services.
#iLSmportent les modules nécessaires et définissent des serializers pour chaque modèle.
# Chaque serializer hérite de serializers.ModelSerializer et spécifie les champs à inclure.
# Ils gèrent également les relations entre les modèles en utilisant des champs liés.
# Voici le code complet pour les serializers dans gestion/serializers.py : 

from rest_framework import serializers
from .models import Client, Ascenseur, Intervention

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "nom", "adresse", "email", "telephone"]

class AscenseurSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source="client",
        write_only=True
    )

    class Meta:
        model = Ascenseur
        fields = [
            "id", "client", "client_id",
            "modele", "marque", "numero_serie",
            "charge", "date_installation"
        ]

class InterventionSerializer(serializers.ModelSerializer):
    ascenseur = AscenseurSerializer(read_only=True)
    ascenseur_id = serializers.PrimaryKeyRelatedField(
        queryset=Ascenseur.objects.all(),
        source="ascenseur",
        write_only=True
    )
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source="client",
        write_only=True
    )

    class Meta:
        model = Intervention
        fields = [
            "id", "ascenseur", "ascenseur_id",
            "client", "client_id",
            "adresse", "date_intervention",
            "type_intervention", "technicien",
            "statut", "fichier_pva", "note"
        ]

