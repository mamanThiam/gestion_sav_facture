# gestion/models.py
#les modèles définissent la structure des données et les relations entre elles dans l'application.
#Chaque modèle correspond à une table dans la base de données et contient des champs qui représentent les
#attributs des entités gérées par l'application.
#Voici le code complet pour les modèles dans gestion/models.py :

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# --- Client ---
class Client(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)

    def clean(self):
        if not self.telephone.isdigit():
            raise ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")

    def __str__(self):
        return self.nom


# --- Ascenseur ---
class Ascenseur(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ascenseurs")
    modele = models.CharField(max_length=255)
    marque = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=255, unique=True)
    charge = models.CharField(
        max_length=15,
        choices=[
            ('450 Kg', '450 Kg'),
            ('630 Kg', '630 Kg'),
            ('800 Kg', '800 Kg'),
            ('1000 Kg', '1000 Kg'),
            ('1500 Kg', '1500 Kg'),
            ('2000 Kg', '2000 Kg'),
        ]
    )
    date_installation = models.DateField()

    def __str__(self):
        return f"{self.marque} - {self.modele}"


# --- Intervention ---
class Intervention(models.Model):

    STATUS = [
        ('planifiée', 'Planifiée'),
        ('en cours', 'En cours'),
        ('terminée', 'Terminée'),
    ]

    TYPE = [
        ('maintenance', 'Maintenance'),
        ('reparation', 'Réparation'),
        ('installation', 'Installation'),
        ('autre', 'Autre'),
    ]

    ascenseur = models.ForeignKey(Ascenseur, on_delete=models.CASCADE, related_name='interventions')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interventions')
    adresse = models.CharField(max_length=255, default="Adresse inconnue")
    date_intervention = models.DateField()
    type_intervention = models.CharField(max_length=20, choices=TYPE)
    technicien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    statut = models.CharField(max_length=20, choices=STATUS, default='planifiée')
    fichier_pva = models.FileField(upload_to='pva_files/', blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type_intervention} - {self.date_intervention}"


