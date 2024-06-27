from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from users.forms import *


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            messages.success(request, f'{name} successfully registered.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid registration form.')
            return redirect('home')
    return render(request, 'sign-up.html')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{user.full_name} successfully logged in.')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')

    return render(request, 'login.html')


@login_required(login_url='/signin')
def signout(request):
    logout(request)
    messages.success(request, 'Successfully signed out')
    return redirect('home')
    

def forgot_password(request):
    return render(request, 'forgot.html')


def user_dashboard(request):
    return render(request, 'user-dashboard.html')


def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        print(request.POST)
        # if form.is_valid():
        #     print(request.POST)

        # else:
        #     print('Invalid Profile')
    return redirect('/')

