from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.
from job.forms.job_form import JobForm
from job.models import Job


@login_required
def add_job(request):
    if request.method == 'POST':
        job_form = JobForm(data=request.POST)

        if job_form.is_valid():
            # Saving to the database
            job_form.save()
            return redirect(reverse('dashboard'))
        else:
            # User inputs invalid info
            context = {'job_form': JobForm()}
            return render(request, 'job/add-job.html', context)

    else:
        # The page is initially loaded with a blank form
        context = { 'job_form': JobForm()}
        return render(request, 'job/add-job.html', context)

@login_required
def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    #if request.user.is_authenticated:

    context = { 'job': job}
    return render(request, 'job/job-details.html', context)