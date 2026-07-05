from .models import Department


class DepartmentService:

    @staticmethod
    def create_department(form, request=None    ):

        return form.save()

    @staticmethod
    def update_department(form):

        return form.save()

    @staticmethod
    def deactivate_department(department):

        department.is_active = False

        department.save()