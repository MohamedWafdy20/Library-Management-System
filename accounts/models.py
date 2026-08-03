
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=11
    )

    address = models.CharField(
        max_length=200
    )

    is_admin = models.BooleanField(
        default=False
    )

    is_librarian = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username

