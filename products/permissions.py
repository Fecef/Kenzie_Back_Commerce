from rest_framework import permissions
from rest_framework.views import View
from .models import Product


class isVendorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.method == "GET":
            return True

        return request.user.is_vendor or request.user.is_admin
