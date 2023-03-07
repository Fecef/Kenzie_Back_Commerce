import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_admin = models.BooleanField(null=True, default=False)
    is_vendor = models.BooleanField(null=True, default=False)
    is_active = models.BooleanField(null=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # address = models.OneToOneField("address.Address", on_delete=models.CASCADE)

    class Meta:
        ordering = ("username",)

    def __repr__(self) -> str:
        return f"<[{self.pk}] {self.email}>"
