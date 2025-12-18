# from django.shortcuts import render
# from django.http import HttpResponse
# import random
# from datetime import datetime

# def about(request):
#     return HttpResponse("Меня зовут Абдымиталийп. Я изучаю Django 🚀")

# def current_time(request):
#     now = datetime.now().time()

#     if now < datetime.strptime("12:00", "%H:%M").time():
#         message = "Сейчас утро 🌅"
#     elif datetime.strptime("12:00", "%H:%M").time() <= now <= datetime.strptime("14:00", "%H:%M").time():
#         message = "Сейчас обед 🍽️"
#     elif datetime.strptime("15:00", "%H:%M").time() <= now <= datetime.strptime("20:00", "%H:%M").time():
#         message = "Сейчас вечер 🌇"
#     else:
#         message = "Сейчас ночь 🌙"

#     return HttpResponse(message)

# def quotes(request):
#     quotes_list = [
#         "Не ошибается тот, кто ничего не делает. — Л.Н. Толстой",
#         "Чтобы быть незаменимым, нужно всё время меняться. — Коко Шанель",
#         "Мы то, что мы думаем. — Будда",
#         "Счастье — это когда мысли, слова и дела совпадают. — Ганди",
#         "Жизнь — это то, что происходит, пока ты строишь планы. — Джон Леннон",
#     ]
#     return HttpResponse(random.choice(quotes_list))


# from django.shortcuts import render, get_object_or_404
# from .models import Book

# # Список всех книг
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books})

# # Детальная страница одной книги
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/book_detail.html', {'book': book})


from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import Book, Review


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "page_obj"
    paginate_by = 5


class BookSearchView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "page_obj"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "description", "published_year"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")


class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "description", "published_year"]
    template_name = "books/book_form.html"

    def get_success_url(self):
        return reverse_lazy("book_detail", kwargs={"pk": self.object.pk})


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book_list")


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            rating = int(request.POST.get("rating"))
            body = request.POST.get("body", "")

            review = Review(book=self.object, rating=rating, body=body)
            review.clean()
            review.save()

        except (ValidationError, ValueError):
            return self.get(request, error="Ставьте оценку только от 1 до 5")

        return self.get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = self.object.reviews.all()
        context["error"] = kwargs.get("error")
        return context
