from django.db import models
from django.core.exceptions import ValidationError

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
        return f"{self.marque} - {self.modele} - {self.numero_serie}"

# Table Intervention
class Intervention(models.Model):
    ascenseur = models.ForeignKey(Ascenseur, on_delete=models.CASCADE, related_name="interventions")
    technicien = models.CharField(max_length=255)
    statut = models.CharField(
        max_length=50, 
        choices=[
            ('En cours', 'En cours'), 
            ('Terminé', 'Terminé')
        ]
    )
    type_intervention = models.CharField(
        max_length=15, 
        choices=[
            ('Entretien', 'Entretien'), 
            ('Réparation', 'Réparation'), 
            ('Diagnostic', 'Diagnostic')
        ]
    )
    date = models.DateField()

    def __str__(self):
        return f"Intervention {self.type_intervention} sur {self.ascenseur}"

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
