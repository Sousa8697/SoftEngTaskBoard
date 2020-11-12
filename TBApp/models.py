from django.db import models
from django import forms

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="",blank=True)
    bio = models.TextField(default="",blank=True)

    def __str__(self):
        return self.username

#Table full of tasks where each task is linked to an account id
# Tasks will have a title, due date, post date, description, section (to-do, doing, done)

class Task(models.Model):

    SECTION_CHOICES = (
        ('to-do', 'TO-DO'),
        ('doing', 'DOING'),
        ('done', 'DONE')
    )

    title = models.CharField(max_length = 255)
    due_date = models.CharField(max_length = 50)
    post_date = models.DateTimeField(auto_now_add=True)     #Timestamp of current date/time
    description = models.CharField(max_length = 512)
    section = models.CharField(max_length=6, choices=SECTION_CHOICES, default='to-do')

    def __str__(self):      #Do we need this? I'll put it here just in case.
        return self.title
# Class Task(models.Model):

