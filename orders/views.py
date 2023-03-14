from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from django.shortcuts import get_list_or_404

from products.models import Product

from .models import Order
from .serializers import OrderSerializer
from .utils import update_stock, send_email_user
from .exceptions import OutOfStock


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    order_kwarg = "order_id"

    def perform_create(self, serializer):
        products = self.request.user.cart.products
        has_unavaliable = get_list_or_404(products, is_avaliable=False)

        if has_unavaliable:
            # ! Customizar
            raise OutOfStock("Product is unavaliable.")

        # order = serializer.save(user=user_id)

        # quantities = [1] * len(products)
        # update_stock(products, quantities)

        # order.products.set(products)
        # return order


# class OrderDetailView(generics.RetrieveUpdateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def perform_update(self, serializer):
#         order = serializer.save()
#         if "status" in serializer.validated_data:
#             send_email_user(order)
#         return order
