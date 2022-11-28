from django.shortcuts import render
from .models import Movie
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def index(request):
    movie = Movie.objects.order_by('-date').all()
    return render(request, template_name="movies/movie_index.html", context={"movie": movie})

class DetailMovie(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class CreateMovie(CreateView):
    model = Movie
    template_name = "movies/create_movie.html"
    success_url = "/movie-index"
    fields = ["title", "genre", "description", "date", "size", "cover_image"]


class ListMovie(ListView):
    model = Movie


class UpdateMovie(UpdateView):
    model = Movie
    template_name = "movies/update_movie.html"
    success_url = "/movie-index"
    fields = ["title", "genre", "description", "date", "size", "cover_image"]


class DeleteMovie(DeleteView):
    model = Movie
    template_name = "movies/delete_movie.html"
    success_url = "/movie-index"
    fields = ["title", "genre", "description", "date", "size"]