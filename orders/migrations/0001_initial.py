# Generated by Django 4.1 on 2023-03-09 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                            ("Pedido Realizado", "Pr"),
                            ("Em Andamento", "Ea"),
                            ("Entregue", "En"),
                            ("Pedido realizado", "Default"),
                        ],
                        default="Pedido realizado",
                        max_length=20,
                    ),
                ),
                ("products", models.TextField()),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_atualizacao", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]