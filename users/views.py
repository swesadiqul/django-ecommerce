from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def signup(request):
    return render(request, 'sign-up.html')


def signin(request):
    return render(request, 'login.html')


@login_required(login_url='/signin')
def signout(request):
    logout(request)
    messages.success(request, 'Successfully signed out')
    

def forgot_password(request):
    return render(request, 'forgot.html')