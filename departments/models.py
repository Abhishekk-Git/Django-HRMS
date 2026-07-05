from django.db import models

from core.models import BaseModel

class Department(BaseModel):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name