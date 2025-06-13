from django.db import models
from django.conf import settings

from authentication.models import Profile


# Create your models here.

class Tweet(models.Model):
    content = models.TextField(max_length=280, blank=False, null=False)
    image = models.ImageField(upload_to="tweets/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tweets"
    )
    likes = models.ManyToManyField(Profile, related_name="likes", blank=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."

    def like_count(self):
        return self.likes.count()

    def is_liked_by(self, profile):
        return self.likes.filter(id=profile.id).exists()

