from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    currenty_inventory = models.IntegerField()

    added_by = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='product'
    )
