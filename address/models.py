from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=150)
    zipCode = models.CharField(max_length=8)
    street = models.CharField(max_length=150)
    number = models.IntegerField()

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
