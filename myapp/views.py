from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile,Follow,Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, UpdateProfileForm,PostForm
from .serializers import PostSerializer
from rest_framework import viewsets
from .tasks import send_welcome_email

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def about(request):
    return render(request, 'about.html')

def profile(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user

    user_profile = get_object_or_404(UserProfile, user=user)
    
    return render(request, 'profile.html', {'user': user, 'profile': user_profile})


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post-list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('user-profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('user-profile', user_id=user_id)

@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    is_following = Follow.objects.filter(follower=request.user, following=user).exists()
    followers = Follow.objects.filter(following=user)
    following = Follow.objects.filter(follower=user)
    return render(request, 'user_profile.html', {
        'user_profile': user,
        'is_following': is_following,
        'followers': followers,
        'following': following
    })

def register_user(request):
    send_welcome_email.delay(User.email)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

