from django.shortcuts import render
from dashboard.models import Dashboard
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    #context = {'dashboard': Dashboard}
    return render(request, 'dashboard/dashboard.html')