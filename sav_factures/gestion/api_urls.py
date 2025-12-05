# gestion/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import ClientViewSet,AscenseurViewSet, InterventionViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'ascenseurs', AscenseurViewSet, basename='ascenseurs')
router.register(r'interventions', InterventionViewSet, basename='interventions')
urlpatterns = router.urls
