from rest_framework import serializers

from products.models import Product
from products.serializers import ProductCartSerializer

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    products = ProductCartSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["products"]

    def create(self, validated_data):
        products = validated_data.pop("products")
        cart_add = self.context["request"].user.cart

        for product_id in products:
            instance = Product.objects.get(pk=product_id["id"])
            cart_add.products.add(instance)

        return cart_add
