from django.shortcuts import render
from .models import Movie
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class CreateMovie (CreateView):
    model = Movie
    template_name = "movies/create_movie.html"
    success_url = "/index"
    fields = ["title", "genre", "description", "date", "size"]

class ListMovie (ListView):
    model = Movie

class UpdateMovie (UpdateView):
    model = Movie
    template_name = "movies/update_movie.html"
    success_url = "/list-movie"
    fields = ["title", "genre", "description", "date", "size"]

class DeleteMovie (DeleteView):
    model = Movie
    template_name = "movies/delete_movie.html"
    success_url = "/list-movie"
    fields = ["title", "genre", "description", "date", "size"]