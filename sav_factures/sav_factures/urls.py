from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API REST (Lovable utilisera uniquement ces routes)
    path('api/', include('gestion.api_urls')),  # <-- API propre via router

    # Anciennes pages HTML (optionnelles)
    path('', include('gestion.urls')),  # <-- Toutes les vues Django classiques
]

# Fichiers médias (développement uniquement)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
