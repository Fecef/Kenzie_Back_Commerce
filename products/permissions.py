from rest_framework import permissions
from rest_framework.views import View
from .models import Product


class isVendor(permissions.BasePermission):
    def has_permission(self, request, view: View):
        return request.user.is_vendor or request.user.is_admin
