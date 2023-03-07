from django.db import models


class Address(models.Model):
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=150)
    number = models.PositiveSmallIntegerField()

    def __repr__(self) -> str:
        return f"<[{self.pk}] {self.email}>"
