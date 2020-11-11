from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from TBApp.forms import AccountForm
from django import forms
# Create your views here.


def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        else:
            loginAttempt = "Login failed, please Check the username and password and try again."
            return render(request,"TBAPP/signIn.html",{'error':loginAttempt})
    return render(request,"TBApp/signIn.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url="/accounts/sign-in/")
def home(request):
    return render(request,"TBApp/index.html")


def signUp(request):
    form = AccountForm()
    errors = ""
    if request.method == "POST":
        profileForm = AccountForm(request.POST)
        if profileForm.is_valid():
            profileForm.save(commit=True)
            return HttpResponseRedirect(reverse('home'))
        else:
            errors = profileForm.errors

    return render(request,"TBApp/signUp.html",{'form':form, 'errors':errors})
@login_required(login_url="/accounts/sign-in/")
def profile(request):
    return render(request,"TBApp/profile.html")