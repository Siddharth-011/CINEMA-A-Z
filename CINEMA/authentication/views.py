from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "index.html")

def signin(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request, "index.html", {'name': user.first_name})
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect('signin')

    return render(request, "signin.html")
    
def signup(request):

    if request.method=="POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        curruser=User.objects.create_user(username=username, password=pass1)
        curruser.first_name=fname
        curruser.last_name=lname

        curruser.save()
        messages.success(request, "Your account has been succesfully created")

        return redirect('signin/')

    return render(request, "signup.html")
    
def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')