from django.db import models
from django import forms
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="",blank=True)
    bio = models.TextField(default="",blank=True)

    def __unicode__(self):
        return self.user.get_username()

#Table full of tasks where each task is linked to an account id
# Tasks will have a title, due date, post date, description, section (to-do, doing, done)

class Task(models.Model):

    SECTION_CHOICES = (
        ('to-do', 'TO-DO'),
        ('doing', 'DOING'),
        ('done', 'DONE')
    )
    accountOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    due_date = models.CharField(max_length = 50)
    post_date = models.DateTimeField(auto_now_add=True)     #Timestamp of current date/time
    description = models.CharField(max_length = 512)
    section = models.CharField(max_length=6, choices=SECTION_CHOICES, default='to-do')

    def __str__(self):
        return self.title+" "+self.accountOwner
    
    def toDo(self):
        self.section = 'to-do'
        self.save(update_fields=('section',))
        
    def toDoing(self):
        self.section = 'doing'
        self.save(update_fields=('section',))
    
    def toDone(self):
        self.section = 'done'
        self.save(update_fields=('section',))
# Class Task(models.Model):

