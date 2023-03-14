from rest_framework import permissions
from user.models import User
from rest_framework.views import View, Request


class IsVendor(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method == "POST":
            return not request.user.is_vendor

        return True
