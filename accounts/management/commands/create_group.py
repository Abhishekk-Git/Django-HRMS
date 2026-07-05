from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        groups  = ["Admin", "HR", "Employee"]

        for group_name in groups:
            Group.objects.get_or_create(name=group_name)

        self.stdout.write(self.style.SUCCESS('Groups created successfully.'))       