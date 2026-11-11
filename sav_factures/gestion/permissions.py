# gestion/permissions.py
from rest_framework.permissions import BasePermission


class IsAdminRole(BasePermission):
    """Seuls les superutilisateurs et les utilisateurs au rôle « admin » passent."""

    def has_permission(self, request, view):
        user = request.user
        if not (user and user.is_authenticated):
            return False
        if user.is_superuser:
            return True
        profil = getattr(user, "profil", None)
        return bool(profil and profil.role == "admin")