from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to access or modify it.
    This permission checks if the authenticated user is the creator of the object.
    Usage:
    - For views that operate on individual objects (e.g., RetrieveUpdateDestroyAPIView), 
    include IsOwner in the permission_classes to restrict access to the object's owner.
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
