from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from TBApp.forms import UserForm
from TBApp.forms import NewTaskForm
from django import forms
from .models import Account, Task, User
# Create your views here.

context={}
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
            return render(request,"TBApp/signIn.html",{'error':loginAttempt})
    return render(request,"TBApp/signIn.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url="/accounts/sign-in/")
def home(request):
    taskForm = NewTaskForm()
    context['task'] = taskForm
    if request.method == "POST":
        taskForm = NewTaskForm(request.POST)
        if taskForm.is_valid():
            task = taskForm.save(commit=False)
            task.accountOwner = User.objects.get(username=request.user)
            task.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            errors = taskForm.errors
            context['errors'] = errors
    context['todoTasks'] = Task.objects.filter(section="to-do", accountOwner_id=request.user.id)
    context['doingTasks'] = Task.objects.filter(section="doing", accountOwner_id=request.user.id)
    context['doneTasks'] = Task.objects.filter(section="done", accountOwner_id=request.user.id)
    return render(request,"TBApp/index.html", context)


def signUp(request):
    form = UserForm()
    errors = ""
    if request.method == "POST":
        profileForm = UserForm(request.POST)
        if profileForm.is_valid():
            profileForm.save(commit=True)
            return HttpResponseRedirect(reverse('home'))
        else:
            errors = profileForm.errors

    return render(request,"TBApp/signUp.html",{'form':form, 'errors':errors})

@login_required(login_url="/accounts/sign-in/")
def profile(request):
    # Get post request and get user id from post request
    user = request.user     #user.ID
    errors = ""
    if request.method == "GET":
        if user.is_authenticated():
            return render(request,"TBApp/profile.html")
        else:
            errors = "Not valid operation"
