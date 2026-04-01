# gestion/models.py
#les modèles définissent la structure des données et les relations entre elles dans l'application.
#Chaque modèle correspond à une table dans la base de données et contient des champs qui représentent les
#attributs des entités gérées par l'application.
#Voici le code complet pour les modèles dans gestion/models.py :

from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
settings.AUTH_USER_MODEL

 
# --- Client ---
# --- Client ---
class Client(models.Model):
    STATUS_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('suspendu', 'Suspendu'),
    ]
    
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    personne_de_contact = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    code_postal = models.CharField(max_length=10, blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='actif')
    notes = models.TextField(blank=True, null=True)

    def clean(self):
        if not self.telephone.isdigit():
            raise ValidationError("Le numéro de téléphone doit contenir uniquement des chiffres.")

    def __str__(self):
        return self.nom

# --- Ascenseur ---
class Ascenseur(models.Model):
    STATUS_CHOICES = [
        ('operationnel', 'Opérationnel'),
        ('maintenance', 'En maintenance'),
        ('hors_service', 'Hors service'),
        ('suspendu', 'Suspendu'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ascenseurs")
    nom = models.CharField(max_length=255, blank=True, null=True)  # Nom de l'ascenseur
    emplacement = models.CharField(max_length=255, blank=True, null=True)  # Localisation
    modele = models.CharField(max_length=255, blank=True, null=True)  # modèle de l'ascenseur
    marque = models.CharField(max_length=50)  # fabricant
    numero_serie = models.CharField(max_length=255, blank=True, null=True)  # numéro de série
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
    capacite = models.CharField(max_length=50, blank=True, null=True)  # capacités
    nombre_etages = models.IntegerField(blank=True, null=True)  # nombre d'étages
    annee_installation = models.DateField()  # année d'installation
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='operationnel')
    dernier_maintenance = models.DateField(blank=True, null=True)  # dernier jour maintenance
    prochain_maintenance = models.DateField(blank=True, null=True)  # prochain jours maintenance
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marque} - {self.modele}"


# --- Intervention ---
class Intervention(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
        ('critical', 'Critique'),
    ]

    STATUS = [
        ('scheduled', 'Planifiée'),
        ('in-progress', 'En cours'),
        ('completed', 'Terminée'),
        ('cancelled', 'Annulée'),
    ]

    TYPE = [
        ('maintenance', 'Maintenance'),
        ('repair', 'Réparation'),
        ('inspection', 'Contrôle'),
    ]

    ascenseur = models.ForeignKey(Ascenseur, on_delete=models.CASCADE, related_name='interventions')
    date_intervention = models.DateField()
    duration = models.CharField(max_length=50, blank=True, null=True)  # durée estimée
    type_intervention = models.CharField(max_length=20, choices=TYPE)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    technicien = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='interventions'
    )
    statut = models.CharField(max_length=20, choices=STATUS, default='scheduled')
    fichier_pva = models.FileField(upload_to='pva_files/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # description/notes
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type_intervention} - {self.date_intervention}"


# model User
class User(models.Model):
    nom = models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # Rôle de l'utilisateur (ex: admin, technicien, etc.)
    statut=models.CharField(max_length=20, choices=[('actif', 'Actif'), ('inactif', 'Inactif')], default='actif')
    def __str__(self):
        return f"{self.user.username} - {self.role}"