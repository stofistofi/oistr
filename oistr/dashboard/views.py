from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Dashboard
from django.http import HttpResponse
# Create your views here.
from job.models import Job

@login_required
def dashboard(request):
    context = {'jobs': Job.objects.all()}
    return render(request, 'dashboard/dashboard.html', context)