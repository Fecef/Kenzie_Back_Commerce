# Generated by Django 4.1 on 2023-03-09 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="products",
            field=models.ManyToManyField(related_name="carts", to="products.product"),
        ),
    ]