import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from exercise.models import Exercise
from programming_language.models import ProgrammingLanguage
from .models import CodeSubmission
from contest.models import Contest
from classes.models import Class

from .utils import check_main


def index(request):

    data = CodeSubmission.objects.filter(user=request.user)

    context = {
        'data': data
    }

    return render(request, 'pages/result.html', context)


# def index(request):
#     return render(request, 'pages/result.html')


def code_submitted(request, slug):
    ex = Exercise.objects.get(slug=slug)
    language = request.POST["language"]
    source = request.POST["code-submit"]
    contest = request.POST.get("contest", False)
    classes = request.POST.get("class", False)

    if contest is False:
        contest_obj = None
    else:
        contest_obj = Contest.objects.get(id=contest)

    if classes is False:
        class_obj = None
    else:
        class_obj = Class.objects.get(id=classes)


    lang = ProgrammingLanguage.objects.get(id=language)

    path_to_source = './media/compile/source.{}'.format(lang.ext)
    input_file = './media/' + str(ex.test_input)
    output_file = './media/' + str(ex.test_output)
    time_limit = ex.time_limits / 1000

    source_file = open('./media/compile/source.txt', 'w')
    source_file.write(source)
    source_file.close()
    os.rename('./media/compile/source.txt', path_to_source)

    status_code, notes = check_main(path_to_source, input_file, output_file, time_limit)

    new_compile = CodeSubmission(
        user=request.user,
        exercise=ex,
        code=source,
        status=status_code,
        time=ex.time_limits,
        memory=0,
        language=lang,
        notes=notes,
        contest=contest_obj,
        class_obj=class_obj
    )

    new_compile.save()

    return redirect('status-page')

