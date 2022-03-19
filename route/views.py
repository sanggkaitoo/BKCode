from django.shortcuts import render, redirect
from django.views import View
from .models import AboutUs


def index(request):
    if request.user.is_authenticated:
        return redirect('problems-page')
    else:
        return render(request, 'index.html')


def error(request):
    return render(request, 'pages/404.html')


def about_us(request):
    information = AboutUs.objects.first()
    context = {
        'information': information,
        'nbar': 'about-us'
    }
    return render(request, 'pages/about-us.html', context)

