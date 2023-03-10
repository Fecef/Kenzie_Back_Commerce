from rest_framework import serializers

from user.serializers import UserTrackSerializer

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    user = UserTrackSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ["id", "state", "city", "zip_code", "street", "number", "user"]
        depth = 1

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
