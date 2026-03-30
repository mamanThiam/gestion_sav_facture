# gestion/api_urls.py
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'clients', api_views.ClientViewSet)
router.register(r'ascenseurs', api_views.AscenseurViewSet)
router.register(r'interventions', api_views.InterventionViewSet)

urlpatterns = router.urls



