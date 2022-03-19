from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='class-page'),
    path('<slug:slug>', views.class_detail, name='class-detail'),
    path('<slug:slug>/problems/<slug:pro_slug>', views.problem_detail, name='class-problems-detail'),
    path('<slug:slug>/submission', views.class_submission, name='class-submission'),
    path('<slug:slug>/student-list', views.student_list, name='student-list'),
    # path('<slug:slug>/ranking', views.contest_ranking, name='contest-ranking'),
]
