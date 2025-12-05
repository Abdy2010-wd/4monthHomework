# from django.contrib import admin
# from django.urls import path
# from books import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.book_list, name='book_list'),  # главная страница — список книг
#     path('book/<int:pk>/', views.book_detail, name='book_detail'),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", admin.site.urls),
    path("books/", include("books.urls")),
    path("myShop/", include("myShop.urls")),   # ← ВОТ ЭТО ДОБАВЬ
]
