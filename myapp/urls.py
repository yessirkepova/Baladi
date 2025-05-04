from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list, name='post_list'),
    path('<int:pid>/', views.Post_details, name='details'),
    path('log_in/', views.log_in, name='log_in'), 
    path('Sign_in/', views.sign_in, name='Sign_in'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancies/create/', views.vacancy_create, name='vacancy_create'),
    path('vacancies/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancies/<int:pk>/delete/', views.vacancy_delete, name='vacancy_delete'), 
]
