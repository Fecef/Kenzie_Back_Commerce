from django.db import models


class Order_Type(models.TextChoices):
    PR = "Pedido Realizado"
    EA = "Em Andamento"
    EN = "Entregue"
    DEFAULT = "Pedido realizado"


class Order(models.Model):
    class Meta:
        ordering = ['id']

    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Order_Type.choices, default=Order_Type.DEFAULT)
    products = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )

    def __repr__(self) -> str:
        return f"{self.user.username} - {self.order_date.strftime('%d/%m/%Y %H:%M:%S')} - {self.status}"
