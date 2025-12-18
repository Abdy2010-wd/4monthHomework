from django.urls import path
from .views import CategoryListView, ClothesByCategoryView

urlpatterns = [
    path("", CategoryListView.as_view(), name="category_list"),
    path("<int:category_id>/", ClothesByCategoryView.as_view(), name="clothes_by_category"),
]


