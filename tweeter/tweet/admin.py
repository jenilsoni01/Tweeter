from django.contrib import admin

# Register your models here.
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'created_at']

admin.site.register(Tweet, TweetAdmin)


