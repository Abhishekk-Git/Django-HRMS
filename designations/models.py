from django.db import models
from departments.models import Department

# Create your models here.


class Designation(models.Model):
    title = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="designations"
    )

    def __str__(self):
        return self.title