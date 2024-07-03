from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Signup, Signin,UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
import requests


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        # Check if all fields are filled
        if not name or not email or not password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('votinghome:signup')
        
        # Check if user with given email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.Please log in.')
            return redirect('votinghome:login') 
        else:
            # Create new user
            new_user = User.objects.create_user(username=email, email=email, password=password)
            UserProfile.objects.create(user=new_user, name=name)
            messages.success(request, 'User registered successfully.')
            return redirect('votinghome:login')
    return render(request, 'pages/home.html', {'signup_active': True})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if all fields are filled
        if not email or not password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('votinghome:login')  # Redirect to the login section of the home page

         # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('votingwebsite:website')  # Redirect to the dashboard or any other page after login
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('votinghome:login')
    return render(request, 'pages/home.html', {'login_active': True})

def logout_view(request):
    logout(request)
    return redirect('votingwebsite:website')
