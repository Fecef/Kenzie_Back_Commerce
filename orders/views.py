from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from products.models import Product
from .serializers import OrderSerializer
from .utils import update_stock, send_email_user
from rest_framework.exceptions import NotFound
import ipdb


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order_id = self.kwargs
        user_id = self.request.user
        products = Product.objects.filter(
            added_by__products__id=order_id
        )

        if not products:
            raise NotFound("Nenhum produto encontrado para este usuário.")

        order = serializer.save(user=user_id)

        quantities = [1] * len(products)
        update_stock(products, quantities)

        order.products.set(products)
        return order


class OrderDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        order = serializer.save()
        if 'status' in serializer.validated_data:
            send_email_user(order)
        return order
