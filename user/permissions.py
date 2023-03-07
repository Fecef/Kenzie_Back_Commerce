from rest_framework import permissions
from rest_framework.views import View
from django.shortcuts import get_object_or_404

from .models import User


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.method == "GET" and request.user.is_authenticated:
            return request.user.is_admin


class UserDetailPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        params_user = get_object_or_404(User, pk=view.kwargs["user_id"])

        if request.user != params_user and request.user.is_authenticated:
            return request.user.is_admin

        return True
