<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-03-08 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 4.1.7 on 2023-03-08 15:17

from django.db import migrations, models
>>>>>>> 8e383a9f284a5f7697c66344825b5ab6463612b3


class Migration(migrations.Migration):
    initial = True

<<<<<<< HEAD
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
=======
    dependencies = []
>>>>>>> 8e383a9f284a5f7697c66344825b5ab6463612b3

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
<<<<<<< HEAD
                            ("Em Andamento", "Ea"),
                            ("Entregue", "En"),
                            ("Pedido Realizado", "Default"),
                        ],
                        default="Pedido Realizado",
=======
                            ("Pedido Realizado", "Pr"),
                            ("Em Andamento", "Ea"),
                            ("Entregue", "En"),
                            ("Pedido realizado", "Default"),
                        ],
                        default="Pedido realizado",
>>>>>>> 8e383a9f284a5f7697c66344825b5ab6463612b3
                        max_length=20,
                    ),
                ),
                ("products", models.TextField()),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_atualizacao", models.DateTimeField(auto_now=True)),
<<<<<<< HEAD
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
=======
>>>>>>> 8e383a9f284a5f7697c66344825b5ab6463612b3
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
