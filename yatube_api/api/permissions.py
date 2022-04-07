from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        if request.method not in permissions.SAFE_METHODS:
            return bool(obj.author == request.user)


class OwnerOrReadOnlyb(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated:
                return True
            raise PermissionDenied(
                'Запрещено для неаутентифицированных пользователей')
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
