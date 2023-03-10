from rest_framework import serializers
from rest_framework.permissions import SAFE_METHODS
from products.models import Product
from products.serializers import ProductCartSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "products", "user_name"]
        read_only_fields = ["user", "user_name"]
        depth = 1

    user_name = serializers.CharField(source="user.first_name", read_only=True)
    products = ProductCartSerializer(many=True, write_only=True)

    def create(self, validated_data):
        products = validated_data.pop("products")
        print(products)
        cart_add = self.context["request"].user.cart
        for product_id in products:
            instance = Product.objects.get(pk=product_id["id"])
            cart_add.products.add(instance)
        # self.Meta.depth = 2
        return cart_add

    # def __init__(self, instance=None, data=..., **kwargs):
    #     super().__init__(instance, data, **kwargs)
    #     if not self.context.get("request") in SAFE_METHODS:
    #         self.Meta.depth = 0
