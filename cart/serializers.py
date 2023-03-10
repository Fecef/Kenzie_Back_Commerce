from rest_framework import serializers
from rest_framework.permissions import SAFE_METHODS
from products.models import Product
from products.serializers import ProductCartSerializer
from user.serializers import UserTrackSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "products"]
        read_only_fields = ["user"]
        depth = 1

    user = UserTrackSerializer(read_only=True)
    products = ProductCartSerializer(many=True)

    def create(self, validated_data):
        products = validated_data.pop("products")

        cart_add = self.context["request"].user.cart
        for product_id in products:
            instance = Product.objects.get(pk=product_id["id"])
            cart_add.products.add(instance)
        return cart_add
