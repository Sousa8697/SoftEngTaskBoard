from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signIn(request):
    if request.method == 'POST':
        pass
    return render(request,"TBApp/signIn.html")

def home(request):
    return render(request,"TBApp/index.html")

def signUp(request):
    return render(request,"TBApp/signUp.html")

def profile(request):
    return render(request,"TBApp/profile.html")