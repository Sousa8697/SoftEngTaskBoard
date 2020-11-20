from django import forms
from django.contrib.auth.models import User
from .models import Account
from .models import Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')
''' Forms Needed:
    New Task Form
    Sign-In Form
    Possibly Update Account Info Form
'''
class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = {'post_date','accountOwner','section'}


