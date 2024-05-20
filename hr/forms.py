from typing import Any
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import *

class LeaveApplyForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type' : 'date', 'class': 'form-control'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type' : 'date', 'class': 'form-control'}))

    class Meta:
        model = Leave
        fields = ["start_date", "end_date"]



    def clean(self):
        cleaned_data = super().clean()

        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                self.add_error('end_date', 'Low Date')
        
        return cleaned_data