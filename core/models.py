import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank = True)

class Profile(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField()
    uuid = models.UUIDField(default = uuid.uuid4)

class Movie(models.Model):
    TYPES = (
        ("Seasonal", "seasonal"),
        ("Single", "single")
    )
    AGE_WISE = (
        ("Above 18", False),
        ("Below 18", True)
    )
    title = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    type = models.CharField(max_length = 255, choices = TYPES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to = 'flyer')
    age_limit = models.CharField(max_length = 10, choices = AGE_WISE)
    uuid = models.UUIDField(default = uuid.uuid4)

class Video(models.Model):
    title = models.CharField(max_length =225, blank = True, null = True)
    file = models.FileField(upload_to = 'movies')