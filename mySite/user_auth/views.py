"""This file will render the login pages"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm

# Create your views here.
def user_login(request):
    """This function sends the user to the main login page."""
    return render(request, 'login.html')

def authenticate_user(request):
    """This function authenticates users and redirects them onwards."""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return redirect('user_auth:login')
    else:
        login(request, user)
        return redirect('polls:index')

def register(request):
    """This is the form to register a new user."""
    form = UserRegisterForm()
    if request.POST:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_auth:login')
    
    return render(request, 'registration.html', {'form':form})
