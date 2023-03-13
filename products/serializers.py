from rest_framework import serializers
from user.serializers import UserTrackSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    added_by = UserTrackSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "category",
            "current_inventory",
            "added_by",
            "is_avaliable",
        ]
        read_only_fields = ["is_avaliable"]
        depth = 1

    def create(self, validated_data: dict) -> Product:
        if validated_data["current_inventory"] == 0:
            return Product.objects.create(**validated_data, is_avaliable=False)
        return Product.objects.create(**validated_data)


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "category"]
        read_only_fields = ["name", "price", "category"]

    id = serializers.UUIDField()

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
