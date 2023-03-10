from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from cart.models import Cart
from cart.serializers import CartSerializer
from products.models import Product


class CartView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
