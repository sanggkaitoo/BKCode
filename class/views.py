from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *


@login_required(login_url='login-page')
def index(request):

    class_list = Student_Class.objects.filter(student__id=request.user.id)

    context = {
        'nbar': 'class',
        'class': class_list
    }
    return render(request, 'pages/class.html', context)


def class_detail(request, slug):

    list_problems = Problem_Class.objects.filter(class_obj__slug=slug)

    context = {
        'nbar': 'class',
        'list_problems': list_problems
    }

    print(list_problems)

    return render(request, 'pages/class-problems.html', context)
