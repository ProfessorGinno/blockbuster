from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView


class UserSignUp(CreateView):
    form_class = UserCreationForm
    success_url: reverse_lazy('home')
    template_name = 'registration/signup.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('account-login')


class UserLogin(LoginView):
    template_name = 'accounts/user_login.html'
    next_page = reverse_lazy('home')


class UserLogout(LogoutView):
    template_name = 'accounts/user_logout.html'