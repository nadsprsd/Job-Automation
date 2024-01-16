# job_automation_app/views.py

from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .forms import ResumeForm

def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add NLP processing and resume update logic here
            return redirect('job_application')
    else:
        form = JobApplicationForm()

    return render(request, 'job_automation_app/job_application.html', {'form': form})


def add_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_application')  # Redirect to a success page or another view
    else:
        form = ResumeForm()

        return render(request, 'job_automation_app/add_resume.html', {'form': form})


    # return render(request, 'add_resume.html', {'form': form})
    
    