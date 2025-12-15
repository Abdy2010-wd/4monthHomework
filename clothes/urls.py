from django.urls import path
from . import views

urlpatterns = [
    path("", views.categories_list, name="categories_list"),
    path("category/<int:category_id>/", views.clothes_by_category, name="clothes_by_category"),
    path("create/", views.clothes_create, name="clothes_create"),
    path("update/<int:pk>/", views.clothes_update, name="clothes_update"),
    path("delete/<int:pk>/", views.clothes_delete, name="clothes_delete"),
]

