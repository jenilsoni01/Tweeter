from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')

admin.site.register(Profile, ProfileAdmin)
