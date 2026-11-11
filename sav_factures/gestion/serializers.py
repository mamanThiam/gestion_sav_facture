# gestion/serializers.py
#les serializers sont utilisés pour convertir les instances de modèles en formats JSON ou autres formats de données.
#Pour chaque modèle (Client, Ascenseur, Intervention), un serializer est défini pour gérer la sérialisation et la désérialisation des données.
#Ces serializers facilitent la communication entre l'application backend et les clients frontend ou d'autres services.
#iLSmportent les modules nécessaires et définissent des serializers pour chaque modèle.
# Chaque serializer hérite de serializers.ModelSerializer et spécifie les champs à inclure.
# Ils gèrent également les relations entre les modèles en utilisant des champs liés.
# Voici le code complet pour les serializers dans gestion/serializers.py : 

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from .models import Client, Ascenseur, Intervention, User

AuthUser = get_user_model()

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "nom", "adresse", "email", "telephone", "personne_de_contact", "ville", "statut", "notes"]

    
    

class AscenseurSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
            queryset=Client.objects.all()
        )   
    class Meta:
        model = Ascenseur
        fields = [
                "id","client", "nom", "emplacement", "modele", "marque",
                "numero_serie", "charge", "capacite", "nombre_etages",
                "date_installation", "statut", "dernier_maintenance",
                "prochain_maintenance", "notes"
            ]



class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = [
                "id","title", "ascenseur", "client",
                "date_intervention", "duration","location",
                "type_intervention", "priority", "technicien",
                "statut", "description","notes", 
            ]

class UserSerializer(serializers.ModelSerializer):
    # Jamais renvoyé par l'API ; sert seulement à créer / changer le mot de passe
    password = serializers.CharField(
        write_only=True, required=False, allow_blank=True,
        style={"input_type": "password"},
    )
    can_login = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "nom", "email", "role", "statut", "password", "can_login"]

    def get_can_login(self, obj):
        return obj.auth_user_id is not None

    def validate_password(self, value):
        if value:
            validate_password(value)
        return value

    def validate_email(self, value):
        # L'email sert de nom d'utilisateur : il ne doit pas déjà appartenir à un autre compte
        existing = AuthUser.objects.filter(username__iexact=value)
        if self.instance is not None and self.instance.auth_user_id:
            existing = existing.exclude(pk=self.instance.auth_user_id)
        if existing.exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà utilisé par un autre compte.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop("password", "")
        profil = super().create(validated_data)
        if password:
            self._sync_auth_user(profil, password)
        return profil

    @transaction.atomic
    def update(self, instance, validated_data):
        password = validated_data.pop("password", "")
        profil = super().update(instance, validated_data)
        if password or profil.auth_user_id:
            self._sync_auth_user(profil, password)
        return profil

    def _sync_auth_user(self, profil, password):
        """Crée ou met à jour le compte de connexion (identifiant = email)."""
        auth_user = profil.auth_user
        if auth_user is None:
            auth_user = AuthUser.objects.create_user(
                username=profil.email, email=profil.email, password=password
            )
            profil.auth_user = auth_user
            profil.save(update_fields=["auth_user"])
        else:
            auth_user.username = profil.email
            auth_user.email = profil.email
            if password:
                auth_user.set_password(password)
        auth_user.first_name = profil.nom[:150]
        auth_user.is_active = profil.statut == "active"   # un utilisateur inactif ne peut plus se connecter
        auth_user.save()