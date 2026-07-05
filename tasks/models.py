from django.db import models
from core.models import BaseModel
from projects.models import Project

from employees.models import Employee
from tasks.choices import Priority, TaskStatus


class Task(BaseModel):

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(blank=True, null=True)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    assigned_to = models.ManyToManyField(
        Employee,
        related_name="tasks",
        blank=True,
    )

    due_date = models.DateField()
    estimated_hours = models.PositiveIntegerField(default=1)

    created_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_tasks",
    )
    
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
    )
    
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    is_active = models.BooleanField(default=True)
    
    def __str__(self):

        return self.title