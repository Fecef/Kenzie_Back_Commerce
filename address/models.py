from django.db import models


class Address(models.Model):
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipCode = models.CharField(max_length=8, unique=True)
    street = models.CharField(max_length=150)
    number = models.IntegerField(null=True, default=0)

    # user = models.OneToOneField("user.User", on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f"<[{self.pk}] {self.email}>"
