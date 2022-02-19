from django.shortcuts import render
from .models import Subjects, Lesson
from django.shortcuts import redirect
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    list_course = Subjects.objects.all()

    context = {
        'list_course': list_course
    }

    return render(request, 'pages/learn.html', context)


def lesson_detail(request, slug):
    try:
        lesson = Lesson.objects.filter(slug__startswith=slug).order_by('section_order')

        first_lesson = Lesson.objects.filter(slug__startswith=slug).order_by('section_order')[0:1].get()

        return redirect('lesson-content', slug=slug, lesson_choose=slugify(first_lesson.section))
    except ObjectDoesNotExist:
        return render(request, 'pages/lesson.html')


def lesson_content(request, slug, lesson_choose):
    try:
        lesson = list(Lesson.objects.filter(slug__startswith=slug).order_by('section_order'))

        list_lesson = []

        for item in lesson:
            list_lesson.append([item, slugify(item.section)])

        print(list_lesson)

        content = Lesson.objects.filter(slug__contains=lesson_choose, slug__startswith=slug).first()

        subject = slugify(content.subject)

        context = {
            'lesson': list_lesson,
            'content': content,
            'subject': subject,
        }

        return render(request, 'pages/lesson.html', context)
    except ObjectDoesNotExist:
        return render(request, 'pages/lesson.html')
