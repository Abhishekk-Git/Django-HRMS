from django.db import transaction
from django.core.exceptions import ValidationError

from employees.models import Employee

from .choices import TaskStatus


class TaskService:

    ALLOWED_STATUS = {

        TaskStatus.TODO: [
            TaskStatus.IN_PROGRESS,
        ],

        TaskStatus.IN_PROGRESS: [
            TaskStatus.TESTING,
        ],

        TaskStatus.TESTING: [
            TaskStatus.DONE,
        ],

        TaskStatus.DONE: [],
    }

    @staticmethod
    @transaction.atomic
    def create(form, request=None):
        print("request.user.employee", request)

        task = form.save(commit=False)
        employee = Employee.objects.get(user=request.user)

        task.created_by = employee if request else None

        task.save()

        form.save_m2m()

        return task

    @staticmethod
    @transaction.atomic
    def update(form):

        task = form.save()

        return task

    @staticmethod
    def delete(task):

        task.delete()

    @classmethod
    def update_status(cls, task, new_status):

        allowed = cls.ALLOWED_STATUS.get(task.status, [])

        if new_status not in allowed:

            raise ValidationError(
                "Invalid status transition."
            )

        task.status = new_status

        task.save()