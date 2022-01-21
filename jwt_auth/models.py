from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50)
    preferred_breed_one = models.CharField(max_length=30)
    preferred_breed_two = models.CharField(max_length=30, null=True, blank=True)
    preferred_breed_three = models.CharField(max_length=30, null=True, blank=True)
    preferred_age = models.CharField(max_length=30)
    preferred_sex = models.CharField(max_length=30)
    has_dogs = models.BooleanField(default=False)
    has_cats = models.BooleanField(default=False)
    has_kids = models.BooleanField(default=False) 