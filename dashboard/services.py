from django.db.models import Count, Q

from departments.models import Department
from employees.models import Employee
from projects.models import Project
from tasks.choices import TaskStatus
from tasks.models import Task

class DashboardService:

    @staticmethod
    def get_statistics(user=None):
        context = {}
        
        if not user:
            return context

        if user.is_hr or user.is_superuser:

            context["employee_count"] = Employee.objects.filter(is_active=True).count()
            context["department_count"] = Department.objects.filter(is_active=True).count()
            context["project_count"] = Project.objects.filter(is_active=True).count()

            task_counts = Task.objects.filter(is_active=True).aggregate(
                pending_task_count=Count("id", filter=Q(status=TaskStatus.TODO)),
                completed_task_count=Count("id", filter=Q(status=TaskStatus.DONE)),
            )
            context.update(task_counts)

        elif user.is_employee:

            employee = Employee.objects.filter(user=user, is_active=True).first()
            if not employee:
                return context

            tasks = Task.objects.filter(
                assigned_to=employee
            )
            context.update(
                tasks.aggregate(
                    my_tasks=Count("id"),
                    completed_tasks=Count("id", filter=Q(status=TaskStatus.DONE)),
                    pending_tasks=Count("id", filter=Q(status=TaskStatus.TODO)),
                    overdue_tasks=Count("id", filter=Q(status=TaskStatus.IN_PROGRESS)),
                )
            )
        return context
        
