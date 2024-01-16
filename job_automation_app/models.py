# job_automation_app/models.py

from django.db import models

class JobApplication(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

class Resume(models.Model):
    name = models.CharField(max_length=255)
    contact_Info = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    personal_Info = models.TextField()
    projects = models.TextField()
