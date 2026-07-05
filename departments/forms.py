from django import forms

from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department

        fields = [
            "name",
            "description",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"