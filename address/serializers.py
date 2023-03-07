from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "city", "zipCode", "street", "number", "user_id"]
        read_only_fields = ["user_id"]
