from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('problems-page')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user + "!")
                return redirect('login-page')
        return render(request, 'pages/signup.html', {'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('problems-page')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('problems-page')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'pages/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login-page')