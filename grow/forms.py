from .models import Grow_From
from django import forms
from django.forms import ModelForm, DateInput

class form_data(ModelForm):
    class Meta:
        model = Grow_From
        fields = (
            'id', 'employee_name', 'employee_email', 'idea_description', 'shift', 'division',
            'department', 'line', 'station', 'type', 'area', 'current_description', 'idea_description')
        widgets = {
            'id': forms.HiddenInput(),
            'employee_name': forms.HiddenInput(),
            'employee_email': DateInput(),
            'idea_description': DateInput(),
            'shift': DateInput(),
            'created_at': forms.HiddenInput(),
            'division': DateInput(),
            'department': forms.HiddenInput(),
            'line': DateInput(),
            'station': DateInput(),
            'type': forms.HiddenInput(),
            'current_description': DateInput(),
            'employee_id': DateInput(),
            'date': DateInput(),
            'date': forms.HiddenInput(),


        }

