from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - profile'
