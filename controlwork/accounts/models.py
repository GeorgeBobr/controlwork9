from django.db import models
from django.contrib.auth.models import User
from webapp.models import Photo, Album


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    favorite_photos = models.ManyToManyField(Photo, related_name='favorited_by_profiles', blank=True)
    favorite_albums = models.ManyToManyField(Album, related_name='favorited_by_profiles', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
