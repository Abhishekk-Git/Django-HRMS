from django import forms

from .models import Project
from django.core.exceptions import ValidationError



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "name",
            "description",
            "start_date",
            "end_date",
            "is_active",
        ]

        widgets = {
            "start_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
            "end_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.setdefault(
                "class",
                "form-control",
            )
            
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and end < start:
            raise ValidationError(
                "End date cannot be before start date."
            )

        return cleaned_data