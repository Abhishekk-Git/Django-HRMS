from django.db import models
from django.conf import settings

from departments.models import Department
from designations.models import Designation


class Employee(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile"
    )

    employee_code = models.CharField(
        max_length=20,
        unique=True,
        editable=False

    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees"
    )

    designation = models.ForeignKey(
        Designation,
        on_delete=models.PROTECT,
        related_name="employees"
    )

    joining_date = models.DateField()

    phone = models.CharField(
        max_length=15
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_code})"