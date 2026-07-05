from django.db import models

from core.models import BaseModel
# Create your models here.


class Project(BaseModel):

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):

        return self.name