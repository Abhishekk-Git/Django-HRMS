from django import forms

from departments.models import Department

from .models import Designation


class DesignationForm(forms.ModelForm):

    class Meta:

        model = Designation

        fields = [
            "title",
            "department",
            "description",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"