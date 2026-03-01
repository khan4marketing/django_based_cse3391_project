from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')
from django.shortcuts import render, redirect
from .models import Customer

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')