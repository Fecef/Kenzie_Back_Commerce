from rest_framework import serializers
from .models import Address
from rest_framework.validators import UniqueValidator


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "state",
            "city",
            "zipCode",
            "street",
            "number",]

        # read_only_fields = ["user_id"]

        extra_kwargs = {
            "zipCode": {
                "validators": [
                    UniqueValidator(
                        queryset=Address.objects.all(),
                        message="Zip Code already registered"
                    )
                ]
            }
        }
