from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from cart.models import Cart
from cart.serializers import CartSerializer


class CartView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CartDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_object(self):
        products = self.request.user.cart.products
        prod_id = self.kwargs.get("prod_id", None)
        obj = get_object_or_404(products, id=prod_id)

        return obj

    def perform_destroy(self, instance):
        products = self.request.user.cart.products
        products.remove(instance)
