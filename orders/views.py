from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from .serializers import OrderSerializer
from .utils import update_stock, send_email_user
from rest_framework.exceptions import NotFound
from .permissions import IsVendor
from django.shortcuts import get_object_or_404
from user.models import User


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        cart = self.request.user.cart
        products = cart.products.filter(is_avaliable=True)

        if not products.exists():
            raise serializers.ValidationError('Out of stock')

        order = serializer.save(user=self.request.user)
        order.products.set(products)
        cart.products.set([])

        return order

    def get_queryset(self):

        queryset = super().get_queryset()

        if not self.request.user.is_vendor:
            queryset = queryset.filter(user=self.request.user)

        return queryset


class OrderDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        obj = get_object_or_404(User, pk=self.request.user.orders.id)
        return obj.orders

    def perform_update(self, serializer):
        order = serializer.save()
        if 'status' in serializer.validated_data:
            send_email_user(order)
        return order
