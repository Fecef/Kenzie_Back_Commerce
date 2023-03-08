# Generated by Django 4.1 on 2023-03-08 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="number",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="zipCode",
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
