from django.contrib.auth import get_user_model
from django.db import transaction

from employees.models import Employee
from django.contrib.auth.models import Group

User = get_user_model()


class EmployeeService:

    @staticmethod
    @transaction.atomic
    def create_employee(form, request=None):

        user = User.objects.create_user(

            username=form.cleaned_data["username"],

            email=form.cleaned_data["email"],

            first_name=form.cleaned_data["first_name"],

            last_name=form.cleaned_data["last_name"],

            password=form.cleaned_data["password"],
        )
        employee_group = Group.objects.get(name="Employee")
        user.groups.add(employee_group)

        employee = form.save(commit=False)
        employee.employee_code = EmployeeService.generate_employee_code()

        employee.user = user

        employee.save()

        return employee
    
    @staticmethod
    def generate_employee_code():

        last_employee = Employee.objects.order_by(
            "-id"
        ).first()

        if not last_employee:

            return "EMP001"

        last_id = last_employee.id + 1

        return f"EMP{last_id:03d}"
    
    @staticmethod
    @transaction.atomic
    def delete_employee(employee):

        user = employee.user

        employee.delete()

        user.delete()