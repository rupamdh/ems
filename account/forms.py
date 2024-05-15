from django import forms
from django.forms import ModelForm
from .models import Employee


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), required=True)
    last_name = forms.CharField(max_length=200, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}), required=True)

    class Meta:
        model = Employee
        fields = ["first_name", "last_name"]




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.errors:
            self.fields['first_name'].widget.attrs.update({'class': 'form-control border-1 border-red-600'})
        

    