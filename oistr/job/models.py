from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Job(models.Model):
    company = models.CharField(max_length=255, default='Company')
    title = models.CharField(max_length=255, default='Title')
    description = models.CharField(max_length=9900, default='Description')
    requirements = models.CharField(max_length=9900, default='Requirements')
    status = models.CharField(max_length=255, default='applied')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.company