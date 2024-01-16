# job_automation_app/admin.py
from django.contrib import admin
from .models import JobApplication, Resume

admin.site.register(JobApplication)
admin.site.register(Resume)
