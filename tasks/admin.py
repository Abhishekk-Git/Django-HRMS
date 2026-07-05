from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project",
        "status",
        "priority",
        "due_date",
    )

    list_filter = (
        "status",
        "priority",
        "project",
    )

    search_fields = (
        "title",
    )

    filter_horizontal = (
        "assigned_to",
    )