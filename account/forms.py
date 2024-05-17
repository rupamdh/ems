from django import forms
from django.forms import ModelForm
from .models import Employee


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=True)
    last_name = forms.CharField(max_length=200, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}), required=True)
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "email", "dob", "phone", "designation", "address", "adhar", "assigned_to", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        

class EmployeeEditForm(forms.ModelForm):
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Employee
        exclude = ["groups", "password", "last_login", "is_superuser", "is_staff", "is_active", "date_joined", "user_permissions", "wrk_status", "booked_by"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'