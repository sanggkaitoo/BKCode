from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='status-page'),
    path('<slug:slug>', views.code_submitted, name='code_submitted'),
    # path('status/', views.submit_status, name='submit_status')
]
