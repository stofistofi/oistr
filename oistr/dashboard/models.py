from django.db import models

# Create your models here.
class Dashboard(models.Model):
    rejected = models.CharField(max_length=255, default='')
    applied = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=255, default='')
    interview = models.CharField(max_length=255, default='')
    offer = models.CharField(max_length=255, default='')
    accepted = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.name