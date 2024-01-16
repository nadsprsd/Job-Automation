# job_automation_app/forms.py

from django import forms
from .models import JobApplication
from .models import Resume

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['title', 'company', 'location', 'description']


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'contact_Info', 'education', 'experience', 'skills', 'personal_Info', 'projects']        
