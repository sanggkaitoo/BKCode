from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='contest-page'),
    path('<slug:slug>/', views.contest_detail, name='contest-detail'),
    path('<slug:slug>/problems/', views.contest_problems, name='contest-problems'),
    path('<slug:slug>/problems/<slug:pro_slug>', views.problem_detail, name='contest-problems-detail'),
    path('<slug:slug>/submission', views.contest_submission, name='contest-submission'),
    path('<slug:slug>/ranking', views.contest_ranking, name='contest-ranking'),
]
