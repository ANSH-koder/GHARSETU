
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Role(models.TextChoices):
        TENANT = 'TENANT', 'Tenant'
        OWNER = 'OWNER', 'Owner'
        AGENT = 'AGENT', 'Agent'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.TENANT
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
