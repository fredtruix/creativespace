from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(default="avatar.svg", null=True)


   

    # social
    instagram = models.CharField(max_length=300, null=True, blank=True)
    linkedin = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



