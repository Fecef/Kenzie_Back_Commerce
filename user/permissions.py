from rest_framework import permissions
from rest_framework.views import View

from .models import User


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return request.user.is_admin


class IsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return request.user.is_authenticated


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(elf, request, view: View, obj: User):
        if request.user != obj:
            return request.user.is_admin

        return request.user == obj
