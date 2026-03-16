# gestion/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import ClientViewSet,AscenseurViewSet, InterventionViewSet
from django.urls import path
from . import api_views

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'ascenseurs', AscenseurViewSet, basename='ascenseurs')
router.register(r'interventions', InterventionViewSet, basename='interventions')
urlpatterns = router.urls



urlpatterns = [
    path('clients/', api_views.ClientListCreate.as_view(), name='clients_api'),
    path('clients/<int:pk>/', api_views.ClientRetrieveUpdateDestroy.as_view()),

    path('ascenseurs/', api_views.AscenseurListCreate.as_view()),
    path('ascenseurs/<int:pk>/', api_views.AscenseurRetrieveUpdateDestroy.as_view()),

    path('interventions/', api_views.InterventionListCreate.as_view()),
    path('interventions/<int:pk>/', api_views.InterventionRetrieveUpdateDestroy.as_view()),
]
