from django import forms

from .models import Archive_file


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('file_name', 'file_id', 'record_date', 'hours_worked', 'employee_id', 'job_group')
