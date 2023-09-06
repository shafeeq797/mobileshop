
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
def index(request):
    return render(request,'index.html')
    # return render(request,'admin.html')

def create(request):
    return render(request,'createaccount.html')
def login(request):
    return render(request,'login.html')
def user(request):
    return render(request,'user.html')


# Create your views here.
