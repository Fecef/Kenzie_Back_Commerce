import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    currenty_inventory = models.IntegerField()

    added_by = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        ordering = ("name",)

    def __repr__(self) -> str:
        return f"<[{self.pk}] {self.name}>"
