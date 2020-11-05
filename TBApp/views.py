from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
from TBApp.forms import AccountForm
from django import forms
# Create your views here.
def signIn(request):
    if request.method == 'POST':
        pass
    return render(request,"TBApp/signIn.html")

def home(request):
    return render(request,"TBApp/index.html")

def signUp(request):
    form = AccountForm()
    errors = ""
    if request.method == "POST":
        profileForm = AccountForm(request.POST)
        if profileForm.is_valid():
            profileForm.save(commit=True)
            return home(request)
        else:
            errors = profileForm.errors

    return render(request,"TBApp/signUp.html",{'form':form, 'errors':errors})

def profile(request):
    return render(request,"TBApp/profile.html")