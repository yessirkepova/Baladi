from django.urls import path, include
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from .views import follow_user, unfollow_user, user_profile
from .views import register, profile, edit_profile
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/<str:username>/', views.profile, name='profile-username'),
    path('profile/', views.profile, name='profile'), 
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<int:user_id>/', user_profile, name='user-profile'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/edit/', edit_profile, name='edit-profile'),
]
