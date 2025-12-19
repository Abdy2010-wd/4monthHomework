from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Rating(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    rating = models.ManyToManyField(Rating, blank=True)
    release_date = models.DateField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movies"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        ratings = self.rating.all()
        if ratings.exists():
            return round(
                sum(r.value for r in ratings) / ratings.count(), 1
            )
        return 0

    def __str__(self):
        return self.title


