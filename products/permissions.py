from rest_framework import permissions
from rest_framework.views import View
from .models import Product


class isVendor(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product):
        return request.user.is_vendor
