from django.shortcuts import render
from .models import Movie
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, FormView
from .forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q


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
    fields = ["title", "genre", "description", "date", "cover_image", "scene_image_1", "scene_image_3", "scene_image_2", "trailer_link", "movie_file_4k", "movie_file_uhd"]


class ListMovie(ListView):
    model = Movie


class UpdateMovie(UpdateView):
    model = Movie
    template_name = "movies/update_movie.html"
    success_url = "/movie-index"
    fields = ["title", "genre", "description", "date", "cover_image", "scene_image_1", "scene_image_3", "scene_image_2", "trailer_link", "movie_file_4k", "movie_file_uhd"]


class DeleteMovie(DeleteView):
    model = Movie
    template_name = "movies/delete_movie.html"
    success_url = "/movie-index"


class SearchMovie(ListView):
    model = Movie
    template_name = 'movies/search_movie.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(Q(title__icontains=query)|Q(genre__icontains=query))
        return object_list