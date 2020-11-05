from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['profile_pic','bio']
        widgets = {
        'password': forms.PasswordInput(),
    }
''' Forms Needed:
    New Task Form
    Sign-In Form
    Possibly Update Account Info Form
'''
# class NewTaskForm(forms.ModelForm):
    # class Meta:
    


