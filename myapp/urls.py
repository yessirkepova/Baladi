from .views import Post_list,Post_details
from django.urls import path


urlpatterns = [
    path('', Post_list, name='post_list'),
    path('<int:pid>/', Post_details, name='details'),
]
