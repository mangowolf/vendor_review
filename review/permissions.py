from rest_framework.permissions import BasePermission
from .models import Company

class IsOwner(BasePermission):
    """Custom permission class to allow only company owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the Company owner."""

        if isinstance(obj, Company):
            return obj.owner == request.user
        return obj.owner == request.user