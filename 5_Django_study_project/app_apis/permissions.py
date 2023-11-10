from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or obj.author == request.user


class CustomPermission(PermissionDenied):
    status_code = 403
    default_detail = 'blablabla'
    default_code = 'custom_permission_denied'