from django.views.generic import ListView
from .models import Category, Clothing


class CategoryListView(ListView):
    model = Category
    template_name = "clothes/categories.html"
    context_object_name = "categories"


class ClothesByCategoryView(ListView):
    model = Clothing
    template_name = "clothes/category_clothes.html"
    context_object_name = "clothes"

    def get_queryset(self):
        return Clothing.objects.filter(category_id=self.kwargs["category_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(id=self.kwargs["category_id"])
        return context

