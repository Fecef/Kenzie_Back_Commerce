from rest_framework import serializers
from .models import Product

from user.serializers import UserTrackSerializer


class ProductSerializer(serializers.ModelSerializer):
    added_by = UserTrackSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "category", "current_inventory", "added_by"]
        depth = 1

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
