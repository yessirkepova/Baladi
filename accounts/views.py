from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView, LogoutView

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматически логинит после регистрации
            return redirect('dashboard')  # перенаправим на главную страницу фрилансеров
    else:
        form = RegistrationForm()
    return render(request, 'accounts/sign_in.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/log_in.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'  # после выхода перекидывает на логин
