from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)

    def __str__(self):
        return self.user.username + ' - profile'

    """
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="accounts", null=True, blank=True)"""