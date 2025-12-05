from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories_list(request):
    """
    Возвращает все категории.
    URL: /shop/categories/ (например)
    """
    categories = Category.objects.all().order_by("name")
    return render(request, "myShop/categories.html", {"categories": categories})


def products_list(request):
    """
    Возвращает все продукты (везде).
    URL: /shop/products/
    """
    products = Product.objects.select_related("category").all().order_by("name")
    return render(request, "myShop/products.html", {"products": products})


def category_products(request, category_id):
    """
    Возвращает продукты для выбранной категории.
    URL: /shop/category/<int:category_id>/
    """
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all().order_by("name")  # thanks to related_name
    return render(request, "myShop/category_products.html", {"category": category, "products": products})
