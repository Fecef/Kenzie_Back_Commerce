from rest_framework import serializers
from .models import Product
from user.models import User


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'currenty_inventory', 'added_by']

    def create(self, validated_data: dict) -> Product:
        print(validated_data)
        return Product.objects.create(**validated_data)
