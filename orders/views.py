from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsVendor
from .models import Order
from .serializers import OrderSerializer
from .utils import send_email_user
from .exceptions import OutOfStock


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsVendor]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        cart = self.request.user.cart
        products = cart.products.filter(is_avaliable=True)

        for product in products:
            product.current_inventory -= 1
            product.save()

        if not products.exists():
            raise OutOfStock("Out of stock")

        order = serializer.save(user=self.request.user)
        order.products.set(products)
        cart.products.set([])

        return order


class OrderDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_url_kwarg = "order_id"

    def perform_update(self, serializer):
        order = serializer.save()

        if "status" in serializer.validated_data:
            send_email_user(order)

        return order
