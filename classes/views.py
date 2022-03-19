from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from code_submission.models import CodeSubmission


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
    classes = Class.objects.get(slug=slug)

    context = {
        'nbar': 'class',
        'list_problems': list_problems,
        'class': classes
    }

    print(list_problems)

    return render(request, 'pages/class-problems.html', context)


@login_required(login_url='login-page')
def problem_detail(request, slug, pro_slug):
    try:
        exercise = Exercise.objects.get(slug=pro_slug)
        class_obj = Class.objects.get(slug=slug)

        context = {
            'exercise': exercise,
            'class': class_obj,
            'nbar': 'class'
        }

        return render(request, 'pages/exercise.html', context)
    except Class.DoesNotExist:
        return render(request, 'pages/login.html')


def student_list(request, slug):
    student_list_data = Student_Class.objects.filter(class_obj__slug=slug)
    list_submission = CodeSubmission.objects.filter(class_obj__slug=slug)
    list_problems = Problem_Class.objects.filter(class_obj__slug=slug)
    class_obj = Class.objects.get(slug=slug)

    ex_count = len(list_problems)

    student_infor = []

    for user in student_list_data:
        count = 0
        for submit in list_submission:
            if submit.user.id == user.student.id and submit.status == "ACCEPTED":
                count = count + 1
        temp = [user, count]
        student_infor.append(temp)

    context = {
        'student_list': student_infor,
        'class': class_obj,
        'nbar': 'class',
        'ex_count': ex_count
    }

    return render(request, 'pages/class-student.html', context)


def class_submission(request, slug):
    class_obj = Class.objects.get(slug=slug)
    list_submission = CodeSubmission.objects.filter(class_obj__slug=slug)

    context = {
        'list_submission': list_submission,
        'class': class_obj,
        'nbar': 'class'
    }

    return render(request, 'pages/class-submission.html', context)
