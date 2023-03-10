from rest_framework import permissions
from rest_framework.views import View

from .models import User


class IsAdminForGET(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.method == "POST":
            return True

        return request.user.is_authenticated and request.user.is_admin


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(elf, request, view: View, obj: User):
        if request.user != obj:
            return request.user.is_admin

        return request.user == obj
