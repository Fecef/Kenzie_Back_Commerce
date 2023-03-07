from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer
from .permissions import UserPermission, UserDetailPermission

import ipdb


class UserView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)

        self.check_object_permissions(self.request, User)

        return queryset


class UserDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [UserDetailPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    # ! Deleção sem o token de usuário
    
    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.save()
