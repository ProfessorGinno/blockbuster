from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView

from .models import UserProfile
from .forms import UserEditForm


class UserSignUp(CreateView):
    model = UserProfile
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'accounts/signup.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserEditForm
    template_name = "accounts/edit_user.html"
    success_url = reverse_lazy('home')


class UserLogin(LoginView):
    template_name = 'accounts/user_login.html'
    next_page = reverse_lazy('movie_index')


class UserLogout(LogoutView):
    template_name = 'accounts/user_logout.html'


def sign_up_success(request):
    return render(request, template_name="accounts/sign_up_success.html")