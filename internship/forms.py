from django import forms

from .models import Intern


class InternForm(forms.ModelForm):
    def clean_postal(self):
        cleaned_data = self.cleaned_data['postal']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('only numeric！')
        return int(cleaned_data)

    class Meta:
        model = Intern
        fields = (
            'job_title', 'company_name','postal','started_time'
        )