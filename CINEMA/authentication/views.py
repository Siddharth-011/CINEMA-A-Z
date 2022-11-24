from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, "index-1.html")

def signin(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect('signin')

    return render(request, "signin.html")
    
def signup(request):

    if request.method=="POST":
        username=request.POST["username"]
        name=request.POST["name"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')

            else:
                if User.objects.filter(email=email):
                    messages.info(request, 'Email already in use')

                else:
                    curruser=User.objects.create_user(username=username, password=pass1, email=email)
                    curruser.first_name=name

                    curruser.save()
                    messages.success(request, "Your account has been succesfully created")

                    return redirect('signin')

        else:
            messages.error(request, 'Passwords entered not matching')

    return render(request, "signup.html")
    
def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('welcome')