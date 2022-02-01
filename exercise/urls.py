from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='problems-page'),
    path('<slug:slug>/', views.exercise, name='exercise')
]