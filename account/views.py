from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, 'auth/register.html', {"error": "Password not matched"})

        print(password1, email, 44444, username)
        try:
            user = User.objects.create_user(email=email, password=password1, username=username)
        except Exception as e:
            return render(request, 'auth/register.html', {"error": str(e)})
        user.save()
        return redirect('/login')
    return render(request, 'auth/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username, password)
        print(user)
        if user:
            login(request, user)
    return render(request, 'auth/login.html')


@login_required
def home(request):
    print(request, 11111)
    return render(request, "index.html")


def user_logout(request):
    logout(request)
    return redirect('login')
