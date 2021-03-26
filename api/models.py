from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    imdb_id = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    director = models.CharField(max_length=200)
    img_url = models.CharField(max_length=2083)

    def __str__(self):
        return f'{self.name} ({self.year})'


class List(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='list')
    movies = models.ManyToManyField(Movie)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')
    rate = models.IntegerField()
    body = models.TextField(null=True)

    def __str__(self):
        return f'{self.user}|{self.rate}|{self.movie}'
