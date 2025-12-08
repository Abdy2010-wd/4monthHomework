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


from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from .models import Book, Review


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        published_year = request.POST.get("published_year")

        Book.objects.create(
            title=title,
            author=author,
            description=description,
            published_year=published_year
        )
        return redirect("book_list")

    return render(request, "books/book_form.html")


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.description = request.POST.get("description")
        book.published_year = request.POST.get("published_year")
        book.save()

        return redirect("book_detail", pk=book.pk)

    return render(request, "books/book_form.html", {"book": book})



def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")
 

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()

    if request.method == "POST":
        try:
            rating = int(request.POST.get("rating"))
            body = request.POST.get("body", "")
            
            review = Review(book=book, rating=rating, body=body)
            review.clean()
            review.save()
            return redirect("book_detail", pk=pk)

        except (ValidationError, ValueError):
            return render(request, "books/book_detail.html", {
                "book": book,
                "reviews": reviews,
                "error": "Ставьте оценку только от 1 до 5"
            })

    return render(request, "books/book_detail.html", {
        "book": book,
        "reviews": reviews
    })
