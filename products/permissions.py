from rest_framework import permissions
from rest_framework.views import View
from .models import Product


class isVendor(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product):
        return request.user.is_vendor or request.user.is_admin

class CustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated and request.user.is_vendor
        )