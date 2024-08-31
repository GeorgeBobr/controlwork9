from django.db import models
from django.contrib.auth.models import User
import uuid

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    access_token = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.caption

    def generate_access_token(self):
        if not self.access_token:
            self.access_token = uuid.uuid4().hex
            self.save()
