from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    # A better way to store images
    profileImage = models.ImageField(upload_to='profileImages/', blank=True, null=True)
    # profileImage = models.ImageField(upload_to='profileImages/', default='/media/profileImages/user.png', blank=True, null=True)

    def __str__(self):
        return self.user.username