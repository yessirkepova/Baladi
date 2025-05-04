from django.shortcuts import render
from .models import Posts,PostAttachments
from .models import Vacancy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def Post_list(request):
  posts= Posts.objects.all()
  for post in posts:
    att=PostAttachments.objects.filter(post_id = post.pk)
    post.att=att
  return render(request, 'posts/post_list.html', {'myapp':posts})


def Post_details(request, pid):
  post = Posts.objects.get(pk=pid)
  att= PostAttachments.objects.filter(post_id = pid)
  return render(request, 'posts/details_page.html', {'post':post , 'images':att})
def log_in(request):
    return render(request, 'posts/log_in.html')
def sign_in(request):
    return render(request, 'posts/Sign_in.html')
def vacancy_list(request):
    vacancies = Vacancy.objects.all().order_by('-posted_at')
    return render(request, 'posts/vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'posts/vacancy_detail.html', {'vacancy': vacancy})

@login_required
def vacancy_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Vacancy.objects.create(title=title, description=description)
            return redirect('vacancy_list')
    return render(request, 'posts/vacancy_create.html')

@login_required
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancy_list')
    return render(request, 'posts/vacancy_delete.html', {'vacancy': vacancy})