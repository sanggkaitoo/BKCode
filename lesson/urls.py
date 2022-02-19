from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='learn-page'),
    path('<slug:slug>/', views.lesson_detail, name='lesson-detail'),
    path('<slug:slug>/<str:lesson_choose>', views.lesson_content, name='lesson-content')
]
