
# gestion/models.py
#les modèles définissent la structure des données et les relations entre elles dans l'application.
#Chaque modèle correspond à une table dans la base de données et contient des champs qui représentent les
#attributs des entités gérées par l'application.
#Voici le code complet pour les modèles dans gestion/models.py :
 
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
 
 
# --- Client ---
# --- Client ---
class Client(models.Model):
    STATUS_CHOICES = [
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('suspendu', 'Suspendu'),
    ]
    
    nom = models.CharField(max_length=255)
    adresse = models.TextField(blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    personne_de_contact = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
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
    date_installation = models.DateField()  # année d'installation
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='operationnel')
    dernier_maintenance = models.DateField(blank=True, null=True)  # dernier jour maintenance
    prochain_maintenance = models.DateField(blank=True, null=True)  # prochain jours maintenance
    notes = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return f"{self.marque} - {self.modele}"
 
 
# --- Intervention ---
class Intervention(models.Model):
    PRIORITY_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
        ('critique', 'Critique'),
    ]
 
    STATUS = [
        ('planifiee', 'Planifiée'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée'),
    ]
 
    TYPE = [
        ('maintenance', 'Maintenance'),
        ('reparation', 'Réparation'),
        ('controle', 'Contrôle'),
    ]
    title = models.CharField(max_length=255, blank=True, null=True)  # titre de l'intervention
    location = models.CharField(max_length=255, blank=True, null=True)  # lieu de l'intervention
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interventions', blank=True, null=True)
    ascenseur = models.ForeignKey(Ascenseur, on_delete=models.CASCADE, related_name='interventions')
    date_intervention = models.DateField()
    duration = models.CharField(max_length=50, blank=True, null=True)  # durée estimée
    type_intervention = models.CharField(max_length=20, choices=TYPE)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='moyenne')
    technicien = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='interventions'
    )
    statut = models.CharField(max_length=20, choices=STATUS, default='planifiee')
    description = models.TextField(blank=True, null=True)  # description/notes
    notes = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return f"{self.type_intervention} - {self.date_intervention}"
 
 
# model User : fiche utilisateur de l'ERP (rôle, statut) liée à un compte de connexion Django
class User(models.Model):
 
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('technicien', 'Technicien'),
        ('manager', 'Manager'),
        ('readonly', 'Readonly'),
    ]
    STATUT_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]
 
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='active')
 
    # Compte de connexion (identifiant + mot de passe haché) géré par Django
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profil',
    )
 
    def delete(self, *args, **kwargs):
        # Supprime aussi le compte de connexion associé
        auth_user = self.auth_user
        super().delete(*args, **kwargs)
        if auth_user:
            auth_user.delete()
 
    def __str__(self):
        return f"{self.nom} - {self.role}"
 

