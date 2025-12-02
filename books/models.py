# from django.db import models


# class Book(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Название книги")
#     author = models.CharField(max_length=255, verbose_name="Автор")
#     description = models.TextField(verbose_name="Описание")
#     published_date = models.DateField(verbose_name="Дата публикации")
#     isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
#     pages = models.PositiveIntegerField(verbose_name="Количество страниц")
#     language = models.CharField(max_length=100, verbose_name="Язык")
#     genre = models.CharField(max_length=100, verbose_name="Жанр")
#     price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
#     stock = models.PositiveIntegerField(verbose_name="Количество в наличии")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    # def __str__(self):
    #     return f"{self.title} ({self.author})"

    # class Meta:
    #     verbose_name = "Книга"
    #     verbose_name_plural = "Книги"
    #     ordering = ['-created_at']

# from django.db import models
# from django.contrib.auth import get_user_model
# from django.db.models import Avg

# User = get_user_model()

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255, blank=True)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.title

#     def average_rating(self):
#         agg = self.reviews.aggregate(avg=Avg('rating'))
#         return agg['avg']

#     def rating_display(self):
#         avg = self.average_rating()
#         return round(avg, 2) if avg is not None else '—'


# class Review(models.Model):
#     RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

#     book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, blank=True)
#     body = models.TextField()
#     rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.book.title} — {self.user.username} ({self.rating})"

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
