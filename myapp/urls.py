from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list, name='post_list'),
    path('<int:pid>/', views.Post_details, name='details'),
    path('log_in/', views.log_in, name='log_in'), 
    path('Sign_in/', views.sign_in, name='Sign_in'), 
]
