from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
import json
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

def allTasks(request):
    data = Task.objects.filter(accountOwner_id=request.user.id)
    dataDict = {}
    for task in data:
        dataDict[task.id] = {"title":str(task.title), "due date":str(task.due_date),"description":str(task.description)}
    return json.dumps(dataDict)

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
    if request.method == "GET":
        if 'toDo' in request.GET:
            taskId = request.GET.get('toDo')
            task = Task.objects.get(id = int(taskId))
            task.toDo()
        elif 'toDoing' in request.GET:
            taskId = request.GET.get('toDoing')
            task = Task.objects.get(id = int(taskId))
            task.toDoing()
        elif 'toDone' in request.GET:
            taskId = request.GET.get('toDone')
            task = Task.objects.get(id = int(taskId))
            task.toDone()
        elif 'delete' in request.GET:
            taskId = request.GET.get('delete')
            Task.objects.get(id=int(taskId)).delete()
    context['todoTasks'] = Task.objects.filter(section="to-do", accountOwner_id=request.user.id)
    context['doingTasks'] = Task.objects.filter(section="doing", accountOwner_id=request.user.id)
    context['doneTasks'] = Task.objects.filter(section="done", accountOwner_id=request.user.id)
    context['allTasks']  = allTasks(request)
    return render(request,"TBApp/index.html", context)


def signUp(request):
    form = UserForm()
    errors = ""
    if request.method == "POST":
        profileForm = UserForm(data=request.POST)
        if profileForm.is_valid():
            user = profileForm.save()
            user.set_password(user.password)
            user.save()
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
        if user.is_authenticated:
            return render(request,"TBApp/profile.html")
        else:
            errors = "Not valid operation"
