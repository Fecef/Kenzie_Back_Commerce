import uuid

from django.db import models


class Order_Type(models.TextChoices):
    PR = "Pedido Realizado"
    EA = "Em Andamento"
    EN = "Entregue"


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=20, choices=Order_Type.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="orders"
    )

    products = models.ManyToManyField("products.Product", related_name="orders")

    def __repr__(self) -> str:
        return f"{self.user.username} - {self.order_date.strftime('%d/%m/%Y %H:%M:%S')} - {self.status}"
