# job_automation_app/urls.py

from django.urls import path
from .views import job_application , add_resume

urlpatterns = [
    path('job_application/', job_application, name='job_application'),
    path('add_resume/', add_resume, name='add_resume'),
]
