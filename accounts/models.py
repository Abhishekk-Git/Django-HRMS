from django.db import models
from django.contrib.auth.models import AbstractUser
from core.constants import EMPLOYEE_GROUP, HR_GROUP, ADMIN_GROUP

# Create your models here.

class User(AbstractUser):
    
    @property
    def is_hr(self):
        return self.groups.filter(name=HR_GROUP).exists()

    @property
    def is_employee(self):
        return self.groups.filter(name=EMPLOYEE_GROUP).exists()

    @property
    def is_admin(self):
        return self.groups.filter(name=ADMIN_GROUP).exists()
