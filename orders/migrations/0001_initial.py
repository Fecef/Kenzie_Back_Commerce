# Generated by Django 4.1.7 on 2023-03-08 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                            ("Em Andamento", "Ea"),
                            ("Entregue", "En"),
                            ("Pedido Realizado", "Default"),
                        ],
                        default="Pedido Realizado",
                        max_length=20,
                    ),
                ),
                ("products", models.TextField()),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_atualizacao", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
