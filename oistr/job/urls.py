from django.urls import path
from . import views

urlpatterns = [
    path('<int:job_id>', views.job_details, name='job-details'),
    path('add-job', views.add_job, name="add-job")
]