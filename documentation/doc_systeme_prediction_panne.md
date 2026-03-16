# 📘 Système Intelligent de Gestion SAV & Prédiction de Pannes d’Ascenseurs

## 📌 1. Introduction
Ce document présente une vision complète du fonctionnement des ascenseurs, de la collecte des données, des paramètres nécessaires pour la maintenance prédictive, ainsi qu’une **architecture technique** et un **schéma de base de données** pour un système intelligent de gestion SAV.

Ce document servira de base pour développer :
- Une plateforme de gestion SAV
- Un module IoT de collecte de données
- Un moteur de prédiction de pannes
- Un tableau de bord pour techniciens et administrateurs

---

# 🏗️ 2. Fonctionnement général d’un ascenseur

## 2.1 Sous-systèmes principaux
- **Système mécanique** : cabine, rails, câbles, contrepoids
- **Système de traction** : moteur, variateur de vitesse
- **Système de portes** : moteur de porte, capteurs
- **Système de sécurité** : parachute, limiteur de vitesse, fins de course
- **Système de contrôle** : automate / carte électronique

---

# 📊 3. Types de données collectables

## 3.1 Données techniques
- Vitesse du moteur
- Température moteur
- Consommation électrique
- Vibrations
- Position cabine
- Température du local machine
- Nombre de cycles

## 3.2 Données d'utilisation
- Nombre d’ouvertures/fermetures des portes
- Poids moyen
- Heures de fonctionnement

## 3.3 Données de pannes
- Logs
- Codes erreurs
- Détections de surcharge
- Défauts variateur

## 3.4 Données environnementales
- Température
- Humidité
- Poussière
- Tension instable

---

# 🔌 4. Méthodes de collecte de données

## 4.1 Accès direct au contrôleur
Via API des fabricants (Sodimas, Otis, Kone…).

## 4.2 Capteurs IoT
Module IoT utilisant :
- Accéléromètre
- Capteur de courant
- Capteur de température
- ESP32 / SIM800L

## 4.3 Remontée manuelle par technicien
- Diagnostics
- Logs
- Pièces changées

---

# 🤖 5. Paramètres utilisés pour la prédiction de pannes

## 5.1 Paramètres mécaniques
- Vibrations anormales
- Temps de freinage
- Allongement câbles

## 5.2 Paramètres portes
- Temps ouverture/fermeture
- Nombre de blockages
- Logs DOOR_TIMEOUT

## 5.3 Paramètres électriques
- Surintensités
- Surchauffe moteur
- Défauts variateur

## 5.4 Historique maintenance
- Âge ascenseur
- Fréquence interventions
- Remplacements pièces

---

# 🧱 6. Architecture technique du système

```
+---------------------------------------------------------+
|                     Utilisateurs                        |
|  - Techniciens  - Administrateurs  - Managers           |
+---------------------------+-----------------------------+
                            |
                            v
+---------------------------------------------------------+
|                Interface Web (Django / Bootstrap)       |
|   - Tableau de bord   - FullCalendar   - Alertes        |
+---------------------------+-----------------------------+
                            |
                            v
+---------------------------------------------------------+
|                        API Django                       |
|   - Gestion SAV  - Historique  - Collecte données IoT   |
+---------------------------+-----------------------------+
                            |
                            v
+----------------------+       +---------------------------+
|  Base de Données    |<----->|  Moteur IA / ML (Python)  |
|  PostgreSQL / MySQL  |       |  - Détection anomalies    |
|                      |       |  - Prédiction pannes      |
+----------------------+       +---------------------------+
                            ^
                            |
+---------------------------------------------------------+
|                         IoT Ascenseur                   |
|  Capteurs (vibration, courant, temp.) + ESP32           |
+---------------------------------------------------------+
```

---

# 🗂️ 7. Schéma de base de données (conception)

## 7.1 Tables principales

### **Table : clients**
| Champ | Type | Description |
|-------|------|-------------|
| id | PK | Identifiant client |
| nom | string | Nom de l’entreprise / client |
| adresse | string | Adresse |
| contact | string | Téléphone |

---

### **Table : ascenseurs**
| Champ | Type | Description |
|-------|------|-------------|
| id | PK | Identifiant ascenseur |
| numero_serie | string | Numéro constructeur |
| modele | string | Modèle |
| fabricant | string | Marque |
| client_id | FK | Appartient à un client |
| date_installation | date | |
| type_ascenseur | string | traction / hydraulique |

---

### **Table : interventions**
| Champ | Type | Description |
|-------|------|-------------|
| id | PK | Identifiant intervention |
| ascenseur_id | FK | Ascenseur concerné |
| type | string | maintenance / dépannage |
| description | text | détail intervention |
| statut | string | programmé / terminé / en cours |
| technicien_id | FK | intervenant |
| date_prevue | datetime | |
| date_realisation | datetime | |

---

### **Table : logs_pannes**
| Champ | Type | Description |
|-------|------|-------------|
| id | PK | |
| ascenseur_id | FK | |
| code | string | code erreur |
| message | string | description |
| criticite | int | 1 à 5 |
| date | datetime | |

---

### **Table : capteurs_donnees**
| Champ | Type | Description |
|-------|------|-------------|
| id | PK | |
| ascenseur_id | FK | |
| temperature_moteur | float | |
| courant_moteur | float | |
| vibrations | float | |
| poids | float | |
| cycles | int | |
| date_capture | datetime | temps réel |

---

### **Table : predictions**
| Champ | Type | Description |
|-------|------|-------------|
| id | PK | |
| ascenseur_id | FK | |
| type_panne | string | moteur, porte, variateur… |
| probabilite | float | 0-1 |
| date_prediction | datetime | |

---

# 🎯 8. Conclusion
Ce document propose une base solide pour concevoir :
- un système SAV structuré
- un module IoT de collecte en temps réel
- un moteur d’analyse prédictive
- une base de données bien architecturée
- une application web professionnelle et scalable

Je peux maintenant t’aider à :
✔ Générer les modèles Django
✔ Construire l'API
✔ Concevoir l’architecture IoT (ESP32)
✔ Développer le dashboard et les graphiques
✔ Construire ton modèle IA

Souhaites‑tu la **version Django (models.py)** du schéma ci‑dessus ?

