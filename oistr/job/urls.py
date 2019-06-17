from django.urls import path
from . import views

urlpatterns = [
    path('add-job', views.add_job, name="add-job")
]