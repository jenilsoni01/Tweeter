from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", default="profile_pictures/picture.jpg"
    )
    cover = models.ImageField(
        upload_to="cover_images/", default="cover_images/cover.jpg"
    )
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )

    def __str__(self):
        return self.user.username

    def get_profile_picture_url(self):
        if self.profile_picture and hasattr(self.profile_picture, "url"):
            return self.profile_picture.url
        return "/media/profile_pictures/picture.jpg"

    def get_cover_image_url(self):
        if self.cover and hasattr(self.cover, "url"):
            return self.cover.url
        return "/media/cover_images/cover.png"
