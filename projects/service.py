from .models import Project


class ProjectService:

    @staticmethod
    def create(form, request=None):

        return form.save()

    @staticmethod
    def update(form):

        return form.save()

    @staticmethod
    def delete(project):

        project.is_active = False

        project.save()