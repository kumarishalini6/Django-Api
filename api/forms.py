from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = "__all__"
