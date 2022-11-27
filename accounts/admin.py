from django.contrib import admin
from accounts.models import UserProfile

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user','phone','address','image']
# Register your models here.
