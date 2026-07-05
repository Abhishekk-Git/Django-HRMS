from django import forms
from employees.models import Employee
from .models import Task
from django.utils import timezone
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):

    class Meta:

        model = Task

        fields = [
            "project",
            "title",
            "description",
            "assigned_to",
            "priority",
            "status",
            "estimated_hours",
            "due_date",
        ]

        widgets = {

            "assigned_to": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                }
            ),

            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["assigned_to"].queryset = Employee.objects.filter(
            is_active=True
        )

        for field in self.fields.values():

            field.widget.attrs.setdefault(
                "class",
                "form-control",
            )
            
    def clean_due_date(self):
        due_date = self.cleaned_data["due_date"]
        if due_date < timezone.now().date():

            raise ValidationError(
                "Due date cannot be in the past."
            )

        return due_date