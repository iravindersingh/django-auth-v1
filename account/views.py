from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.success(request, 'Registration successful')
                return redirect('/login')

        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'auth/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username, password)
        if user:
            login(request, user)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'auth/login.html')


@login_required
def home(request):
    print(request, 11111)
    return render(request, "index.html")


def user_logout(request):
    logout(request)
    return redirect('login')
