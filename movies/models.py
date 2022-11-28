from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField()
    cover_image = models.ImageField(upload_to='cover_image/', blank=False, default=None)
    scene_image_1 = models.ImageField(upload_to='cover_image/', blank=False, default=None)
    scene_image_2 = models.ImageField(upload_to='cover_image/', blank=False, default=None)
    scene_image_3 = models.ImageField(upload_to='cover_image/', blank=False, default=None)
    trailer_link = models.CharField(max_length=50, default=None)
    movie_file_4k = models.FileField(upload_to='movie_file/', blank=False, default=None)
    movie_file_uhd = models.FileField(upload_to='movie_file/', blank=False, default=None)

 
    def __str__(self) -> str:
        return f"title is {self.title}, the id is {self.id}, the image is {self.cover_image}"