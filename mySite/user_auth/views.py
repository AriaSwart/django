from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm

# Create your views here.
def user_login(request):
    return render(request, 'login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return redirect('user_auth:login')
    else:
        login(request, user)
        return redirect('polls:index')

def register(request):
    form = UserRegisterForm()
    if request.POST:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_auth:login')
    
    return render(request, 'registration.html', {'form':form})
