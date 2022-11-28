from django.urls import path
from .views import CreateMovie, ListMovie, UpdateMovie, DeleteMovie, index, DetailMovie

urlpatterns = [
    path("create-movie/", CreateMovie.as_view(), name="create_movie"),
    path("list-movie/", ListMovie.as_view(), name="list_movie"),
    path("update-movie/<int:pk>", UpdateMovie.as_view(), name="update_movie"),
    path("delete-movie/<int:pk>", DeleteMovie.as_view(), name="delete_movie"),   
    path("movie-index/", index, name="movie_index"),
    path("detailed-movie/<int:pk>", DetailMovie.as_view(), name="detalied_view"),
]
