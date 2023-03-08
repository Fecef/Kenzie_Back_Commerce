from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

# from .permissions import UserPermission, UserDetailPermission


class AddressView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [UserPermission]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
