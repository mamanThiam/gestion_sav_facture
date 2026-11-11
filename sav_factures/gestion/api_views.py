# gestion/api_views.py
# viewsets.ModelViewSet te fournit automatiquement toutes les routes CRUD.
# queryset : source des données.
#serializer_class : comment convertir objets ↔ JSON.
# permission_classes : IsAuthenticated (JWT requis) ; la gestion des utilisateurs est réservée aux admins.

from rest_framework import viewsets, permissions
from .models import Client
from .serializers import ClientSerializer
from .models import Ascenseur, Intervention, User
from .serializers import AscenseurSerializer, InterventionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminRole

class ClientViewSet(viewsets.ModelViewSet):
    """
    API CRUD pour les Clients.
    GET /api/clients/        -> liste
    POST /api/clients/       -> création
    GET /api/clients/{pk}/   -> détail
    PUT/PATCH /api/clients/{pk}/ -> modifier
    DELETE /api/clients/{pk}/ -> supprimer
    """
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]



class AscenseurViewSet(viewsets.ModelViewSet):
    """
    API CRUD pour les Ascenseurs.
    GET /api/ascenseurs/        -> liste
    POST /api/ascenseurs/       -> création
    GET /api/ascenseurs/{pk}/   -> détail
    PUT/PATCH /api/ascenseurs/{pk}/ -> modifier
    DELETE /api/ascenseurs/{pk}/ -> supprimer
    """
    queryset = Ascenseur.objects.all().order_by('id')
    serializer_class = AscenseurSerializer
    permission_classes = [IsAuthenticated]

class InterventionViewSet(viewsets.ModelViewSet):
    """
    API CRUD pour les Interventions.
    GET /api/interventions/        -> liste
    POST /api/interventions/       -> création
    GET /api/interventions/{pk}/   -> détail
    PUT/PATCH /api/interventions/{pk}/ -> modifier
    DELETE /api/interventions/{pk}/ -> supprimer
    """
    queryset = Intervention.objects.all().order_by('id')
    serializer_class = InterventionSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API CRUD pour les Users.
    GET /api/users/        -> liste
    POST /api/users/       -> création
    GET /api/users/{pk}/   -> détail
    PUT/PATCH /api/users/{pk}/ -> modifier
    DELETE /api/users/{pk}/ -> supprimer
    """

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminRole]