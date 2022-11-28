from django.shortcuts import render


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.views.generic import DeleteView, CreateView

from .forms import UserEditForm
from . models import UserProfile


class UserSignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'accounts/signup.html'


class UserLogin(LoginView):
    template_name = 'accounts/user_login.html'
    next_page = reverse_lazy('movie_index')


class UserLogout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/user_logout.html'

