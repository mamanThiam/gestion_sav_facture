# Documentation API - Projet SAV Ascenseurs

## But
Ce document liste les endpoints exposés par le backend Django (DRF) et décrit leur usage pour l'intégration avec Lovable.

## Base URL (dev)
`http://127.0.0.1:8000/api/`

---

## Endpoints implémentés (initial)
### Clients
- `GET /clients/` : Liste des clients
- `POST /clients/` : Créer un client
  - Body JSON attendu : `{"nom":"...", "adresse":"...", "email":"...","telephone":"..."}`
- `GET /clients/{id}/` : Détail client
- `PUT /clients/{id}/` : Remplacer client
- `PATCH /clients/{id}/` : Mettre à jour client partiellement
- `DELETE /clients/{id}/` : Supprimer client

---

## Notes de développement
- Environnement : `env` (virtualenv)
- Commandes utiles :
  - `python manage.py runserver`
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- CORS : activé via `django-cors-headers` pour localhost
- Authentification : à ajouter (JWT) pour production

---

## Contacts / Références
- Encadrant  : guide pas-à-pas pour intégration API

Présentation générale

Le backend de l’application SAV Ascenseurs est développé avec Django et Django REST Framework afin de fournir une API REST fiable, rapide et extensible.
Cette API est utilisée par un frontend développé séparément dans Lovable.

Elle gère trois ressources essentielles du système :

Clients

Ascenseurs

Interventions

2.  Technologies utilisées
Composant	Version / Infos
Python	3.11
Django	5.x
Django REST Framework	Dernière version
Base de données	SQLite (développement)
CORS Headers	Pour autoriser le front Lovable
Environnement virtuel	env/

3. Structure du backend
sav_factures/
│
├── gestion/                 # App principale
│   ├── models.py            # Modèles (Clients, Ascenseurs, Interventions)
│   ├── serializers.py       # Sérialise les modèles
│   ├── api_views.py         # Vues API REST
│   ├── api_urls.py          # Routes API
│   ├── views.py             # Anciennes vues HTML (désormais inutiles)
│   └── urls.py              # Anciennes URLs templates
│
├── sav_factures/
│   └── urls.py              # URLs globales du projet
│
└── env/                     # Virtual environment
