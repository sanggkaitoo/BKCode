from django.contrib import admin
from django.urls import path, include


from . import views
from user_profile import views as user_views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('login/', user_views.login_page, name='login-page'),
    path('logout/', user_views.logout_user, name='logout-user'),
    path('sign-up/', user_views.register, name='signup-page'),
    path('problems/', include('exercise.urls')),
    path('learn/', include('lesson.urls')),
    path('status/', include('code_submission.urls')),
    path('profile/', include('user_profile.urls'))
]
