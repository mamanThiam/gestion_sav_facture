from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User   #les techniciens utilisent le système d'authentification par  défaut Django

# Table Client
class Client(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)

    def clean(self):
        if not self.telephone.isdigit():
            raise ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")
# Table Ascenseur
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
            ('1000 Kg ', '1000 Kg'), 
            ('1500 Kg', '1500 Kg'), 
            ('2000 Kg', '2000 Kg')
        ]
    )
    date_installation = models.DateField()

    def __str__(self):
        return f"{self.marque} - {self.modele} "

# Table Intervention
class Intervention(models.Model):
  from django.db import models

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

    ascenseur = models.ForeignKey('Ascenseur', on_delete=models.CASCADE, related_name='interventions',default=1)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='interventions', default= 1)  # Lien avec le client
    adresse = models.CharField(max_length=255,default="Adresse Inconnue")  # Adresse où l'intervention a lieu
    date_intervention = models.DateField()
    type_intervention = models.CharField(max_length=20, choices=TYPE)
    technicien = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUS, default='planifiée')  # Statut de l'intervention
    fichier_pva = models.FileField(upload_to='pva_files/', blank=True, null=True)  # Fichier PVA scanné
    note = models.TextField(blank=True, null=True)  # Note ou observation pour le technicien

    def __str__(self):
        return f"{self.type_intervention} ({self.statut}) - {self.date_intervention} - {self.technicien}"

from django.conf import settings

class Intervention(models.Model):
    ...
    technicien = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    ...



# Table Facture
class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="factures")
    description_services = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(
        max_length=15, 
        choices=[
            ('Payé', 'Payé'), 
            ('Non payé', 'Non payé')
        ]
    )
    date_emission = models.DateField()

    def __str__(self):
        return f"Facture #{self.id} - {self.client.nom} - {self.statut}"
