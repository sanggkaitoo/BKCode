from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from exercise.models import *
from code_submission.models import CodeSubmission
from django.contrib.auth import get_user_model


def index(request):

    list_contests = Contest.objects.all()

    context = {
        'contests': list_contests,
        'nbar': 'contest'
    }

    return render(request, 'pages/contest.html', context)


@login_required(login_url='login-page')
def contest_detail(request, slug):
    try:
        contest = Contest.objects.get(slug=slug)

        context = {
            'contest': contest,
        'nbar': 'contest'
        }
        return render(request, 'pages/infor-contest.html', context)
    except Contest.DoesNotExist:
        return render(request, 'pages/login.html')


@login_required(login_url='login-page')
def contest_problems(request, slug):
    try:
        contest = Contest.objects.get(slug=slug)
        list_id = ContestDetail.objects.filter(contest__slug=slug)
        list_id_pro = []

        for i in list_id:
            list_id_pro.append([i.exercise, i.score])

        context = {
            'contest': contest,
            'list_problems': list_id_pro,
        'nbar': 'contest'
        }

        return render(request, 'pages/contest-problems.html', context)
    except Contest.DoesNotExist:
        return render(request, 'pages/404/html')


@login_required(login_url='login-page')
def problem_detail(request, slug, pro_slug):
    try:
        exercise = Exercise.objects.get(slug=pro_slug)
        contest = Contest.objects.get(slug=slug)

        context = {
            'exercise': exercise,
            'contest': contest,
            'nbar': 'contest'
        }

        return render(request, 'pages/exercise.html', context)
    except Contest.DoesNotExist:
        return render(request, 'pages/login.html')


def contest_submission(request, slug):
    try:
        list_submission = CodeSubmission.objects.filter(contest__slug=slug)
        contest = Contest.objects.get(slug=slug)

        context = {
            'list_submission': list_submission,
            'contest': contest,
            'nbar': 'contest'
        }
        return render(request, 'pages/contest-submission.html', context)
    except Contest.DoesNotExist:
        return render(request, 'pages/404.html')


def check_name(id, list_arr):
    for i in range(len(list_arr)):
        if id == list_arr[i][0]:
            return i
    return -1


def get_score(ex_id, list_ex):
    for item in list_ex:
        if item.exercise.id == ex_id:
            return item.score


def contest_ranking(request, slug):
    try:
        list_submission = CodeSubmission.objects.filter(contest__slug=slug)
        list_problems = ContestDetail.objects.filter(contest__slug=slug)

        list_data = []
        total_score = 0

        for item in list_submission:
            if item.status == "ACCEPTED":
                if check_name(item.user.id, list_data) == -1:
                    list_ex_score = []
                    ex_score = [item.exercise.id, get_score(item.exercise.id, list_problems)]
                    list_ex_score.append(ex_score)
                    obj_data = [item.user.username, list_ex_score, total_score]
                    list_data.append(obj_data)
                else:
                    ex_score = [item.exercise.id, get_score(item.exercise.id, list_problems)]
                    list_data[check_name(item.user.id, list_data)][1].append(ex_score)

        for item in list_data:
            score = 0
            for sc in item[1]:
                score += sc[1]
            item[2] = score

        contest = Contest.objects.get(slug=slug)

        context = {
            'list_submission': list_submission,
            'contest': contest,
            'list_data': list_data,
            'list_problems': list_problems,
            'nbar': 'contest'
        }
        return render(request, 'pages/contest-ranking.html', context)
    except Contest.DoesNotExist:
        return render(request, 'pages/404.html')
