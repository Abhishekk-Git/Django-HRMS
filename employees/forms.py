from django import forms
from django.contrib.auth import get_user_model
from .models import Employee

User = get_user_model()

class EmployeeCreateForm(forms.ModelForm):
    
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Employee
        fields = [
            # 'user',
            # 'employee_code',
            'department',
            'designation',
            'joining_date',
            'phone',
        ]
        
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields([
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "department",
            "designation",
            "joining_date",
            "phone",
        ])
        for field in self.fields.values():
            print(field)
            field.widget.attrs['class'] = 'form-control'
            
    def clean_employee_code(self):
        code = self.cleaned_data["employee_code"]

        if Employee.objects.filter(employee_code=code).exists():

            raise forms.ValidationError(
                "Employee code already exists."
            )

        return code 
    
    
    def clean_username(self):

        username = self.cleaned_data["username"]

        if User.objects.filter(
            username=username
        ).exists():

            raise forms.ValidationError(
                "Username already exists."
            )

        return username
    
    
class EmployeeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = [
            'department',
            'designation',
            'joining_date',
            'phone',
        ]
        
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = [
#             # 'user',
#             'employee_code',
#             'department',
#             'designation',
#             'joining_date',
#             'phone',
#         ]
        
#         widgets = {
#             'joining_date': forms.DateInput(attrs={'type': 'date'}),
#         }
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
            
#     def clean_employee_code(self):
#         code = self.cleaned_data["employee_code"]

#         if Employee.objects.filter(employee_code=code).exists():

#             raise forms.ValidationError(
#                 "Employee code already exists."
#             )

#         return code