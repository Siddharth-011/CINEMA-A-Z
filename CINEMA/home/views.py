from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Titles

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('welcome')

def search(request):
    results=Titles.objects.filter(name__icontains=request.GET['query']).values()
    return render(request, 'search.html', {'results':results})