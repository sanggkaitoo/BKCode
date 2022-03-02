from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .models import User, UserProfile
from code_submission.models import CodeSubmission

from django.contrib.auth.decorators import login_required


def index(request):

    profile = UserProfile.objects.get(user=request.user)

    submit = CodeSubmission.objects.filter(user=request.user)
    accept = CodeSubmission.objects.filter(user=request.user, status='ACCEPTED')
    point = 0
    for item in accept:
        if item.exercise.level == 'easy':
            point = point + 50
        elif item.exercise.level == 'medium':
            point = point + 100
        else:
            point = point + 150

    submit_status = [len(submit), len(accept), point]

    context = {
        'user': request.user,
        'profile': profile,
        'submit': submit_status
    }
    print(submit_status)

    return render(request, 'pages/profile.html', context)


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