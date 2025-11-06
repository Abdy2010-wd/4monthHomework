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

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField("Название книги", max_length=200)
    author = models.CharField("Автор", max_length=100)
    rating = models.FloatField("Средний рейтинг", default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Отзыв")
    rating = models.IntegerField("Оценка", default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
