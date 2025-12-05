from django.urls import path
from . import views

app_name = "myShop"

urlpatterns = [
    path("categories/", views.categories_list, name="categories_list"),
    path("products/", views.products_list, name="products_list"),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
]
