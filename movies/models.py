from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    description = models.TextField()
    size = models.IntegerField()
    date = models.DateField()
    cover_image = models.ImageField(upload_to='cover_image/', blank=True)

 
    def __str__(self) -> str:
        return f"title is {self.title}, the id is {self.id}, the image is {self.cover_image}"