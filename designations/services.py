from .models import Designation


class DesignationService:

    @staticmethod
    def create_designation(form, request=None):

        return form.save()

    @staticmethod
    def update_designation(form):

        return form.save()

    @staticmethod
    def deactivate_designation(designation):

        designation.is_active = False

        designation.save()