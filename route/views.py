from django.shortcuts import render, redirect
from django.views import View


def index(request):
    if request.user.is_authenticated:
        return redirect('problems-page')
    else:
        return render(request, 'index.html')

