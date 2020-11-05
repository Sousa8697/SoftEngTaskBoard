from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="",blank=True)
    bio = models.TextField(default="",blank=True)
