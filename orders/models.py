from django.db import models
import uuid


class Order_Type(models.TextChoices):
    EA = "Em Andamento"
    EN = "Entregue"
    DEFAULT = "Pedido realizado"


class Order(models.Model):
    class Meta:
        ordering = ['id']

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Order_Type.choices, default=Order_Type.DEFAULT)
    products = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )

    def __repr__(self) -> str:
        return f"{self.user.username} - {self.order_date.strftime('%d/%m/%Y %H:%M:%S')} - {self.status}"
