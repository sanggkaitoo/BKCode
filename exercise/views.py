from django.shortcuts import render, get_object_or_404
from .models import Exercise

from django.contrib.auth.decorators import login_required


@login_required(login_url='login-page')
def index(request):
    list_exercise = Exercise.objects.all()

    context = {
        'exercise': list_exercise,
        'nbar': 'problem'
    }

    return render(request, 'pages/problems.html', context)


@login_required(login_url='login-page')
def exercise(request, slug):
    try:
        exercise = Exercise.objects.get(slug=slug)

        context = {
            'exercise': exercise,
            'nbar': 'problem'
        }

        return render(request, 'pages/exercise.html', context)
    except Exercise.DoesNotExist:
        return render(request, 'pages/login.html')
