
# gestion/api_views.py
# viewsets.ModelViewSet te fournit automatiquement toutes les routes CRUD.
# queryset : source des données.
#serializer_class : comment convertir objets ↔ JSON.
# permission_classes : pour l'instant AllowAny pour tester rapidement ; on verrouillera plus tard

from rest_framework import viewsets, permissions
from .models import Client
from .serializers import ClientSerializer
from .models import Ascenseur, Intervention
from .serializers import AscenseurSerializer, InterventionSerializer

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
    # Pour l'instant en dev, on autorise tout.
    # Plus tard on mettra IsAuthenticated ou des permissions basées sur rôles.
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.AllowAny]

