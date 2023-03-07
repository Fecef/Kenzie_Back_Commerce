from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from .permissions import IsAuthenticated, IsAdmin, IsOwnerOrAdmin


class UserView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)

        self.check_object_permissions(self.request, User)

        return queryset


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    def perform_destroy(self, instance: User):
        instance.is_active = False
        instance.save()


class UserAccounRecoverView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    def perform_update(self, serializer):
        instance = serializer.save()

        if self.request.data.get("is_active", None):
            instance.is_active = True
            instance.save()
