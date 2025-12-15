from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.passport_create, name="passport_create"),
    path("", views.passport_list, name="passport_list"),
]
