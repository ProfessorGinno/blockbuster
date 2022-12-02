from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Movie


class DetailMovie(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class CreateMovie(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Movie
    permission_required = "movies.add_movie"
    template_name = "movies/create_movie.html"
    success_url = reverse_lazy("movie_index")
    fields = ["title", "genre", "description", "date", "cover_image", "scene_image_1", "scene_image_3", "scene_image_2", "trailer_link", "movie_file_4k", "movie_file_uhd"]


class ListMovie(LoginRequiredMixin, ListView):
    model = Movie


class UpdateMovie(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Movie
    permission_required = "movies.change_movie"
    template_name = "movies/update_movie.html"
    success_url = reverse_lazy("movie_index")
    fields = ["title", "genre", "description", "date", "cover_image", "scene_image_1", "scene_image_3", "scene_image_2", "trailer_link", "movie_file_4k", "movie_file_uhd"]


class DeleteMovie(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Movie
    permission_required = "movies.delete_movie"
    template_name = "movies/delete_movie.html"
    success_url = reverse_lazy("movie_index")


class SearchMovie(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movies/search_movie.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(Q(title__icontains=query)|Q(genre__icontains=query))
        return object_list


def index(request):
    movie = Movie.objects.order_by('-date').all()
    return render(request, template_name="movies/movie_index.html", context={"movie": movie})