from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('status', 'order_date', 'user', 'products')

    def create(self, validated_data: dict) -> Order:
        return Order.objects.create(**validated_data)
