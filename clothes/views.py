from django.shortcuts import render
from .models import Category, Clothing

def categories_list(request):
    categories = Category.objects.all()
    return render(request, "clothes/categories.html", {"categories": categories})

def clothes_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    clothes = Clothing.objects.filter(category=category)
    return render(request, "clothes/category_clothes.html", {"category": category, "clothes": clothes})

